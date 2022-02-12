def evaluaMeteorito(dimension, velocidad):
  if dimension >= 1000:
    return "F por nosotros"
  if dimension >= 25 or velocidad >= 25:
    return "EMBOSACADA EMBOSCADA!!"
  if dimension >= 20 and dimension < 25:
    return "Wachen el paisaje Homies!"

print(evaluaMeteorito(1010, 1))
print(evaluaMeteorito(25, 20))
print(evaluaMeteorito(20, 25))
print(evaluaMeteorito(20, 5))