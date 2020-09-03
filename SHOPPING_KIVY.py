
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock


# Creates the main app class.
# Uses two custom .png images which need to be stored in the same location
# as this .py file. Set the .png images to whatever you want with any size.
# In this script they are 796x300.

class StartPage(App):
    def build (self):
         
        StartPage.TopLayout =BoxLayout(padding='2sp',
                             spacing ='10sp',
                             orientation ='vertical',
                             size =(Window.width, Window.height))
       
        StartPage.Layout1 = GridLayout(cols=1,
                             spacing='2sp',
                             size_hint_y=1)
        
#       Unconventional, but was the quickest way to give the 'Label' a background colour.
        L1 = Button (text ='Shopping List',
                     size_hint_y =None,
                     height ='60sp',
                     font_size ='40sp',
                     background_disabled_normal =('LabelBackground.png'), 
                     disabled =True)
                    
       
        StartPage.E1 = TextInput (hint_text ='Type item here:',
                                  hint_text_color =(0.76, 0.76, 0.76, 1),
                                  cursor_color =(0.76, 0.76, 0.76, 1),
                                  foreground_color =(1, 1, 1, 1),
                                  halign ='center',                                 
                                  font_size ='40sp',
                                  size_hint_y =None,
                                  height ='60sp',
                                  background_normal ='',
                                  background_color =(0.45, 0.45, 0.45, 1),
                                  multiline =False)
        
        B1 = Button (text ='ADD',
                     font_size ='40sp',
                     background_normal =('LabelBackground.png'),
                     bold =True)
        B1.bind (on_press = ListManager.ListAppend)
        
        B2 = Button (text ='DONE',
                     font_size ='40sp',
                     background_normal =('LabelBackground.png'),
                     bold =True)
        B2.bind (on_press = ListManager.WidgetRemoval)
        
        
        
        StartPage.TopLayout.add_widget(StartPage.Layout1)
        StartPage.Layout1.add_widget(L1)
        StartPage.Layout1.add_widget(StartPage.E1)
        StartPage.Layout1.add_widget(B1)
        StartPage.Layout1.add_widget(B2)
       
        
      
    
   
        return StartPage.TopLayout
        
        
# This class has the functions.


class ListManager():
    ShoppingList =[]
    
#   Adds items to the list as needed.
    def ListAppend(*args):
        
        ListManager.Item =str(StartPage.E1.text)
        if ListManager.Item not in ListManager.ShoppingList:
            ListManager.ShoppingList.append (ListManager.Item)
            StartPage.E1.text =''
           
        else:
            StartPage.E1.text =''
            StartPage.E1.hint_text ='Already done'
            Clock.schedule_once(ListManager.EntryDeletion, 0.3)
    
#   Disables buttons which causes their colours to change.
    def ButtonDisabler(each):
        each.disabled =True
        
        
#   Deletes the content of the TextInput field as called.     
    def EntryDeletion(*args):
        StartPage.E1.hint_text =''
        
#   Removes everything displayed at app start so that the list items can be displayed as buttons.     
    def WidgetRemoval(*args):
        StartPage.TopLayout.remove_widget(StartPage.Layout1)
        
        StartPage.Layout2 =GridLayout(cols =1, spacing ='10sp', size_hint_y =None)
        
        StartPage.Layout2.bind(minimum_height =StartPage.Layout2.setter('height'))
       
        
#       Creates the buttons from the list.
        for each in ListManager.ShoppingList:
            each = Button (text=each,
                           font_size ='40sp',
                           bold =True,
                           size_hint_y =None,
                           background_disabled_normal =('ButtonDisabled.png'),
                           disabled_color =(0.44, 0.50, 0.46, 1),
                           height ='100sp')
                          
                           
            each.bind(on_press = lambda each =each: ListManager.ButtonDisabler(each))
            StartPage.Layout2.add_widget(each)
            
        StartPage.Scroll =ScrollView(size_hint_y =None, size=(StartPage.TopLayout.width, StartPage.TopLayout.height))
        StartPage.Scroll.add_widget(StartPage.Layout2)
       
        
        StartPage.TopLayout.add_widget(StartPage.Scroll)
        return StartPage.TopLayout





if __name__ == '__main__':
    StartPage().run()
