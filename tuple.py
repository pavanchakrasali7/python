tuple1=(1,2,3,4,5)
a,b,c,*all=tuple1
print(all)

tuple1=(1,2,3,4)
tuple2=(9,7,6,5)
my=tuple1 + tuple2
my=tuple1 * 3
print(my)
dict1={}
dict1['name']='pavan'
# dict1.popitem('pavan')
print(dict1.popitem())

x = ("apple", "banana", "cherry")
y=list(x)
y[1]="mango"
x=tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
i=0
while i<len(thistuple):
    print(thistuple[i])
    i=i+1
t=(1,2,3,4)
del t
print(t)