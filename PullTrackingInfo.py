import requests
import json
from Secrets import *

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
    print r.content
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
     

    weight  = shipmentInfo["ShipmentWeight"]
    measurement = weight["Weight"]
    units = weight["UnitOfMeasurement"]["Code"]
    serviceCode = shipmentInfo["Service"]["Code"]
    
    if shipmentInfo.has_key("PickupDate"):
        pickUp = shipmentInfo["PickupDate"]
    else:
        print "no"

    pickUp = shipmentInfo["PickupDate"]

    timeInTransitAPI(shippedFrom, shippedTo, measurement, units, serviceCode, pickUp)

def timeInTransitAPI(sF, sTo, measurement, units, serviceCode, pickUp):
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
                        "Date": "20170208"
            }, 
            "ShipmentWeight": {
                "UnitOfMeasurement": { 
                    "Code": "LBS", 
                    "Description": "Pounds"
                },
                "Weight": "0.80" 
            },
            "MaximumListSize": "20" 
        }
    }
    
    r = requests.post(TIME_IN_TRANSIT_API, data=json.dumps(payload), headers=HEADERS)
    print r.content


