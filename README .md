
# Introduction to Datatypes
Datatype is actually the type of data or value that is stored in a variable. To check the type of the data we use type() function. There are five data types in python and these are further divided into other types:

1. sequence (string, tuple, lists)

2. Sets

3. Dictionary

4. Numeric (int, float, complex)

5. Boolean




##  * Python Strings

It is a sequence datatype. In Python, strings are used to represent data as text. Once we create a string we cannot change it (immutable datatype).In python there is no char datatype, string is a collection of characters.
##  Creating Strings In Python:
Declare a variable and assign it a value that can be text. Text in the string can be written in single, double, or triple quotation marks.
We can use triple (single or double) quotes for multiline strings. We can check the length of the variable by the len() function. In parantheses write the name of the variable to which string is assigned. 

## Accessing characters of string:
we can access specific characters of the string by the use of the index. The positive index can be used to access the character from the start of the string and the negative index can be used to access the character from the end of the string. 
## * Python Lists
List is a collection of multiple things or items. In Python, lists are used to store multiple items in a single variable. It is an ordered collection of items. Once we create list we can change items in it (mutable). The types of element can be string, int, float, and any other type. The length of the list can be checked by using the len() function.

## Creating python list:
we can create the list by writing the name of list then write the items separete the items by a comma and enclose them within square brackets.

## Accessing elements of the list:
we can access specific elements of the list by the use of the index. The positive index can be used to access element from the start of the list and the negative index can be used to access elements from the end of the list. 
## * Python Tuple
It is a sequece datatype. A tuple is similar to a list; the only difference is that once a tuple has been created it can not be changed (immutable).
It can store values of different data types. Duplicate values can also be stored in tuples. if we store one element in a tuple the datatype of the tuple will be changed so it is necessary to put more than one element.

## Creating tuples in python:
Create a name of the tuple and write the values separated by commas and enclosed within parentheses (). 
## * Python sets
The set is collection of items which is unordered so we cannot access its elements using an index. Elements in a set can not be repeated. sets are mutable datatype.

## creating sets in python:
create a variable as a name of the set, and assign it the items you want to put in the set. separate the items by comma and enclose them with curly braces {}. 
if we want to make an empty set we cannot write is in with curly braces. set = {} if we create set like this the interpreter will show you this as dictionary type. so if we want to create an empty set we can write it as moon(). Now it is an empty set named moon. we can add an element to the set by using set() method.


## * Python Dictionary
Dictionar is used to store data in key: values pair. key immutable while value can be repeated.It is ordered collection of data onwards 3.7 version of python. before this dictionaries were unordered. 
## creating dictionary in python:
it can created by separating the key and value with colon and values with comma and enclose them with curly braces.
## Accessing elements in dictionary:
we can access the elements in dictionary by its key or by get() method. just write write the name of the dictionary then .get() write the key in parantheses enclosed with square brackets.
we can also access multiple values by using keys() function or by usingg for loop.


## * python arrays
An array is a collection of items . it is used to store more than one element. Biggest difference in arrays and list is that list can have elements of different datatype while array cotains all elements of only one datatype. The size of array is not fixed we can add and remove elements from it.
For creating array we have to import array module.
## accessing elements of array:
Elememnt of the array can be accessed by using their index number. we can access elements from tha end of the array by using negative index.
## Adding and removing element from array:

we can add element in array by using:

append() method:

it is used to add element at the end of the array.

insert():

it is used to add elements at specific position in array.

extend() method:

it is used to add ore than one elements in array.

we can remove element in array by using:

pop():

it removes the last element of the array. if we don't give index number.

remove():

in remove fuction we write value in paratheses that we want to remove from array.







