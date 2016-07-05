#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    argvs = sys.argv

    if "dev" in argvs:
        argvs.remove("dev")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plots.dev_settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plots.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(argvs)
