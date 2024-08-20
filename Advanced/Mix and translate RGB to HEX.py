class RGB:
    def __init__(self, red, green, blue):
        # _clamp method ensures that RGB values are within the valid range 0 - 255
        self.red = self._clamp(red)
        self.green = self._clamp(green)
        self.blue = self._clamp(blue)
    
    def _clamp(self, value):   #method to keep the value in range
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
        # formting an integer into hexadecimal representation: 02X
        # 02 should be at least 2 characters, padded with 0, if needed
        # X to uppercase hexadecimal
        # {} {} {} three times

    def blend(self, other, ratio):
        #blend with another RGB color by ratio thats between 0 and 1
        ratio = max(0, min(1, ratio))
        r = int(self.red * (1 - ratio) + other.red * ratio)
        g = int(self.green * (1 - ratio) + other.green * ratio)
        b = int(self.blue * (1 - ratio) + other.blue * ratio)
        return RGB(r, g, b)
    
#hardcoded example:
# color1 = RGB(255, 0, 0)  #red
# color2 = RGB(0, 0, 255)  #blue

color1_input = input("Enter the RGB values for color 1: \nExample: 255 0 0\n\n")
red1, green1, blue1 = map(int, color1_input.split())
#map() is a function, applies a given function to all items of an iterable (like a list or a tuple)
#result of map() is an iterator that contains the transformed items (here - splitted str)
# split makes a substring ['255', '0', '0']
# map applies int to every element
color1 = RGB(red1, green1, blue1)

color2_input = input("\nEnter the RGB values for color 1: \nExample: 255 0 0\n\n")
red2, green2, blue2 = map(int, color2_input.split())
color2 = RGB(red2, green2, blue2)

print(f"\nColor 1: {color2}")
print(f"Color 2: {color2}\n")

print(f"Color 1 Hex: {color1.to_hex()}")
print(f"Color 2 Hex: {color2.to_hex()}")

blended_color = color1.blend(color2, 0.5)

print(f"Blended Color: {blended_color}")
print(f"Blended Color Hex: {blended_color.to_hex()}")
