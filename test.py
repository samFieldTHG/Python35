import datetime
get = datetime.datetime.now()
name = input("Please enter your name:\n ")
age = int (input("please enter your age: \n"))

curryear = get.year
century =((100 -age)+curryear)
print  ("""Hello %s. Your current age is %s and you will turn 100 in year %s\n"""
      %(name,age,century))

