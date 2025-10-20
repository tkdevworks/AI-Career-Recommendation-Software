from ._anvil_designer import frmHomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class frmHome(frmHomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # button redirection

  def btnLogin_click(self, **event_args):
    open_form('frmLogin')

  def btnSignup_click(self, **event_args):
    open_form('frmSignup')

  def btnDashboard_click(self, **event_args):
    alert("You'll need to login to access this")
    open_form('frmLogin')

  def btnSupport_click(self, **event_args):
    open_form('frmSupport')

  def btnHome_click(self, **event_args):
    open_form('frmHome')

  def btnAbout_click(self, **event_args):
    open_form('frmAbout')

  def button_1_click(self, **event_args):
    open_form('frmLogin')