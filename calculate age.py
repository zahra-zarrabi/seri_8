from my_dataa import my_data

year_1=int(input('date1:\nEnter the year: '))
month_1=int(input('Enter the month: '))
day_1=int(input('Enter the day: '))
obj=my_data(year_1,month_1,day_1)

print('isvalid:',obj.isValidData())
obj.show()

year_2=int(input('date2:\nEnter the year: '))
month_2=int(input('Enter the month: '))
day_2=int(input('Enter the day: '))
obj2=my_data(year_2,month_2,day_2)
obj2.show()

result=obj.add_data(obj2)
print('sum of two dates: ')
obj.add_data(obj2).show()

result=obj.sub_data(obj2)
print('Subtraction of two dates: ')
obj.sub_data(obj2).show()

print('Name of the desired month: ',obj.getMonthName())

print(obj.isLeapyear())

int_today=input('Please Enter today\'date as follows: year/month/day')
today=int_today.split('/')
date_today=my_data(int(today[0]),int(today[1]),int(today[2]))

int_birth = input('Please Enter your date of birth as follows: year/month/day')
birth=int_birth.split('/')
date_birth=my_data(int(birth[0]),int(birth[1]),int(birth[2]))

if date_today.isValidData() and date_birth.isValidData():
    ege=date_today.sub_data(date_birth)
    print(ege.year, 'year', ege.month, 'month', ege.day, 'day')



