from ._anvil_designer import frmLoginTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..mdlState import setLoggedInUser

class frmLogin(frmLoginTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)


  def btnDashboard_click(self, **event_args):
    alert("You'll need to login to access this")
    open_form('frmLogin')

  def btnSupport_click(self, **event_args):
    open_form('frmSupport')

  def btnHome_click(self, **event_args):
    open_form('frmHome')

  def btnAbout_click(self, **event_args):
    open_form('frmAbout')


# checking if user actually already used the service
  def btnLogin_click(self, **event_args):
    username = self.tbUsername.text
    password = self.tbPassword.text

    result = anvil.server.call('authenticateUser', username, password)

    if result == "exists":
      setLoggedInUser(username)
      alert("Log in successful!")
      open_form('frmInvoice')
    else:
      alert("Incorrect user credentials.")
    pass

# allowing for new users to be made
  def btnSignup_click(self, **event_args):
    open_form('frmSignup')

  def button_1_copy_click(self, **event_args):
    open_form('frmSignup')

