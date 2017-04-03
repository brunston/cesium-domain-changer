# changes the docker-compose.yml based on inputs in fields.conf
# brunston apr 2017

import fileinput
import re

# get the information from the conf file
conf = open('fields.conf', 'r')
domain = conf.readline().rstrip()
email = conf.readline().rstrip()
conf.close()

for line in fileinput.input(inplace=1, backup='.bak'):
    line = re.sub('test@example.com', email, line.rstrip())
    line = re.sub('example.com', domain, line.rstrip())
    print(line)

