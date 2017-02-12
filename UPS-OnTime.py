from PullTrackingInfo import trackingAPI
from Analytics import analytics
import csv

# working - 1Z301E180319608393
# not working - 1Z3Y51839013624746

def getUserInput():
    userChoice = raw_input("Enter debug mode (debug )or live mode (live): ")
    if userChoice == "debug":
        with open("debugData.txt", "r") as f:
            reader = csv.reader(f)
            csvList = list(reader)

            count = 0
            zipcode = 0
            serviceType = 0
            for i in csvList:
                for x in range(len(i)):
                    i[x] = int(i[x])
                serviceType = i[4]
                zipcode = i[5]
                if(i[2] - i[0] >= 0):
                    if(i[3] - i[1] >= 0):
                        count +=1

            count = float(count)
            total = float(len(csvList))

            if serviceType == 1:
                strServiceType = "GROUND"

            print "{}% On Time Percentage for {} at Zip Code {}".format(((count/total) * 100), strServiceType, zipcode)
    else:
        trackingNumber = raw_input("Enter tracking number: ")
        trackingAPI(trackingNumber)


getUserInput()
