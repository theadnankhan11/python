# print('adnan khan')
# for command line use py or python and use exit()
# indentation  is very important in python

# if 5 > 2: 
#     print("five is  greater than two!")

# x = 5 
# y = "John"
# print(x)
# print(y)


name = "awesome"

def myfunc():
    global name 
    name = "fantastic"
    print('python is ' + name)

myfunc()
print(name)