#!/usr/bin/env python

import sys
from getopt import getopt

opts, args = getopt(sys.argv[1:], [], ['type'])

if opts[0][0] == '--type':
    print "Create"
