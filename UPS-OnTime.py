from PullTrackingInfo import trackingAPI
from Analytics import analytics
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
        if userChoice == "debug":
            fileName = raw_input("Enter debug file name in directory: ")
            with open(fileName, "r") as f:
                reader = csv.reader(f)
                csvList = list(reader)

                zipcode = 0
                serviceType = 0
                for i in csvList:
                    for x in range(len(i)):
                        i[x] = int(i[x])
                    serviceType = i[4]
                    zipcode = i[5]
                    if(i[2] - i[0] >= 0):
                        if(i[3] - i[1] >= 0):
                            global count
                            count = count + 1

                count = float(count)
                global total
                total = float(total) + float(len(csvList))

                if serviceType == 1:
                    strServiceType = "GROUND"
                print "Count {} : Total {}".format(count, total)
                print "{}% On Time Percentage for {} at Zip Code {}".format(((count/total) * 100), strServiceType, zipcode)
        else:
            trackingNumber = raw_input("Enter tracking number: ")
            trackingAPI(trackingNumber)


getUserInput()
