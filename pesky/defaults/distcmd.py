# Copyright 2010-2014 Michael Frank <msfrank@syntaxjockey.com>
#
# This file is part of Pesky.  Pesky is BSD-licensed software;
# for copyright information see the LICENSE file.

import os, json
from setuptools import Command
from distutils import log
from pkg_resources import safe_name, to_filename


class set_default(Command):

    # Brief (40-50 characters) description of the command
    description = "set default"

    # List of option tuples: long name, short name (None if no short
    # name), and help string.
    user_options = [
        ('key=', None, "set default named KEY"),
        ('value=', None, "set default to the specified VALUE"),
        ]

    def initialize_options(self):
        self.egg_name = None
        self.egg_base = None
        self.defaults_path = None
        self.key = None
        self.value = None

    def finalize_options(self):
        self.egg_name = safe_name(self.distribution.get_name())
        log.info("egg_name = " + self.egg_name)

        if self.egg_base is None:
            dirs = self.distribution.package_dir
            self.egg_base = (dirs or {}).get('',os.curdir)
        log.info("egg_base = " + self.egg_base)

        self.ensure_dirname('egg_base')
        self.egg_info = to_filename(self.egg_name) + '.egg-info'
        if self.egg_base != os.curdir:
            self.egg_info = os.path.join(self.egg_base, self.egg_info)
        log.info("egg_info = " + self.egg_info)

        self.defaults_path = os.path.join(self.egg_info, "pesky_defaults.json")
        

    def read_defaults(self):
        if not os.access(self.defaults_path, os.F_OK):
            return dict()
        with open(self.defaults_path, 'r') as f:
            return json.loads(f.read())

    def write_defaults(self, defaults):
        log.info("writing pesky defaults to %s", self.defaults_path)
        if not self.dry_run:
            with open(self.defaults_path, 'w') as f:
                f.write(json.dumps(defaults))

    def run(self):
        defaults = self.read_defaults()
        log.info("setting %s = '%s'" % (self.key, self.value))
        defaults[self.key] = self.value
        self.write_defaults(defaults)
