from google.appengine.ext import db

class Notes(db.Model):

    author = db.StringProperty()
    owner = db.UserProperty(auto_current_user_add=True)
    text = db.StringProperty(multiline=True)
    priority = db.StringProperty()
    status = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    
# class Chats(db.Model):

    # author = db.StringProperty()
    # message = db.StringProperty(multiline=True)
    # owner = db.UserProperty(auto_current_user_add=True)
    # date = db.DateTimeProperty(auto_now_add=True)
    # updated = db.DateTimeProperty(auto_now=True)

class Accounts(db.Model):

    name = db.StringProperty(required=True)
    amount = db.FloatProperty(required=True)
    owner = db.UserProperty(auto_current_user_add=True)
    date = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    
class Categories(db.Model):

    name = db.StringProperty(required=True)
    amount = db.FloatProperty(required=True)
    owner = db.UserProperty(auto_current_user_add=True)
    date = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    
class Goals(db.Model):

    name = db.StringProperty(required=True)
    amount = db.FloatProperty(required=True)
    category = db.ReferenceProperty(Categories)
    owner = db.UserProperty(auto_current_user_add=True)
    date = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    
# class Transactions(db.Model):

    # account = db.ReferenceProperty(Accounts, collection_name='Accounts')
    # category = db.ReferenceProperty(Categories, collection_name='Categories')
    # goal = db.ReferenceProperty(Goals, collection_name='Goals')
    # amount = db.FloatProperty(required=True)
    # owner = db.UserProperty(auto_current_user_add=True)
    # date = db.DateTimeProperty(auto_now_add=True)
    # updated = db.DateTimeProperty(auto_now=True)
