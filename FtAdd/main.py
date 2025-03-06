from logging import root
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from kivymd.app import MDApp


class Test(MDApp):


    def doThis(self, *args):
        try:
            root = self.root  # Get a reference to the root widget
            first_length_feet = float(root.ids.oft.text)
            first_length_inches = float(root.ids.oin.text)
            second_length_feet = float(root.ids.tft.text)
            second_length_inches = float(root.ids.tin.text)
            
            total_inches=first_length_inches+second_length_inches
            feet = total_inches // 12
            remaining_inches = int(total_inches % 12)

            total_feet= int(first_length_feet + second_length_feet + feet)


            self.root.ids.f1.text = f"{total_feet}"
            self.root.ids.f2.text = f"{remaining_inches}"
        except ValueError:
            self.show_warning_dialog()


    def show_warning_dialog(self):
        dialog = MDDialog(
            title="Woops!",
            text="Please fill in all the fields.",
            md_bg_color="#FFCCD5",
            radius=[28,28,28,28],
            buttons=[
                MDFlatButton(text="OK", theme_text_color="Custom", text_color="#A4133C", rounded_button="True", on_release=lambda x: dialog.dismiss())
            ]
        )
        dialog.open()

    def move_focus(self, current_field, next_field):
        next_field.focus = True

    
    def on_back_button(self, window, key, *args):
        if key == 27:  # Android back button code
            current_tab = self.root.ids.home_bottom_nav.current
            if current_tab == "home":
                self.stop()  # Exit the app if on the home screen
            else:
                self.root.ids.home_bottom_nav.switch_tab("home")  # Go back to home screen
            return True  # Return True to indicate that you handled the back button
        return False



    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        panel_color: "#FFCCD5"
        selected_color_background: "#FF758F"
        text_color_active: "black"

        MDBottomNavigationItem:
            name: 'home'
            text: 'Home'
            icon: 'home'
            md_bg_color: "#FFF0F3"

            

            
            MDAnchorLayout:
            
                anchor_x:'center'
                anchor_y:'top'
            
                MDBoxLayout:
                    orientation: 'vertical'
                    adaptive_height: True
                    
                    MDTopAppBar:
                        title: "Feet Adder"
                        elevation: 0
                        anchor_title: "left"
                        md_bg_color: "#FFF0F3"
                        specific_text_color:"black"
                        
                
                
                
                    MDLabel:
                        text: 'Enter the values'
                        text_size: root.width, root.height
                        padding: 0, 50, 0, 0
                        markup: True
                        halign: 'center'
                        valign: 'top'
                        
                    MDBoxLayout:
                        orientation: 'horizontal'
                        adaptive_height: True
                        padding: 20,50,20,20
                        spacing: dp(10)
                        
                        
                        MDLabel:
                            text: "1st Length"
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                            
                            
                            
                        MDTextField:
                            hint_text: "Feet"
                            mode: "rectangle"
                            id :oft
                            input_filter: "float"
                            on_text_validate: app.move_focus(self, oin)
                            
                        MDTextField:
                            hint_text: "Inches"
                            mode: "rectangle"
                            id :oin
                            input_filter: "float"
                            on_text_validate: app.move_focus(self, tft)
                            
                    MDBoxLayout:
                        orientation: 'horizontal'
                        adaptive_height: True
                        padding: 20,10,20,10
                        spacing: dp(10)
                        
                        
                        
                        MDLabel:
                            text: "2st Length"
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                            
                        MDTextField:
                            hint_text: "Feet"
                            mode: "rectangle"
                            id: tft
                            input_filter: "float"
                            on_text_validate: app.move_focus(self, tin)
                            
                            
                        MDTextField:
                            hint_text: "Inches"
                            mode: "rectangle"
                            id : tin
                            input_filter: "float"
                            on_text_validate: app.doThis()
                            
                    MDAnchorLayout:
                        anchor_x:'center'
                        padding: 0,80,0,0
                        
                        
                        
                        MDFillRoundFlatButton:
                            text: "Add"
                            md_bg_color: "#A4133C"
                            halign: 'center'
                            on_release: app.doThis()
                            
                    MDBoxLayout:
                        orientation: 'horizontal'
                        adaptive_height: True
                        padding: 20,100,20,20
                        spacing: dp(10)
                        MDLabel:
                            text:"Result:- "
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                        MDLabel:
                            text:""
                            id: f1
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                        MDLabel:
                            text:'"'
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                        MDLabel:
                            id : f2
                            text:""
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                        MDLabel:
                            text:"'"
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                            
                            
                        
                
                


        MDBottomNavigationItem:
            name: 'about'
            text: 'Info'
            icon: 'information'
            badge_icon: "numeric-1"
            md_bg_color: "#FFF0F3"

            MDAnchorLayout:
            
                anchor_x:'center'
                anchor_y:'top'
            
                MDBoxLayout:
                    orientation: 'vertical'
                    adaptive_height: True



                    TwoLineListItem:
                        text: "Version"
                        secondary_text: "1.0.0"

                    TwoLineListItem:
                        text: "Made By"
                        secondary_text: "Biraja Prasad Pradhan"
                       
                    
                    TwoLineListItem:
                        text: "For"
                        secondary_text: "PyProjects"
                        
'''
        )
        EventLoop.window.bind(on_keyboard=self.on_back_button)


Test().run()