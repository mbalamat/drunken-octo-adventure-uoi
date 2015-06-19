#!/usr/bin/env python

import os
import subprocess

p = subprocess.Popen("hostname", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()



x="scylla.cs.uoi.gr"



if x in output:
	os.system("ssh hp6000ws02")
else:
	print "Connected"

