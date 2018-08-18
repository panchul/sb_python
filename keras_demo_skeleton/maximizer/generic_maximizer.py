# -*- coding: utf-8 -*-

import sys
import time
import json
from collections import defaultdict


class GenericMaximizer(object):
    flags = defaultdict()
    data = {}
    app_start_time = 0

    def __init__(self):
        """
            Initialize code
        """
        self.app_start_time = time.time()

    def get_name(self):
        return self.flags['name']

    def get_config_filename(self):
        return self.flags['config_filename']

    def indent(self, my_indent):
        if my_indent > 0:
            return " " + self.indent(my_indent-1)
        else:
            return ""

    def sys_info(self):
        """
            Prints information about where it is running on.
        """
        my_indent = 2
        # print(self.indent(my_indent), "Running on ", sys.getwindowsversion())
        print(self.indent(my_indent), "Running since ", time.ctime(self.app_start_time), " for ", time.time() - self.app_start_time, " seconds")
        print(self.indent(my_indent), "flags['name'] is ", self.flags['name'])
        print(self.indent(my_indent), "flags['quiet'] is ", self.flags['quiet'])
        print(self.indent(my_indent), "flags['debug'] is ", self.flags['debug'])
        print(self.indent(my_indent), "flags['unattended'] is ", self.flags['unattended'])
        print(self.indent(my_indent), "flags['config_filename'] is ", self.flags['config_filename'])
        print(self.indent(my_indent), "self.data is ", self.data)

    def use_command_line(self):
        """
            Interpreting the command line arguments.
        """

        if '--name' in sys.argv or '-n' in sys.argv:
            if '-n' in sys.argv:
                self.flags['name'] = sys.argv[sys.argv.index('-n')+1]
            else:
                self.flags['name'] = sys.argv[sys.argv.index('--name')+1]
        else:
            self.flags['name'] = "default_app_name"
            print("defining name as default, ", self.get_name())

        if '--config_filename' in sys.argv or '-f' in sys.argv:
            if '-f' in sys.argv:
                self.flags['config_filename'] = sys.argv[sys.argv.index('-f')+1]
            else:
                self.flags['config_filename'] = sys.argv[sys.argv.index('--config_filename')+1]
        else:
            self.flags['config_filename'] = "config/config.json"
            print("defining config_filename as default, ", self.get_config_filename())

        self.flags['quiet'] = self.flags.get('quiet', 0) or '--quiet' in sys.argv
        self.flags['debug'] = self.flags.get('debug', 0) or '--debug' in sys.argv
        self.flags['unattended'] = self.flags.get('unattended', 0) or '--unattended' in sys.argv

    def use_config_file(self):
        try:
            with open(self.get_config_filename()) as f:
                self.data = json.loads(f.read())
        except Exception as e:
            print("error", e)
            sys.exit(-1)
