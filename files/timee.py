import win32evtlog


class Time(object):
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def __str__(self):
        return "%d:%d:%d" % (self.hour, self.minute, self.second)


def time_sub(time1,
             time2):  # a function which calculates time intervals between two different times time format:hh/mm/ss
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


server = 'localhost'  # name of the target computer to get event logs
logtype = 'Application'  # 'Application' # 'Security'
hand = win32evtlog.OpenEventLog(server, logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
# total = win32evtlog.GetNumberOfEventLogRecords(hand)


# while True:
events = win32evtlog.ReadEventLog(hand, flags, 0,
                                  2 ** 19)  # max buffer size 0.5 MB (The maximum size of this buffer is 0x7ffff bytes. 2**19-1)

time1 = Time(0, 24, 50)
time2 = Time(0, 20, 53)
print str(time1)
print str(time2)
print "start: "
[h, m, s] = time_sub(time1, time2)
print [h, m, s]
if h == 0 and m < 4:
    print "O.K , countinue"
