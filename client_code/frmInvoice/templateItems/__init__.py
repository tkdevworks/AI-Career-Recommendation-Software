from ._anvil_designer import templateItemsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class templateItems(templateItemsTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
# 

