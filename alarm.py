# -----------------------------------------------------------
# IMPORTING MODULES
# -----------------------------------------------------------

# time module is used to pause the program for some seconds
import time

# datetime module helps to get current system date and time
import datetime as dt

# winsound module is used to play alarm sound in Windows
import winsound as ws

# Thread module is used to run alarm in a separate process/thread
from threading import Thread

# tkinter module is used to create GUI (Graphical User Interface)
from tkinter import *

# * means importing all tkinter functions and widgets


# -----------------------------------------------------------
# THREAD FUNCTION
# -----------------------------------------------------------

# This function starts a new thread
# so GUI does not freeze while alarm is running

def threading():

    # target = myalarm means calling myalarm() function
    t1 = Thread(target=myalarm)

    # start the thread
    t1.start()


# -----------------------------------------------------------
# ALARM FUNCTION
# -----------------------------------------------------------

def myalarm():

    # infinite loop to continuously check time
    while True:

        # getting selected alarm time from dropdown menus
        set_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # getting current system time
        current_time = dt.datetime.now().strftime("%H:%M:%S")

        # printing both times in terminal
        print("Alarm Time:", set_time)
        print("Current Time:", current_time)

        # checking if current time matches alarm time
        if current_time == set_time:

            print("Wake Up !!!")

            # playing alarm sound asynchronously
            ws.PlaySound(
                r"C:\Users\Kishan Vishwakarma\Downloads\fire_alarm.wav",
                ws.SND_ASYNC
            )

            # stop loop after alarm rings
            break

        # wait for 1 second before checking again
        time.sleep(1)


# -----------------------------------------------------------
# CREATING TKINTER WINDOW
# -----------------------------------------------------------

# creating main window object
alarm = Tk()

# title of window
alarm.title("Alarm Clock")

# size of window
alarm.geometry("600x400")

# background color
alarm.config(bg="white")


# -----------------------------------------------------------
# HEADING LABELS
# -----------------------------------------------------------

# main heading label
Label(
    alarm,
    text="Alarm Clock",
    font=("Calibri", 24, "bold"),
    fg="blue",
    bg="white"
).pack(pady=20)

# subheading label
Label(
    alarm,
    text="Set Alarm Time",
    font=("Calibri", 16, "bold"),
    fg="green",
    bg="yellow"
).pack(pady=10)

# pack() places widget inside window
# pady adds vertical spacing


# -----------------------------------------------------------
# FRAME
# -----------------------------------------------------------

# Frame is used to organize widgets properly
frame = Frame(alarm, bg="white")

# placing frame in window
frame.pack(pady=20)


# -----------------------------------------------------------
# HOUR DROPDOWN
# -----------------------------------------------------------

# StringVar stores selected hour value
hour = StringVar(alarm)

# default selected value
hour.set("00")

# tuple containing hour values
hours = (
    '00','01','02','03','04','05','06','07','08','09',
    '10','11','12','13','14','15','16','17','18','19',
    '20','21','22','23'
)

# creating dropdown menu
hrs = OptionMenu(frame, hour, *hours)

# placing dropdown from left side
hrs.pack(side=LEFT, padx=10)


# -----------------------------------------------------------
# MINUTE DROPDOWN
# -----------------------------------------------------------

# StringVar stores selected minute value
minute = StringVar(alarm)

# default selected value
minute.set("00")

# tuple containing minute values
minutes = (
    '00','01','02','03','04','05','06','07','08','09',
    '10','11','12','13','14','15','16','17','18','19',
    '20','21','22','23','24','25','26','27','28','29',
    '30','31','32','33','34','35','36','37','38','39',
    '40','41','42','43','44','45','46','47','48','49',
    '50','51','52','53','54','55','56','57','58','59'
)

# creating dropdown menu
mins = OptionMenu(frame, minute, *minutes)

# placing dropdown
mins.pack(side=LEFT, padx=10)


# -----------------------------------------------------------
# SECOND DROPDOWN
# -----------------------------------------------------------

# StringVar stores selected second value
second = StringVar(alarm)

# default selected value
second.set("00")

# seconds values are same as minutes
seconds = minutes

# creating dropdown menu
secs = OptionMenu(frame, second, *seconds)

# placing dropdown
secs.pack(side=LEFT, padx=10)


# -----------------------------------------------------------
# SET ALARM BUTTON
# -----------------------------------------------------------

# Button widget executes threading() function
Button(
    alarm,
    text="Set Alarm",
    font=("Calibri", 15, "bold"),
    bg="red",
    fg="white",
    command=threading
).pack(pady=30)


# -----------------------------------------------------------
# MAINLOOP
# -----------------------------------------------------------

# mainloop keeps window running continuously
alarm.mainloop()