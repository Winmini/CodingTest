a = input()
n = 0
n += a.count('c=')
a = a.replace('c='," ")
n += a.count('c-')
a = a.replace('c-'," ")
n += a.count('dz=')
a = a.replace('dz='," ")
n += a.count('d-')
a = a.replace('d-'," ")
n += a.count('lj')
a = a.replace('lj'," ")
n += a.count('nj')
a = a.replace('nj'," ")
n += a.count('s=')
a = a.replace('s='," ")
n += a.count('z=')
a = a.replace('z='," ")
a = a.replace(' ','')
n += len(a)
print(n)

a = input()
count = len(a)
b = ['c=','c-','dz=','d-','lj','nj','s=','z=']
sum=0
for i in b:
    sum += a.count(i)