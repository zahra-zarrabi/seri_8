class my_fraction():
    def __init__(self,s,m):
        self.so=s
        self.ma=m

    def my_mul(self,other):
        result=my_fraction(None,None)
        result.so=self.so * other.so
        result.ma=self.ma * other.ma
        return result

    def my_sum(self,other):
        result = my_fraction(None, None)
        result.so=(self.so*other.ma)+(other.so*self.ma)
        result.ma = self.ma* other.ma
        return result

    def my_sub(self,other):
        result = my_fraction(None, None)
        result.so = (self.so*other.ma)-(other.so*self.ma)
        result.ma = self.ma* other.ma
        return result

    def my_div(self,other):
        s=(self.so*other.ma)/(self.ma*other.so)
        return s

sorat1=int(input('Please enter the sort of first deduction: '))
makhraj1=int(input('Please enter the denominator of the first fraction:'))
sorat2=int(input('Please enter the form of Second deduction: '))
makhraj2=int(input('Please enter the denominator of the Second fraction:'))
obj1=my_fraction(sorat1,makhraj1)
obj2=my_fraction(sorat2,makhraj2)

result =obj1.my_mul(obj2)
print('(', obj1.so, '/', obj1.ma, ')*(', obj2.so, '/', obj2.ma, ')= ',result.so,'/',result.ma)

result=obj1.my_sum(obj2)
print('(', obj1.so, '/',obj1.ma, ')+(', obj2.so, '/', obj2.ma, ')= ',result.so,'/',result.ma)

result=obj1.my_sub(obj2)
print('(',obj1.so, '/',obj1.ma, ')-(', obj2.so, '/', obj2.ma, ')= ',result.so,'/',result.ma)


print('(', obj1.so, '/',obj1.ma, ')/(', obj2.so, '/', obj2.ma, ')= ',obj1.my_div(obj2))