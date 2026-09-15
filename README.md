# Final-Project-2018-Windows-Eventlog-tracker
A 2018 project before Ai era, The main goal of the project is to notify about security problems on windows. Automatic scanning of the Event Log Viewer files of the security domain, filtering it to the relevance ones, and presenting it to the user. In addition the user can scan a file within the program which uses on VirusTotal API
### Running the program
you need:\
windows\
python 2.X\
installing packages winshell,pywin32,requests\
An api key of VirusTotal to insert in the GUIOBJ.py code

There are some **premissions** you need to give to run the program adm.py.\
**Otherwise**, you can run as administrator the code1.py and it should work fine.\
An example of running it as administraor through the cmd:\
  •Open CMD as ADMINSTRATOR\
  •go to the folder location of "code1.py"\
  •run the command:\
   C:\PYTHON27\PYTHON.EXE "filelocation"\
  •for example:\
   C:\PYTHON27\PYTHON.EXE "C:\USERS\URI\PROJECT\NECESSARYFILES\CODE1.PY"

### Video
<img width="736" height="544" alt="record_000002-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/942d3e7b-dafd-4ffe-920a-1f48b248f0f8" />
<img width="736" height="544" alt="record_000002-ezgif com-video-to-gif-converter (1)" src="https://github.com/user-attachments/assets/15109a40-0ffb-4e1b-ac59-67c61f615d65" />


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
