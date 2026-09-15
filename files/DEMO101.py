import win32evtlog
import time
import win32api
import win32event
import win32con
import sys
import pickle
import subprocess

enters = 5
time_intervals = 2
idle_time = 1


def lastevent_func(x):
    x = x
    x = pickle.dumps(x)
    lastevent_file = open('lastevent_file.txt', 'w+')
    lastevent_file.write(x)
    lastevent_file.close()


def read_lastevent():
    try:
        lastevent_file = open('lastevent_file.txt', 'r')
        x = lastevent_file.read()
        x = pickle.loads(x)
        return x
    except:
        print "no last event found !"


def read_save():
    variables = enters, time_intervals, idle_time
    try:
        file_save = open('file_save.txt', 'r')
        i = 0
        for var in variables:
            k = file_save.readline()
            k = k.split(':')
            k = k[1].split(' ')
            var = int(k[1])
        file_save.close()
    except IOError as e:
        print "I/O error({0}): {1} - You had never saved your settings".format(e.errno, e.strerror)


def generate_massage(info_text, time_generated, eventid, more_info):
    message = {'info_text': info_text, 'time_generated': str(time_generated), 'eventid': eventid, 'more_info': more_info}
    return message


def send_warnings(message_list):
    warnings_str = pickle.dumps(["Warnings: ", pickle.dumps(message_list)])
    print warnings_str
    warnings_file = open('warnings.txt', 'w+')
    warnings_file.write(warnings_str)
    warnings_file.close()


def getIdleTime():
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0


def notify(hand):
    h_event = win32event.CreateEvent(None, 1, 0, 'function_wait')

    if win32evtlog.NotifyChangeEventLog(hand, h_event) == 0:
        print "failed"
        print win32api.GetLastError()
        return False
    else:  # func succeded
        flag = 0
        win32event.ResetEvent(h_event)
        while flag == 0 and win32event.WaitForSingleObject(h_event, -1) == win32con.WAIT_OBJECT_0:  # 0xFFFFFFF
            print "hEvent:", h_event
            print "Succeeded, do something"
            flag = 1
            return True


def time_sub(time1,
             time2):  # a function which calculates time intervals between two different times, time format:hh/mm/ss
    h1 = time1.hour
    m1 = time1.minute
    s1 = time1.second
    h2 = time2.hour
    m2 = time2.minute
    s2 = time2.second
    h_sub = 0
    m_sub = 0
    s_sub = 0
    if h1 > h2:
        if s1 - s2 < 0:
            m2 += 1
            s_sub = s1 - s2 + 60
        else:
            s_sub = s1 - s2
        if m1 - m2 < 0:
            h2 += 1
            m_sub = m1 - m2 + 60
        else:
            m_sub = m1 - m2
        h_sub = h1 - h2
    elif h2 > h1:
        if s2 - s1 < 0:
            m1 += 1
            s_sub = s2 - s1 + 60
        else:
            s_sub = s2 - s1
        if m2 - m1 < 0:
            h1 += 1
            m_sub = m2 - m1 + 60
        else:
            m_sub = m2 - m1
        h_sub = h2 - h1
    else:  # if h1==h2
        if m2 > m1:
            if s2 - s1 < 0:
                m1 += 1
                s_sub = s2 - s1 + 60
            else:
                s_sub = s2 - s1
            m_sub = m2 - m1
        if m1 > m2:
            if s1 - s2 < 0:
                m2 += 1
                s_sub = s1 - s2 + 60
            else:
                s_sub = s1 - s2
            m_sub = m1 - m2
        else:  # m2==m1
            if s2 - s1 < 0:
                s_sub = s2 - s1 + 60
            else:
                s_sub = s2 - s1
            m_sub = 0
        h_sub = 0  # in case h1+=1

    return [h_sub, m_sub, s_sub]


read_save()

lastevent = ''
CountArray = {4625: 0, 4649: 0, 4803: 0, 4725: 0, 4726: 0, 4720: 0, 4688: 0, 4698: 0, 4946: 0, 4947: 0, 4697: 0}
time_generated = {4625: (), 4649: (), 4803: (), 4725: (), 4726: (), 4720: (), 4688: (), 4698: (), 4946: (), 4947: (),
                  4697: ()}
handles = {4625: []}  # no need
messages_list = ""

server = 'localhost'  # name of the target computer to get event logs
logtype = 'Security'  # 'Application' # 'Security'
hand = win32evtlog.OpenEventLog(server, logtype)
flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
# total = win32evtlog.GetNumberOfEventLogRecords(hand)


try:
    x = open('warnings.txt', 'r')
    x.close()
    t = read_lastevent()
    print "t", t
    flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEEK_READ
    events = win32evtlog.ReadEventLog(hand, flags, t,
                                      2 ** 19 - 1)  # max buffer size 0.5 MB (The maximum size of this buffer is 0x7ffff bytes. 2**19-1)
    while len(events) != 0:
        print len(events)
        if events:
            for event in events:
                if event.EventID in CountArray:
                    CountArray[event.EventID] += 1
                if event.EventID in time_generated:
                    # CountArray[4625] += 1
                    time_generated[event.EventID] = (event.TimeGenerated,) + time_generated[event.EventID]
                    handles[4625].append(hand)
                    print "Computer Name", event.ComputerName
                    print 'Event Category:', event.EventCategory
                    print 'Time Generated:', event.TimeGenerated
                    print 'Source Name:', event.SourceName
                    print 'Event ID:', event.EventID
                    print 'Event Type:', event.EventType
                    print 'Record Number:', event.RecordNumber
                    data = event.StringInserts
                    if data:
                        print 'Event Data:'
                        for msg in data:
                            print msg
                    print
                lastevent = event.RecordNumber
        flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(hand, flags, 0,
                                          2 ** 19 - 1)  # max buffer size 0.5 MB (The maximum size of this buffer is 0x7ffff bytes. 2**19-1)
    lastevent_func(lastevent)


except IOError as e:  # put here all the code that is not real time api and send it first time warnings
    print "I/O error({0}): {1} - First time run, please wait we are making the file".format(e.errno, e.strerror)
    flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(hand, flags, 0,
                                      2 ** 19 - 1)  # max buffer size 0.5 MB (The maximum size of this buffer is 0x7ffff bytes. 2**19-1)
    while len(events) != 0:
        print len(events)
        if events:
            for event in events:
                if event.EventID in CountArray:
                    CountArray[event.EventID] += 1
                if event.EventID in time_generated:
                    # CountArray[4625] += 1
                    time_generated[event.EventID] = (event.TimeGenerated,) + time_generated[event.EventID]
                    handles[4625].append(hand)
                    print "Computer Name", event.ComputerName
                    print 'Event Category:', event.EventCategory
                    print 'Time Generated:', event.TimeGenerated
                    print 'Source Name:', event.SourceName
                    print 'Event ID:', event.EventID
                    print 'Event Type:', event.EventType
                    print 'Record Number:', event.RecordNumber
                    data = event.StringInserts
                    if data:
                        print 'Event Data:'
                        for msg in data:
                            print msg
                    print
                lastevent = event.RecordNumber
        events = win32evtlog.ReadEventLog(hand, flags, 0, 2 ** 19 - 1)

    lastevent_func(lastevent)


time.sleep(3)
print "*"
temp = []
g1 = []
if len(time_generated[4625]) > enters:
    i = 0
    for i in xrange(len(time_generated[4625])):
        if i < len(time_generated[4625]) - 1:
            [h, m, s] = time_sub(time_generated[4625][i], time_generated[4625][i + 1])
            if h == 0 and m < time_intervals:
                print i, "eeeeeeeeeeeeee"
                temp.append(time_generated[4625][i])
            else:
                if len(temp) > enters - 2:
                    print "generated message, temp:", temp
                    g1.append(
                        generate_massage(
                            "Someone has tried {} times to log on your computer and failed.".format(len(temp) + 1),
                            time_generated[4625][i], 4625, ''))
                temp = []
        else:
            if len(temp) > enters - 2:
                print "generated message, temp:", temp
                g1.append(
                    generate_massage(
                        "Someone has tried {} times to log on your computer and failed.".format(len(temp) + 1),
                        time_generated[4625][i], 4625, ''))

print "g1", g1

for eventid in CountArray:
    if CountArray[eventid] != 0:
        if eventid == 4649:
            print "A replay attack was detected, event id:", eventid
            print time_generated[4649][len(time_generated[4649]) - 1]
            g1.append(generate_massage("A replay attack was detected",
                                       time_generated[eventid][0], eventid, ''))
        elif eventid == 4803:  # Screen saver opened
            print time_generated[4803]
            g1.append(generate_massage("Screen saver opened",
                                       time_generated[eventid][0], eventid, ''))
        elif eventid == 4801:  # workstation unlocked
            print time_generated[4801]
        elif eventid == 4697:
            g1.append(generate_massage("A service was installed in the system.",
                                       time_generated[eventid][0], eventid, ''))
            print "A service was installed in the system."
        elif eventid == 4946:
            g1.append(generate_massage("A rule added in windows firewall.",
                                       time_generated[eventid][0], eventid, ''))
            print "A rule added in windows firewall."
        elif eventid == 4947:
            g1.append(generate_massage("A rule modified in windows firewall.",
                                       time_generated[eventid][0], eventid, ''))
            print "A rule modified in windows firewall."
        elif eventid == 4698:
            g1.append(generate_massage("A scheduled task was created.",
                                       time_generated[eventid][0], eventid, ''))
            print "A scheduled task was created."
        elif eventid == 4720:
            g1.append(generate_massage("A user account was created.",
                                       time_generated[eventid][0], eventid, ''))
            print "A user account was created."
        elif eventid == 4726:
            g1.append(generate_massage("A user account was deleted.",
                                       time_generated[eventid][0], eventid, ''))
            print "A user account was deleted."
        elif eventid == 4725:
            g1.append(generate_massage("A user account was disable.",
                                       time_generated[eventid][0], eventid, ''))
            print "A user account was disable."
        print eventid, " Watch out!"

print "*"
send_warnings(g1)
time.sleep(3)
print "*"

p1 = subprocess.Popen('python GUI2.py')

CountArray = {4625: 0, 4649: 0, 4803: 0}
time_generated = {4625: (), 4649: (), 4803: ()}
handles = {4625: []}
messages_list = ""
while True:
    if notify(hand) == True:
        events = win32evtlog.ReadEventLog(hand, flags, 0,
                                          2 ** 19)  # max buffer size 0.5 MB (The maximum size of this buffer is 0x7ffff bytes. 2**19-1)
        for event in events:
            print "Event id:", event.EventID