from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDActionBottomAppBarButton
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp



KV = '''
MDScreen:
    #:import MDActionBottomAppBarButton kivymd.uix.toolbar.MDActionBottomAppBarButton


    MDFloatLayout:
        md_bg_color: "#E6F2FF"


        MDAnchorLayout:
        
            anchor_x:'center'
            anchor_y:'top'
        
            MDBoxLayout:
                orientation: 'vertical'
                adaptive_height: True
                
                MDTopAppBar:
                    title: "Salary App"
                    elevation: 0
                    anchor_title: "left"
                    md_bg_color: "#E6F2FF"
                    specific_text_color:"black"
                    
            
            
            
                MDLabel:
                    text: 'Enter details'
                    text_size: root.width, root.height
                    padding: 0, 50, 0, 0
                    markup: True
                    halign: 'center'
                    valign: 'top'
                    
                MDBoxLayout:
                    orientation: 'vertical'
                    adaptive_height: True
                    padding: 20,50,20,20
                    spacing: dp(10)
                    
                    
                        
                        
                        
                    MDTextField:
                        hint_text: "Name of the employee"
                        mode: "rectangle"
                        id :name
                        on_text_validate: app.move_focus(self, basic)
                        
                    MDTextField:
                        hint_text: "Basic salary (₹)"
                        mode: "rectangle"
                        id :basic
                        input_filter: "float"
                        on_text_validate: app.doThis()
                        
                        
                MDBoxLayout:
                    orientation: 'horizontal'
                    adaptive_height: True
                    padding: 20, 120, 20, 20
                    spacing: dp(10)
                    MDLabel:
                        text: "Result:- "
                        size_hint_x: None
                        width: self.texture_size[0]
                        text_size: None, None
                        halign: 'left'  # Enable word wrap by setting halign to 'left'
                        valign: 'top'   # Enable word wrap by setting valign to 'top'
                    MDLabel:
                        text: ""
                        id: result
                        size_hint_x: None
                        width: self.texture_size[0]
                        text_size: None, None
                        halign: 'left'  # Enable word wrap by setting halign to 'left'
                        valign: 'top'   # Enable word wrap by setting valign to 'top'
                        

        MDBottomAppBar:
            id: bottom_appbar
            md_bg_color: "#CCDCFF"
            icon_color: "#9A99F2"
            action_items:
                [
                MDActionBottomAppBarButton(icon="information", on_release=lambda x: info.open()),
                ]

            MDFabBottomAppBarButton:
                icon: "arrow-right"
                md_bg_color: "#805EBF"
                on_release: app.doThis()


    MDBottomSheet:
        id: info
        bg_color: "white"
        size_hint_y: None
        max_opening_height: self.height
        default_opening_height: self.max_opening_height
        adaptive_height: True
        auto_positioning: False
        
    

        MDBottomSheetDragHandle:

        

        MDBottomSheetContent:

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
    '''


class Example(MDApp):
    def doThis(self):
        try:
            # Get the values from the MDTextField widgets
            name = self.root.ids.name.text
            basic_salary = self.root.ids.basic.text

            # Check if both fields are not empty
            if name and basic_salary:
                basic_salary = float(basic_salary)

                # Calculate DA, HRA, and PF based on the given percentages
                DA = 0.30 * basic_salary
                HRA = 0.18 * basic_salary
                PF = 0.125 * basic_salary

                # Calculate Gross Salary
                gross_salary = basic_salary + DA + HRA

                # Calculate Net Salary
                net_salary = gross_salary - PF

                # Update the result label in the KivyMD interface
                self.root.ids.result.text = (
                    f"Name: {name}\n"
                    f"Basic Salary: ₹{basic_salary:.2f}\n"
                    f"DA: ₹{DA:.2f}\n"
                    f"HRA: ₹{HRA:.2f}\n"
                    f"PF: ₹{PF:.2f}\n"
                    f"Gross Salary: ₹{gross_salary:.2f}\n"
                    f"Net Salary: ₹{net_salary:.2f}"
                )
                
            else:
                self.root.ids.result.text = "Please fill up the fields."

        except ValueError:
            self.root.ids.result.text = "Please fill up the fields."

    def move_focus(self, current_textfield, next_textfield):
        if current_textfield.focus and current_textfield.text.strip() != "":
            next_textfield.focus = True

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Indigo"

        return Builder.load_string(KV)


Example().run()