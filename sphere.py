"""this is for circle class object . Finding volume and surface
   volume = 4/3*pie*r**3
   surface area=4.pie.r*2"""

class Circle():
    def __init__(self,radius=1):
        self.radius=radius

    def volume(self):
        v=(4/3)*3.14*self.radius**3
        return f"volume of circle with radius {self.radius} = {v}"

    def surfaceArea(self):
        sa=4*3.14*self.radius**2
        return f"surface area of sphere with {self.radius} = {sa}"

x=Circle(10)
print(x.volume())
print(x.surfaceArea())
y=Circle()
print("without giving anything",y.volume())
