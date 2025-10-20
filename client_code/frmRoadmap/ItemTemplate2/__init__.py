from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    self.init_components(**properties)

   
    if not self.item:
      return

   
    text = f"{self.item['title']}\n"
    for point in self.item['dotpoints']:
      text += f"• {point}\n"

      
    self.text_area_1.text = text
