class Line():
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2


    def distance(self):
        x1,y1=self.coor1        #tupple unpacking
        x2,y2=self.coor2
        distance= (((x2-x1)**2+(y2-y1)**2)**0.5)
        return f"the distance between {self.coor1} and {self.coor2} is {distance}"
    def slope(self):
        x1=self.coor1[0]
        y1=self.coor1[1]
        x2=self.coor2[0]
        y2=self.coor2[1]
        slope= (y2-y1)/(x2-x1)
        return f"slope is {slope}"
cor1=(3,2)
cor2=(8,10)

li=Line(cor1,cor2)
print(li.distance())
print(li.slope())
