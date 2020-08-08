#! /usr/bin/python3

import os
import sys

mount_point = ""

if (len(sys.argv) > 1):
    mount_folder = sys.argv[1]
    mount_point = "/mnt/" + mount_folder.replace('/', '')
else:
    print("Please specify a mount point.")
    exit()

# Resolving mount point
if (not os.path.exists(mount_point)):
    print('Creating mount point.')
    ret = os.system('mkdir {}'.format(mount_point))
    if (ret): 
        print("Make sure you have right permission.")
        exit()

# mounting webdav
domain = "https://dms.uom.lk"
ret = os.system('mount -t davfs -o noexec {}/remote.php/webdav/ {}'.format(domain, mount_point))
