# Copyright 2010-2014 Michael Frank <msfrank@syntaxjockey.com>
#
# This file is part of Pesky.  Pesky is BSD-licensed software;
# for copyright information see the LICENSE file.

import sys

from pesky.defaults.errors import UndefinedDefault, DefaultsError

class Defaults(object):
    """
    """
    def __init__(self, project):
        self._project = project
        self._defaults = self._load()

    @property
    def project(self):
        return self._project

    def _load(self):
        defaults = dict()
        # load system defaults
        from mandelbrot.defaults.system import system_defaults
        for name,value in system_defaults().items():
            defaults[name] = value
        # load site overrides
        try:
            from mandelbrot.defaults.site import site_defaults
            for name,value in site_defaults().items():
                defaults[name] = value
        except ImportError, e:
            pass
        # load package overrides
        from mandelbrot.defaults.package import package_defaults
        for name,value in package_defaults(self._project).items():
            defaults[name] = value
        return defaults

    def get(self, name):
        try:
            return self._defaults[name]
        except KeyError:
            raise UndefinedDefault("default %s is undefined" % name)

    def has(self, name):
        if name in self._defaults:
            return True
        return False
