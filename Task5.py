#Intro to datatypes

z = "mamoona"
print(type(z))
x = 19
print(type(x))
x = "19"
print(type(x))

#strings

z = 'moon'           #single qoutes
print(z)

x = "How are you?"       #double qoutes
print(x)

a = """My name is Ayesha."""      #tripple double qoutes
print(a)
intro = '''My name is mamoona.             
 I read in virual university.              
 I am 21 years old.
 I love to do painting.'''
print(" My intro:\n",intro)              #multiline / tripple qoutes string

a = "Welcome to my world."
print(len(a))                      #length of the string
 
       
s = "I love to learn Python"
print(s)
print("Frst char is: ")
print(s[0])
print("Third last char: ")
print(s[-3])

#Python lists

names = ['Hiba' , 'Mahnoor' , 'Hina' , 'Amina']
print(names)
print(len(names))                          #length of list


list = ["blue" , 4 , "white" , 5 , "black" , 5 , "yellow" , 6]          #mixed datatype of elements of list
print("Names of colours and numbers of their latters: " , list) 
print("First element of list is: " , list[0])                       #accessing elements of list
print("Last element of list is: " , list[-1]) 

list[2] = 'pink'                                               ##inserting element in a list by using index
print(list)

list.insert(0 , 'gold')                                        #by using insert() method
print("List after inerting elements: ", list )


list.extend(['green' , 5])                                    #using extend() method
print("After inserting element at and: " , list)


l = [["Mamoona" , 7] , ["Ayesha" , 6]]           #multi_dimentional list
print(l)

#Tuple in python
stdmks = (90 , 60 , 33 , 45)                     #int elements
print("Mark of students are: " , stdmks)
print(type(stdmks))

m = ("stylo" , 1 , "metro" , 2 , "borjan" , 3)         #mixed datatype of elements
print(m)

nested = (("stylo" , "metro" , "borjan") , (1 , 2 , 3))            #nested tuple
print(nested)

#Python sets

flowers = {'rose' , 'lily' , 'sunflower' , 'daisy'}
print("Name of flowers are: " , flowers)

for items in flowers:         # accessing the items of the set
    print(items)               #unordered

flowers.add('violet')             #adding element in set
print(flowers)

#python Dictionar
std = {
    24: 'Nayab',
    34: 'Hoorain',
    56: 'Minahil',
    23: 'Hamna' 
}
print(std)
print(std[23])           #accsessing element by its key
print(std.get(56))        #by get() method

print(std.keys())                #keys() method
for keys in std.keys():           #for loop
    print(std[keys])

del(std[24])                   #deleting key: value by using del()
print(std)






