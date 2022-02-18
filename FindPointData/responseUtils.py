import json
from .geographyUtils import isWithinUrbanArea
import azure.functions as func
import string

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
        #rspstring += " Point ({}, {}) is within the city of \"{}\" (population of {}).".format(lonxf, latyf, containgCity.name, containgCity.population) + "\n"
        rspstring += "\n\t{\"type\": \"Feature\", \n\t\t\"properties\":{\"urbanize\":\"" + str(urbanized) + "\","
        rspstring += "\"location\":\"" + str(containgCity.name) + "\",\"population\": \"" + str(containgCity.population) + "\",\"error\": \"none\","
        rspstring += "\"orig longitude\": \"" + str(lonxf) + "\", \"orig latitude\": \"" + str(latyf) + "\"},\n"
        rspstring += "\t\t\"geometry\":{ \"type\":\"Point\",\"coordinates\": [" + str(lonxf) + "," + str(latyf) + "] } }"
    else:
        urbanized = False
        #rspstring += " Point ({}, {}) is not within any urban area.".format(lonxf, latyf) + "\n"
        rspstring += "\n\t{\"type\": \"Feature\", \n\t\t\"properties\":{\"urbanize\":\"" + str(urbanized) + "\","
        rspstring += "\"location\":\"N/A\",\"population\": \"N/A\",\"error\": \"none\","
        rspstring += "\"orig longitude\": \"" + str(lonxf) + "\", \"orig latitude\": \"" + str(latyf) + "\"},\n"
        rspstring += "\t\t\"geometry\":{ \"type\":\"Point\",\"coordinates\": [" + str(lonxf) + "," + str(latyf) + "] } }"

    return rspstring

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
        #rspstring += " Point ({}, {}) is within the city of \"{}\" (population of {}).".format(longitudef, latitudef, containgCity.name, containgCity.population) + "\n"
        rspstring += "\n\t{\"type\": \"Feature\", \n\t\t\"properties\":{\"urbanize\":\"" + str(urbanized) + "\","
        rspstring += "\"location\":\"" + str(containgCity.name) + "\",\"population\": \"" + str(containgCity.population) + "\",\"error\": \"none\","
        rspstring += "\"orig longitude\": \"" + str(longitudef) + "\", \"orig latitude\": \"" + str(latitudef) + "\"},\n"
        rspstring += "\t\t\"geometry\":{ \"type\":\"Point\",\"coordinates\": [" + str(longitudef) + "," + str(latitudef) + "] } }"
    else:
        urbanized = False
        #rspstring += " Point ({}, {}) is not within any urban area.".format(longitudef, latitudef) + "\n"
        rspstring += "\n\t{\"type\": \"Feature\", \n\t\t\"properties\":{\"urbanize\":\"" + str(urbanized) + "\","
        rspstring += "\"location\":\"N/A\",\"population\": \"N/A\",\"error\": \"none\","
        rspstring += "\"orig longitude\": \"" + str(longitudef) + "\", \"orig latitude\": \"" + str(latitudef) + "\"},\n"
        rspstring += "\t\t\"geometry\":{ \"type\":\"Point\",\"coordinates\": [" + str(longitudef) + "," + str(latitudef) + "] } }"
    return rspstring

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
        rspstring += "\n\t{\"type\": \"Feature\", \n\t\t\"properties\":{\"urbanize\":\"" + str(urbanized) + "\","
        rspstring += "\"location\":\"N/A\",\"population\": \"N/A\",\"error\": \"Latitude and Longitude need to be an valid number.\","
        rspstring += "\"orig longitude\": \"" + str(lonerror) + "\", \"orig latitude\": \"" + str(laterror) + "\"},\n"
        rspstring += "\t\t\"geometry\":{ \"type\":\"Point\",\"coordinates\": [" + str(longhold) + "," + str(lathold) + "] } }"
        print("String Error")

    elif (hasError == "longitude"):
        #run error handling if longitude is out of range
        rspstring += "\n\t{\"type\": \"Feature\", \n\t\t\"properties\":{\"urbanize\":\"" + str(urbanized) + "\","
        rspstring += "\"location\":\"N/A\",\"population\": \"N/A\",\"error\": \"Longitude is out of range.\","
        rspstring += "\"orig longitude\": \"" + str(lonerror) + "\", \"orig latitude\": \"" + str(laterror) + "\"},\n"
        rspstring += "\t\t\"geometry\":{ \"type\":\"Point\",\"coordinates\": [" + str(longhold) + "," + str(lathold) + "] } }"
        print("Longitude Error")

    elif (hasError == "latitude"):
        #run error handling if latitude is out of range
        rspstring += "\n\t{\"type\": \"Feature\", \n\t\t\"properties\":{\"urbanize\":\"" + str(urbanized) + "\","
        rspstring += "\"location\":\"N/A\",\"population\": \"N/A\",\"error\": \"Latitude is out of range.\","
        rspstring += "\"orig longitude\": \"" + str(lonerror) + "\", \"orig latitude\": \"" + str(laterror) + "\"},\n"
        rspstring += "\t\t\"geometry\":{ \"type\":\"Point\",\"coordinates\": [" + str(longhold) + "," + str(lathold) + "] } }"
        print("Latitude Error")

    return rspstring

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
