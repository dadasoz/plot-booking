#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    argvs = sys.argv

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plots.openshift_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(argvs)
