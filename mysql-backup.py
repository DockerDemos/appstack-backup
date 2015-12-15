#!/usr/bin/env python

import yaml
import sys
import os
import datetime
import subprocess
import bz2

yamlfile = '/conf/.creds/dbdata.yaml'
date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
host = os.getenv('DB_PORT_3306_TCP_ADDR', None)
bakdir = '/var/backup'


def err(message):
    print ("ERROR: %s \n" % message)
    sys.exit(1)

with open(yamlfile) as file:
    data = yaml.safe_load(file)

    pw = data.get('backup', None)

    if pw is None:
        err('No password found in data container secret file')

    if host is None:
        err('No database container linked (Missing Docker ENV Variable)')

filename = date + ".sql.bz2"


p = subprocess.Popen(["mysqldump", "-A", "-C",
                      "-ubackup", "-p%s" % pw, "-h%s" % host],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE)

out, err = p.communicate()

output = bz2.BZ2File(os.path.join(bakdir, filename), 'wb')
try:
    output.write(out)
finally:
    output.close()

sys.exit(0)
