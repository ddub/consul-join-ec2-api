#!/usr/local/bin/python

import boto.ec2
import sys
import os

conn = boto.ec2.connect_to_region(
    os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
)
reservations = conn.get_all_instances(
    filters={sys.argv[1]: sys.argv[2]}
)
joinflag = ' -{}join '.format(os.getenv('CONSUL_JOIN', ''))
print ('{} {}'.format(
    joinflag,
    joinflag.join([i.private_ip_address
                   for r in reservations
                   for i in r.instances
                   if i.state == 'running'])))
