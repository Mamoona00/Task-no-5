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
       
s = "I love to learn Python"          #Accessing characters
print(s)
print("Frst char is: ")
print(s[0])                         #from start of string
print("Third last char: ")
print(s[-3])                         #from the end of string

#python arrays
import array 
num = array.array('i' , [46,79,67,34,90])
print(num)

print(num[1])            #accessing the element of the array   (positive index)
print(num[-2])            #negative index

print(len(num))

num.append(100)                          #append()
print("Array after adding element at the end: " , num)

num.extend([89,54,70])                     #extend()
print("Array more than one element in array: " , num)

num.insert(1, 60)                            #inset()
print("Array after adding selement at specific place: " , num)

num.pop()
print("Array after removing last elemunt: " , num)

num.remove(34)
print("Array after removing spcific element: " , num)




