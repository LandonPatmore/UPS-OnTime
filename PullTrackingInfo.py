import requests
import json
from Analytics import analyzeJSON
from Secrets import *

def pullData(t_Num):
    
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

    HTTP_REQUEST = "https://onlinetools.ups.com/rest/Track"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    r = requests.post(HTTP_REQUEST, data=json.dumps(payload), headers=headers)
    analyzeJSON(r.json()) 


    '''
    TT = "https://onlinetools.ups.com/rest/TimeInTransit"
    newPayload = {
            "Security": {
                "UsernameToken": { "Username": ("" + USERNAME), "Password": ("" + PASSWORD)
                    }, "UPSServiceAccessToken": {
                        "AccessLicenseNumber": ("" + AUTHENTICATION_TOKEN) }
                    }, "TimeInTransitRequest": {
                        "Request": { "RequestOption": "TNT", "TransactionReference": {
                            "CustomerContext": "",
                            "TransactionIdentifier": "" }
                            }, "ShipFrom": {
                                "Address": {
                                    "StateProvinceCode": "IL", "CountryCode": "US", "PostalCode": "60436"
                                    } },
                                "ShipTo": { "Address": {
                                    "StateProvinceCode": "NY", "CountryCode": "US", "PostalCode": "13126"
                                    } },
                                "Pickup": { "Date": "20170208"
                                    }, "ShipmentWeight": {
                                        "UnitOfMeasurement": { "Code": "LBS", "Description": "Pounds"
                                            },
                                        "Weight": "0.80" },
                                    "MaximumListSize": "20" }

    }

    s = requests.post(TT, data=json.dumps(newPayload), headers=headers)
    print(s.text)
    '''
