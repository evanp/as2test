#!/usr/bin/env python

import sys
from getopt import getopt

opts, args = getopt(sys.argv[1:], [], ['type', 'actor-id', 'object-id'])

if opts[0][0] == '--type':
    print "Create"
elif opts[0][0] == '--actor-id':
    print "http://www.test.example/martin"
elif opts[0][0] == '--object-id':
    print "http://example.org/foo.jpg"
