from os import path
from json import load
from shapely import geometry

from .city import City

def getCitiesFromFile():
  result = []

  # Read JSON from GEOJSON file
  dir_path = path.dirname(path.realpath(__file__))
  data = load(open(dir_path + '/' + 'data.geojson', 'r'))

  # Constructs list of Cities
    #data[] = array of data.features
  for city in data['features']:
    cityName = city['properties']['location']
      #take the city item at element "properties" and get properties.location value 
    cityPopulation = city['properties']['population']
      ##take the city item at element "properties" and get properties.popultion value 

    cityPolygon = []
    tempPolygon = city['geometry']['coordinates'][0]
    for point in tempPolygon:
      point = (point[0], point[1])
      cityPolygon.append(point)

    temp = City(cityName, cityPopulation, cityPolygon)
    result.append(temp)

  return result

def isWithinUrbanArea(x, y):
  # Cosntruct Point geometric object from given args
  targetPoint = geometry.Point([x, y])
  print('x: ' + str(x) + ' y: ' + str(y) + ' Point: ' + str(targetPoint))
  
  # Create list of Cities
  cities = getCitiesFromFile()

  # Iterate over Cities
  for city in cities:
    # Construct geometric Polygon object from current city element
    line = geometry.LineString(city.polygon)
    polygon = geometry.Polygon(line)

    # isWithinCity = polygon.contains(targetPoint)
    isWithinCity = targetPoint.within(polygon)
    #print(str(isWithinCity))

    if isWithinCity:
      return city
