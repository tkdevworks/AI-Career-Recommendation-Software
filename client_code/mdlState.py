import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

loggedInUser = None

# creating user
def setLoggedInUser(username):
  global loggedInUser
  loggedInUser = username
  
# getting user for checks
def getLoggedInUser():
  return loggedInUser
