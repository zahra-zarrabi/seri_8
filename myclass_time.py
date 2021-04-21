class my_time():
    def __init__(self):
        if item==1 or item==2:
            self.time1={'hour':int(input('Time 1:\nhour : ')),'minute':int(input('Minutes : ')),'second':int(input('Seconds :'))}
            self.time2 = {'hour': int(input('Time 2:\nhour : ')), 'minute': int(input('Minutes : ')), 'second': int(input('Seconds :'))}

    def my_sum(self):
        h=obj.time1['hour']+obj.time2['hour']
        m=obj.time1['minute']+obj.time2['minute']
        s=obj.time1['second']+obj.time2['second']
        if s>60:
            s-=60
            m+=1
        if m>60:
            m-=60
            h+=1
        return str(h)+':'+str(m)+':'+str(s)

    def my_sub(self):
        h = obj.time1['hour'] - obj.time2['hour']
        m = obj.time1['minute'] - obj.time2['minute']
        s = obj.time1['second'] - obj.time2['second']
        if s<0:
            s+=60
            m-=1
        if m<0:
            m+=60
            h-=1
        return str(h)+':'+str(m)+':'+str(s)

    def my_second(self):
        times = int(input('second:'))
        hour = int(times / 3600)
        times = times % 3600
        minute = int(times / 60)
        second = int(times % 60)
        return str(hour) + ':' + str(minute) + ':' + str(second)

    def my_time(self):
        hour = int(input("Time 1:\nhour : "))
        minute = int(input("Minutes : "))
        second = int(input("Seconds :"))
        h = hour * 3600
        m = minute * 60
        r = h + m + second
        return r


while True:
    item = int(input('Time calculations:\n1 sum of two time\n2 Subtraction of two time\n3 Convert seconds to time\n4 Convert time to seconds'))
    obj = my_time()
    if item == 1:
        print('sum of two time:', obj.my_sum())
    elif item == 2:

        print('Subtraction of two time:',obj.my_sub())
    elif item==3:

        print('is time: ',obj.my_second())
    elif item==4:

        print('Seconds: ',obj.my_time())


