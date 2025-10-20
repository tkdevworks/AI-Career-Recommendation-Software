from ._anvil_designer import frmAITemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..mdlState import getLoggedInUser

class frmAI(frmAITemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
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

  # generating the recommendations

  def button_1_click(self, **event_args):
    interests = self.tbInterests.text
    hobbies = self.tbHobbies.text
    subjects = self.tbSubjects.text + " Year" + self.tbYear.text
    aims = self.tbAims.text
    skills = self.tbSkills.text

    if not all([interests, hobbies, subjects, aims, skills]):
      alert("Please fill in all fields.")
      return

    userId = getLoggedInUser()
    if not userId:
      alert("No user logged in!")
      return


    anvil.server.call('deleteData', userId)

    advice = anvil.server.call(
      'career_advice',
      interests, hobbies, subjects, aims, skills
     )

    anvil.server.call('addData', interests, hobbies, subjects, aims, skills, userId, advice)
    
    self.lblResponse.text = advice

    # for the followup feature

  def btesend_click(self, **event_args):
    followup = self.text_area_1.text
    if not followup.strip():
      alert("Please fill in")

    self.userId = getLoggedInUser()
    if not self.userId:
      alert("No user logged in!")
      return

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
      
    word = anvil.server.call('followup', interests, hobbies, subjects, aims, skills, advice, followup)
    self.lblResponse.text = word
    

    
