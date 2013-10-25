import jinja2
import os
import webapp2
import logging
from datetime import datetime
from google.appengine.ext import db
from google.appengine.api import users

from models import Notes, Accounts, Categories, Goals

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

# ---------- General ----------
class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))


class MainPage(BaseHandler):

    def get(self):
        user = users.get_current_user()
        logging.info('************ ' + user.nickname() + ' on MainPage *******')
        
        if user:
          notes = Notes.all().filter('owner = ', user).order('priority').order('date')
          nickname = user.nickname()
          users.create_logout_url('/')
          self.render_template('index.html', {'notes': notes,'user':user,'nickname':nickname},)
        else:
          self.redirect(users.create_login_url(self.request.uri))

class Help(BaseHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()
        logging.info('************ ' + user.nickname() + ' on Help *******')
        self.render_template('help.html', {'nickname':nickname})

        
# ---------- Accounts ----------
class ViewAccounts(BaseHandler):

    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()
        logging.info('************ ' + user.nickname() + ' on View Accounts*******')
        if user:
          accts = Accounts.all().filter('owner =', user).order('name')
          self.render_template('view_accounts.html', {'accts': accts,'nickname':nickname},)
        else:
          self.redirect(users.create_login_url(self.request.uri))

class AddAccount(BaseHandler):

    def post(self):
        user = users.get_current_user()
        a = Accounts(name=self.request.get('name'),
                     amount=float(self.request.get('amount')))
        a.put()
        logging.info('************ ' + user.nickname() + ' Added Account ' + a.name + ' *******')
        return webapp2.redirect('/view_accounts')

    def get(self):
        user = users.get_current_user()
        logging.info('************ ' + user.nickname() + ' on Add Account *******')
        nickname = user.nickname()
        self.render_template('add_account.html', {'nickname':nickname})
      

class EditAccount(BaseHandler):

    def post(self, acct_id):
        user = users.get_current_user()
        iden = int(acct_id)
        acct = db.get(db.Key.from_path('Accounts', iden))
        acct.name = self.request.get('name')
        acct.amount = float(self.request.get('amount'))
        acct.updated = datetime.now()
        acct.put()
        logging.info('************ ' + user.nickname() + ' Updated Account ' + acct.name + ' *******')
        return webapp2.redirect('/view_accounts')

    def get(self, acct_id):
        user = users.get_current_user()
        nickname = user.nickname()
        logging.info('************ ' + user.nickname() + ' on Edit Account *******')
        iden = int(acct_id)
        acct = db.get(db.Key.from_path('Accounts', iden))
        self.render_template('edit_account.html', {'acct': acct,'nickname':nickname},)

class DeleteAccount(BaseHandler):

    def get(self, acct_id):
        user = users.get_current_user()
        iden = int(acct_id)
        acct = db.get(db.Key.from_path('Accounts', iden))
        db.delete(acct)
        logging.info('************ ' + user.nickname() + ' Deleted Account ' + acct.name + ' *******')
        return webapp2.redirect('/view_accounts')

        
# ---------- Categories ---------- 

class ViewCategories(BaseHandler):

    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()
        logging.info('************ ' + user.nickname() + ' on View Categories*******')
        if user:
          cats = Categories.all().filter('owner =', user).order('name')
          self.render_template('view_categories.html', {'cats': cats,'nickname':nickname},)
        else:
          self.redirect(users.create_login_url(self.request.uri))

class AddCategory(BaseHandler):

    def post(self):
        user = users.get_current_user()
        c = Categories(name=self.request.get('name'),
                     amount=float(self.request.get('amount')))
        c.put()
        logging.info('************ ' + user.nickname() + ' Added Category ' + c.name + ' *******')
        return webapp2.redirect('/view_categories')

    def get(self):
        user = users.get_current_user()
        logging.info('************ ' + user.nickname() + ' on Add Category *******')
        nickname = user.nickname()
        self.render_template('add_category.html', {'nickname':nickname})
      

class EditCategory(BaseHandler):

    def post(self, cat_id):
        user = users.get_current_user()
        iden = int(cat_id)
        cat = db.get(db.Key.from_path('Categories', iden))
        cat.name = self.request.get('name')
        cat.amount = float(self.request.get('amount'))
        cat.updated = datetime.now()
        cat.put()
        logging.info('************ ' + user.nickname() + ' Updated Category ' + cat.name + ' *******')
        return webapp2.redirect('/view_categories')

    def get(self, cat_id):
        user = users.get_current_user()
        nickname = user.nickname()
        logging.info('************ ' + user.nickname() + ' on Edit Category *******')
        iden = int(cat_id)
        cat = db.get(db.Key.from_path('Categories', iden))
        self.render_template('edit_category.html', {'cat': cat,'nickname':nickname},)

class DeleteCategory(BaseHandler):

    def get(self, cat_id):
        user = users.get_current_user()
        iden = int(cat_id)
        cat = db.get(db.Key.from_path('Categories', iden))
        db.delete(cat)
        logging.info('************ ' + user.nickname() + ' Deleted Category ' + cat.name + ' *******')
        return webapp2.redirect('/view_categories') 
 
 
# ---------- Goals ---------- 

class ViewGoals(BaseHandler):

    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()
        logging.info('************ ' + user.nickname() + ' on View Goals*******')
        if user:
          goals = Goals.all().filter('owner =', user).order('name')
          cats = Categories.all().filter('owner =', user).order('name')
          self.render_template('view_goals.html', {'goals': goals,'cats':cats, 'nickname':nickname},)
        else:
          self.redirect(users.create_login_url(self.request.uri))

class AddGoal(BaseHandler):

    def post(self):
        user = users.get_current_user()
        categories = db.Key.from_path('Goals','category',self.request.get('category'))
        g = Goals(name=self.request.get('name'),
            category = categories,
                     amount=float(self.request.get('amount')))
        g.put()
        logging.info('************ ' + user.nickname() + ' Added Goal ' + g.name + ' *******')
        return webapp2.redirect('/view_goals')

    def get(self):
        user = users.get_current_user()
        cats = Categories.all().filter('owner =', user).order('name')
        logging.info('************ ' + user.nickname() + ' on Add Goal *******')
        nickname = user.nickname()
        self.render_template('add_goal.html', {'cats':cats,'nickname':nickname})
      

class EditGoal(BaseHandler):

    def post(self, goal_id):
        user = users.get_current_user()
        iden = int(goal_id)
        cats = Categories.all().filter('owner =', user).order('name')
        goal = db.get(db.Key.from_path('Goals', iden))
        goal.name = self.request.get('name')
        goal.category = self.request.get('id_cat')
        goal.amount = float(self.request.get('amount'))
        goal.updated = datetime.now()
        goal.put()
        logging.info('************ ' + user.nickname() + ' Updated Goal ' + goal.name + ' *******')
        return webapp2.redirect('/view_goals')

    def get(self, goal_id):
        user = users.get_current_user()
        cats = Categories.all().filter('owner =', user).order('name')
        nickname = user.nickname()
        logging.info('************ ' + user.nickname() + ' on Edit Category *******')
        iden = int(goal_id)
        goal = db.get(db.Key.from_path('Goals', iden))
        self.render_template('edit_goal.html', {'goal': goal,'cats':cats,'nickname':nickname},)

class DeleteGoal(BaseHandler):

    def get(self, goal_id):
        user = users.get_current_user()
        iden = int(goal_id)
        cats = Categories.all().filter('owner =', user).order('name')
        goal = db.get(db.Key.from_path('Goals', iden))
        db.delete(goal)
        logging.info('************ ' + user.nickname() + ' Deleted Goal ' + goal.name + ' *******')
        return webapp2.redirect('/view_goals') 
 
# ---------- Transactions ---------- 
      
# ---------- Notes ----------          
class CreateNote(BaseHandler):

    def post(self):
        n = Notes(author=self.request.get('author'),
                  text=self.request.get('text'),
                  priority=self.request.get('priority'),
                  status=self.request.get('status'))
        n.put()
        return webapp2.redirect('/')

    def get(self):
        self.render_template('create_note.html', {})
        
class EditNote(BaseHandler):

    def post(self, note_id):
        iden = int(note_id)
        note = db.get(db.Key.from_path('Notes', iden))
        note.author = self.request.get('author')
        note.text = self.request.get('text')
        note.priority = self.request.get('priority')
        note.status = self.request.get('status')
        note.date = datetime.now()
        note.put()
        return webapp2.redirect('/')

    def get(self, note_id):
        iden = int(note_id)
        note = db.get(db.Key.from_path('Notes', iden))
        self.render_template('edit_note.html', {'note': note})

class DeleteNote(BaseHandler):

    def get(self, note_id):
        iden = int(note_id)
        note = db.get(db.Key.from_path('Notes', iden))
        db.delete(note)
        return webapp2.redirect('/')
        

