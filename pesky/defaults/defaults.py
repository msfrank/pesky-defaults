# Copyright 2010-2014 Michael Frank <msfrank@syntaxjockey.com>
#
# This file is part of Pesky.  Pesky is BSD-licensed software;
# for copyright information see the LICENSE file.

import sys, collections

from pesky.defaults.errors import UndefinedDefault, DefaultsError

class Defaults(collections.Mapping):
    """
    """
    def __init__(self, project=None):
        self._project = project
        self._defaults = self._load(project)

    @property
    def project(self):
        return self._project

    def _load(self, project):
        defaults = dict()
        # load system defaults
        from pesky.defaults.system import system_defaults
        for name,value in system_defaults().items():
            defaults[name] = value
        # load site overrides if the module exists
        try:
            from pesky.defaults.site import site_defaults
            for name,value in site_defaults().items():
                defaults[name] = value
        except ImportError, e:
            pass
        # load package overrides
        if project is not None:
            from pesky.defaults.package import package_defaults
            for name,value in package_defaults(project).items():
                defaults[name] = value
        return defaults

    def get(self, name):
        try:
            return self._defaults[name]
        except KeyError:
            raise UndefinedDefault("default %s is undefined" % name)

    def getorelse(self, name, default=None):
        try:
            return self._defaults[name]
        except KeyError:
            return default

    def has(self, name):
        if name in self._defaults:
            return True
        return False

    def __getitem__(self, name):
        return self._defaults[name]

    def __iter__(self):
        return iter(self._defaults)

    def __len__(self):
        return len(self._defaults)
