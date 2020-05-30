import webapp2
from google.appengine.ext import db
from google.appengine.api import taskqueue
from google.net.proto2.python import public

class Employee(db.Model):
    name = db.StringProperty()
    height = db.IntegerProperty()
    
emp1 = Employee.get_or_insert('employeea', name = 'John', height = 175)
emp2 = Employee.get_or_insert('employeeb', name = 'Jack', height = 176)
emp3 = Employee.get_or_insert('employeec', name = 'Mark', height = 177)
emp4 = Employee.get_or_insert('employeed', name = 'Jordan', height = 178)



html = """<form method="post" action="/move">
                <button>Enqueue task</button>
            </form>"""

qobj = db.GqlQuery('SELECT * FROM Employee')
count = qobj.count()



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('Hello world!!<br>')
        self.response.write(html)
        print(count)
        
class TaskHandler(webapp2.RequestHandler):
    def post(self):
        queue = taskqueue.Queue(name='default')
        task = taskqueue.add(url = '/migrate')
        self.response.out.write('{} enqueued!!'.format(task.name))
        
        

        
        
        

app = webapp2.WSGIApplication([('/', MainPage), ('/move', TaskHandler)], debug=True)
