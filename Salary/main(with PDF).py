from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDActionBottomAppBarButton
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer




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
                self.root.ids.bottom_appbar.action_items = [
                    MDActionBottomAppBarButton(icon="information",on_release=lambda x: self.root.ids.info.open()),
                    MDActionBottomAppBarButton(icon="file-pdf-box",on_release=lambda x: self.doPrint()),
                ]
            else:
                self.root.ids.result.text = "Please fill up the fields."

        except ValueError:
            self.root.ids.result.text = "Please fill up the fields."

    def move_focus(self, current_textfield, next_textfield):
        if current_textfield.focus and current_textfield.text.strip() != "":
            next_textfield.focus = True


    def doPrint(self):
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.lib import colors
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet

            # Function to calculate Gross Salary and Net Salary
            def calculate_salary(basic_salary):
                da = 0.30 * basic_salary
                hra = 0.18 * basic_salary
                pf = 0.125 * basic_salary
                gross_salary = basic_salary + da + hra
                net_salary = gross_salary - pf
                return da, hra, pf, gross_salary, net_salary

            # Get user input
            
            name = float(self.root.ids.name.text)
            basic_salary = float(self.root.ids.basic.text)
            # Calculate salary components
            da, hra, pf, gross_salary, net_salary = calculate_salary(basic_salary)

            # Create a PDF report
            report = SimpleDocTemplate("Employee_Report.pdf", pagesize=letter)
            story = []

            # Add heading
            styles = getSampleStyleSheet()
            heading = Paragraph("<font size='16'><b>Employee Report</b></font>", styles["Heading1"])
            story.append(heading)

            # Add indigo colored 2pt line
            story.append(Spacer(1, 12))
            spacer = Spacer(1, 24)
            story.append(spacer)
            story.append(Spacer(1, 12))

            # Add employee details
            employee_details = f"<b>Name:</b> {name}<br/><b>Basic Salary:</b> Rs.{basic_salary:.2f}"
            story.append(Paragraph(employee_details, styles["Normal"]))
            story.append(Spacer(1, 12))

            # Add salary details
            salary_details = f"<b>DA:</b> Rs.{da:.2f}<br/><b>HRA:</b> Rs.{hra:.2f}<br/><b>PF:</b> Rs.{pf:.2f}<br/><b>Gross Salary:</b> Rs.{gross_salary:.2f}<br/><b>Net Salary:</b> Rs.{net_salary:.2f}"
            story.append(Paragraph(salary_details, styles["Normal"]))

            # Build the PDF report
            report.build(story)


        except ValueError:
            pass


    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Indigo"

        return Builder.load_string(KV)


Example().run()