class Vehicle:
    def __init__(self,brand,model,color,electric):
        self.brand = brand
        self.model = model
        self.color = color
        self.electric = electric

    def drive(self):
        print(f"You drive {self.brand} {self.model}")