# GR-DOS

## A DOS for classic PCs

**GR-DOS** is a fork of the MS-DOS 4.00 source that Microsoft published
under the MIT license. It runs on everything from a 360 KB floppy to a hard
disk or CF card, and it has been checked on an 8088 and a V20 as well as
in emulators.

GR-DOS is built on Linux with open tools, booted in QEMU, and tested in
GitHub Actions. Development happens in the open at
[github.com/gr-dos](https://github.com/gr-dos).

### Get GR-DOS

Each [release](https://github.com/gr-dos/gr-dos/releases/latest) has four
bootable floppy images, a ZIP of the system files and utilities, and
checksums for all of them:

* 3.5" 1.44 MB and 720 KB
* 5.25" 1.2 MB and 360 KB

Write an image to a floppy disk of the same format, or boot it in an
emulator:

```
qemu-system-i386 -drive file=gr-dos-VERSION-1440k.img,if=floppy,format=raw -boot a
```

The `README.txt` in the release ZIP explains how to write the images from
Linux, Windows and DOS.

### Hard disks and CF cards

With FDISK, FORMAT and SYS, GR-DOS installs on a hard disk and boots from
it. From Linux, `scripts/deploy-cf` in the source tree installs GR-DOS on a
CF card or disk image, and later updates C: without touching your data
drives ([how](https://github.com/gr-dos/gr-dos/blob/main/docs/deploy-cf.md)).

### What's included?

The kernel and `COMMAND.COM`, and the MS-DOS 4.00 utilities, from FORMAT,
SYS, CHKDSK and FDISK to DEBUG, EDLIN, MEM and MODE. The larger floppies
carry more of them, with keyboard layouts, code pages and printer support.

Every disk also has `TICO.EXE`, the
[tico16](https://github.com/tico-edit/tico16) text editor. The release
ZIP and hard disk install add DOS programs from the gr-dos organization,
such as LESS, DIFF16 and TAR.

### Documentation and source

* [Building GR-DOS](https://github.com/gr-dos/gr-dos#building)
* [Documentation](https://github.com/gr-dos/gr-dos/tree/main/docs)
* [Source and releases](https://github.com/gr-dos/gr-dos)

### Project background

In 2024 Microsoft published the source of MS-DOS 4.00 under the MIT
license. GR-DOS builds on that source: apart from its branding and the
kernel's GR-DOS identification call, the assembly programs build
byte-identical to the original MASM/LINK build. GR-DOS's own work is MIT
licensed too ([provenance](https://github.com/gr-dos/gr-dos/blob/main/docs/provenance.md)).

MS-DOS is a trademark of Microsoft. GR-DOS is an independent project, not
endorsed by Microsoft or IBM.
