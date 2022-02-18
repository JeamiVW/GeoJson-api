# GeoJson-api
## Task:
  Build a basic API which accepts latitude/longitude parameter and returns a value indicating whether the given point is in an urbanized area.
    The API accepts an Http POST request with a JSON payload of latitude and longitude. It should return True if the given point is in an urbanized 
    area, and false otherwise.
## Submission:
  This API accepts Http POST requests with multiple points or a single point as well as Http GET requests. With a JSON payload of latitude and longitude this api returns GEOJSON data for the given point in the below format. 
```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "urbanize": "False",
        "location": "N/A",
        "population": "N/A",
        "error": "Latitude and Longitude need to be an valid number.",
        "orig longitude": "-45.91376224438353",
        "orig latitude": "42.071395g39374084"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          0,
          0
        ]
      }
    }
  ]
} 
```
## Explaination of functions:
### geographyUtils.py:
- getCitiesFromFile(): Pulls all of the data points out of the GEOJSON file and constructs data structures
            to hold the data for each city individually so it can be parse through later in the program.
- isWithinUrbanArea(x, y): Takes in an x and y parameter (longitude and latitude) to test if the 
            given coordinates are within a polygon (city within the list) and will return the city object
            or will return "none" if the point doesn't fall within a city's polygon.
### responseUtils.py:
- readBody(lonx, laty): If there are no errors with the longitude and latitude inputs, they are passed to this function. Here is where the returned city object (or the return of "none") is coded into GEOJSON format when the parameters are read from a POST method.
- urlQuery(lonx, laty): If there are no errors with the longitude and latitude inputs, they are passed to this function. Here is where the returned city object (or the return of "none") is coded into GEOJSON format when the parameters are read from a GET method.
- inputErrors(lonm, latm): This fuction tests the longitude and latitude parameters given to see if there are errors. It will test for the following error possibilities...
  - The latitude or longitude given have characters in it and cannot be converted to a float value.
  - The longitude is out of range of -180.00 and 180.00. Known longitude values.
  - The latitude is out of range of -90.00 and 90.00. Kown latitude values.
- The type of error will be returned as a string.
  - Return values:
    - "string"
    - "longitude"
    - "latitude"
    - "pass" <-- no errors found in the inputs.
- geoErrors(lonerror, laterror, hasError): Pulls the longitude, latitude, and type of error as parameters. This function will then generate the correct GEOJSON code for the error, setting the "error" property to display what type of error the longitude and latitude had. It also changes the longitude and latitude to 0.00 and 0.00 so it is displayed on the map.


### Test Points within an Urbanized Area
- -75.91376224438353, 42.07139539374084 (Random Binghamton)
- -73.02105606055635, 40.76718728206796
- -78.90088203001112, 35.99620904561505
### Test Points not within an Urbanized Area
- -74.65047087616452, 44.543362328416606
### Test Points with errors
- -74.65047f087616452, 44.543362328416606 (string)
- -74.65047087616452, 44.5433623f28416606 (string)
- -7222224.65047087616452, 44.543362328416606 (Longitude out of range)
- -74.65047087616452, 4004.543362328416606 (Latitude out of range)

### TEST DATA JSON FORMAT
```
[
  {"x":"-75.91376224438353","y":"42.07139539374084"},
  {"x":"-73.02105606055635","y":"40.76718728206796"},
  {"x":"-78.90088203001112","y":"35.99620904561505"},
  {"x":"-74.65047f087616452","y":"44.543362328416606"},
  {"x":"-74.65047087616452","y":"44.5433623f28416606"},
  {"x":"-7222224.65047087616452","y":"44.543362328416606"},
  {"x":"-74.65047087616452","y":"4004.543362328416606"},
  {"x":"-74.65047087616452","y":"44.543362328416606"}
]
```
