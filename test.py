# Requirements:
# python 3.6
# kivy 1.11.1
# translate (library) and
# other libraries help to run these code




#Task 2
#check the length of the number
n = input("Enter the number: ")
if len(str(n)) > 8:
    print("the number must be less than 8")

else:
    print(n)


# Task 3
#replaces a specified number to *
n = input("Enter the number: ")
print(n.replace(n[0:-4], "* * * * "))




# Task 4
#check if year is leap or not
#a year, occurring once every four years, which has 366 days
# including 29 February as an intercalary day.
n = int(input("Enter the year: "))
if n % 400 == 0:
    print("The year is leap year")
else:
    print("The year is NOT leap year")




# Task 5
# Game to guess the word was chosen from computer
import random
Word_array = ["Red","white","black","pink"]
a = random.choice(Word_array)
print(Word_array)

n = input("Chose one world: ")
if n == a:
    print("You Win")
    print(a)

elif n != a:
    print("False, try again")
    print(a)
    n = input("Chose one world:")
    if n == a:
        print("You Win")
    else:
        print("False, Game Over")
        play = input("You want play again? Yes or No ")
        if play == "Yes":
            n = input("Chose one world: ")
            print(Word_array)
            if n == a:
                print("You Win")
            elif n != a:
                print("False, try again")
                print(a)
                n = input("Chose one world:")
                if n == a:
                    print("You Win")
                else:
                    print("False, Game Over")
        else:
            exit()


# Task 6
#Choose the process then will display the money
#in account after process

account_1 = 300
account_2 = 100
account = input("Enter your account")
Process = input("Enter your Process")
if account == "account_1" and Process == "transe":
    mony = int(input("Enter mony "))
    New_mony = account_1 - mony
    second_mony = account_2 + mony
    print("New mony in account:", New_mony, "Second account", second_mony)

elif account == "account_2" and Process == "transe":
    mony = int(input("Enter mony "))
    New_mony = account_2 - mony
    second_mony = account_1 + mony
    print("New mony in account:", New_mony, "Second account", second_mony)

elif account == "account_1" and Process == "Pull":
    mony = int(input("Enter mony "))
    Newpull_mony_1 = account_1 - mony
    print(Newpull_mony_1)

elif account == "account_2" and Process == "Pull":
    mony = int(input("Enter mony "))
    Newpull_mony_2 = account_2 - mony
    print(Newpull_mony_2)

else:
    print("Not correct")




# Task 7
# Calculate calories in body
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Builder.load_string("""
<cala>:
    name: "secreen"
    wight_input: wight_input
    hight_input: hight_input
    age_input: age_input
    female: chk_Female
    male: chk_Male
    result: result

    canvas.before:
        Color:
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        padding: 6
        spacing: 3
        size_hint_y: None


        RelativeLayout:
            orientation: "vertical"
            padding: 6
            spacing: 20

            canvas:
                Color:

                Rectangle:
                    size: 350,60
                    pos: 0,620
                Line:
                    width: 2
                    rectangle: .1, 85, 350, 460   #self.x, self.y, self.width, self.height

            Label:
                text: 'Wight'
                font_size: 20
                text_size: self.size
                color: [0.0,0.0,0.0,100]
                center_x:150
                center_y:550

            TextInput:
                id: wight_input
                center_x:150
                center_y:490
                size_hint: 1.5,.4
                font_size: 20
                input_type :'number'
                input_filter: 'float'
                color: [0.0,0.0,0.0,0.4]

            Label:
                text: 'Hight'
                font_size: 20
                text_size: self.size
                color: [0.0,0.0,0.0,100]
                center_x:150
                center_y:450

            TextInput:
                id: hight_input
                center_x:150
                center_y:390
                size_hint: 1.5,.4
                font_size: 20
                input_type :'number'
                input_filter: 'float'
                color: [0.0,0.0,0.0,0.4]

            Label:
                text: 'Age'
                font_size: 20
                text_size: self.size
                color: [0.0,0.0,0.0,100]
                center_x:150
                center_y:350

            TextInput:
                id: age_input
                center_x:150
                center_y:290
                size_hint: 1.5,.4
                font_size: 20
                input_type :'number'
                input_filter: 'float'
                color: [0.0,0.0,0.0,0.4]

            CheckBox:
                group: 'check_1'
                center_x:90
                center_y:200
                text: "Male"
                color: [0.0,0.0,0.0,100]
                id : chk_Male
                on_active:
                    root.cala = self.text

            Label:
                text: 'Male'
                font_size: 20
                text_size: self.size
                color: [0.0,0.0,0.0,100]
                center_x:150
                center_y:230

            CheckBox:
                group: 'check_1'
                center_x:220
                center_y:200
                text: "Female"
                color: [0.0,0.0,0.0,100]
                id : chk_Female
                on_active:
                    root.cala = self.text
            Label:
                text: 'Female'
                font_size: 20
                text_size: self.size
                color: [0.0,0.0,0.0,100]
                center_x:280
                center_y:230

           ################################################
            Label:
                id: result
                center_x:150
                center_y:170
                size_hint: 1.5,.4
                font_size: 20
                input_type :'number'
                input_filter: 'float'
                readonly: True
                color: [0.0,0.0,0.0,100]

            Button:
                text: "Calculate"
                font_size: 20
                size_hint:1.5,.5
                on_release:root.calory()
                background_color: 1, .3, .4, .85

""")

from kivy.core.window import Window
Window.size = (360, 680)
class cala(Widget):
    def calory(self):
        Age = self.age_input.text
        Weight = self.wight_input.text
        Height = self.hight_input.text
        result = ObjectProperty(None)
        male = ObjectProperty(None)
        female = ObjectProperty(None)


        if self.male.active:
            Result_2 = ((10 * float(Weight)) + (6.25 * float(Height)) - (5 * float(Age)) + 5)
            #Result = TextInput(text= Result_2)
            self.result.text = str(Result_2)
            print(Result_2)
            print("male")
        elif self.female.active:
            Result_1 = ((10 * float(Weight))+(6.25 * float(Height)) - (5 * float(Age)) - 161)
            print(Result_1)
            self.result.text = str(Result_1)
            print("Female")
        else:
            print("None")

class Calories(App):
    def build(self):
        return cala()
Calories().run()



# Task 8
# Convert US size to UK
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Builder.load_string("""
<Sizec>:
    name: "secreen"
    us_input: us_input
    shoes: chk_Shoes
    blouse: chk_Blouse


    result: result

    canvas.before:
        Color:



        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        padding: 6
        spacing: 3
        size_hint_y: None


        RelativeLayout:
            orientation: "vertical"
            padding: 6
            spacing: 20

            canvas:
                Color:
                Rectangle:
                    size: 350,60
                    pos: 0,620
                Line:
                    width: 2
                    rectangle: .1, 85, 350, 460

            Label:
                text: 'Enter US size'
                font_size: 20
                text_size: self.size
                color: [0.0,0.0,0.0,100]
                center_x:150
                size_hint: 1.5,.4
                center_y:550

            TextInput:
                id: us_input
                center_x:150
                center_y:490
                size_hint: 1.5,.4
                font_size: 20
                input_type :'number'
                input_filter: 'float'
                color: [0.0,0.0,0.0,0.4]




            CheckBox:
                group: 'check_1'
                center_x:90
                center_y:400
                text: "Blouse"
                color: [0.0,0.0,0.0,100]
                id : chk_Blouse
                on_active:
                    root.cala = self.text

            Label:
                text: 'Blouse'
                font_size: 20
                text_size: self.size
                color: [0.0,0.0,0.0,100]
                center_x:150
                center_y:430

            CheckBox:
                group: 'check_1'
                center_x:220
                center_y:400
                text: "Shoes"
                color: [0.0,0.0,0.0,100]
                id : chk_Shoes
                on_active:
                    root.cala = self.text
            Label:
                text: 'Shoes'
                font_size: 20
                text_size: self.size
                color: [0.0,0.0,0.0,100]
                center_x:280
                center_y:430



            Label:
                id: result
                center_x:150
                center_y:270
                size_hint: 1.5,.4
                font_size: 20
                input_type :'number'
                input_filter: 'float'
                readonly: True
                color: [0.0,0.0,0.0,100]


            Button:
                text: "Calculate"
                font_size: 20
                size_hint:1.5,.5
                center_x:150
                center_y:170
                on_release:root.size55()
                background_color: 1, .3, .4, .80

""")

from kivy.core.window import Window
Window.size = (360, 680)


class Sizec(Widget):
    def size55(self):
        US_size = self.us_input.text

        blouse = ObjectProperty(None)
        shoes = ObjectProperty(None)


        #Shose
        if self.shoes.active:
            Uk_size = (float(US_size)) - 2
            self.result.text = str(Uk_size)
            print(float(Uk_size))

        #Blouse
        elif self.blouse.active:
            Uk_size = (float(US_size)) + 2
            self.result.text = str(Uk_size)
            print(float(Uk_size))


class Size(App):

    title = "Size Of Shoes and Clothes"
    def build(self):
        return Sizec()
Size().run()



# Task 9
#translate to different languages
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Builder.load_string("""
<trans_app>:
    text_input:text_input
    lang_text:lang_text
    result:result


    result: result

    canvas.before:
        Color:
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        padding: 6
        spacing: 3
        size_hint_y: None


        RelativeLayout:
            orientation: "vertical"
            padding: 6
            spacing: 20

            canvas:
                Color:
                Rectangle:
                    size: 350,60
                    pos: 0,620
                Line:
                    width: 2
                    rectangle: .1, 85, 350, 460

            Label:
                text: 'Enter your text'
                font_size: 20
                text_size: self.size
                color: [0.0,0.0,0.0,100]
                center_x:210
                size_hint: 1.5,.4
                center_y:570

            TextInput:
                id: text_input
                center_x:190
                center_y:490
                size_hint: 2.,.8
                font_size: 20
                #input_filter: 'float'
                color: [0.0,0.0,0.0,0.4]


            Label:
                id: result
                center_x:150
                center_y:270
                size_hint: 1.5,.4
                font_size: 20
                readonly: True
                color: [0.0,0.0,0.0,100]

            Label:
                text: "Select the language:"
                #size_hint_x: 1
                color: 0,0,0,1
                #center_x: (root.width/2)
                #top: (root.top/2) + 700
                pos: 100, 1060

            Spinner:
                center_x: 50
                center_y:500
                #pos: 40, 200
                background_color: 1, .3, .4, .85
                size_hint:1.5,.5 #width , hieght
                id: lang_text
                #size_hint: 1,.3
                font_size: 13
                #on_text: root.spinner_clicked(sym_text.text)
                text:'Select the language:'
                values: ['English','German','spanish']


            Button:
                text: "Translate"
                font_size: 20
                size_hint:1.5,.5
                center_x:150
                center_y:170
                on_release:root.translate()
                background_color: 1, .3, .4, .80

""")
from kivy.core.window import Window
from translate import Translator
Window.size = (360, 680)
class trans_app(Widget):
    def translate(self):
        text = self.text_input.text
        selection = self.lang_text.text
        if selection == "English":
            translate_1 = Translator(to_lang="English")
            T_1= translate_1.translate(text)
            self.result.text = T_1
            print(T_1)
        elif selection == "German":
            translate_2 = Translator(to_lang="German")
            T_2 = translate_2.translate(text)
            self.result.text = T_2
            print(T_2)
        elif selection == "spanish":
            translate_3 = Translator(to_lang="spanish")
            T_3 = translate_3.translate(text)
            self.result.text = T_3
            print(T_3)
class main(App):
    title = "Translate"
    def build(self):
        return trans_app()
main().run()


# Task 10
#Code for send email

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Builder.load_string("""
<Email_app>:
     from_input:from_input
     to_text:to_text
     masg_text: masg_text
     sub_text: sub_text



     canvas.before:
          Color:
          Rectangle:
               pos: self.pos
               size: self.size

     BoxLayout:
          padding: 6
          spacing: 3
          size_hint_y: None

#
          RelativeLayout:
               orientation: "vertical"
               padding: 6
               spacing: 20

               canvas:
                    Color:
                    Rectangle:
                         size: 350,60
                         pos: 0,620
                    Line:
                         width: 2
                         rectangle: .1, 85, 350, 460

               Label:
                    text: 'From'
                    font_size: 20
                    text_size: self.size
                    color: [0.0,0.0,0.0,100]
                    center_x:210
                    size_hint: 1.5,.4
                    center_y:570

               TextInput:
                    id: from_input
                    center_x:190
                    center_y:490
                    size_hint: 2.,.5
                    font_size: 15
                 #input_filter: 'float'
                    color: [0.0,0.0,0.0,0.4]



               Label:
                    text: 'To'
                    font_size: 20
                    text_size: self.size
                    color: [0.0,0.0,0.0,100]
                    center_x:210
                    size_hint: 1.5,.4
                    center_y:450

               TextInput:
                    id: to_text
                    center_x:190
                    center_y:400
                    size_hint: 2.,.5
                    font_size: 15
                 #input_filter: 'float'
                    color: [0.0,0.0,0.0,0.4]

               Label:
                    text: 'Subject'
                    font_size: 20
                    text_size: self.size
                    color: [0.0,0.0,0.0,100]
                    center_x:210
                    size_hint: 1.5,.4
                    center_y:360

               TextInput:
                    id: sub_text
                    center_x:190
                    center_y:310
                    size_hint: 2.,.5
                    font_size: 15
                 #input_filter: 'float'
                    color: [0.0,0.0,0.0,0.4]

#
               Label:
                    text: 'Massage'
                    font_size: 20
                    text_size: self.size
                    color: [0.0,0.0,0.0,100]
                    center_x:210
                    size_hint: 1.5,.4
                    center_y:280

               TextInput:
                    id: masg_text
                    center_x:190
                    center_y:190
                    size_hint: 3.,1.
                    font_size: 15
                 #input_filter: 'float'
                    color: [0.0,0.0,0.0,0.4]

               Button:
                    text: "Send"
                    font_size: 20
                    size_hint:1.5,.5
                    center_x:150
                    center_y:130
                    on_release:root.email()
                    background_color: 1, .3, .4, .80

""")

import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email_app(Widget):
    def email(self):

        #"Yor Email"
        send = self.from_input.text
        password = "Your password"
        recive = self.to_text.text
        subject = self.sub_text.text
        massage = self.masg_text.text

        msg = MIMEMultipart()

        msg['From'] = send
        msg['To'] = recive
        msg['Subject'] = subject

        msg.attach(MIMEText(massage, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(send, password)
        text = msg.as_string()
        server.sendmail(send, recive, text)
        print("correct")

        server.quit()

class main(App):
     title = "Email"
     def build(self):
        return Email_app()
main().run()

#task_11
# Camera code
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
import time
Window.size = (360, 680)
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False


    Label:
        id: label

    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        #Time to Captured Image
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        self.ids['label'] = camera

class TestCamera(App):

    def build(self):
        return CameraClick()
TestCamera().run()


#lower case
print([i.lower() for i in "STUDENT"])

#sort() function
list=['1','5','3','10','7','2']
list.sort()
print(list[5])



#task

for number in range(1,51):
   if number % 5 == 0:
      print('X')

   elif number % 3 == 0:
      print('y')

   elif number % 3 == 0 and number % 5 == 0:
      print('XY')




