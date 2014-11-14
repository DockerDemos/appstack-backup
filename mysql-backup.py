#!/usr/bin/env python

import yaml
import sys
import os
import datetime
import subprocess

yamlfile = '/root/.secret/dbdata.yaml'
date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
host = os.getenv('DB_PORT_3306_TCP_ADDR', None)
bakdir = '/var/backup'

def err(message):
    print ("ERROR: %s \n" % message)
    sys.exit(1)

with open(yamlfile) as file:
    data = yaml.safe_load(file)

    pw = data.get('mysql', None)

    if pw is None:
        err('No password found in data container secret file')

    if host is None:
        err('No database container linked (Missing Docker ENV Variable)')

filename = db + "_" + date + ".sql.bz2"
dumpfile = open(os.path.join(bakdir, filename), 'w')

subprocess.Popen(["mysqldump -A -C -uroot -p" + pw + " -h " + host + " | bzip2 "],
                 stdin=subprocess.PIPE,
                 stdout=dumpfile,
                 shell=True,
                 preexec_fn=os.setsid)

dumpfile.close();

sys.exit(0)

