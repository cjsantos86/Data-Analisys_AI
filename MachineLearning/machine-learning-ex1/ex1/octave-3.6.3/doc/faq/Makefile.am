# Makefile for octave's doc/faq directory
#
# Copyright (C) 1996-2012 John W. Eaton
#
# This file is part of Octave.
# 
# Octave is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at
# your option) any later version.
# 
# Octave is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Octave; see the file COPYING.  If not, see
# <http://www.gnu.org/licenses/>.

include $(top_srcdir)/build-aux/common.mk

## Automake generated rules for documentation are not parallel-safe.
## Restrict current directory to run serially
.NOTPARALLEL:

TEXINFO_TEX = ../texinfo.tex

info_TEXINFOS = OctaveFAQ.texi

all-local: dvi html pdf ps

EXTRA_DIST = OctaveFAQ.dvi OctaveFAQ.html OctaveFAQ.pdf OctaveFAQ.ps

