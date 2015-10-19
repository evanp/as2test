#!/usr/bin/env python

import sys
import os
from subprocess import Popen, PIPE
import unittest

consumer = None

class ConsumerTestCase(unittest.TestCase):
    def run_consumer(self, data, arg, expected):
        p = Popen([consumer, arg], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        result, err = p.communicate(data)
        result = result.strip()
        if isinstance(expected, str):
            assert result == expected, "consumer returned '%s' instead of '%s'" % (result, expected)
        elif isinstance(expected, list):
            assert result in expected, "consumer returned '%s' not in '%s'" % (result, expected.join(','))

class Example1TestCase(ConsumerTestCase):
    example1 = """
{
  "@context": "http://www.w3.org/ns/activitystreams",
  "@type": "Create",
  "actor": "http://www.test.example/martin",
  "object": "http://example.org/foo.jpg"
}
"""
    def test_type(self):
        self.run_consumer(self.example1, "--type", ["Create", "http://www.w3.org/ns/activitystreams#Create"])

    def test_actor_id(self):
        self.run_consumer(self.example1, "--actor-id", "http://www.test.example/martin")

    def test_object_id(self):
        self.run_consumer(self.example1, "--object-id", "http://example.org/foo.jpg")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "USAGE: testconsumer.py <consumer>"
        sys.exit(-1)

    consumer = sys.argv[1]
    del sys.argv[1]

    unittest.main()
