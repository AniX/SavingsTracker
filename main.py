import webapp2
from views import MainPage, Help, ViewAccounts, AddAccount, EditAccount, DeleteAccount, ViewCategories, AddCategory, EditCategory, DeleteCategory, ViewGoals, AddGoal, EditGoal, DeleteGoal, CreateNote, DeleteNote, EditNote

app = webapp2.WSGIApplication([
        ('/', MainPage), 
        ('/help', Help),
        
        ('/add_account', AddAccount),
        ('/view_accounts', ViewAccounts),
        ('/edit_account/([\d]+)', EditAccount),
        ('/delete_account/([\d]+)', DeleteAccount),
        
        ('/add_category', AddCategory),
        ('/view_categories', ViewCategories),
        ('/edit_category/([\d]+)', EditCategory),
        ('/delete_category/([\d]+)', DeleteCategory),
        
        ('/add_goal', AddGoal),
        ('/view_goals', ViewGoals),
        ('/edit_goal/([\d]+)', EditGoal),
        ('/delete_goal/([\d]+)', DeleteGoal),
        
        ('/create_note', CreateNote), 
        ('/edit_note/([\d]+)', EditNote),
        ('/delete_note/([\d]+)', DeleteNote)
        ],
        debug=True)