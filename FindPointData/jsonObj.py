class JsonCity:
  urbanized = bool
  name = ""
  population = 0
  error = ""
  originalLon = ""
  originalLat = ""
  x = 0.00
  y = 0.00
  

  def __init__(self, urbanized, name, population, error, originalLon, originalLat, x, y): 
    self.urbanized = urbanized
    self.name = name
    self.population = population
    self.error = error
    self.originalLon = originalLon
    self.originalLat = originalLat
    self.x = x
    self.y = y
    