import os, winshell

desktop = winshell.desktop()
path = os.path.join(desktop, "myNeatWebsite.url")
print path
target = "http://www.google.com/"

shortcut = file(path, 'w')

shortcut.write('URL=%s' % target)
shortcut.close()

desktop = winshell.desktop()
path = os.path.join(desktop, "adm.lnk")
target = 'd:\Python27\python.exe runas r'"D:\\Users\\Uri\\Documents\\לימודים יב'\\סייבר\\project\\files\\adm.py"''
print target

shortcut = file(path, 'w')

shortcut.write(target)
shortcut.close()
