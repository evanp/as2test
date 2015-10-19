#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE
import json
import unittest

producer = None

class ProducerTestCase(unittest.TestCase):
    def setUp(self):
        command = [producer]
        for key in self.pairs:
            value = self.pairs[key]
            command.append("--%s=%s" % (key, value))
        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        result, err = p.communicate('')
        result = result.strip()
        self.obj = json.loads(result)
    def assertMatch(self, prop, expected):
        obj = self.obj
        if isinstance(obj[prop], unicode):
            assert obj[prop] == expected, "producer created object with %s = %s instead of %s" % (prop, obj[prop], expected)
        elif isinstance(obj[prop], list):
            assert expected in obj[prop], "expected value %s not in object property %s (%s)" % (expected, prop, obj[prop])

class Example1TestCase(ProducerTestCase):
    """Tests for Example 1 from activitystreams-core"""
    pairs = {
      "type": "Create",
      "actor": "http://www.test.example/martin",
      "object": "http://example.org/foo.jpg"
    }
    def test_type(self):
        """Test that type from example 1 is generated correctly"""
        self.assertMatch(u'@type', u'Create')

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "USAGE: testproducer.py <producer>"
        sys.exit(-1)

    producer = sys.argv[1]
    del sys.argv[1]

    unittest.main()
