#!/usr/bin/env perl

use strict;
use warnings;
use XOR 0.10;

my $xor = XOR->new(
  root => '.',
  org  => 'gr-dos',
  site_name => 'gr-dos.org',
);

$xor->builder->build;
