# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO DISPLAY CURRENT YEAR'S CALENDAR AND USER-INPUT YEAR'S CALENDAR USING THE calendar PACKAGE
#
# The calendar module allows output calendars like the program and provides additional useful functions
# related to the calendar. Functions and classes defined in the Calendar module use an idealized calendar,
# the current Gregorian calendar extended indefinitely in both directions. By default, these calendars
# have Monday as the first day of the week, and Sunday as the last (the European convention).
# The functions and classes defined in this module use an idealized calendar, current Gregorian calendar
# extended indefinitely in both directions.
#
# The calendar package is an inbuilt package in Python

# Importing necessary packages
import calendar
import tkinter as tk
from tkinter import *
from datetime import date

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    root.calLabel = Label(root, bg="royalblue4", fg="white", font=('Comic Sans MS',20))
    root.calLabel.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

    root.calendarTxt = Text(root, bg="khaki3", borderwidth=2, relief="raised", width=70, height=35)
    root.calendarTxt.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

    root.calendarEntry = Entry(root, width=30, textvariable=year, justify="center")
    root.calendarEntry.grid(row=3, column=1, padx=10, pady=10)

    root.getCalendarButton = Button(root, width=20, text="DISPLAY CALENDAR", command=getCalendar)
    root.getCalendarButton.grid(row=3, column=2, padx=10, pady=10)

    onStartUp()

# Defining onStartUp() to display current year's calendar when the application starts
def onStartUp():
    # Fetching the current year using year property of today() method of date class of datetime
    current_year = date.today().year
    # Fetching the calendar of the user-input year and storing it in calendar_text variable
    calendar_text = calendar.calendar(current_year)
    # Configuring label to display the year of the calendar
    root.calLabel.config(text=str(current_year)+" CALENDAR")
    # Displaying the calendar in the calendar Text Widget using the insert() method
    root.calendarTxt.insert(0.0, calendar_text)

# Defining getCalendar() to fetch user-input year and display the calendar of user-input yeat
def getCalendar():
    # Retrieving the user-input year and storing it in calendar_year variable as integer
    calendar_year = int(year.get())
    # Fetching the calendar of the user-input year and storing it in calendar_text variable
    calendar_text = calendar.calendar(calendar_year)
    # Configuring label to display the year of the calendar
    root.calLabel.config(text=str(calendar_year)+" CALENDAR")
    # Displaying the calendar in the calendar Text Widget using the insert() method
    root.calendarTxt.insert(0.0, calendar_text)

# Creating object of tk class
root = tk.Tk()
# Setting the title, window size, background color and disabling the resizing property
root.title("PythonCalendar")
root.geometry("520x600")
root.resizable(False, False)
root.configure(background = "royalblue4")
# Creating tkinter variables
year = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
