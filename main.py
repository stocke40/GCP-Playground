#!/usr/bin/env python

# Copied from https://cloud.google.com/source-repositories/docs/quickstart#create_a_hello_world_script 
# Also installed Python 2.7, which went EOS Dec-31 2020.  
# See also https://docs.python-guide.org/writing/structure/ 

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)