class my_data():
    def __init__(self, date):
        self.data=date

    def isValidData(self):
        if 1<=self.data['year']<=9999 and 1<=self.data['month']<=12 and 1<=self.data['day']<=30:
            return True
        else:
            return False

    def isLeapyear(self):
        year = int(input("Enter the desired year to specify the leap year "))
        if (year % 4 == 3):
            return True
        else:
            return False

    def add_data(self):
        self.data2 = {'year': int(input('date2:\nEnter the year: ')), 'month': int(input('Enter the month: ')), 'day': int(input('Enter the day: '))}
        y=self.data['year']+self.data2['year']
        m=self.data['month'] + self.data2['month']
        d=self.data['day'] + self.data2['day']
        if d>30:
            d-=30
            m+=1
        if m>12:
            m-=12
            y+=1
        return str(y)+'/'+str(m)+'/'+str(d)

    def sub_data(self):
        self.data2 = {'year': int(input('date2:\nEnter the year: ')), 'month': int(input('Enter the month: ')), 'day': int(input('Enter the day: '))}
        y = self.data['year'] - self.data2['year']
        m = self.data['month'] - self.data2['month']
        d = self.data['day'] - self.data2['day']
        if d<=0:
            d += 30
            m -= 1
        if m <=0:
            m += 12
            y -= 1
        return str(y) + '/' + str(m) + '/' + str(d)


    def getMonthName(self):
        number=input('Choose a number from 1 to 12 to display the name of the month: ')
        self.month = {'1': 'farvardin','2':'ordibehesht','3':'khordad','4':'tir','5':'mordad','6':'shahrivar','7':'mehr','8':'aban','9':'azar','10':'dey','11':'bahman','12':'esfand'}
        return self.month[number]

    def show(self,data2):
        self.data=data2
        return str(self.data['year'])+'/'+str(self.data['month'])+'/'+str(self.data['day'])


