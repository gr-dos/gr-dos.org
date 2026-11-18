#!/usr/bin/env python3
"""Boot a GR-DOS floppy image in headless QEMU, type some commands, and save
an authentic screenshot of the 80x25 text screen.

    extra/screen/capture.py gr-dos-0.04-1440k.img docs/images/gr-dos-screen.png

Needs qemu-system-i386 and Pillow.  No display is needed: QEMU runs with
-display none and the screen is read with the monitor's screendump command.
"""

import os
import socket
import subprocess
import sys
import tempfile
import time

from PIL import Image

COMMANDS = ["cls", "ver", "dir /w"]

KEYS = {
    " ": "spc", "/": "slash", "\\": "backslash", ".": "dot", ":": "shift-semicolon",
    "-": "minus", "*": "shift-8", "\n": "ret",
}


def keyname(ch):
    if ch in KEYS:
        return KEYS[ch]
    if ch.isupper():
        return "shift-" + ch.lower()
    return ch


def main(image, out):
    work = tempfile.mkdtemp()
    sock = os.path.join(work, "mon")
    # Boot a copy, so the release image is never written to.
    disk = os.path.join(work, "a.img")
    with open(image, "rb") as src, open(disk, "wb") as dst:
        dst.write(src.read())
    qemu = subprocess.Popen([
        "qemu-system-i386", "-display", "none", "-m", "4", "-nic", "none",
        "-drive", f"file={disk},if=floppy,format=raw", "-boot", "a",
        "-monitor", f"unix:{sock},server,nowait",
    ])
    try:
        for _ in range(50):
            if os.path.exists(sock):
                break
            time.sleep(0.1)
        mon = socket.socket(socket.AF_UNIX)
        mon.connect(sock)

        def cmd(line):
            mon.sendall((line + "\n").encode())
            time.sleep(0.05)

        time.sleep(8)  # boot, and let AUTOEXEC.BAT finish
        for line in COMMANDS:
            for ch in line + "\n":
                cmd("sendkey " + keyname(ch))
            time.sleep(2)
        ppm = os.path.join(work, "screen.ppm")
        cmd("screendump " + ppm)
        time.sleep(1)
        Image.open(ppm).save(out)
        print(f"wrote {out} ({Image.open(out).size[0]}x{Image.open(out).size[1]})")
    finally:
        qemu.kill()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(f"usage: {sys.argv[0]} IMAGE OUT.png")
    main(*sys.argv[1:])
