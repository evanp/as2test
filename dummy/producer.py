#!/usr/bin/env python

import sys
from getopt import getopt

opts, args = getopt(sys.argv[1:], [], ['type=', 'actor-id=', 'object-id='])

for opt in opts:
    if opt[0] == '--type' and  opt[1] == "Create":
        print """
        {
          "@context": "http://www.w3.org/ns/activitystreams",
          "@type": "Create",
          "actor": "http://www.test.example/martin",
          "object": "http://example.org/foo.jpg"
        }
        """
