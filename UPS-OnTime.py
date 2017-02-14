from PullTrackingInfo import trackingAPI
from DebugAnalytics import debugAnalytics
import csv

count = 0
total = 0

# working - 1Z301E180319608393
# not working - 1Z3Y51839013624746

def getUserInput():
    while True:
        userChoice = raw_input("Enter debug mode (debug) or live mode (live) or exit: ")
        if userChoice == "exit":
            break
        elif userChoice == "debug":
            fileName = raw_input("Enter debug file name in directory: ")
            debugAnalytics(fileName)
        elif userChoice == "live":
            trackingNumber = raw_input("Enter tracking number: ")
            trackingAPI(trackingNumber)
        else:
            print "Unknown input"

getUserInput()
