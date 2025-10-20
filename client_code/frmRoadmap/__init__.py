from ._anvil_designer import frmRoadmapTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..mdlState import getLoggedInUser

class frmRoadmap(frmRoadmapTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.userId = getLoggedInUser()
    if not self.userId:
      alert("No user logged in!")
      return
    steps = anvil.server.call('get_user_roadmap', self.userId)
    self.rpRoad.items = steps

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

  

  def btnGenerate_click(self, **event_args):
    self.userId = getLoggedInUser()
    if not self.userId:
      alert("No user logged in!")
      return
    
#saving the roadmap functionality
    userRow = app_tables.data.get(userId=self.userId)
    if not userRow:
      alert("No user data found. Please fill in your profile first.")
      return

    interests = userRow['interests']
    hobbies = userRow['hobbies']
    subjects = userRow['subjects']
    aims = userRow['aims']
    skills = userRow['skills']
    advice = userRow['advice']

    roadmapText = anvil.server.call('createRoad', interests, hobbies, subjects, aims, skills, advice)

    steps = []
    blocks = roadmapText.strip().split("\n\n")
    for block in blocks:
      lines = block.strip().split("\n")
      if not lines:
        continue
      title = lines[0].strip()
      dotpoints = [l.replace("§","").strip() for l in lines[1:] if l.strip()]
      steps.append({"title": title, "dotpoints": dotpoints})

    # 
    anvil.server.call('save_roadmap', self.userId, steps)

    
    self.rpRoad.items = steps
    self.text_area_1.text = "Step 5: Enjoy your lasting success!"

  def btnDelete_click(self, **event_args):
    if self.userId:
      anvil.server.call('delete_user_roadmap', self.userId)
      self.rpRoad.items = []  # Clear display
      alert("Roadmap deleted")