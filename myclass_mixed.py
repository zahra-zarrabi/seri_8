class my_mixed():
    def __init__(self,a,b):
        self.n1=a
        self.n2=b

    def my_mul(self):
        r=obj.n1*obj.n2
        return r

    def my_sum(self):
        r=obj.n1+obj.n2
        return r

    def my_sub(self):
        r=obj.n1-obj.n2
        return r

    def my_div(self):
        r={'a':None,'b':None}
        r['a']=a*complex(real_2,-imaginary_2)
        r['b']=b*complex(real_2,-imaginary_2)
        return str(r['a'])+'/'+str(r['b'])

real_1=int(input('Enter the real part of the first number: '))
imaginary_1=int(input('Enter the imaginary part of the first number: '))
real_2=int(input('Enter the real part of the Second number: '))
imaginary_2=int(input('Enter the imaginary part of the Second number: '))
a = complex(real_1,imaginary_1)
b = complex(real_2,imaginary_2)
obj=my_mixed(a,b)

print(a,'*',b,'=',obj.my_mul())

print(a,'+',b,'=',obj.my_sum())

print(a,'-',b,'=',obj.my_sub())

print(a,'/',b,'=',obj.my_div())