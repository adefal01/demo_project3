a=[10,20,30,40,50]
a.append(50)
a.append(5)
a.append(6)
a.append(7)
print(a)
#element removal
a.remove(50)
print(a)
if 99 in a:
    a.remove(99)

a.pop()
print(a)
a.pop(2)
print(a)

a.sort()
print(a)
a.reverse()
print(a)

#slicing
slice=a[2:4]
print(a,slice)

b=a
print(a,b)
b[0]=99
print(b)

b=a.copy()
b=a[:]
print(b[-2])

empty=[]
empty.append(5)

for  val in a:
    if val>=20 and val<=100:
        empty.append(val)
print(empty)

empty=[0]*5
print(empty)
empty[0]=50
print(empty)

squares=[]
for val in range(1,10):
    squares.append(val*val)
print(squares)

squares=[x*x for x in range(1,10) if x%2==0]
print(squares)

aset=set()
aset.add(1)
aset.add(1)
aset.add(2)
aset.add(3)
aset.add(3)
print(aset)


fav_foods={'kathleen':'tacos', 'steve': 'pizza', 'savannah': 'frieds', 'michelle' : 'pasta', 'patrick': 'ribs'}
print(fav_foods)



