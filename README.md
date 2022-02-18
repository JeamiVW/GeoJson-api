# GeoJson-api
##Task:
  Build a basic API which accepts latitude/longitude parameter and returns a value indicating whether the given point is in an urbanized area.
    The API accepts an Http POST request with a JSON payload of latitude and longitude. It should return True if the given point is in an urbanized 
    area, and false otherwise.
##Submission:
  This API accepts Http POST requests with multiple points or a single point as well as Http GET requests. With a JSON payload of latitude and longitude this api returns GEOJSON data for the given point in the below format. 
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
