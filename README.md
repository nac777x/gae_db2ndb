# gae_db2ndb
There are 2 kinds of entities 
Employee is derived from db model class 
Person is derived from ndb model class

The main ('/') page has a button which migrates the instances from db to ndb model using taskqueue in one go.
I will also implement cursor on it.
