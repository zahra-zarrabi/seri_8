from my_dataa import my_data

print('Enter date today:')
obj =my_data()

data2 = {'year': int(input('data2:\nEnter the year: ')), 'month': int(input('Enter the month: ')), 'day': int(input('Enter the day: '))}

y = obj.data['year'] - data2['year']
m = obj.data['month'] - data2['month']
d = obj.data['day'] - data2['day']
if d <= 0:
    d += 30
    m -= 1
if m <= 0:
    m += 12
    y -= 1
print(y,'year',m,'month',d,'day')


