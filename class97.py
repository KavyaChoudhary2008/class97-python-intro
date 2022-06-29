print("Welcome to python")

if 5 < 2:
    print("Hello")
#print("Five is greater than two!")
    print("hi")

x = 5
y = "John"
print(type(x))
print(type(y))

fruits = ["apple", "banana", "cherry"]
print(type(fruits))

username = input("Enter username:")
print("Username is: " + username)

fruits = ["apple", "banana", "cherry" , "mango"]
for x in fruits:
  print(x) 

introString=input("Enter string:")
characterCount=0
wordCount=1
for i in introString:
      characterCount=characterCount+1
      if(i==' '):
            wordCount=wordCount+1
print("Number of word in the string:")
print(wordCount)
print("Number of character in the string:")
print(characterCount)