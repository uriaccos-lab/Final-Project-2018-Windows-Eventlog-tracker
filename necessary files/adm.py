# This file should be located at c:\ to work

import os
import winshell
import sys


def winshell_shortcut(shortcut_name):
    # creating shortcut to run the code through so you could elevate the code, bring UAC and make the event.logtype
    # = "security" works.
    filepath = os.path.join(os.getcwd(), shortcut_name)
    path = sys.executable  # running python location \python27\python.exe
    sh = winshell.shortcut(filepath)  # winshell.shortcut(location)
    sh.path = path
    sh.description = "Shortcut to code1"
    sh.arguments = '"%s\\code1.py"' % os.getcwd()
    sh.write(filepath)  # necessary


def runad(file_name):  # run as administrator
    path = "'%s\\%s'" % (os.getcwd(), file_name)
    st1 = "powershell.exe Start-Process "
    st2 = " -Verb RunAs "  #  -WindowStyle Hidden
    commamd = st1 + path + st2
    print commamd
    os.system(commamd)


if __name__ == "__main__":
    runad("auditadmin.bat")  # changing audit policy :)
    winshell_shortcut("python.lnk")
    raw_input("Insert data from: ")  # last day, week, year, all-times
    runad("python.lnk")
