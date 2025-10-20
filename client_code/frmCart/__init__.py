from ._anvil_designer import frmCartTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..mdlState import getLoggedInUser

class frmCart(frmCartTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.rpSelections.set_event_handler('x-itemDeleteRefreshCart', self.refreshCart)
    self.refreshCart()

# button redirection
  def btnTaskAdd_click(self, **event_args):
    open_form('frmCart')

  def button_2_click(self, **event_args):
    open_form('frmAI')

  def btnRoad_click(self, **event_args):
    open_form('frmRoadmap')

  def button_2_copy_copy_copy_click(self, **event_args):
    open_form('frmSure')

  def btnSettings_click(self, **event_args):
    alert('Settings are on default mode. Please contact support if you have any bugs or glitches. Thank you')

  def btnDash_click(self, **event_args):
    open_form('frmInvoice')

  def btnOrderAgain_click(self, **event_args):
    open_form('frmOrder')

  # task adding functionalities 
  
  def refreshCart(self, **event_args):
    userId = getLoggedInUser()
    if userId:
      self.rpSelections.items = anvil.server.call('getCartItems', userId)
    else:
      alert("No user logged in!")
      self.rpSelections.items = []

  def btnConfirmOrder_click(self, **event_args):
    userId = getLoggedInUser()
    if not userId:
      alert("No user logged in!")
      return
    cartItems = anvil.server.call('getCartItems', userId)
    if not cartItems:
      alert("Cart is empty!")
      return
    open_form('frmInvoice')
