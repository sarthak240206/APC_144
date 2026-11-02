class Camera:
    def take_photo(self):
        print("Photograph captured.")


class Phone:
    def make_call(self, number):
        print("Calling", number)


class Smartphone(Camera, Phone):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


phone = Smartphone("Samsung", "Galaxy")
phone.display()
phone.take_photo()
phone.make_call("9876543210")
