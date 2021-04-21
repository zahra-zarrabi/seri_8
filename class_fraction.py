class my_fraction():
    def __init__(self,s1,m1,s2,m2):
        self.n1={'s':s1 ,'m':m1}
        self.n2={'s':s2,'m':m2}

    def my_mul(self):
        s=self.n1['s']*self.n2['s']
        m=self.n1['m']*self.n2['m']
        return str(s)+'/'+str(m)

    def my_sum(self):
        s=(self.n1['s']*self.n2['m'])+(self.n2['s']*self.n1['m'])
        m = self.n1['m'] * self.n2['m']
        return str(s) + '/' + str(m)

    def my_sub(self):
        s = (self.n1['s'] * self.n2['m']) - (self.n2['s'] * self.n1['m'])
        m = self.n1['m'] * self.n2['m']
        return str(s) + '/' + str(m)

    def my_div(self):
        s=(self.n1['s']*self.n2['m'])/(self.n1['m']*self.n2['s'])
        return s

sorat1=int(input('Please enter the sort of first deduction: '))
makhraj1=int(input('Please enter the denominator of the first fraction:'))
sorat2=int(input('Please enter the form of Second deduction: '))
makhraj2=int(input('Please enter the denominator of the Second fraction:'))
obj=my_fraction(sorat1,makhraj1,sorat2,makhraj2)

print('(', obj.n1['s'], '/', obj.n1['m'], ')*(', obj.n2['s'], '/', obj.n2['m'], ')= ',obj.my_mul())

print('(', obj.n1['s'], '/', obj.n1['m'], ')+(', obj.n2['s'], '/', obj.n2['m'], ')= ',obj.my_sum())

print('(', obj.n1['s'], '/', obj.n1['m'], ')-(', obj.n2['s'], '/', obj.n2['m'], ')= ',obj.my_sub())

print('(', obj.n1['s'], '/', obj.n1['m'], ')/(', obj.n2['s'], '/', obj.n2['m'], ')= ',obj.my_div())