
from logging import root
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from kivymd.app import MDApp
from kivy.core.window import Window


class Test(MDApp):

    def doThis(self, *args):
        try:
            # Get the user input
            input_number = self.root.ids.input_number.text

            # Check if the input is a three-digit number
            if len(input_number) != 3 or not input_number.isdigit():
                 raise ValueError("Please enter a valid three-digit number.")

            # Calculate the sum of the digits
            digit_sum = sum(int(digit) for digit in input_number)

            # Calculate the reverse of the number
            number_reverse = int(input_number[::-1])

            # Update the result labels
            sum_label = self.root.ids.sum_label
            reverse_label = self.root.ids.reverse_label

            sum_label.text = f"Sum of Digits: {digit_sum}"
            reverse_label.text = f"Reverse of Number: {number_reverse}"
        except ValueError:
            self.show_warning_dialog()


    def show_warning_dialog(self):
        dialog = MDDialog(
            title="Woops!",
            text="Please fill in all the fields or put a three digit no. only...",
            md_bg_color="#FFCCD5",
            radius=[28,28,28,28],
            buttons=[
                MDFlatButton(text="OK", theme_text_color="Custom", text_color="#A4133C", rounded_button="True", on_release=lambda x: dialog.dismiss())
            ]
        )
        dialog.open()

    def move_focus(self, current_field, next_field):
        next_field.focus = True

    


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
                        title: "Number Magic"
                        elevation: 0
                        anchor_title: "left"
                        md_bg_color: "#FFF0F3"
                        specific_text_color:"black"
                        
                
                
                
                    MDLabel:
                        text: 'Enter a three digit number'
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
                            hint_text: "Number (3 digit)"
                            mode: "rectangle"
                            id :input_number
                            input_filter: "float"
                            on_text_validate: app.doThis()    
                            
                    MDAnchorLayout:
                        anchor_x:'center'
                        padding: 0,80,0,0
                        
                        
                        
                        MDFillRoundFlatButton:
                            text: "OK"
                            md_bg_color: "#A4133C"
                            halign: 'center'
                            on_release: app.doThis()
                            
                    MDBoxLayout:
                        orientation: 'vertical'
                        adaptive_height: True
                        padding: 20,100,20,20
                        spacing: 10
                        MDLabel:
                            text:"Result:- "
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                        MDLabel:
                            text:""
                            id: sum_label
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                            padding: 0,30,0,0

                        MDLabel:
                            text:""
                            id: reverse_label
                            size_hint_x: None
                            width: self.texture_size[0]
                            text_size: None, None
                            padding: 0,60,0,0
                            
                        
                
                


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


if __name__ == '__main__':
    app = Test()
    app.run()