import webapp2
from google.appengine.ext import ndb
from helloworld import qobj, Employee
import helloworld

class Person(ndb.Model):
    name = ndb.StringProperty()
    height = ndb.IntegerProperty()
    
class Migrate(webapp2.RequestHandler):
    def post(self):
        per = []
        #per is localized in the below for loop
        for i in qobj:
            per= Person(name = i.name, 
                     height = i.height)
            per.put()
        
        
app = webapp2.WSGIApplication([('/migrate', Migrate)], debug = True)