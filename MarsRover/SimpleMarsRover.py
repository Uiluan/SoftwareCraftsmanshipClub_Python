import sys
from Rover import *

rover = Rover()
print("Landed at: " + str(rover.GetPositionAndDirection()))

while True:
    userCommand = input("Command: ")
    if userCommand == "exit":
        sys.exit()
    elif rover.Execute(userCommand):
        print("Current Location: " + str(rover.GetPositionAndDirection()))
    else:
        print("Error: Invalid Command")
