import math
class Figur:
    def __init__(self, name):
        self.name = "Figur"
        
    def umfang(self):
            return 0
        
    def __str__(self):
            return self.name

class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y
    
    def __str__(self):
         return f"Punkt ({self.x}, {self.y})"

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis") 
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def umfang(self):
         return self.radius*2*math.pi
    
    def __str__(self):
         return f"Kreis M={self.mittelpunkt} r={self.radius}"
    
class Rechteck(Figur):
    def __init__(self, punkt1, punkt2):
          super().__init__("Rechteck")
          self.punkt1 = punkt1
          self.punkt2 = punkt2
    
    def umfang(self):
         return ((self.punkt2.x-self.punkt1.x)+(self.punkt2.y-self.punkt1.y))*2
    
    def __str__(self):
         return f"Rechteck parallel zu den Achsen, Ecke linkts unten {self.punkt1}, Ecke rechts oben {self.punkt2}"
    
class Dreieck(Figur):
    def __init__(self, punkt1, punkt2, punkt3):
         super().__init__("Dreieck")
         self.punkt1 = punkt1
         self.punkt2 = punkt2
         self.punkt3 = punkt3
    
    def umfang(self):
         a = math.sqrt((self.punkt1.x-self.punkt2.x)**2+(self.punkt1.y-self.punkt2.y)**2)
         b = math.sqrt((self.punkt2.x-self.punkt3.x)**2+(self.punkt2.y-self.punkt3.y)**2)
         c = math.sqrt((self.punkt3.x-self.punkt1.x)**2+(self.punkt3.y-self.punkt1.y)**2)
         return a+b+c
    def __str__(self):
         return f"Dreieck mit Punkten {self.punkt1}, {self.punkt2}, {self.punkt3}"
    
class Polygon(Figur):
    def __init__(self, punkte):
         super().__init__("Polygon")
         self.punkte = punkte
    
    def umfang(self):
        umfang = 0
        for i in range(len(self.punkte)):
            if i == len(self.punkte) - 1:
                umfang += math.sqrt((self.punkte[i].x - self.punkte[0].x)**2 + (self.punkte[i].y - self.punkte[0].y) ** 2)
            else:
                umfang += math.sqrt((self.punkte[i+1].x - self.punkte[i].x) ** 2 + (self.punkte[i+1].y - self.punkte[i].y) ** 2)
            
        return umfang
    
    def __str__(self):
        punkte = ", ".join(str(punkt) for punkt in self.punkte)
        return f"Polygon({punkte})"


p1=Punkt(2,4)
p2=Punkt(4,4)
p3=Punkt(3,6)
p4=Punkt(9,3)
k1=Rechteck(p1,p2)
k2=Kreis(p1, 10)
k3=Dreieck(p1,p2,p3)
k4=Polygon([p1,p2,p3])
print(k1.umfang())
print(k2.umfang())
print(k3.umfang())
print(k4.umfang())
print(k4)