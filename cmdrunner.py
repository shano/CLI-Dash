#!/usr/bin/python
'''
author:Shane Dowling
date:29/12/10

This class represents a rough bunch of functions for getting data from the os
'''

import subprocess

class cmdRunner:
    def __init__(self):
        pass

    def resolve_func(self, func):
        func_lookup = {
                "running":"get_is_running",
                "ext_ip":"get_external_ip",
                "int_ip":"get_internal_ip",
                "free_space":"get_avail_space",
                "total_space":"get_total_space",
                "cpu_use":"get_cpu_use",
                "mem_use":"get_mem_use",
                }
        return func_lookup[func]

    def get_avail_space(self):
        import os
        s = os.statvfs('/')
        return "Avail Space: " + str((s.f_frsize * s.f_bavail) / (1024 * 1024 * 1024)) + " GB"

    def get_total_space(self):
        import os
        s = os.statvfs('/')
        return "Total Space: " + str((s.f_frsize * s.f_blocks) / (1024 * 1024 * 1024)) + " GB"

    def get_cpu_use(self):
        import psutil
        return "CPU:" + str("%.2f" % round(psutil.cpu_percent(),2)) + "%"

    def get_mem_use(self):
        import psutil
        mem_percent = (psutil.avail_phymem()*100)/psutil.TOTAL_PHYMEM
        return "MEM:" + str(mem_percent) + "%"

    def get_internal_ip(self):
        import socket
        ips = ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0])
        return "Internal IPs:" + ips 

    def get_external_ip(self):
        import urllib
        whatismyip = 'http://www.whatismyip.com/automation/n09230945.asp'
        return "External IP:" + urllib.urlopen(whatismyip).readlines()[0]

    def get_is_running(self, process_name):
        import commands
        output = commands.getoutput('ps -A')
        if process_name in output:
          return process_name + " is running"
        else:
          return process_name + " is not running"

    def execute_cmd(self, cmd_string):
        a = system(cmd_string)
        return a

    def default_func(self):
        pass

    def do_command(self, cmd, *args):
        return getattr(self, cmd, self.default_func)(*args)
