import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import winsound
import smtplib
import requests, json
import webbrowser
import random
import pyjokes
import os
import psutil
import subprocess
import threading
from tkinter import *
from tkinter.messagebox import *
from itertools import count
import tkinter as tk
import time
from tkinter import ttk

from PIL import ImageTk, Image

win = tk.Tk()


def Startbtn():
    # Button(win,text='Started',bg='red',fg='white').pack()
    Button(win, text='Started', width=20, height=2, bg='black', fg='white', state=DISABLED,
           command=threading.Thread(target=StartMainPart).start()).place(x=50, y=425)


def Exitbtn():
    # print('quit clicked')

    os._exit(1)


def Restartbtn():
    # print('Restart clicked')
    os.execv(sys.executable, ['python'] + sys.argv)


def StartMainPart():
    # speak part

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 118)

    def speak(audio):

        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak('Good Morning')
        elif hour >= 18 and hour < 18:
            speak('Good Afternoon')
        else:
            speak('Good evening ')
        speak('I am your assistant, how may i help you')

    def takeCommand():
        '''
        It takes microphone input from the user and returns string output  '''

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=0.5)

            audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio)
            query = query.lower()

            print(f"User Said: {query}\n")
            speak(query)

        except Exception as e:
            # print(e)

            print('Say that again please...')

            return "None"
        return query

    # ***To send Email By SMTP Enabed less secure apps i****

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('Your email', '****************')
        server.sendmail('Your email', to, content)
        server.close()

    if __name__ == '__main__':
        wishMe()

        while True:

            query = takeCommand().lower()

            # Logic for executing tasks based on the query
            if 'wikipedia' in query or 'something about' in query:
                speak("Searching wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open google' in query:
                webbrowser.open('www.google.com')

            elif 'open youtube' in query:
                webbrowser.open('www.youtube.com')

            elif 'open geeks' in query:
                webbrowser.open('https://www.geeksforgeeks.org/')
            elif 'open amazon' in query:
                webbrowser.open('www.amazon.com')



            # elif 'google search' in query:
            #     query =

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                speak(f"The time is {strTime}")

            elif 'date' in query:
                strDate = datetime.date.today()
                speak('Today is')
                speak(strDate)

            elif 'you listening' in query:
                speak('Yes Sir,i am listening')
            elif 'online' in query:
                speak('Yes Sir, I am online')



            elif 'open interpreter' in query:
                PythonPath = "C:\\Users\\HOME\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe"
                os.startfile(PythonPath)

            elif 'send email to (name whom you want to send email)' in query:
                try:
                    speak('What should i say')
                    content = takeCommand()
                    to = "email of the user whom you want to send mail"
                    sendEmail(to, content)
                    speak("Email has been sent.")
                except Exception as e:
                    print(e)
                    speak("Sorry, i am unable to send the email at this time")

            elif 'quit' in query or 'exit' in query or 'offline' in query:
                speak('Thank You Sir,See you later')
                exit()

            elif 'who are you' in query or 'your name' in query or 'call you' in query:
                speak("My name is zaara,what i can do for you")
                print("My name is zaara, what i can do for you")


            elif 'do for me' in query:
                speak('Sir,Tell me whatever you want to do,then i will decide that i can do that or not')



            elif 'hello' in query or 'hai' in query or 'hi' in query or 'hey' in query:
                speak("hello,sir")


            elif 'how are you' in query:

                speak("I'm having great day! I was just looking up some fun things to do")

                print("I'm having great day! I was just looking up some fun things to do")


            elif 'weather' in query:

                api_key = "ac17fa1911e625599c89ec2d30080736"

                # Store url
                base_url = "http://api.openweathermap.org/data/2.5/weather?"

                # Get city name by user
                speak("Please,tell me your city name")
                print('Please,tell me your city name')

                city_name = takeCommand()

                # complete_url variable to store
                # complete url address
                complete_url = base_url + "appid=" + api_key + "&q=" + str(city_name)

                # get method of requests module
                # return response object
                response = requests.get(complete_url)

                # json method of response object
                # convert json format data into
                # python format data
                x = response.json()

                # "404", means city is found otherwise,
                # city is not found

                if x["cod"] != "404":

                    # store the value of "main"
                    # key in variable y
                    y = x["main"]

                    # store the value corresponding
                    # to the "temp" key of y
                    current_temperature = y["temp"]

                    # store the value corresponding
                    # to the "pressure" key of y
                    current_pressure = y["pressure"]

                    # store the value corresponding
                    # to the "humidity" key of y
                    current_humidiy = y["humidity"]

                    # store the value of "weather"
                    # key in variable z
                    z = x["weather"]

                    # store the value corresponding
                    # to the "description" key at
                    # the 0th index of z
                    weather_description = z[0]["description"]

                    # print following values
                    temperature_celcius = current_temperature - 273.15
                    print(speak(" The Temperature outside  is  = " +

                                str(current_temperature) + " Kelvin " +
                                "\n and the temperature  in Cellceeus is " + str(
                        round(temperature_celcius)) + " Celcius " +

                                "\n The weather is = " +
                                str(weather_description) + " outside" +

                                "\n The atmospheric pressure (in hPa unit) = " +
                                str(current_pressure) + " hecto Pascals " +
                                "\n humidity is(in percentage) = " +
                                str(current_humidiy) + " % "
                                ))



                else:
                    speak(" City Not Found,Try again")


            elif 'joke' in query:
                speak('Only a programmer can understand these jokes here')
                speak(pyjokes.get_joke())

                # for music/Play songs

            elif 'play music' in query:
                music_dir = 'C:\\Users\\Public\\Music\\Sample Music'
                music = os.listdir(music_dir)
                print(music)
                os.startfile(os.path.join(music_dir, music[5]))

                ########NOT WORKING TRYING
            elif 'battery' in query or 'charging' in query:
                bpercent = psutil.sensors_battery()
                speak('Your system is')
                speak(bpercent.percent)
                speak('percent charged')

            # for shutdown

            elif 'shutdown' in query or 'shut down':
                # os.system(["shutdown"," /s"])
                os.system("shutdown /r /t 1")

            # for restart

            elif "restart" in query:
                os.system("shutdown /r /t 0")

    takeCommand()


# Main GUI Code
win.geometry('932x530')

win.resizable(False, False)


class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


lbl = ImageLabel(win)
lbl.pack()
lbl.load('futur.gif')
# gif end

# Button(win,text='START',width=20,height=2,bg='black',fg='white',command=threading.Thread(target=Start).start()).place(x=300,y=425)

######################################## For Start Button
frame = Frame(win, width='130', height='2', bg='red')
startbtn = Button(frame, command=Startbtn)
startbtn.pack()
btnimage = PhotoImage(file='startcoolcentered.png')
startbtn.config(image=btnimage)
frame.place(x=30, y=55)

######################################## For Restart Button

frame = Frame(win, width='130', height='2', bg='grey')
restartbtn = Button(frame, command=Restartbtn)
restartbtn.pack()
btnimage2 = PhotoImage(file='restartcoolm.png')
restartbtn.config(image=btnimage2)
frame.place(x=30, y=143)

################################## Exit Button ##################################################


frame = Frame(win, width='130', height='2', bg='red')
exitbtn = Button(frame, command=Exitbtn)
exitbtn.pack()
btnimage3 = PhotoImage(file='exitcool.png')
exitbtn.config(image=btnimage3)
frame.place(x=30, y=230)


# #################Dispay time

def clock():
    h = str(time.strftime('%H'))
    m = str(time.strftime('%M'))
    s = str(time.strftime('%S'))
    no = time.strftime('%p')
    # print(h,m,s)
    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)
    lbl_noon.config(text=no)
    if int(h) > 12:
        hw = str(int(h) - 12)
        lbl_hr.config(text=hw)

    lbl_hr.after(200, clock)


# Hour
lbl_hr = Label(win, text='12', font=('times new roman', 25, 'bold'), bg='yellow', fg='red', relief=SUNKEN)
lbl_hr.place(x=610, y=0, width=70, height=55)

lbl_hr2 = Label(win, text='Hour', font=('times new roman', 15, 'bold'), bg='black', fg='white')
lbl_hr2.place(x=610, y=55, width=70, height=30)

# min
lbl_min = Label(win, text='12', font=('times new roman', 25, 'bold'), bg='yellow', fg='red', relief=SUNKEN)
lbl_min.place(x=690, y=2, width=70, height=55)

lbl_min2 = Label(win, text='Minute', font=('times new roman', 15, 'bold'), bg='black', fg='white')
lbl_min2.place(x=690, y=55, width=70, height=30)

# second

lbl_sec = Label(win, text='12', font=('times new roman', 25, 'bold'), bg='yellow', fg='red', relief=SUNKEN)
lbl_sec.place(x=770, y=2, width=70, height=55)

lbl_sec2 = Label(win, text='Seconds', font=('times new roman', 15, 'bold'), bg='black', fg='white')
lbl_sec2.place(x=770, y=55, width=70, height=30)

# Noon

lbl_noon = Label(win, text='AM', font=('times new roman', 25, 'bold'), bg='yellow', fg='red', relief=SUNKEN)
lbl_noon.place(x=850, y=2, width=74, height=55)

lbl_noon2 = Label(win, text='Noon', font=('times new roman', 15, 'bold'), bg='black', fg='white')
lbl_noon2.place(x=850, y=55, width=70, height=30)

clock()

# Battery Status

text = psutil.sensors_battery().percent
# print(text)
label2 = Label(win, text=f'Battery Status: {text}%', bg='#1A1110', fg='silver', font=('verdana', 18, 'bold'))
label2.place(x=610, y=100)


####################  Power Status
def powerstatus():
    power_status = psutil.sensors_battery().power_plugged
    # print(power_status)
    if power_status == True:
        label = Label(win, text=f'Power: Plugged In   ', bg='#1A1110', fg='silver', font=('verdana', 18, 'bold')).place(
            x=610, y=135)
    else:
        label = Label(win, text=f'Power: Plugged out  ', bg='#1A1110', fg='silver', font=('verdana', 18, 'bold')).place(
            x=610, y=135)


powerstatus()

# blank for battery and power

label = Label(win, bg='#1A1110', width=4, height=6).place(x=890, y=100)


############################## Disk Usage

def diskUsage():
    obj = psutil.disk_usage('/')
    totaldisk = obj.total // 1024 ** 3
    diskused = obj.used // 1024 ** 3
    diskusable = obj.free // (1024 ** 3)

    label = Label(win, text=f'Total Disk: {totaldisk} GB', bg='#1A1110', fg='silver',
                  font=('verdana', 18, 'bold')).place(
        x=610, y=170)
    label = Label(win, text=f'Disk Used: {diskused} GB', bg='#1A1110', fg='silver', font=('verdana', 18, 'bold')).place(
        x=610, y=205)
    label = Label(win, text=f'Disk Usable: {diskusable} GB', bg='#1A1110', fg='silver',
                  font=('verdana', 18, 'bold')).place(
        x=610, y=240)

    # To cover the Blanck Space
    # For 1nd one
    label = Label(win, bg='#1A1110', width=11, height=7).place(x=845, y=170)
    # For 2nd one
    label = Label(win, bg='#1A1110', width=44, height=1).place(x=610, y=275)


diskUsage()


def Askmebtn():
    # speak part

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices[0].id)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 118)

    def speak(audio):

        engine.say(audio)
        engine.runAndWait()

    def TakeInputCommand():
        try:
            query = InputSearchBox.get()
            InputSearchBox.delete(0, END)
            # print(query)
            # speak(query)
        except Exception as e:
            print(e)
            print('Ooops seems you have lost your connection check and try again...')

            return "None"
        return query

    if __name__ == '__main__':

        query = TakeInputCommand().lower()

        if 'hello' in query or 'hai' in query or 'hi' in query or 'hey' in query:
            print('hello Sir')
            speak('hello Sir')
            # InputSearchBox.delete(0,END)

        elif 'how are you' in query or 'how r u' in query:

            speak("I'm having great day! I was just looking up some fun things to do")
            print("I'm having great day! I was just looking up some fun things to do")



        elif 'joke' in query:
            speak('Only a programmer can understand these jokes here')
            speak(pyjokes.get_joke())

            print('Only a programmer can understand these jokes here')

        elif 'you doing' in query or 'r u doing' in query:
            print('I am waiting, for your command')
            speak('I am waiting, for your command')

        elif 'your name' in query:
            print('My name is Zara,your personel assistant ,how can i help you')
            speak('My name is Zara')
            speak('Your personel assistant')
            speak('How can i help you')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Public\\Music\\Sample Music'
            music = os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir, music[5]))


        elif 'battery' in query or 'charging' in query:
            bpercent = psutil.sensors_battery()
            speak('Your system is')
            speak(bpercent.percent)
            speak('percent charged')


        elif 'do for me' in query:
            speak('Sir,Tell me whatever you want to do,then i will decide that i can do that or not')


        elif 'who are you' in query or 'who r u' in query :
            speak('My name is Zara')
            speak('Your personel assistant')
            speak('what can i do for you')

        elif 'call you' in query or 'call u' in query:
            speak('You can call me Zaara')
            speak('It will be my pleasure, that you are finding me helpfull')
            print('You can call me Zaara')

        elif 'i hate you' in query or 'i hate u' in query or 'i dont like you' in query or 'i dont like u' in query or "i don't like you" in query or "i don't like u" in query:
            print('Sorry Sir, if you are not impressed by my work')
            speak('Sorry Sir, if you are not impressed by my work')
            speak('I am continuously trying to improve myself')

        elif 'quit' in query or 'exit' in query or 'offline' in query:
            speak('Thank You Sir,See you later')
            os._exit(1)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {strTime}")

        elif 'date' in query:
            strDate = datetime.date.today()
            speak('Today is')
            speak(strDate)


        elif 'open google' in query:
            speak('opening google,just a moment')
            webbrowser.open('www.google.com')

        elif 'open youtube' in query:
            speak('opening youtube,just a moment')
            webbrowser.open('www.youtube.com')

        ### NEW ONE ADDED WORKING

        elif 'on youtube' in query:
            speak('opening youtube , just a moment')
            print('www.youtube.com/results?search_query=' + query)
            webbrowser.open('www.youtube.com/results?search_query=' + query)

        





        elif 'open geeks' in query:
            speak('opening geeks,just a moment')
            webbrowser.open('https://www.geeksforgeeks.org/')
        elif 'open amazon' in query:
            speak('opening amazon,just a moment')
            webbrowser.open('www.amazon.com')

        # On System
        elif 'set alarm' in query or 'alarm' in query:
            speak('Okay')
            speak('Set your alarm')
            showinfo('Nofitication', 'Set Your Alarm')

            clock = Toplevel()

            def alarm(set_alarm_timer):

                while True:
                    time.sleep(1)
                    current_time = datetime.datetime.now()
                    now = current_time.strftime('%H:%M:%S')
                    date = current_time.strftime('%d/%m/%Y')
                    print('The set date is:', date)
                    print(now)
                    clock.update()
                    if now == set_alarm_timer:
                        print('alarm Raised')
                        winsound.PlaySound('alrwavsound.wav', winsound.SND_ASYNC)

                        break


            def actual_time():
                showinfo('Notification', 'Your Alarm is set')
                set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
                if hour.get() == '' or min.get() == '' or sec.get() == '':
                    showinfo('Warning','set the values first')
                alarm(set_alarm_timer)



            clock.title('Alarm Clock')
            clock.geometry('400x150')
            clock.resizable(False, False)
            time_format = Label(clock, text='Enter time in 24-hr format', fg='red', bg='black', font='Verdana').place(
                x=60, y=120)
            addTime = Label(clock, text='Hour  Min  Sec', font=60).place(x=110)
            setAlarm = Label(clock, text='Alarm Time', fg='blue', relief=SOLID, font=('Verdana,7,bold')).place(x=0,
                                                                                                               y=29)

            # Variables require to set the alarm
            hour = StringVar()
            min = StringVar()
            sec = StringVar()

            # Time to set alarm

            hourTime = Entry(clock, textvariable=hour, bg='pink', width=15).place(x=110, y=30)
            minTime = Entry(clock, textvariable=min, bg='pink', width=15).place(x=150, y=30)
            secTime = Entry(clock, textvariable=sec, bg='pink', width=8).place(x=200, y=30)

            # Button To set the alarm
            submit = Button(clock, text='Set Alarm', fg='red', width=10, command=actual_time).place(x=110, y=70)


            clock.mainloop()





        elif 'open interpreter' in query:
            speak('opening interpreter')
            PythonPath = "C:\\Users\\HOME\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe"
            os.startfile(PythonPath)

        elif 'open c drive' in query:
            speak('Opening C drive')
            os.startfile('C:')

        elif 'open d drive' in query:
            speak('Opening d drive')
            os.startfile('D:')

        elif 'open e drive' in query:
            speak('Opening E drive')
            os.startfile('E:')

        else:
            # speak('Sorry Sir')
            # NEW oNE ADDED 12/15/20
            
            webbrowser.open("https://www.google.com/search?q=" +query)
            
            speak('Searching for' + query)
            time.sleep(5)
            speak('Wait just a moment')
            # time.sleep()

            speak('Here is what i found')

    TakeInputCommand()


def on_enter(e):
    InputsearchBtn['background'] = 'red'
    # print('dfgddf')


def on_leave(e):
    InputsearchBtn['background'] = 'blue'


# test variable

InputSearchBox = Entry(win, width=50, font=('verdana', 12))
InputSearchBox.place(x=200, y=430, height=40)
InputsearchBtn = Button(win, text='Ask Me', width=10, height=2, bg='blue', fg='white',
                        command=lambda: threading.Thread(target=Askmebtn).start())
InputsearchBtn.bind('<Enter>', on_enter)
InputsearchBtn.bind('<Leave>', on_leave)
InputsearchBtn.place(x=697, y=430)

win.mainloop()
