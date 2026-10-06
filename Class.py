class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            print("Error: Lebar dan panjang harus bernilai positif.")
            self.length = 0
            self.width = 0
        else:
            self.length = length
            self.width = width