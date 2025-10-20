from ._anvil_designer import frmSupportTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class frmSupport(frmSupportTemplate):
  def __init__(self, **properties):
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

