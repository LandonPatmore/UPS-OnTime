count = 0
total = 0


def analytics(actualDate, actualTime, estDate, estTime, serviceType, zipcode):
    print "Actual Date: " + actualDate
    print "Actual Time: " + actualTime
    print "Est. Date: " + estDate
    print "Est. Time: " + estTime
    print "Service: " + serviceType
    print "Zipcode: " + zipcode

    global total 
    total = total + 1
    if (int(estDate) - int(actualDate) >= 0):
        if(int(estTime) - int(actualTime) >= 0):
            global count
            count = count + 1
    
    print "Count {} : Total {}".format(count, total)
    print "{}% On Time Percentage for {} at Zip Code {}".format(((count/total) * 100), serviceType, zipcode)

