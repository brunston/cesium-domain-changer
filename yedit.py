# changes the docker-compose.yml based on inputs in fields.conf
# brunston apr 2017
# mit license

import re
import sys

try:
    yaml = open('docker-compose.yml', 'w')
except FileNotFoundError:
    sys.exit("YAML file docker-compose.yml not found")

# get the information from the conf file
conf = open('fields.conf', 'r')
domain = conf.readline().rstrip()
email = conf.readline().rstrip()
conf.close()

for line in yaml:
    line = re.sub('test@example.com', email, line.rstrip())
    line = re.sub('example.com', domain, line.rstrip())

yaml.close()
