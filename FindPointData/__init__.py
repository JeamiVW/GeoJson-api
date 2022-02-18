import logging
from multiprocessing.sharedctypes import Value
import string
from urllib import request
# from xmlrpc.client import boolean
import azure.functions as func
#import json

from .geographyUtils import isWithinUrbanArea
from .responseUtils import inputErrors, readbody
from .responseUtils import urlQuery
from .responseUtils import geoErrors

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Attempt to grab params from URL query
    longitude = req.params.get('x')
    latitude = req.params.get('y')
    lonm = None
    latm = None

    #Variables
    payload = []
    message = ""
    geomsg = ""

    #process if args are not in URL query
    #check if args are in the body as raw data
    if not (latitude and longitude):
        #try loop through payload array, return error if nothing in body
        try:
            print('Using body params - Longitude: ' + str(longitude) + ' Latitude: ' + str(latitude))
            #get information from body and put into payload array
            payload = req.get_json()
            payloadlen = len(payload) - 1
            payloadpt = 0

            for point in payload:
                point = (point['x'], point['y'])
                print('point(0):' + point[0] + ' point(1):' + point[1])

                #set lat and lon
                lonm = point[0]
                latm = point[1]

                #ERROR HANDLING
                hasError = inputErrors(lonm, latm)

                if ((hasError == "string") or (hasError == "longitude") or (hasError == "latitude")):
                    #pass to error handling
                    message += geoErrors(lonm, latm, hasError)

                else:
                    #Run points through readbodydef
                    message += readbody(lonm, latm)

                #if there are more points in payload[], add ","
                if payloadpt == payloadlen:
                    message += ""
                else:
                    message += ","

                #Increase payloadpt
                payloadpt += 1

        except ValueError:
            pass
    else:
        # Cast request args to correct type
        print('Using URL Query - Longitude: ' + str(longitude) + ' Latitude: ' + str(latitude))
        #ERROR HANDLING
        hasError = inputErrors(longitude, latitude)

        if ((hasError == "string") or (hasError == "longitude") or (hasError == "latitude")):
            #pass to error handling
            message += geoErrors(longitude, latitude, hasError)

        else:
            #Run points through readbodydef
            message = urlQuery(longitude, latitude)

    # Alert user if args were not given
    if not ((longitude and latitude) or (lonm and latm)):
        return func.HttpResponse(
            "Please give a set of points as x (longitude) and y (latitude).",
            status_code=400
        )

    #format GEOJSON
    geomsg = "{\"type\": \"FeatureCollection\",\n\t" + "\"features\" : ["
        #add the response\
    geomsg += message + "\n\t]\n}"

    # Return response payload
    return func.HttpResponse(
            geomsg,
            status_code=200
        )
