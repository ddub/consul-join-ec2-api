#!python

import boto.ec2
import sys, os

conn = boto.ec2.connect_to_region(os.getenv('AWS_DEFAULT_REGION', 'us-east-1'))
reservations = conn.get_all_instances(filters={"tag:aws:autoscaling:groupName" : sys.argv[1]})
print (' '.join([i.private_ip_address for r in reservations for i in r.instances if i.state == 'running']))