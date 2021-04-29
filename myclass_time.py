class my_time():
    def __init__(self,h,m,s):
            self.hour=h
            self.minute = m
            self.seconds = s

    def my_sum(self,other):
        result=my_time(None, None,None)
        result.hour=self.hour + other.hour
        result.minute=self.minute + other.minute
        result.seconds=self.seconds + other.seconds
        if result.seconds > 60:
            result.seconds -= 60
            result.minute+=1
        if result.minute>60:
            result.minute-=60
            result.hour+=1
        return result

    def my_sub(self,other):
        result=my_time(None, None,None)
        result.hour = self.hour - other.hour
        result.minute = self.minute- other.minute
        result.seconds = self.seconds- other.seconds
        if result.seconds<0:
            result.seconds+=60
            result.minute-=1
        if result.minute<0:
            result.minute+=60
            result.hour-=1
        return result
    #
    def my_second(self,m):
        result = my_time(None, None, None)
        times = int(input('second:'))
        result.hour = int(times / 3600)
        times = times % 3600
        result.minute = int(times / 60)
        result.seconds = int(times % 60)
        return result
    #
    def convert_time_seconds(self):
        result =self.hour * 3600 +  self.minute * 60  + self.seconds
        return result

    def show(self):
        print(self.hour,':',self.minute, ':' ,self.seconds)

hour_1=int(input('Time 1:\nhour : '))
minutes_1=int(input('Minutes : '))
seconds_1=int(input('Seconds :'))
obj_1 = my_time(hour_1,minutes_1,seconds_1)

hour_2=int(input('Time 2:\nhour : '))
minutes_2=int(input('Minutes : '))
seconds_2=int(input('Seconds :'))
obj_2 = my_time(hour_2,minutes_2,seconds_2)

while True:
    item = int(input('Time calculations:\n1 sum of two time\n2 Subtraction of two time\n3 Convert seconds to time\n4 Convert time to seconds'))

    if item == 1:
        print('sum of two time:',obj_1.my_sum(obj_2).show())
    elif item == 2:
        print('Subtraction of two time:',obj_1.my_sub(obj_2).show())
    if item==3:
        print('is time: ',obj_1.my_second(minutes_1).show())
    elif item==4:
        print('Seconds: ',obj_1.convert_time_seconds())


