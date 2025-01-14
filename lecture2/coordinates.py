class Coordinates():
    def __init__(self, pointx, pointy):
        self.x = pointx
        self.y = pointy

point = Coordinates(10, 20)

print(f"x: {point.x}")
print(f"y: {point.y}")