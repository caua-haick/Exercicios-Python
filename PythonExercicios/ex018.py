import math
an = int(input("Quanto é o ângulo? "))
seno = math.sin(math.radians(an)) # passa para radiano e depois calcula
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print(" o cosseno é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}". format(cos,seno,tan))
