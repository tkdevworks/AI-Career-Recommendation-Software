from ._anvil_designer import frmSureTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class frmSure(frmSureTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
# whether user replies yes or no
  def btnYes_click(self, **event_args):
    open_form('frmHome')

  def btnNo_click(self, **event_args):
    open_form("frmInvoice")

  

  
