from ._anvil_designer import frmInvoiceTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..mdlState import getLoggedInUser
import random

class frmInvoice(frmInvoiceTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
  
    userId = getLoggedInUser()
    self.rpInvoice.items = anvil.server.call('getCartItems',userId)
    self.rpAdvice.items = anvil.server.call('getData', userId)
    self.updateTaskCounters()

    
    # all button redirection
    
    
    def btnTaskAdd_click(self, **event_args):
      open_form('frmCart')

  def button_2_click(self, **event_args):
    open_form('frmAI')

  def btnRoad_click(self, **event_args):
    open_form('frmRoadmap')

  def button_2_copy_copy_copy_click(self, **event_args):
    open_form('frmSure')

  def btnLogout_click(self, **event_args):
    open_form('frmSure')

  def btnSettings_click(self, **event_args):
    alert('Settings are on default mode. Please contact support if you have any bugs or glitches. Thank you')

  def btnDash_click(self, **event_args):
    open_form('frmInvoice')

  # plotly graphs  (6 of them) utilising the import plotly function


  
  def updateTaskCounters(self):
    userId = getLoggedInUser()
    if not userId:
      return
    openTasks = anvil.server.call('getOpenTasks', userId)
    tasksAdded = anvil.server.call('getTasksAdded', userId)
    completedTasks = tasksAdded - openTasks

    self.lblOpen.text = openTasks
    self.lblTasks.text = tasksAdded
    self.lblComp.text = completedTasks

    fig1 = go.Figure(data=[go.Pie(
      labels=['Completed', 'Open'],
      values=[completedTasks, openTasks],
      hole=0.4
    )])
    self.plot_1.figure = fig1
    fig2 = go.Figure(data=[go.Bar(
      x=['Tasks Added', 'Completed', 'Open'],
      y=[tasksAdded, completedTasks, openTasks],
      marker_color=['blue', 'green', 'red']
    )])
    self.plot_2.figure = fig2
    fig3 = go.Figure(data=[
      go.Bar(name='Completed', x=['Tasks'], y=[completedTasks], marker_color='green'),
      go.Bar(name='Open', x=['Tasks'], y=[openTasks], marker_color='red')
    ])
    fig3.update_layout(barmode='stack')
    self.plot_3.figure = fig3
    fig4 = go.Figure(data=[go.Indicator(
      mode="gauge+number",
      value=completedTasks,
      number={'suffix': f"/{tasksAdded}"},
      gauge={'axis': {'range': [0, max(1, tasksAdded)]},
             'bar': {'color': "green"},
             'steps': [{'range': [0, openTasks], 'color': "red"}]}
    )])
    self.plot_4.figure = fig4
    fig5 = go.Figure(data=[
      go.Scatter(
        x=['Start', 'Now'],
        y=[0, completedTasks],
        fill='tozeroy',
        mode='lines+markers',
        name='Completed Tasks',
        line_color='green'
      ),
      go.Scatter(
        x=['Start', 'Now'],
        y=[0, openTasks],
        fill='tozeroy',
        mode='lines+markers',
        name='Open Tasks',
        line_color='red'
      )
    ])
    self.plot_5.figure = fig5
    remaining = max(0, tasksAdded - (completedTasks + openTasks))
    fig6 = go.Figure(data=[go.Pie(
      labels=['Completed', 'Open', 'Remaining to Add'],
      values=[completedTasks, openTasks, remaining],
      hole=0.5
    )])
    self.plot_6.figure = fig6

  def btnTaskAdd_click(self, **event_args):
    open_form('frmCart')







