import csv

count = 0
total = 1

def debugAnalytics(filename):
    with open(filename, "r") as f:
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
