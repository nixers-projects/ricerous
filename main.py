#!/usr/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.uix.popup import Popup

from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty, ObjectProperty
from getpass import getuser
from socket import gethostname
from backend import JsonInfoReader, State, Outputer
import time
import os


jfile = JsonInfoReader.JsonInfoReader("info.json")
state = State.State()
out   = Outputer.Outputer("plugins")

subButtons = {}

DEFAULT_ON_OPEN    = "Bootloader"

DEFAULT_COMMENT    = "Insert a comment here\n\n"
UPDATE_SUCC_TEXT   = "Update Successful! :)"
UPDATE_UNSUCC_TEXT = "Update Unsuccessful :( "
NO_UPDATE_TEXT     = "No new update available"
HELP_TEXT          = """
Check info about riceable things.
Mark them as riced.
Comment on them about what you've done.
Export or import your setup to use in the program later.
Output to different visual formats.
"""

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class TitleBar(BoxLayout):

    def __init__(self, **kwargs):
        super(TitleBar, self).__init__(**kwargs)


class Prompt(Label):

    def __init__(self, **kwargs):
        super(Prompt, self).__init__(**kwargs)
        self.text = getuser() + "@" + gethostname()


class SwitchScreen(BoxLayout):
    accordion = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SwitchScreen, self).__init__(**kwargs)
        self.accordion.bind(selected=self.viewitem)
        self.infos = InfoScreen(DEFAULT_ON_OPEN)
        self.add_widget(self.infos)

    def viewitem(self, object, text):
        self.remove_widget(self.infos)
        self.infos = InfoScreen(text)
        self.add_widget(self.infos)


class InfoScreen(BoxLayout):
    # txts = ObjectProperty(None)

    def __init__(self, value = "", **kwargs):
        super(InfoScreen, self).__init__(**kwargs)
        self.value = value
        self.orientation = "vertical"
        if not self.value: return
        width = self.width
        height = self.height

        self.add_widget(HeadInfo(self.value))

        global jfile
        inst = jfile

        inf = inst.getInfo(self.value)
        txts = TextInput(text = inf, background_color = (0.15, 0.15, 0.15, 1),
            foreground_color = (1, 1, 1, 1), multiline = True, readonly = True,
            size_hint = (1.0, None))
        txts.bind(minimum_height=txts.setter('height'))
        txts.text = inf
        scroll = ScrollView(size_hint = (1, 1), size = (width, height))
        scroll.add_widget(txts)
        self.add_widget(scroll)

        scroll2 = ScrollView(size_hint = (1, 0.2), size = (width, height))
        comments = TextInput(multiline=True, foreground_color = [0.9, 0.9, 0.9, 1], 
            size_hint = (1.0, None), background_color = (0.5, 0.5, 0.5,1))
        comments.bind(minimum_height=comments.setter('height'))
        if self.value in state.comments.keys():
            comments.text = state.comments[self.value]
        else :
            comments.text = DEFAULT_COMMENT
        
        comments.bind(text=self.on_text)

        scroll2.add_widget(comments)
        self.add_widget(scroll2)

        self.add_widget(ButtonBar())
    
    def on_text(self, instance, newText):
        #remove trailing spaces
        newText             = newText.rstrip()
        defaultWithoutSpace = DEFAULT_COMMENT.replace(" ","").replace("\n","")
        newTextWithoutSpace = newText.replace(" ","").replace("\n","")
        if newTextWithoutSpace in defaultWithoutSpace or newTextWithoutSpace == "":
            if self.value in state.comments.keys():
                del(state.comments[self.value])
        else:
            state.comments[self.value] = newText


class HeadInfo(Widget):
    header = ObjectProperty(None)

    def __init__(self, value, **kwargs):
        super(HeadInfo, self).__init__(**kwargs)
        self.header.text = value
        self.value = value
        if self.value in state.selected:
            self.riced.active = True
        else :
            self.riced.active = False
        self.riced.bind(active=self.on_checkbox_active)

    def resetState(self):
        if self.value in state.selected:
            self.riced.active = True
        else :
            self.riced.active = False
        if self.header.text in self.state.comments.keys():
            self.riced.text = self.state.comments[self.header.text]


    def on_checkbox_active(self, checkbox, value):
        if value:
            if self.header.text not in state.selected:
                state.selected.append(self.header.text)
                subButtons[self.header.text].color = [ 0.306, 0.464, 0.80, 1]
        else:
            if self.header.text in state.selected:
                state.selected.remove(self.header.text)
                subButtons[self.header.text].color = [1.0, 1.0, 1.0,1]

class AccordionThing(Accordion):
    selected = StringProperty("")

    def __init__(self, **kwargs):
        super(AccordionThing, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.blades      = []
        subButtons       = []
        self.draw()

    def switch(self, object):
        self.selected = object.text

    def draw(self):
        global jfile
        inst = jfile

        for cat in inst.listCategories():
            self.blades.append(AccordionItem(title = cat, font_size = "20sp"))
            box = BoxLayout(orientation = 'vertical')
            subs = inst.listInsideCategories(cat)

            for sub in subs:
                butt = Button(text = sub, background_color = [0.35, 0.35, 0.35,
                    1], font_size = "16sp", size_hint_y = 0.1)
                butt.bind(on_press = self.switch)
                subButtons[sub] = butt
                box.add_widget(butt)

            self.blades[-1].add_widget(box)
            self.add_widget(self.blades[-1])

        self.blades[-1].collapse = True
        self.blades[0].collapse = False


class ButtonBar(BoxLayout):

    def __init__(self, **kwargs):
        super(ButtonBar, self).__init__(**kwargs)
        self.outputing = False

    def showImport(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Import config", content=content,
            size_hint=(0.9, 0.9))
        self._popup.open()

    def showExport(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def save(self, path, filename):
        try:
            if self.outputing==True:
                selected = ""
                for choice in self.allChoices:
                    if choice.state == 'down':
                        selected = choice.text
                        break
                out.output(selected,state,jfile,os.path.join(path,filename))
            else:
                state.save(os.path.join(path, filename))
            self.dismiss_popup()
        except Exception:
            self.error("Could not save to file")

    def showHelp(self):
        content = BoxLayout(orientation = 'vertical')
        content.add_widget(Label(text=HELP_TEXT))
        closeButton = Button(text='Close',size_hint_y = 0.15)
        content.add_widget(closeButton)
        self._popup = Popup(title='Help', content=content,size_hint=(0.9, 0.9))
        closeButton.bind(on_press=self._popup.dismiss)
        self._popup.open()

    def showUpdate(self):
        try:
            status = jfile.update()
            content = BoxLayout(orientation = 'vertical')
            if status == 0:
                content.add_widget(Label(text=UPDATE_SUCC_TEXT))
            elif status == -1:
                content.add_widget(Label(text=UPDATE_UNSUCC_TEXT))
            else :
                content.add_widget(Label(text=NO_UPDATE_TEXT))
            self._popup = Popup(title='Update', content=content,size_hint=(0.6, 0.6))
            self._popup.open()
        except Exception:
            self.error("Could not perform update")

    def showOutput(self):
        content = BoxLayout(orientation='vertical')

        box = BoxLayout(orientation='vertical')
        availables = out.getAvailable()
        first = True
        self.allChoices = []
        for available in availables:
            checkbox = ToggleButton(text=available, group='output')
            self.allChoices.append(checkbox)
            if first:
                checkbox.state = 'down'
                first = False
            box.add_widget(checkbox)
        content.add_widget(box)

        menu = BoxLayout(orientation = "horizontal", size_hint_y = 0.2)
        cancelButton = Button(text="Cancel")
        outputButton = Button(text="Output")
        menu.add_widget(outputButton)
        menu.add_widget(cancelButton)
        content.add_widget(menu)

        self._popup = Popup(title="Output", content= content, size_hint=(0.9,0.9))
        cancelButton.bind(on_release=self.cancelOutput)
        self.outputing = True
        outputButton.bind(on_release=self.saveOutput)
        self._popup.open()

    def cancelOutput(self,what):
        self.dismiss_popup()

    def saveOutput(self,what):
        self.dismiss_popup()
        self.outputing = True
        self.showExport()

    def load(self, path, filename):
        try:
            state.load(os.path.join(path,filename[0]))
            #reset the buttons
            for subButton in subButtons.values():
                subButton.color = [1.0,1.0,1.0,1]
            for select in state.selected:
                subButtons[select].color = [ 0.306, 0.464, 0.80, 1]
            self.dismiss_popup()
        except Exception:
            self.error("Could not load config file")

    def error(self, message):
        self.dismiss_popup()
        content = BoxLayout(orientation = 'vertical')
        content.add_widget(Label(text=message))
        closeButton = Button(text='OK',size_hint_y = 0.15)
        content.add_widget(closeButton)
        self._popup = Popup(title='Error', content=content,size_hint=(0.5, 0.5))
        closeButton.bind(on_press=self._popup.dismiss)
        self._popup.open()


    def dismiss_popup(self):
        self.outputing = False
        self._popup.dismiss()


class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        titleb = TitleBar()
        switch = SwitchScreen()
        switch.viewitem(object, DEFAULT_ON_OPEN)
        self.add_widget(titleb)
        self.add_widget(switch)


class RiceApp(App):

    def build(self):
        win = MainScreen()
        Window.clearcolor = (0.15, 0.15, 0.15, 1)
        return win


if __name__ == '__main__':
  RiceApp().run()
