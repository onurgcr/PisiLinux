#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "aalib-1.4.0"

def setup():
    pisitools.dosed("configure.in", "gpm_mousedriver_test=yes", "gpm_mousedriver_test=no")
    autotools.autoreconf("-vfi")

    autotools.configure("--with-slang-driver \
                         --with-x11-driver \
                         --disable-static")

def build():
    autotools.make("CC=%s" % get.CC())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*", "COPYING", "ANNOUNCE")

