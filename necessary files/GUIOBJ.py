from Tkinter import *
import Tkconstants, tkFileDialog, ttk
import os
import time
import sys
import pickle
import threading
import requests

# the full documentation is in the written work

class gui(Tk):

    def __init__(self):
        Tk.__init__(self)  #  self._number=1
        self._enters = IntVar()
        self._enters.set(5)
        self._timeintervals = IntVar()
        self._timeintervals.set(2)
        self._idletime = IntVar()
        self._idletime.set(1)

        self._logon = BooleanVar()
        self._screen_saver = BooleanVar()
        self._user_accound_d = BooleanVar()
        self._user_accound_cr = BooleanVar()
        self._user_accound_wd = BooleanVar()
        self._scheduled_task = BooleanVar()
        self._service_installed = BooleanVar()
        self._windows_firwall_changed = BooleanVar()
        self._windows_firwall_added = BooleanVar()

        self._logon.set(True)
        self._screen_saver.set(True)
        self._user_accound_d.set(True)
        self._user_accound_cr.set(True)
        self._user_accound_wd.set(True)
        self._scheduled_task.set(True)
        self._service_installed.set(False)
        self._windows_firwall_changed.set(True)
        self._windows_firwall_added.set(True)

        # Tabs
        self._n = ttk.Notebook(self, padding=(10, 10, 10, 10), width=0, height=0)
        self._f1 = ttk.Frame(self._n, borderwidth=5, relief="sunken")
        self._f2 = ttk.Frame(self._n, borderwidth=5, relief="sunken")
        self._f3 = ttk.Frame(self._n, borderwidth=5, relief="sunken")
        self._n.add(self._f1, text="Warnings")
        self._n.add(self._f2, text="Virus Scan")
        self._n.add(self._f3, text="Settings")
        self._namelbl = ttk.Label(self._f1, text="Name")
        self._name = ttk.Entry(self._f1)

        # Tree
        self._tree = ttk.Treeview(self._f1, columns=('Date & Time', 'Event Id'))
        # tree['columns'] = ('Date & Time','Event Id')
        self._tree.column('#0', width=100, anchor='center')
        self._tree.heading('#0', text='info')
        self._tree.column('Date & Time', width=100, anchor='center')
        self._tree.heading('Date & Time', text='Date & Time')
        self._tree.column('Event Id', width=100, anchor='center')
        self._tree.heading('Event Id', text='Event Id')

        self.filename = ""
        self._md5 = ""

        self.read_save()
        print self._logon.get()
        self.title("Uri's anti hack")
        self.update()
        self.minsize(470, 400)
        self.iconbitmap(os.getcwd() + '\\favicon.ico')
        self.option_add('*tearOff', FALSE)

        # win = Toplevel(root)
        # win['menu'] = menubar - add in the end

        # menu bar
        self._menubar = Menu(self)
        self._menu_file = Menu(self._menubar)
        self._menu_help = Menu(self._menubar)

        self._menubar.add_cascade(menu=self._menu_file, label='File')
        self._menubar.add_cascade(menu=self._menu_help, label='Help')

        self._menu_help.add_command(label="Help & doc", command=self.openHelp)
        self._menu_help.add_separator()
        self._menu_help.add_command(label="About", command=self.openAbout)
        self.config(menu=self._menubar)

        # tree.insert('', 'end', 'widgets', text='Widget Tour')
        # tree.insert('', 0, 'gallery', text='Applications')
        # tree.insert('', 'end', text='Tutorial')
        # id = tree.insert('widgets', 'end', text='Canvas')
        # tree.insert(id, 'end', text='Tree')
        # tree.detach('widgets')
        # tree.move('widgets', 'gallery', 'end')
        # tree.item('widgets', open=TRUE)
        # tree.set('widgets', 'size', '12KB')
        # size = tree.set('widgets', 'size')
        # tree.insert('', 'end', text='Listbox', values=('15KB Yesterday mark'))
        # tree.insert('', 'end', text='button', tags=('ttk', 'simple'))
        # tree.tag_configure('ttk', background='yellow')
        # tree.tag_bind('ttk', '<1>', itemClicked)  # the item clicked can be found via tree.focus()
        self._tree.bind('<ButtonRelease-3>', lambda x: self.itemClicked(x.x_self, x.y_self))
        self._tree.bind(' <Double-Button-1>', lambda x: self.itemClicked(x.x_self, x.y_self))
        # Virus Scan Widgets
        self._File_Label1 = ttk.Label(self._f2, text="File:")
        self._menu_file.add_command(label="Scan warnings", command=self.get_warnings)
        self._menu_file.add_command(label="Open", command=lambda: self.openFile(self._File_Label1))
        self._menu_file.add_command(label="Save", command=self.save)
        self._menu_file.add_command(label="Prefences", command=self.Prefences)
        self._menu_file.add_separator()
        self._menu_file.add_command(label="Exit", command=self.Exit)

        Open_Button1 = ttk.Button(self._f2, text="Open", command=lambda: self.openFile(self._File_Label1))
        Send_Button1 = ttk.Button(self._f2, text="Send file to scan", command=self.sendFile)
        namelbl3 = ttk.Label(self._f2, text="The Answers will be in the warnings tab in a few minutes")
        namelbl4 = ttk.Label(self._f2, text="Can't find the scan answers? get it again")
        File_Label2 = ttk.Label(self._f2, text="File:")
        Open_Button2 = ttk.Button(self._f2, text="Open", command=lambda: self.openFile(File_Label2))
        Send_Button2 = ttk.Button(self._f2, text="Send file to get report", command=self.sendFile2)

        # Settings
        label_warn = ttk.Label(self._f3, text="Warn me when:")
        label_logon = ttk.Label(self._f3, text="Logon:")
        label_screensaver = ttk.Label(self._f3, text="Screen Saver")
        label_useraccount = ttk.Label(self._f3, text="User account")
        label_application = ttk.Label(self._f3, text="Application")
        label_firewall = ttk.Label(self._f3, text="Windows firewall")

        logon_button = ttk.Checkbutton(self._f3,
                                       text="Someone has tried to enter your password {0} times in time intervals of {1} and failed.".format(
                                           self._enters.get(), self._timeintervals.get()), onvalue=True, offvalue=False,
                                       variable=self._logon)
        screensaver_button = ttk.Checkbutton(self._f3,
                                             text="Someone/Something has waken up your computer and the computer was idle for {0} hours".format(
                                                 self._idletime.get()), variable=self._screen_saver, onvalue=True, offvalue=False)
        useraccountd_button = ttk.Checkbutton(self._f3, text="deleted", variable=self._user_accound_d, onvalue=True, offvalue=False)
        useraccountcr_button = ttk.Checkbutton(self._f3, text="created", variable=self._user_accound_cr, onvalue=True,
                                               offvalue=False)
        useraccountwd_button = ttk.Checkbutton(self._f3, text="disabled", variable=self._user_accound_wd, onvalue=True,
                                               offvalue=False)
        windowsfirewalladded_button = ttk.Checkbutton(self._f3, text="windows firewall rule added", variable=self._windows_firwall_added, onvalue=True,
                                         offvalue=False)
        service_button = ttk.Checkbutton(self._f3, text="new service installed", variable=self._service_installed,
                                              onvalue=True, offvalue=False)
        windowsfirewallchanged_button = ttk.Checkbutton(self._f3, text="windows firewall rule changed",
                                                        variable=self._windows_firwall_changed,
                                                        onvalue=True, offvalue=False)
        scheduled_button = ttk.Checkbutton(self._f3, text="scheduled task was created",
                                                        variable=self._scheduled_task,
                                                        onvalue=True, offvalue=False)
        ok = ttk.Button(self, text="Okay")
        cancel = ttk.Button(self, text="Cancel")

        self._logon_id=4625
        self._screen_saver_id=4803
        self._user_accound_d_id=4726
        self._user_accound_wd_id=4725
        self._user_accound_cr_id=4720
        self._service_installed_id=4697
        self._windows_firwall_changed_id=4947
        self._windows_firwall_add_id = 4946
        self._scheduled_task_id = 4698

        self.dictionary = {self._logon_id: self._logon, self._screen_saver_id: self._screen_saver,
                      self._user_accound_d_id: self._user_accound_d, self._user_accound_cr_id:
                          self._user_accound_cr, self._user_accound_wd_id: self._user_accound_wd,
                      self._service_installed_id: self._service_installed, self._scheduled_task_id:
                          self._scheduled_task, self._windows_firwall_add_id: self._windows_firwall_added,
                      self._windows_firwall_changed_id: self._windows_firwall_changed}

        self._n.grid(column=0, row=0, sticky=(N, E, W, S))

        self._tree.grid(column=0, row=1, sticky=(N, E, W, S))
        # namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
        # name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        # one.grid(column=0, row=2, sticky=S)
        # two.grid(column=1, row=2, sticky=S)
        # three.grid(column=2, row=2, sticky=S)

        self._File_Label1.grid(column=0, row=0, sticky=(W))
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
        useraccountcr_button.grid(column=0, row=7, sticky=(W))
        useraccountwd_button.grid(column=0, row=8, sticky=(W))
        scheduled_button.grid(column=0, row=10, sticky=(W))
        service_button.grid(column=0, row=11, sticky=(W))
        windowsfirewallchanged_button.grid(column=0, row=13, sticky=(W))
        windowsfirewalladded_button.grid(column=0, row=14, sticky=(W))

        ok.grid(column=1, row=1, )
        cancel.grid(column=2, row=1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self._n.rowconfigure(0, weight=1)
        self._n.columnconfigure(0, weight=1)

        self._f1.columnconfigure(0, weight=1)
        self._f1.rowconfigure(1, weight=1)
        self._f1.rowconfigure(0, weight=1)

        self._f2.columnconfigure(0, weight=1)
        self._f2.columnconfigure(1, weight=1)
        self._f2.rowconfigure(0, weight=1)
        self._f2.rowconfigure(1, weight=1)
        self._f2.rowconfigure(2, weight=1)
        self._f2.rowconfigure(3, weight=1)
        self._f2.rowconfigure(4, weight=1)
        self._f2.rowconfigure(5, weight=1)
        # f1.columnconfigure(1, weight=1)
        # f1.columnconfigure(2, weight=1)
        # f1.columnconfigure(3, weight=1)
        # f1.rowconfigure(2, weight=1)
        self._f3.columnconfigure(0, weight=1)
        self._f3.rowconfigure(1, weight=1)
        self._f3.rowconfigure(0, weight=1)
        self._f3.rowconfigure(2, weight=1)
        self._f3.rowconfigure(3, weight=1)
        self._f3.rowconfigure(4, weight=1)
        self._f3.rowconfigure(5, weight=1)
        self._f3.rowconfigure(6, weight=1)
        self._f3.rowconfigure(7, weight=1)
        self._f3.rowconfigure(8, weight=1)
        self._f3.rowconfigure(9, weight=1)
        self._f3.rowconfigure(10, weight=1)
        self._f3.rowconfigure(11, weight=1)
        self._f3.rowconfigure(12, weight=1)
        self._f3.rowconfigure(13, weight=1)
        self.get_warnings()

    # functions
    def Exit(self):
        try:
            os.remove(os.getcwd() + '\\warnings.txt')
        except:
            print "warnings.txt not found"
        self.destroy()

    def save(self):
        file_save = open('file_save.txt', 'w+')
        file_save.write('enters: {} \ntime intervals: {} \nidle time: {} \nlogon: {} \nscreen_saver: {} \nuser_accound_d: {} \n\
    user_accound_ch: {} \nuser_accound_cr: {} \nprocess_started: {} \napplication_installed: {} \nwindows_\
    firwall_changed: {} \n'.format(self._enters.get(), self._timeintervals.get(), self._idletime.get(), self._logon.get(), self._screen_saver.get()
                                   , self._user_accound_d.get(), self._user_accound_cr.get(), self._user_accound_wd.get(),
                                   self._scheduled_task.get(), self._service_installed.get(), self._windows_firwall_changed.get(), self._windows_firwall_added))

        file_save.close()

        file_save2 = open('file_save2.txt', 'w')
        l = []
        for child in self._tree.get_children():
            print(self._tree.item(child))
            l.append(self._tree.item(child))
        print l
        file_save2.write(pickle.dumps(l))
        file_save2.close()

    def read_save(self):
        variables = self._enters, self._timeintervals, self._idletime, self._logon, self._screen_saver, \
                    self._user_accound_d, self._user_accound_cr, self._user_accound_wd, \
                    self._scheduled_task, self._service_installed, self._windows_firwall_changed, self._windows_firwall_added
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

        try:
            file_save2 = open('file_save2.txt', 'r')
            info = pickle.loads(file_save2.read())
            print "info", info
            file_save2.close()
            for item in info:
                self._tree.insert('', 0, text='{}'.format(item['text']), values=(item['values']))
        except IOError as e:
            print "I/O error({0}): {1} - You had never saved your settings".format(e.errno, e.strerror)

    def get_warnings(self):
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
        pb.grid(column=0, row=1)
        result=None
        i=0
        while result==None and i<10:
            try:
                f_size=os.path.getsize(os.getcwd()+'\\warnings.txt')
                if f_size>0:
                    info = open('warnings.txt', 'r')
                    y = pickle.loads(info.read())
                    x = []
                    if y[0] == "Warnings: ":
                        x = pickle.loads(y[1])
                    print "its x: ", x
                    for item in x:
                        if self.dictionary[item['eventid']]==True:
                            self._tree.insert('', 0, text='{}'.format(item['info_text']),
                                              values=(item['time_generated'], item['eventid'],item['more_info']))
                    info.close()
                    result=1
            except os.error as e:
                print e
                i+=1
        pb.stop()
        text1.configure(text="Done! :)")

    def openFile(self, File_Label):
        self.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("exe files", "*.exe"), ("all files", "*.*")))
        print self.filename
        File_Label.configure(text="File:" + self.filename)

    def openHelp(self):
        top = Toplevel()
        top.title("Help")
        top.grab_set()
        # top.geometry("700x100")
        top.resizable(0, 0)
        text = open('Help.txt', 'r')
        text1 = Text(top)
        text1.insert(INSERT, text.read())
        text1.grid(column=0, row=0)
        scrollbar = Scrollbar(top, orient=VERTICAL)
        text1.configure(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text1.yview)
        scrollbar.grid(column=1, row=0, sticky=N + S + E)
        text.close()

    def openAbout(self):
        top3 = Toplevel()
        top3.title("About")
        # top3.geometry("300x400")
        text = "This Program created to help the simple windows \nuser to protect and keep an eye at his own computer! \n\n2018 Uri Accos"
        text1 = ttk.Label(top3, text=text, font=("Arial", 11))
        text1.grid(column=0, row=0)
        top3.grab_set()
        # top3.resizable(0, 0)

    def itemClicked(self,x, y):
        menu = Menu()
        menu.add_command(label="delete", command=self.delete)
        menu.post(x, y)

    def item_double_clicked(self):
        item=self._tree.focus()
        if item!='':
            top = Toplevel()
            top.title("More Info")
            top.grab_set()
            top.resizable(0, 0)
            text = item['values'][2]
            text1 = ttk.Label(top, text=text, font=("Arial", 11))
            text1.grid(column=0, row=0)

    def sendFile(self):
        self._md5
        params = {'apikey': 'c1e5a2ec5a91f6270157e43c0f05ba8cf66a99e419d14707d64dd90b628c4af4'}
        files = {'file': (self.filename + ".exe", open(self.filename, 'rb'))}
        response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
        json_response = response.json()
        for line in json_response:
            print line, json_response[line]
        self._md5 = json_response['md5']
        print self._md5

    def sendFile2(self):
        print 'md5', self._md5
        params = {'apikey': 'c1e5a2ec5a91f6270157e43c0f05ba8cf66a99e419d14707d64dd90b628c4af4',
                  'resource': self._md5}
        headers = {"Accept-Encoding": "gzip, deflate",
                   "User-Agent": "gzip, My Python requests library example client or username"}
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)
        json_response = response.json()  # <type 'dict'>
        i = 0
        if (json_response["positives"] / json_response["total"]) * 100 > 50:
            print "malware detected"
            self._tree.insert('', 0, text='malware detected! : {}'.format(self.filename), values=())
        else:
            print "clean!"
            self._tree.insert('', 0, text='clean! : {}'.format(self.filename), values=())
        for line in json_response:
            if isinstance(json_response[line], dict):
                print i
                for l in json_response[line]:
                    print l, json_response[line][l]
            else:
                print i, line, type(json_response[line]), json_response[line]
            i += 1

    def Prefences(self):
        top3 = Toplevel()
        top3.title("Prefences")
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
        enters_spinbox = Spinbox(top3, from_=1, to=10, textvariable=self._enters, width=2)
        idletime_spinbox = Spinbox(top3, from_=1, to=3, textvariable=self._timeintervals, width=2)
        timeintervals_spinbox = Spinbox(top3, from_=1, to=20, textvariable=self._idletime, width=2)
        self._enters.set(enters_spinbox.get())
        self._timeintervals.set(timeintervals_spinbox.get())
        self._idletime.set(idletime_spinbox.get())
        print self._enters.get()
        print self._timeintervals.get()
        print self._idletime.get()
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

    def apply(self):
        self.save()

    def delete(self):
        print self._tree.focus()
        if self._tree.focus() != '':
            self._tree.delete(self._tree.focus())


if __name__=='__main__':
    root=gui()
    root.mainloop()
