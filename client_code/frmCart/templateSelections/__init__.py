from ._anvil_designer import templateSelectionsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ...mdlState import getLoggedInUser

class templateSelections(templateSelectionsTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.lblPrice.text = f"{self.item['price']:.1f}/10.0"

  # setting up delete
  def btnDelete_click(self, **event_args):
    alert("Congratulations, another task done and dusted!")
    userId = getLoggedInUser()
    if not userId:
      alert("No user logged in!")
      return
    row = self.item
    anvil.server.call('deleteCartItem', row.get_id(),userId)
    self.parent.raise_event('x-itemDeleteRefreshCart')
    pass

