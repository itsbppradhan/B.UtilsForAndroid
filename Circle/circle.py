from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

import math
KV = '''
<ContentNavigationDrawer>
    MDAnchorLayout:
        
        anchor_x:'center'
        anchor_y:'top'

        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            adaptive_width: False
            padding: [10, 50, 0, 10]

            MDLabel:
                text:"Circle"
                font_style:"H5"  # Allow automatic width adjustment
                size: self.texture_size  # Automatically adjust size to fit the text
                halign: "left"
                valign: "middle"
                text_size: self.width, dp(50)  # Enable text wrapping
            MDBoxLayout:
                orientation: 'vertical'
                adaptive_height: True
                adaptive_width: False
                padding: [10, 30, 0, 10]

            MDLabel:
                text:"Made by itsbppradhan"  # Allow automatic width adjustment
                size: self.texture_size  # Automatically adjust size to fit the text
                halign: "left"
                valign: "middle"
                text_size: self.width, dp(50)  # Enable text wrapping

        
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            adaptive_width: False
            padding: [10, 120, 0, 10]

          

            
            MDList:

                OneLineListItem:
                    text: "Home"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 1"

                OneLineListItem:
                    text: "Settings"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 2"


MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "Circle"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                
            
                MDAnchorLayout:
                
                    anchor_x:'center'
                    anchor_y:'top'
                    
                    padding:[0,100,0,0]
                
                    MDBoxLayout:
                        orientation: 'vertical'
                        adaptive_height: True
                            
                    
                    
                    
                        MDLabel:
                            text: 'Enter the data'
                            text_size: root.width, root.height
                            padding: 0, 50, 0, 0
                            markup: True
                            halign: 'center'
                            valign: 'top'
                            
                        MDBoxLayout:
                            orientation: 'horizontal'
                            adaptive_height: True
                            padding: 20,50,20,0
                            spacing: dp(10)
                            
                            
                            
                                
                                
                                
                            MDTextField:
                                hint_text: "Radius (m)"
                                id :radius
                                input_filter: "float"
                                on_text_validate: app.doThis()

                        MDBoxLayout:
                            orientation: 'horizontal'
                            adaptive_height: True
                            spacing: dp(10)
                            padding:[20,5,20,20]

                            MDTextField:
                                hint_text: "Rate per m. (fencing)"
                                text: "30"
                                id :rf
                                input_filter: "float"
                                on_text_validate: app.doThis()

                            MDTextField:
                                hint_text: "Rate per m². (grass)"
                                text: "50"
                                id :rg
                                input_filter: "float"
                                on_text_validate: app.doThis()

                                                
                                
                                
                        MDAnchorLayout:
                            anchor_x:'center'
                            padding: 0,80,0,0
                            
                            
                            
                            MDRaisedButton:
                                text: "Calculate"
                                halign: 'center'
                                on_release: app.doThis()
                                
                        MDBoxLayout:
                            orientation: 'horizontal'
                            adaptive_height: True
                            padding: 20,150,20,20
                            spacing: dp(10)
                            MDLabel:
                                text:"Result:- "
                                size_hint_x: None
                                width: self.texture_size[0]
                                text_size: None, None
                            MDLabel:
                                text:""
                                id: d
                                size_hint_x: None
                                width: self.texture_size[0]
                                text_size: None, None
                            

            MDScreen:
                name: "scr 2"

                MDAnchorLayout:
                    anchor_y:"top"
                    padding:[0,100,0,0]
                    MDList:
                        TwoLineListItem:
                            text: "Version"
                            secondary_text: "0.1"

                        TwoLineListItem:
                            text: "Made By"
                            secondary_text: "Biraja Prasad Pradhan"
                        
                        
                        TwoLineListItem:
                            text: "For"
                            secondary_text: "PyProjects"
                        

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()




class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M2"
        return Builder.load_string(KV)
    
    def doThis(self):
        # Get values from the text fields using their IDs
        try:
            radius_value = float(self.root.ids.radius.text)
            rf_value = float(self.root.ids.rf.text)
            rg_value = float(self.root.ids.rg.text)

  
            circumference = float(2 * math.pi * radius_value)
            rounded_circumference = round(circumference, 2)

            area = math.pi * (radius_value ** 2)
            rounded_area = round(area, 2)

            ratefi = rf_value * rounded_circumference
            ratef = round(ratefi,2)
            rategi = rg_value * rounded_area
            rateg = round(rategi,2)

            self.root.ids.d.text = f"Circumference: {rounded_circumference:.2f} m\nRadius: {rounded_area} m²\nRate for fencing: Rs.{ratef}\nRate for laying grass: Rs.{rateg}"
        except ValueError:
            self.show_warning_dialog("Please fill in all fields.")
    
    def show_warning_dialog(self, text):
        dialog = MDDialog(
            text=text,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()


Example().run()