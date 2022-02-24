import json
from unittest import result
from .geographyUtils import isWithinUrbanArea
import azure.functions as func
import string
from .jsonObj import JsonCity

#Put data from the body into an array and test each point
    #Append the message string to show output for each point

def readbody(lonx, laty):
    #Variables
    rspstring = ""
    urbanized = False

    #Cast as a float
    lonxf = float(lonx)
    latyf = float(laty)

    #pass each point through isWithinUrbanArea
    containgCity = isWithinUrbanArea(lonxf, latyf)

    #pull out information from response
    if containgCity is not None:
        urbanized = True
        jCity = JsonCity(urbanized, containgCity.name, containgCity.population, "none", lonxf, latyf, lonxf, latyf)
    else:
        urbanized = False
        jCity = JsonCity(urbanized, "N/A", "N/A", "none", lonxf, latyf, lonxf, latyf)
    
    #return value
    return jCity

#Read URL query
def urlQuery(lonx, laty):
    #variables
    rspstring = ""
    urbanized = False

    #Cast as float
    longitudef = float(lonx)
    latitudef = float(laty)

    #pass each point through isWithinUrbanArea
    containgCity = isWithinUrbanArea(longitudef, latitudef)

    #pull out information from response
    if containgCity is not None:
        urbanized = True
        jCity = JsonCity(urbanized, containgCity.name, containgCity.population, "none", longitudef, latitudef, longitudef, latitudef)
    
    else:
        urbanized = False
        jCity = JsonCity(urbanized, "N/A", "N/A", "none", longitudef, latitudef, longitudef, latitudef)
    
    #return value
    return jCity

#Handles errors with the inputs
def geoErrors(lonerror, laterror, hasError):
    #variables
    rspstring = ""
    urbanized = False
    longhold = 0.00
    lathold = 0.00
    

    #Edit return message based on error
    if (hasError == "string"):
        #run error handling for strings
        jCity = JsonCity(urbanized, "N/A", "N/A", "Latitude and Longitude need to be an valid number.", lonerror, laterror, longhold, lathold)
        print("String Error")

    elif (hasError == "longitude"):
        #run error handling if longitude is out of range
        jCity = JsonCity(urbanized, "N/A", "N/A", "Longitude is out of range.", lonerror, laterror, longhold, lathold)
        print("Longitude Error")

    elif (hasError == "latitude"):
        #run error handling if latitude is out of range
        jCity = JsonCity(urbanized, "N/A", "N/A", "Latitude is out of range.", lonerror, laterror, longhold, lathold)
        print("Latitude Error")

    # return rspstring
    return jCity

#Test if there are errors in the longitude or latitude
def inputErrors(lonm, latm):
    #try to cast lat and lon as float and Error: sets errorstr = "string"
    try:
        lonmf = float(lonm)
        latmf = float(latm)
        lonlaterr = "pass"
        print(lonlaterr)
    except ValueError:
        lonlaterr = "string"

    hasError = ""
    #set hasError = "error" if there is an issue with inputs
    if (lonlaterr == "string"):
        #mark error as strings
        hasError = "string"

    elif ((lonmf < -180.00) or (lonmf > 180.00)):
        #mark error as longitude is out of range
        hasError = "longitude"

    elif ((latmf < -90.00) or (latmf > 90.00)):
        #mark error as longitude is out of range
        hasError = "latitude"

    return hasError
