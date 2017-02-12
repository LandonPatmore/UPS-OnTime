import simplejson as json
import requests
from Secrets import *


def analyzeJSON(not_analyzed):
    toAnalyze = json.loads(not_analyzed)
   
    shipmentInfo = toAnalyze["TrackResponse"]["Shipment"] 

    shippedFrom = []
    shippedTo = []
    
    countFrom = 0
    for key, value in shipmentInfo["ShipmentAddress"][0]["Address"].items():
        if(countFrom != 1 and countFrom != 2):
            shippedFrom.append(value)
            print value
        countFrom += 1
    
    countTo = 0
    for key, value in shipmentInfo["ShipmentAddress"][1]["Address"].items():
        if(countTo != 1):
            shippedTo.append(value)
            print value
        countTo += 1
     

    weight  = shipmentInfo["ShipmentWeight"]
    measurement = weight["Weight"]
    units = weight["UnitOfMeasurement"]["Code"]
    serviceType = shipmentInfo["Service"]["Description"]
    pickUp = shipmentInfo["PickupDate"]

    transitTrack(shippedFrom, shippedTo, measurement, units, serviceType, pickUp)

def transitTrack(sF, sTo, measurement, units, serviceType, pickUp):
    
    transit = "https://onlinetools.ups.com/rest/TimeInTransit"
    newPayload = {
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
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} 
    
    r = requests.post(transit, data=json.dumps(newPayload), headers=headers)
    print r.content
