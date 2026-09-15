from Tkinter import *
import Tkconstants, tkFileDialog, ttk
import os
import time
import sys
import pickle
import threading


def Gui():
    root = Tk()

    enters = IntVar()
    enters.set(5)
    timeintervals = IntVar()
    timeintervals.set(1)
    idletime = IntVar()
    idletime.set(1)

    logon = BooleanVar()
    screen_saver = BooleanVar()
    user_accound_d = BooleanVar()
    user_accound_ch = BooleanVar()
    user_accound_cr = BooleanVar()
    process_started = BooleanVar()
    application_installed = BooleanVar()
    windows_firwall_changed = BooleanVar()

    logon.set(True)
    screen_saver.set(True)
    user_accound_d.set(True)
    user_accound_ch.set(True)
    user_accound_cr.set(True)
    process_started.set(True)
    application_installed.set(False)
    windows_firwall_changed.set(True)


    # functions
    def Exit():
        root.destroy()


    def save():
        file_save = open('file_save.txt', 'w+')
        file_save.write('enters: {} \ntime intervals: {} \nidle time: {} \nlogon: {} \nscreen_saver: {} \nuser_accound_d: {} \n\
    user_accound_ch: {} \nuser_accound_cr: {} \nprocess_started: {} \napplication_installed: {} \nwindows_\
    firwall_changed: {} \n'.format(enters.get(), timeintervals.get(), idletime.get(), logon.get(), screen_saver.get()
                                   , user_accound_d.get(), user_accound_ch.get(), user_accound_cr.get(),
                                   process_started.get(), application_installed.get(), windows_firwall_changed.get()))

        file_save.close()


    def read_save():
        variables = enters, timeintervals, idletime, logon, screen_saver, \
                    user_accound_d, user_accound_ch, user_accound_cr, \
                    process_started, application_installed, windows_firwall_changed
        try:
            file_save = open('file_save.txt', 'r')
            i = 0
            # print file_save
            # print file_save.read()
            for line in file_save:
                print line
                k = line.split(':')
                print k
                k = k[1].split(' ')
                if k[1] == "True":
                    variables[i].set(True)
                elif k[1] == "False":
                    variables[i].set(False)
                else:
                    variables[i].set(int(k[1]))
                i += 1
            file_save.close()
        except IOError as e:
            print "I/O error({0}): {1} - You had never saved your settings".format(e.errno, e.strerror)



    def get_warnings():
        print "started getting warnings"
        top = Toplevel()
        top.title("Scan")
        top.grab_set()
        top.resizable(0, 0)
        text = "Do not close this window!\nPlease wait while scaning computer info..."
        text1 = ttk.Label(top, text=text, font=("Arial", 11))
        pb = ttk.Progressbar(top, orient=HORIZONTAL, mode='indeterminate')
        pb.start()
        text1.grid(column=0, row=0)
        pb.grid(column=0,row=1)
        try:
            info = open('warnings.txt','r')
            y = pickle.loads(info)
            x = []
            if y[0] == "Warnings: ":
                x = pickle.loads(y[1])
            print "its x: ", x
            file_save2 = open('file_save2.txt', 'w+')
            file_save2.write(str(x))
        except IOError as e:
            print "I/O error({0}): {1} - Please run again adm.py and wait that code1.py will save settings".format(e.errno, e.strerror)
        pb.stop()
        text1.configure(text="Done! :)")



    def openFile(File_Label):
        root.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        print root.filename
        File_Label.configure(text="File:" + root.filename)


    def openHelp():
        top = Toplevel()
        top.title("Help")
        top.grab_set()
        # top.geometry("700x100")
        top.resizable(0, 0)
        text = open('Help.txt', 'rb')
        text1 = Text(top)
        text1.insert(INSERT, text.read())
        text1.grid(column=0, row=0)
        scrollbar = Scrollbar(top, orient=VERTICAL)
        text1.configure(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text1.yview)
        scrollbar.grid(column=1, row=0, sticky=N + S + E)


    def openAbout():
        top3 = Toplevel()
        top3.title("About")
        # top3.geometry("300x400")
        text = "This Program created to help the simple windows \nuser to protect and keep an eye at his own computer! \n\n2018 Uri Accos"
        text1 = ttk.Label(top3, text=text, font=("Arial", 11))
        text1.grid(column=0, row=0)
        top3.grab_set()
        # top3.resizable(0, 0)


    def itemClicked(x, y):
        menu = Menu()
        menu.add_command(label="delete", command=delete)
        menu.post(x, y)


    def sendFile():
        pass


    def Prefences():
        top3 = Toplevel()
        top3.title("About")
        # root.update()
        # root.minsize(470, 400)
        # top3.geometry("300x400")
        apply_button = ttk.Button(top3, text="Apply", command=apply)
        enters_text = "logon: " \
                      "if someone has tried"
        enters_text2 = "times to insert password in"
        timeintervals_text = "minutes time spaces, warn me! \n"
        idletime_text = "screen saver:" \
                        "if someone has \nwoke up screen saver and the \ncomputer was idle for"
        text2 = ttk.Label(top3, text=enters_text, font=("Arial", 11))
        text2_5 = ttk.Label(top3, text=enters_text2, font=("Arial", 11))
        text3 = ttk.Label(top3, text=timeintervals_text, font=("Arial", 11))
        text4 = ttk.Label(top3, text=idletime_text, font=("Arial", 11))
        text5 = ttk.Label(top3, text="hours, warn me!", font=("Arial", 11))
        enters_spinbox = Spinbox(top3, from_=1, to=10, textvariable=enters, width=2)
        idletime_spinbox = Spinbox(top3, from_=1, to=3, textvariable=timeintervals, width=2)
        timeintervals_spinbox = Spinbox(top3, from_=1, to=20, textvariable=idletime, width=2)
        enters.set(enters_spinbox.get())
        timeintervals.set(timeintervals_spinbox.get())
        idletime.set(idletime_spinbox.get())
        print enters.get()
        print timeintervals.get()
        print idletime.get()
        text2.grid(column=0, row=0, sticky=(W))
        text2_5.grid(column=0, row=1, sticky=(W))
        text3.grid(column=0, row=2, sticky=(W))
        text4.grid(column=0, row=3, sticky=(W))
        text5.grid(column=0, row=4, sticky=(W))
        enters_spinbox.grid(column=1, row=0, sticky=(E))
        timeintervals_spinbox.grid(column=1, row=1, sticky=(E))
        idletime_spinbox.grid(column=0, row=3, sticky=(S, E))
        apply_button.grid(column=1, row=5, sticky=(S, E))
        top3.grab_set()
        top3.resizable(0, 0)


    def apply():
        pass


    def delete():
        print tree.focus()
        if tree.focus() != '':
            tree.delete(tree.focus())


    # set up

    read_save()
    print logon.get()
    root.title("Uri's anti hack")
    root.update()
    root.minsize(470, 400)
    root.iconbitmap(os.getcwd() + '\\favicon.ico')
    root.option_add('*tearOff', FALSE)

    # win = Toplevel(root)
    # win['menu'] = menubar - add in the end

    # menu bar
    menubar = Menu(root)
    menu_file = Menu(menubar)
    menu_help = Menu(menubar)

    menubar.add_cascade(menu=menu_file, label='File')
    menubar.add_cascade(menu=menu_help, label='Help')

    menu_help.add_command(label="Help & doc", command=openHelp)
    menu_help.add_separator()
    menu_help.add_command(label="About", command=openAbout)
    root.config(menu=menubar)

    # Tabs
    n = ttk.Notebook(root, padding=(10, 10, 10, 10), width=0, height=0)
    f1 = ttk.Frame(n, borderwidth=5, relief="sunken")
    f2 = ttk.Frame(n, borderwidth=5, relief="sunken")
    f3 = ttk.Frame(n, borderwidth=5, relief="sunken")
    n.add(f1, text="Warnings")
    n.add(f2, text="Virus Scan")
    n.add(f3, text="Settings")
    namelbl = ttk.Label(f1, text="Name")
    name = ttk.Entry(f1)

    # Tree
    tree = ttk.Treeview(f1, columns=('Date & Time', 'Event Id'))
    # tree['columns'] = ('Date & Time','Event Id')
    tree.column('#0', width=100, anchor='center')
    tree.heading('#0', text='info')
    tree.column('Date & Time', width=100, anchor='center')
    tree.heading('Date & Time', text='Date & Time')
    tree.column('Event Id', width=100, anchor='center')
    tree.heading('Event Id', text='Event Id')
    tree.insert('', 'end', 'widgets', text='Widget Tour')
    tree.insert('', 0, 'gallery', text='Applications')
    tree.insert('', 'end', text='Tutorial')
    id = tree.insert('widgets', 'end', text='Canvas')
    tree.insert(id, 'end', text='Tree')
    # tree.detach('widgets')
    # tree.move('widgets', 'gallery', 'end')
    # tree.item('widgets', open=TRUE)
    # tree.set('widgets', 'size', '12KB')
    # size = tree.set('widgets', 'size')
    # tree.insert('', 'end', text='Listbox', values=('15KB Yesterday mark'))
    # tree.insert('', 'end', text='button', tags=('ttk', 'simple'))
    # tree.tag_configure('ttk', background='yellow')
    # tree.tag_bind('ttk', '<1>', itemClicked)  # the item clicked can be found via tree.focus()
    tree.bind('<ButtonRelease-3>', lambda x: itemClicked(x.x_root, x.y_root))
    # Virus Scan Widgets
    File_Label1 = ttk.Label(f2, text="File:")
    menu_file.add_command(label="Open", command=lambda: openFile(File_Label1))
    menu_file.add_command(label="Save", command=save)
    menu_file.add_command(label="Prefences", command=Prefences)
    menu_file.add_separator()
    menu_file.add_command(label="Exit", command=Exit)

    Open_Button1 = ttk.Button(f2, text="Open", command=lambda: openFile(File_Label1))
    Send_Button1 = ttk.Button(f2, text="Send file to scan", command=sendFile)
    namelbl3 = ttk.Label(f2, text="The Answers will be in the warnings tab in a few minutes")
    namelbl4 = ttk.Label(f2, text="Can't find the scan answers? get it again")
    File_Label2 = ttk.Label(f2, text="File:")
    Open_Button2 = ttk.Button(f2, text="Open", command=lambda: openFile(File_Label2))
    Send_Button2 = ttk.Button(f2, text="Send file to scan", command=sendFile)

    # Settings
    label_warn = ttk.Label(f3, text="Warn me when:")
    label_logon = ttk.Label(f3, text="Logon:")
    label_screensaver = ttk.Label(f3, text="Screen Saver")
    label_useraccount = ttk.Label(f3, text="User account")
    label_application = ttk.Label(f3, text="Application")
    label_firewall = ttk.Label(f3, text="Windows firewall")

    logon_button = ttk.Checkbutton(f3,
                                   text="Someone has tried to enter your password {0} times in time intervals of {1} and failed.".format(
                                       enters.get(), timeintervals.get()), onvalue=True, offvalue=False, variable=logon)
    screensaver_button = ttk.Checkbutton(f3,
                                         text="Someone/Something has waken up your computer and the computer was idle for {0} hours".format(
                                             idletime.get()), variable=screen_saver, onvalue=True, offvalue=False)
    useraccountd_button = ttk.Checkbutton(f3, text="deleted", variable=user_accound_d, onvalue=True, offvalue=False)
    useraccountch_button = ttk.Checkbutton(f3, text="changed", variable=user_accound_ch, onvalue=True, offvalue=False)
    useraccountcr_button = ttk.Checkbutton(f3, text="created", variable=user_accound_cr, onvalue=True, offvalue=False)
    process_button = ttk.Checkbutton(f3, text="process started", variable=process_started, onvalue=True, offvalue=False)
    appinstalled_button = ttk.Checkbutton(f3, text="new application installed", variable=application_installed,
                                          onvalue=True, offvalue=False)
    windowsfirewallchanged_button = ttk.Checkbutton(f3, text="windows firewall changed", variable=windows_firwall_changed,
                                                    onvalue=True, offvalue=False)
    ok = ttk.Button(root, text="Okay")
    cancel = ttk.Button(root, text="Cancel")

    n.grid(column=0, row=0, sticky=(N, E, W, S))

    tree.grid(column=0, row=1, sticky=(N, E, W, S))
    # namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
    # name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
    # one.grid(column=0, row=2, sticky=S)
    # two.grid(column=1, row=2, sticky=S)
    # three.grid(column=2, row=2, sticky=S)

    File_Label1.grid(column=0, row=0, sticky=(W))
    Open_Button1.grid(column=1, row=0)
    Send_Button1.grid(column=0, row=1)
    namelbl3.grid(column=0, row=2, sticky=(W))
    namelbl4.grid(column=0, row=3, sticky=(W))
    File_Label2.grid(column=0, row=4, sticky=(W))
    Open_Button2.grid(column=1, row=4)
    Send_Button2.grid(column=0, row=5)

    label_warn.grid(column=0, row=0, sticky=(W))
    label_logon.grid(column=0, row=1, sticky=(W))
    label_screensaver.grid(column=0, row=3, sticky=(W))
    label_useraccount.grid(column=0, row=5, sticky=(W))
    label_application.grid(column=0, row=9, sticky=(W))
    label_firewall.grid(column=0, row=12, sticky=(W))

    logon_button.grid(column=0, row=2, sticky=(W))
    screensaver_button.grid(column=0, row=4, sticky=(W))
    useraccountd_button.grid(column=0, row=6, sticky=(W))
    useraccountch_button.grid(column=0, row=7, sticky=(W))
    useraccountcr_button.grid(column=0, row=8, sticky=(W))
    process_button.grid(column=0, row=10, sticky=(W))
    appinstalled_button.grid(column=0, row=11, sticky=(W))
    windowsfirewallchanged_button.grid(column=0, row=13, sticky=(W))

    ok.grid(column=1, row=1, )
    cancel.grid(column=2, row=1)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    n.rowconfigure(0, weight=1)
    n.columnconfigure(0, weight=1)

    f1.columnconfigure(0, weight=1)
    f1.rowconfigure(1, weight=1)
    f1.rowconfigure(0, weight=1)

    f2.columnconfigure(0, weight=1)
    f2.columnconfigure(1, weight=1)
    f2.rowconfigure(0, weight=1)
    f2.rowconfigure(1, weight=1)
    f2.rowconfigure(2, weight=1)
    f2.rowconfigure(3, weight=1)
    f2.rowconfigure(4, weight=1)
    f2.rowconfigure(5, weight=1)
    # f1.columnconfigure(1, weight=1)
    # f1.columnconfigure(2, weight=1)
    # f1.columnconfigure(3, weight=1)
    # f1.rowconfigure(2, weight=1)
    f3.columnconfigure(0, weight=1)
    f3.rowconfigure(1, weight=1)
    f3.rowconfigure(0, weight=1)
    f3.rowconfigure(2, weight=1)
    f3.rowconfigure(3, weight=1)
    f3.rowconfigure(4, weight=1)
    f3.rowconfigure(5, weight=1)
    f3.rowconfigure(6, weight=1)
    f3.rowconfigure(7, weight=1)
    f3.rowconfigure(8, weight=1)
    f3.rowconfigure(9, weight=1)
    f3.rowconfigure(10, weight=1)
    f3.rowconfigure(11, weight=1)
    f3.rowconfigure(12, weight=1)
    f3.rowconfigure(13, weight=1)


    root.mainloop()
if __name__=="__main__":
    Gui().get_warnings()
    t1=threading.Thread(target=Gui)
    t1.start()
    t2=threading.Thread(target=Gui.get_warnings)
    t2.start()
