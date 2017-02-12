import requests
import json
from Secrets import *
from Analytics import analytics

def trackingAPI(t_Num):
    
    payload = {
        "UPSSecurity": { 
            "UsernameToken": {
                "Username":("" + USERNAME),
                "Password":("" + PASSWORD)
            },
            "ServiceAccessToken": { 
                "AccessLicenseNumber":("" + AUTHENTICATION_TOKEN)
            } 
        },
        "TrackRequest": {
            "Request": { 
                "RequestOption": "1", 
                "TransactionReference": {
                    "CustomerContext": "Your Test Case Summary Description" 
                }
            },
            "InquiryNumber": ("" + t_Num) }
    }

    r = requests.post(TRACKING_API, data=json.dumps(payload), headers=HEADERS)
    #print r.content
    analyzeTrackingAPI(r.content)

def analyzeTrackingAPI(not_analyzed):
    toAnalyze = json.loads(not_analyzed)   
    shipmentInfo = toAnalyze["TrackResponse"]["Shipment"] 
    

    shippedFrom = []
    shippedTo = []
    
    countFrom = 0
    for key, value in shipmentInfo["ShipmentAddress"][0]["Address"].items():
        if(countFrom != 1 and countFrom != 2):
            shippedFrom.append(value)
        countFrom += 1
    
    countTo = 0
    for key, value in shipmentInfo["ShipmentAddress"][1]["Address"].items():
        if(countTo != 1):
            shippedTo.append(value)
        countTo += 1
     

    packageDeliveryDate = shipmentInfo["Package"]["Activity"][0]["Date"]
    packageDeliveryTime = shipmentInfo["Package"]["Activity"][0]["Time"]
    weight  = shipmentInfo["ShipmentWeight"]
    measurement = weight["Weight"]
    units = weight["UnitOfMeasurement"]["Code"]
    serviceCode = shipmentInfo["Service"]["Description"]

    
    if shipmentInfo.has_key("PickupDate"):
        pickUp = shipmentInfo["PickupDate"]
    else:
        for i in range(len(shipmentInfo["Package"]["Activity"])):
            if(i == (len(shipmentInfo["Package"]["Activity"])) - 2):
                pickUp = shipmentInfo["Package"]["Activity"][i]["Date"]


    timeInTransitAPI(shippedFrom, shippedTo, measurement, units, serviceCode, pickUp, packageDeliveryDate, packageDeliveryTime)

def timeInTransitAPI(sF, sTo, measurement, units, serviceCode, pickUp, packageDate, packageTime):
    payload = {
        "Security": {
            "UsernameToken": {
                "Username": ("" + USERNAME), 
                "Password": ("" + PASSWORD)
            }, "UPSServiceAccessToken": {
                    "AccessLicenseNumber": ("" + AUTHENTICATION_TOKEN) 
                }
        }, 
        "TimeInTransitRequest": {
            "Request": { 
                "RequestOption": "TNT", 
                "TransactionReference": {
                    "CustomerContext": "Developer",
                    "TransactionIdentifier": "UPS On-Time Analytics" 
                }
            }, 
            "ShipFrom": {
                "Address": {
                    "StateProvinceCode": ("" + sF[2]), 
                    "CountryCode": sF[1], 
                    "PostalCode": sF[0]
                } 
            }, 
            "ShipTo": { 
                "Address": {
                    "StateProvinceCode": sTo[1], 
                    "CountryCode": sTo[2], 
                    "PostalCode": sTo[0]
                } 
            }, 
            "Pickup": { 
                        "Date": pickUp
            }, 
            "ShipmentWeight": {
                "UnitOfMeasurement": { 
                    "Code": units, 
                    "Description": "Pounds"
                },
                "Weight": measurement 
            },
            "MaximumListSize": "20" 
        }
    }
    
    r = requests.post(TIME_IN_TRANSIT_API, data=json.dumps(payload), headers=HEADERS)
    notAnalyzed = r.content

    toAnalyze = json.loads(notAnalyzed)

    service = toAnalyze["TimeInTransitResponse"]["TransitResponse"]["ServiceSummary"]
    serviceType = ""
    serviceArrivalTime = ""
    serviceArrivalDate = ""

    for i in range(len(service)):
        if(serviceCode.lower() == service[i]["Service"]["Description"].lower()):
            serviceType = service[i]["Service"]["Description"]
            serviceArrivalTime = service[i]["EstimatedArrival"]["Arrival"]["Time"]
            serviceArrivalDate = service[i]["EstimatedArrival"]["Arrival"]["Date"]

    analytics(packageDate, packageTime, serviceArrivalDate, serviceArrivalTime, serviceType, sTo[0])
