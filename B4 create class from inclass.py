class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def to_dict(self):
        return {"width": self.width, "height": self.height}

    @classmethod
    def from_dict(cls, data):
        return cls(data["width"], data["height"])

rectangles_data = [
    {"width": 10, "height": 20},
    {"width": 15, "height": 25},
    {"width": 8, "height": 8}
]

rectangles = [Rectangle.from_dict(data) for data in rectangles_data]

for rect in rectangles:
    print("Rectangle - Width:", rect.width, "Its Height:", rect.height)
