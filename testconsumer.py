#!/usr/bin/env python

import sys
import os
from subprocess import Popen, PIPE
from StringIO import StringIO

def test1(consumer):
    activity = """
                {
                  "@context": "http://www.w3.org/ns/activitystreams",
                  "@type": "Create",
                  "actor": "http://www.test.example/martin",
                  "object": "http://example.org/foo.jpg"
                }
                """
    p = Popen([consumer, "--type"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result, err = p.communicate(activity)
    result = result.strip()
    if result != "Create":
        raise Exception("consumer returned '%s' instead of correct type '%s' for test1" % (result, "Create"))

if len(sys.argv) != 2:
    print "USAGE: testconsumer.py <consumer>"
    sys.exit(-1)

consumer = sys.argv[1]

test1(consumer)
