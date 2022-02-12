text = """
Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.
"""

phrases = text.split('. ')

# for phrase in phrases:
#   if "temperature" in phrase or "average" in phrase:
#     print(phrase.replace(' C', ' Celsius'))

name = 'Moon'
gravity = 0.00135
planet = 'Earth'

title = f'Facts about {name}'

facts = f"""{'-'*80}
Nombre del planeta: {planet} 
Gravedad en {name}: {gravity * 1000} m/s2 
"""

template = f"""{title.title()} 
{facts} 
""" 

print(template)

planet = 'Marte '
gravity = 0.00143
name = 'Ganímedes'

title = f'Facts about {name}'

facts = f"""{'-'*80}
Nombre del planeta: {planet} 
Gravedad en {name}: {gravity * 1000} m/s2 
"""
template = f"""{title.title()} 
{facts} 
""" 
print(template)