
# Introduction to Datatypes
Datatype is actually type of the data or value that is stored in a variable. To check the type of the data we use type() function.There are five datatypes in python and these are further divided into other types:

1. sequence (string, tuple, lists)

2. Sets

3. Dictionary

4. Numeric (int, float, complex)

5. Boolean




##  * Python Strings

It is sequence datatype. In python, strings are used to represent data as text. Once we created string we cannot change it (immutable datatype).In python there is no char datatype, string is a collection of characters.
##  Creating Strings In Python:
Declare a variable assign it a value that can be text.Text in string can be written in single, double, or triple qoutation marks.
We can use tripple (single or double) quotes for multiline strings. We can check the length of the variable by len() fuction. In parantheses write the name of the variable to which string is assigned. 

## Accessing characters of string:
we can access specific character of the string by th use of index. Positive index can be used to access character from the start of string and negative index can be used to access character from the and of the string. 
## * Python Lists
List is collection of multiple thing or items. In Python lists are used to store multiple items in a single variable. It is ordered collection of items. Once we create list we can change items in it (mutable). The types of element can be string, int, float and any other type. Length of the list can be checked by usin len() function.

## Creating python list
we can create the list by writing the name of list then write the items separete the items by comma and enclosed them within square brackets.

## Accessing elements of list:
we can access specific element of the list by th use of index. Positive index can be used to access element from the start of list and negative index can be used to access element from the and of the list. 
## * Python Tuple
It is a sequece datatype. Tuple is similar to list only one difference is that once tuple has been created it can not be changed (immutable).
It can store values of different datatypes. Duplicate values can also be stored in tuple. if we store one element in tuple the datatype of tuple will be changed so it is neccessary to put more than one elements.

## creating tuples in python:
Create a variable, assign it values separated by commas and enclosed within parantheses(). 
## * Python sets
Set is collection of items which is unordered so we cannot access its elements using index. Elements in set can not be repeated. sts are mutable datatype.

## creating sets in python:
create a variable as a name of the set, assign it the items you want to put in set. separate the items by comma and enclosed them with curly braces {}. 
if we want to make empty set we cannot write is in with curly braces. set = {} if we create set like this the interpreter will show you this as dictionary type. so if we want to create empty set we can write it as moon(). Now it is empty set named moon. we can add element in set by using set() method.


## * Python Dictionary
Dictionar is used to store data in key: values pair. key immutable while value can be repeated.It is ordered collection of data onwards 3.7 version of python. before this dictionaries were unordered. 
## creating dictionary in python
it can created by separating the key and value with colon and values with comma and enclose them with curly braces.
## Accessing elements in dictionary:
we can access the elements in dictionary by its key or by get() method. just write write the name of the dictionary then .get() write the key in parantheses enclosed with square brackets.
we can also access multiple values by using keys() function or by usingg for loop.