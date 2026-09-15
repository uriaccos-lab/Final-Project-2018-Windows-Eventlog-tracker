# Final-Project-2018-Windows-Eventlog-tracker
A 2018 project with no Ai been used.
###Running the program
you need:\ 
windows\
python 2.X\
installing packages winshell,pywin32,requests,.
There are some premissions you need to give to run the 
The main goal of the project is to notify about security problems on windows. Automatic scanning of the Event Log Viewer files of the security domain, filtering it to the relevance ones, and presenting it to the user. In addition the user can scan a file within the program which uses on VirusTotal API

### The system can detect and notify the user about the following:
•	Viruses in an executable file the user suspected.\
•	Incorrect password entry during user login.\
•	Screensaver activation following a prolonged period of inactivity.\
•	Windows Firewall.\
•	Scheduled tasks.\
•	System users.\

### Development Environment
•Python: I chose Python for this project because it is an easy, user-friendly language with an endless array of libraries.\
•winshell: Windows features user interfaces defined as "Shell" functions. These include the desktop, shortcuts, special folders, and data stores. This module allows us to use Python to communicate with Windows and interact with these interfaces.\
•Tkinter: A library included with Python that is used to create graphical user interfaces (GUIs). It essentially serves as a Python interface for Tcl/Tk. Tcl is a high-level, cross-platform programming language—meaning, like Python, it can run on various operating systems—while Tk is the GUI toolkit built alongside Tcl, which is also compatible with a wide range of platforms.\
•PyWin32: win32evtlog, win32api, win32event, win32con.\
•os: A built-in Python library for general interaction with the operating system; it can be used on any platform where Python is installed.
•sys: A built-in Python library that provides access to variables and functions related to the Python interpreter.\
•pickle: A Python library that allows Python data structures—such as variables or dictionaries—to be converted into a string format. subprocess: A Python library that enables the use of processes and allows for interfacing with a process's standard input, output, and error streams.\
•requests: A highly powerful Python library focused on networking (specifically HTTP/port 80). It significantly reduces the amount of code required for sending and receiving data over the internet; it is user-friendly, facilitates interaction with websites and their APIs, and simplifies the process.\
Details regarding the development environment and required tools:
•PyCharm

### Module Description
An overview of the modules comprising the product and the interrelationships between them.\
adm.py -> auditadmin.bat -> code1.py ->GUIOBJ.py

<img width="486" height="892" alt="image" src="https://github.com/user-attachments/assets/d481be6d-3db7-405f-b949-9af080f443bd" />
