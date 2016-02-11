#!/usr/local/bin/python

import boto.ec2
import sys
import os

if len(sys.argv) < 4:
    print('3 arguments required, filter-by filter-match subnet-id')
    sys.exit(101)

conn = boto.ec2.connect_to_region(
    os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
)

reservations = conn.get_all_instances(
    filters={sys.argv[1]: sys.argv[2]}
)

subnet_id = sys.argv[3]

joinflag = ' -{}join '.format(os.getenv('CONSUL_JOIN', ''))

lan = [i.private_ip_address
       for r in reservations
       for i in r.instances
       if i.state == 'running' and i.subnet_id == subnet_id]

if len(lan) < 2:
    print('Insufficient peers found: {}'.format(len(lan)))
    sys.exit(102)

sys.stdout.write('{}{}'.format(
    joinflag,
    joinflag.join(lan)))

wan = [i.private_ip_address
       for r in reservations
       for i in r.instances
       if i.state == 'running' and i.subnet_id != subnet_id]
if len(wan) > 0:
    wanflag = ' -join-wan '
    sys.stdout.write('{}{}'.format(
        wanflag,
        wanflag.join(wan)))
sys.stdout.flush()
