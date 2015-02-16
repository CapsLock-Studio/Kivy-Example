# -*- coding: utf8 -*-

import random
import re
import ctypes
from kivy.config import Config
Config.set('graphics', 'height', 220)
Config.set('graphics', 'width', 500)
Config.set('graphics', 'resizable', 0)
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class root_object(GridLayout):
  def __init__(self, **kwargs):
    super(root_object, self).__init__(**kwargs)
    self.range_min_text_notice = Label(text='Please Enter Your Min Range.')
    self.add_widget(self.range_min_text_notice)
    self.range_min_text = TextInput(multiline=False, input_filter='int', hint_text='Please Enter A Number')
    self.add_widget(self.range_min_text)
    self.range_max_text_notice = Label(text='Please Enter Your Max Range.')
    self.add_widget(self.range_max_text_notice)
    self.range_max_text = TextInput(multiline=False, input_filter='int', hint_text='Please Enter A Number')
    self.add_widget(self.range_max_text)
    self.select_text_notice = Label(text='Please Your Select Number Count.')
    self.add_widget(self.select_text_notice)
    self.select_text = TextInput(multiline=False, input_filter='int', hint_text='Please Enter A Number')
    self.add_widget(self.select_text)
    self.send_button = Button(text='SEND')
    self.send_button.bind(on_press=self.btn_send)
    self.add_widget(Widget())
    self.add_widget(self.send_button)

  def btn_send(self, value):
    range_min_text = self.range_min_text.text
    range_max_text = self.range_max_text.text
    select_text = self.select_text.text

    if not re.match('^\d+$', range_min_text):
      return

    if not re.match('^\d+$', range_max_text):
      return

    if not re.match('^\d+$', select_text):
      return

    result = ''
    min_int = int(range_min_text)
    max_int = int(range_max_text)
    select_int = int(select_text)
    used_int = []
    
    if max_int < min_int:
      return

    if select_int > (max_int - min_int + 1):
      return

    while True:
      rand_int = random.randint(min_int, max_int)
      break_condition = (len(used_int) == select_int) or (len(used_int) == (max_int - min_int + 1))

      if rand_int not in used_int:
        result += str(rand_int) + ('' if break_condition else ', ')
        used_int.append(rand_int)

      if break_condition:
        break

    popup = ctypes.windll.user32.MessageBoxA
    popup(None, result, 'Result', 0)

class HelloApp(App):
  def build(self):
    self.title = 'Just Click!!'
    return root_object(cols=2, rows=4, row_force_default=True, row_default_height=40, spacing=[15, 15])

if __name__ == '__main__':
  HelloApp().run()