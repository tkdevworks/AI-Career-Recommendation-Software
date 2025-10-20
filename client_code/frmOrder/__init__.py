from ._anvil_designer import frmOrderTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..mdlState import getLoggedInUser

class frmOrder(frmOrderTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

# allowing user to continuously add tasks
  def cartAdd_click(self, **event_args):
    userId = getLoggedInUser()
    if not userId:
      alert("No user logged in!")
      return
    mealSize = self.ddSize.selected_value
    if not mealSize:
      alert("Please select a priority level.")
      return
    
    anvil.server.call('incrementTasksAdded', userId)


    #  value score system
    basePrices = {'Low': 3.0 , 'Medium': 5.0, 'High': 7.0}
    price = basePrices[mealSize]
   
    taskName = self.tbTaskName.text
    if taskName == "":
      alert("Please name your task")
   
    timeTake = self.ddTime.selected_value
    if not timeTake:
      alert("Please select time taken.")
      return
   
    datePick = self.date.date
    if not datePick:
      alert("Please select date")
      return
    

    addOns = []
    if self.cbHam.checked:
      addOns.append('Extra Learning')
      price += 1.0
    if self.cbPrawns.checked:
      addOns.append('Subject Work')
      price += 1.0
    if self.cbSalami.checked:
      addOns.append('Revision')
      price += 1.0

    # giving them the message and actually storing it
    anvil.server.call('addToCart', mealSize, addOns, price,userId, timeTake, taskName, datePick)
    addOnsStr = ", ".join(addOns) if addOns else "None"
    self.lblOrder.text = f"The following task has been added: {taskName} with the priority {mealSize} in category {addOnsStr}. Recommended time is {timeTake} within date {datePick}. Value score assigned is {price:.1f}/10.0"

    #
    self.ddSize.selected_value = None
    self.cbHam.checked = False
    self.cbPrawns.checked = False
    self.cbSalami.checked = False
    self.date.date = None
    self.ddTime.selected_value = None
    self.tbTaskName.text = None
    pass

  def cartGo_click(self, **event_args):
    open_form('frmCart')


  def ddSize_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def btnCartGo_click(self, **event_args):
    open_form('frmInvoice')

  
