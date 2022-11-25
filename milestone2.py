
#%%
word_list = ['apple', 'mango', 'banana', 'orange', 'grapes']
print(word_list)
#%%
a={1,2,3,4}
b={3,4,5,6}
a.intersection(b)
# %%
a=set([10,2,3,4])
b=set([3,4,5,6,10])
a.intersection(b)
#%%
x=set()
for i in range(10):
    x.add(i)
print(x)

#%%
x={20,30,40,12}
max_set=max(x)
print(max_set)

#%%
set_int = {4, 12, 10, 9, 4, 13} 
print(min(set_int))
set_str = {'b', 'z', 't', 'm', 'y', 'c'}
print(min(set_str))
# %%
#set_int = {8, 16, 24, 1, 25, 3, 10, 65, 55} 
#print(max(set_int))
set_str = {'f', 'l', 'k', 'a', 'w'}
print(max(set_str))
# %%
prime_numbers = {3, 5, 7, 11, 13}
prime_numbers.add(17)
prime_numbers.update({10,20,30})
print(prime_numbers)


# %%
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

# %%
set1 = {15, 25, 35, 45, 55} 
set2 = {35, 45, 55, 65, 75}
set1.intersection(set2)
set1.union(set2)
set1.difference(set2)
set2.difference(set1)
#%%
lst1 = set([1, 2, 3, 4, 5, 6, 7, 8])
lst2 = set([5, 6, 7, 8, 9, 10, 11, 12])
miss_v=lst2.difference(lst1)
add_v=lst1.difference(lst2)
print(miss_v)
print(add_v)
# %%
list1 = set([1, 5, 10, 20, 40, 80])
list2 = set([6, 7, 20, 80, 100])
list3 = set([3, 4, 15, 20, 30, 70, 80, 120])
list1.intersection(list2).intersection(list3)
# %%
# flexibility of data assignment, including lists and sub-dictionaries
d = {'k1': 50, 'k2': 123, 'k3': [0,1,2], 'k4': {'insidekey': [100, 200]}}
print(d)
print(d.items())
print(d.keys())
print(d.values())
for i in d.values():
    print(i)
print(d['k4'])
# %%
one_deep_dictionary = {'start here':1,
'k1':[1,2,3,{'k2':[1,2,{'k3':['keep going',
{'further':[1,2,3,4,[{'k4':'Python'}]]}]}]}]}

one_deep_dictionary['k1'][-1]['k2'][2]['k3'][-1]['further'][-1][-1]['k4']
# %%
print(99 > 5)
print(0 == False)
print(1 == True)
print(6.2 < 7)
print(9 >= 9)
print(False < True)
# %%
a = True
b = False
c = a or b
d = a and b
not_d=not(d)
xor = c and not_d
print(c)
print(d)
print(not_d)
print(xor)
# %%
print('AAA' > 'BBB') 
print('AAB' > 'AAA')
print('aaa' > 'AAA')
# %%
x = 10
n=int(input('Enetr a number:'))
print(f'{n} is greater than {x}')
# %%
shop={'tomatoes':18,'washing_sponges':2,
       'juice':4.5,'foil':4,'sugar':2
}
shop['prices']={'tomatoes':0.87,'washing_sponges':0.29,
       'juice':1.89,'foil':1.29,'sugar':1.09
}
shop['pack_sizes']={'tomatoes':6,'washing_sponges':10,
       'juice':1.5,'foil':30,'sugar':0.5
}
tomatoes_total_price=(shop['tomatoes']/shop['pack_sizes']['tomatoes'])*shop['prices']['tomatoes']
print(tomatoes_total_price)
juice_total_price=(shop['juice']/shop['pack_sizes']['juice'])*shop['prices']['juice']
print(juice_total_price)
sponges_total_price=(shop['washing_sponges']/shop['pack_sizes']['washing_sponges'])*shop['prices']['washing_sponges']
print(round(sponges_total_price,2))
foil_total_price=(shop['foil']/shop['pack_sizes']['foil'])*shop['prices']['foil']
print(round(foil_total_price,2))
sugar_total_price=(shop['sugar']/shop['pack_sizes']['sugar'])*shop['prices']['sugar']
print(sugar_total_price)
Total_price=tomatoes_total_price+juice_total_price+sponges_total_price+foil_total_price+sugar_total_price
print(round(Total_price,2))
order_total=1.2*Total_price
print(round(order_total,2))

#tuple
lst=[]
for i in list(range(10)):
    lst.append(i)
print(lst)
print(tuple(lst))
    
a=()
b=(1,)
c=('python', 3+3j, 4.5)
print(type(a))
print(b,type(b))
print(c, type(c))
print(b+c)


# %%
count=0
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
for i in range(len(vowels)):
    if vowels[i]=='i':
        count+=1
print(count)

# %%
numbers = (1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6, 7, 7, 7)
count=0
for i in range(len(numbers)):
    if numbers[i]==7:
        count+=1
print(count)

# %%
count=0
tuple = (1, 'f', [1, 2, 3], [4, 5], ('f', 'd'), ('f', 'd', 'e'), [1, 2, 3], 'a')
for i in range(len(tuple)):
    if tuple[i]==[1,2,3] or tuple[i]==['f','d']:
        count+=1
print(count)
#%%
vowels = ('a', 'e', 'i', 'o', 'i', 'u')

for i in range(len(vowels)):
    if vowels[i]=='e':
        print(i)

# %%
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
def find_index(input_tup,input_value):
    return input_tup.index(input_value)
answer = find_index(('a', 'e', 'i', 'o', 'i', 'u'), 'i')
print(answer)
#%%
alphabet = ('a', 'e', 'i', 'o', 'u', 'g', 'l', 'i', 'u')
def find_index(input_tup,input_value):
    return input_tup.index(input_value)
answer = find_index(alphabet[4:9], 'i')
print(answer)
# %%
x=((1,100),(2,200),(3,300),(4,400),(5,500))
list(zip(x))
# %%
#tuple unpacking
tup=(100,200,300,400)
a,b,c,d=tup
print(a)
print(b)
print(c)
print(d)
#%%
tuple = (70, "AiCore", 10, "Programming", 70, 80)
x, *y, z = tuple
print(x)
print(y)
print(z)
# %%
tuple = (70, "AiCore", 10, "Programming", 70)
x, y, *z = tuple
print(x)
print(y)
print(z)
# %%
