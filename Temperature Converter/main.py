from logging import root
from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu


from kivymd.app import MDApp

KV='''

            
MDScreen:

    MDBottomNavigation:
        panel_color: "#B7E4C7"
        selected_color_background: "#95D5B2"
        text_color_active: "black"

        MDBottomNavigationItem:
            name: 'home'
            text: 'Home'
            icon: 'home'
            md_bg_color: "#D8F3DC"

            

            
            MDAnchorLayout:
            
                anchor_x:'center'
                anchor_y:'top'
            
                MDBoxLayout:
                    orientation: 'vertical'
                    adaptive_height: True
                    
                    MDTopAppBar:
                        title: "TempConverter"
                        elevation: 0
                        anchor_title: "left"
                        md_bg_color: "#D8F3DC"
                        specific_text_color:"black"
                        
                
                
                
                    MDLabel:
                        text: 'Enter the temperature'
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
                        
                        
                        
                            
                            
                            
                        MDTextField:
                            hint_text: "Enter Temperature"
                            mode: "rectangle"
                            id :temp
                            input_filter: "float"
                            on_text_validate: app.doThis()
                            line_color_focus:"#2D6A4F"   # Change the border color when focused (black)
                            hint_text_color_focus: "#2D6A4F"  # Change the hint text color (a shade of green)
                            text_color_focus: "#2D6A4F"


                            
                        MDDropDownItem:
                            id: drop_item
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            text: 'ºC to ºF'
                            on_release: app.menu.open()
                                            
                            
                            
                    MDAnchorLayout:
                        anchor_x:'center'
                        padding: 0,80,0,0
                        
                        
                        
                        MDFillRoundFlatButton:
                            text: "Convert"
                            md_bg_color: "#1B4332"
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
                            id: d
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                        
                            
                            
                        
                
                


        MDBottomNavigationItem:
            name: 'about'
            text: 'Info'
            icon: 'information'
            badge_icon: "numeric-1"
            md_bg_color: "#D8F3DC"

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


class Test(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "text": f"ºC to ºF",
                "on_release": lambda x=f"ºC to ºF": self.set_item1(x),
            },
            {
                "text": f"ºF to ºC",
                "on_release": lambda x=f"ºF to ºC": self.set_item2(x),
            }
        ]
        self.menu = MDDropdownMenu(
            background_color="#D8F3DC",
            caller=self.screen.ids.drop_item,
            items=menu_items,
            position="bottom",
        )
         
        self.menu.bind()
        self.op = 1

        

    def set_item1(self, text_item):
        self.screen.ids.drop_item.text = text_item 
        self.menu.dismiss()
        self.op=1

    def set_item2(self, text_item):
        self.screen.ids.drop_item.text = text_item
        self.menu.dismiss()
        self.op=2


    def doThis(self, *args):
        
        if (self.op==1):
            try:
                tempr=0
                ftemp=0
                root = self.root  # Get a reference to the root widget
                ftemp = float(root.ids.temp.text)
                tempr=(ftemp * 9/5) + 32
                self.root.ids.d.text = f"{ftemp}ºC is {tempr}ºF"
            except ValueError:
                self.show_warning_dialog()


                
        if(self.op==2):
            try:

                tempr=0
                ftemp=0
                root = self.root  # Get a reference to the root widget
                ftemp = float(root.ids.temp.text)
                tempr=(ftemp-32) * 5/9
                self.root.ids.d.text = f"{ftemp}ºF is {tempr}ºC"


                
            except ValueError:
                self.show_warning_dialog()


    def show_warning_dialog(self):
        dialog = MDDialog(
            title="Woops!",
            text="Please fill in all the fields.",
            md_bg_color="#D8F3DC",
            radius=[28,28,28,28],
            buttons=[
                MDFlatButton(text="OK", theme_text_color="Custom", text_color="#081C15", rounded_button="True", on_release=lambda x: dialog.dismiss())
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
        self.theme_cls.theme_style = "Light"
        return self.screen


Test().run()