#!/usr/bin/env python

import sys
from subprocess import check_output
import json

def test1(producer):
    command = [
        producer,
        "--type=Create",
        "--actor-id=http://www.test.example/martin",
        "--object-id=http://example.org/foo.jpg",
    ]
    result = check_output(command)
    obj = json.loads(result)
    if obj[u'@type'] != u'Create':
        raise Exception("consumer object without correct type")

if len(sys.argv) != 2:
    print "USAGE: testproducer.py <consumer>"
    sys.exit(-1)

producer = sys.argv[1]

test1(producer)
