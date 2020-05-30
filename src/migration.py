import webapp2
from google.appengine.ext import ndb
from helloworld import qobj
#import helloworld

class Person(ndb.Model):
    name = ndb.StringProperty()
    height = ndb.IntegerProperty()

#qobj.fetch(1)
cur = qobj.cursor()

class Migrate(webapp2.RequestHandler):
    def post(self):
        per = []
        global cur
        #cur = qobj.cursor()
        #data = qobj.with_cursor(start_cursor = cur)
        #per is localized in the below for loop
        for i in qobj.with_cursor(cur).fetch(1):
            per= Person(name = i.name, 
                     height = i.height)
            per.put()
            cur = qobj.cursor()
            
            
        
        
app = webapp2.WSGIApplication([('/migrate', Migrate)], debug = True)