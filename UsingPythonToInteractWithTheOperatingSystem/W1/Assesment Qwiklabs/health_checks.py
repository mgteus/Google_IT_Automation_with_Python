#!/usr/bin/env python3
import shutil
import psutil

from network import *

def check_disk_usage(disk):
    """Verifies that there's enough free space on dick"""
    du = shutil.disk_usage(disk)
    free == du.free / du.total *100
    return free > 20

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75
# If there's not enough disk, or not enough cpu, print an error
if not check_disk_usage('/') and not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")
