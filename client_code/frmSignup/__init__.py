from ._anvil_designer import frmSignupTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class frmSignup(frmSignupTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

# adding the user in by checking they are not already a  user


  def btnDashboard_click(self, **event_args):
    alert("You'll need to login to access this")
    open_form('frmLogin')

  def btnSupport_click(self, **event_args):
    open_form('frmSupport')

  def btnHome_click(self, **event_args):
    open_form('frmHome')

  def btnAbout_click(self, **event_args):
    open_form('frmAbout')

  def btnSignup_click(self, **event_args):
    username = self.tbUsername.text
    password = self.tbPassword.text
    confirmPassword = self.tbPasswordConfirm.text
    if password != confirmPassword:
      alert("Passwords do not match. Please try again.")
    else:
      result = anvil.server.call('createUser', username, password)
      if result == "exists":
        alert("Username Taken! Please use Login option or choose a new username")
      else:
        alert("Your username and password are successfully created. Please Log in")
        open_form('frmLogin')

  def btnLogin_click(self, **event_args):
    open_form('frmLogin')

  def button_1_click(self, **event_args):
    open_form('frmLogin')



