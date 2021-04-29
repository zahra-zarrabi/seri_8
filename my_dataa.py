class my_data():
    def __init__(self, y=None,m=None,d=None):
        self.year=y
        self.month=m
        self.day=d

    def isValidData(self):
        if 1<=self.year<=9999 and 1<=self.month<=12 and 1<=self.day<=30:
            return True
        else:
            return False

    def isLeapyear(self):
        year = int(input("Enter the desired year to specify the leap year "))
        if (year % 4 == 3):
            return True
        else:
            return False

    def add_data(self,other):
        result=my_data()
        result.year=self.year+ other.year
        result.month=self.month + other.month
        result.day=self.day + other.day
        if result.day>30:
            result.day-=30
            result.month+=1
        if result.month>12:
            result.month-=12
            result.year+=1
        return result

    def sub_data(self,other):
        result = my_data()
        result.year = self.year - other.year
        result.month = self.month - other.month
        result.day = self.day - other.day
        if result.day<=0:
            result.day += 30
            result.month -= 1
        if result.month <=0:
            result.month += 12
            result.year -= 1
        return result


    def getMonthName(self):
        number=input('Choose a number from 1 to 12 to display the name of the month: ')
        self.month = {'1': 'farvardin','2':'ordibehesht','3':'khordad','4':'tir','5':'mordad','6':'shahrivar','7':'mehr','8':'aban','9':'azar','10':'dey','11':'bahman','12':'esfand'}
        return self.month[number]

    def show(self):
        print(self.year,'/',self.month,'/',self.day)


