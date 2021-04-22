from my_dataa import my_data

date={'year':int(input('date1:\nEnter the year: ')),'month':int(input('Enter the month: ')),'day':int(input('Enter the day: '))}
obj=my_data(date)

print('isvalid:',obj.isValidData())
print(obj.show(obj.data))

print('sum of two dates: ',obj.add_data())

print('Name of the desired month: ',obj.getMonthName())

print('Subtraction of two dates: ',obj.sub_data())
print(obj.show(obj.data2))

print(obj.isLeapyear())


date_today={'year':int(input('Enter date today:\nEnter the year: ')),'month':int(input('Enter the month: ')),'day':int(input('Enter the day: '))}
obj =my_data(date_today)

birth = {'year': int(input('Enter the date of birth:\nEnter the year: ')), 'month': int(input('Enter the month: ')), 'day': int(input('Enter the day: '))}

y = obj.data['year'] - birth['year']
m = obj.data['month'] - birth['month']
d = obj.data['day'] - birth['day']
if d <= 0:
    d += 30
    m -= 1
if m <=0:
    m += 12
    y -= 1
print(y,'year',m,'month',d,'day')


