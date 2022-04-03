from string import ascii_letters, digits
from unicodedata import digit
from Account import *

#TODO: create live interface to enter and edit database
#TODO: Add hashed passwords to file storage
manager = AccountManager()

print("Test invalid input")
# Test variety of invalid usernames
manager.SetPassword("us", "Password%45")
manager.SetPassword("usernamethatistoolongeventuallyatsomepoint", "Password%45")
manager.SetPassword("username!", "Password%45")
manager.SetPassword("9username", "Password%45")

# Test variety of invalid passwords
manager.SetPassword("username", "password%45")
manager.SetPassword("username", "Password%")
manager.SetPassword("username", "Password45")
manager.SetPassword("username", "Password/45")
manager.SetPassword("username", "Pa1^")
manager.SetPassword("username", "Password%45Password%45Password%45Password%45Password%45Password%45Password" + \
    "%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45" + \
    "Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45Password%45" + \
    "Password%45Password%45Password%45Password%45")
manager.SetPassword("username", "PASSWORD%45")
manager.SetPassword("username", "UserNAME%45")

print("\n\nTest valid input")
testName = "username"
if not manager.GetUser(testName):
    print("\"" + testName + "\" does not exist, adding")
    manager.SetPassword(testName, "Password%45")
else:
    print("\"" + testName + "\" already exists")

testName = "admin"
if not manager.GetUser(testName):
    print("\"" + testName + "\" does not exist, adding")
    manager.SetPassword(testName, "$VVBv@vmE0v7")
else:
    print("\"" + testName + "\" already exists")

testName = "username"
if not manager.GetUser(testName):
    print("\"" + testName + "\" does not exist, adding")
    manager.SetPassword(testName, "Password%45")
else:
    print("\"" + testName + "\" already exists")

testName = "admin"
if not manager.GetUser(testName):
    print("\"" + testName + "\" does not exist, adding")
    manager.SetPassword(testName, "$VVBv@vmE0v7")
else:
    print("\"" + testName + "\" already exists")