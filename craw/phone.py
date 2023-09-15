class phone:
    def __init__(self, id, name, prince, brand):
        self.id = id
        self.name = name
        self.prince = prince
        self.brand = brand
    def __str__(self):
        return self.name

