#!/usr/bin/env python

import rt
import toml
import sys
from pathlib import Path

if not len(sys.argv) == 4:
    print("Please enter type, ticket number and filename")
    sys.exit(1)

replytype = sys.argv[1]
ticket = sys.argv[2]
filename = sys.argv[3]

config = toml.load('rt.toml')
rt_url = config['rt'] + "/REST/1.0"

tracker = rt.Rt(rt_url, config['user'], config['pass'], verify_cert=config['sslverify'])
tracker.login()

contents = Path(filename).read_text()
tracker.reply(ticket,text=contents)
