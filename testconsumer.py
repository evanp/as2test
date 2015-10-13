#!/usr/bin/env python

import sys
import os
from subprocess import Popen, PIPE
from StringIO import StringIO

activity1 = """
            {
              "@context": "http://www.w3.org/ns/activitystreams",
              "@type": "Create",
              "actor": "http://www.test.example/martin",
              "object": "http://example.org/foo.jpg"
            }
            """

def run_test(consumer, data, arg, expected):
    p = Popen([consumer, arg], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result, err = p.communicate(data)
    result = result.strip()
    if isinstance(expected, str):
        if result != expected:
            raise Exception("consumer returned '%s' instead of '%s'" % (result, expected))
    elif isinstance(expected, list):
        if result not in expected:
            raise Exception("consumer returned '%s' not in '%s'" % (result, expected.join(',')))

def test1(consumer):
    run_test(consumer, activity1, "--type", ["Create", "http://www.w3.org/ns/activitystreams#Create"])

def test2(consumer):
    run_test(consumer, activity1, "--actor-id", "http://www.test.example/martin")

def test3(consumer):
    run_test(consumer, activity1, "--object-id", "http://example.org/foo.jpg")

if len(sys.argv) != 2:
    print "USAGE: testconsumer.py <consumer>"
    sys.exit(-1)

consumer = sys.argv[1]

test1(consumer)
test2(consumer)
test3(consumer)
