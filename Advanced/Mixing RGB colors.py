class RGB:
    def __init__(self, red, green, blue):
        # _clamp method ensures that RGB values are within the valid range 0 - 255
        self.red = self._clamp(red)
        self.green = self._clamp(green)
        self.blue = self._clamp(blue)
    
    def _clamp(self, value):
        return max(0, min(255, value))
    
    def set_red(self, red):    #modifies the value of an attribute
        self.red = self._clamp(red)
    
    def set_green(self, green):
        self.green = self._clamp(green)
    
    def set_blue(self, blue):
        self.blue = self._clamp(blue)
    
    def get_red(self):         #retrieves the value of an attribute, read-only access
        return self.red
    
    def get_green(self):
        return self.green
    
    def get_blue(self):
        return self.blue
    
    def __str__(self):
        return f"RGB({self.red}, {self.green}, {self.blue})"
    
    def to_hex(self):
        return "#{:02X}{:02X}{:02X}".format(self.red, self.green, self.blue)

    def blend(self, other, ratio):

        #blend with another RGB color by ratio thats between 0 and 1
        ratio = max(0, min(1, ratio))
        r = int(self.red * (1 - ratio) + other.red * ratio)
        g = int(self.green * (1 - ratio) + other.green * ratio)
        b = int(self.blue * (1 - ratio) + other.blue * ratio)
        return RGB(r, g, b)

color1 = RGB(255, 0, 0)  #red
color2 = RGB(0, 0, 255)  #blue

print(f"Color 1: {color2}")
print(f"Color 2: {color2}\n")

print(f"Color 1 Hex: {color1.to_hex()}")
print(f"Color 2 Hex: {color2.to_hex()}")

blended_color = color1.blend(color2, 0.5)

print(f"Blended Color: {blended_color}")
print(f"Blended Color Hex: {blended_color.to_hex()}")

