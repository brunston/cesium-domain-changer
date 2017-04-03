# changes the cesium_web/public/scripts/main.jsx to use wss instead of ws
# (secure websocket connections)
# brunston apr 2017

import fileinput
import re

for line in fileinput.input(inplace=1, backup='.bak'):
    line = re.sub('ws://', 'wss://', line.rstrip())
    print(line)

