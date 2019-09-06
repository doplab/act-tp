class NumberConverter:
    @staticmethod    
    def to_base_10(value, new_base):
        return int(str(value), new_base)

    def __init__(self, value, base):
        self.base = base
        self.value = self.to_base_10(value, base)

    def convert(self, new_base):
        new_base = int(new_base) # Check for invalid types
        if new_base < 2 or new_base > 36:
            raise ValueError("Invalid base, the base should be >= 2 and <= 36")
        output = ""
        base_number = self.value
        while base_number >= 1:
            modulo = base_number % new_base
            if modulo >= 10:
                output += chr(55+modulo)
            else:
                output += str(modulo)
            base_number = int(base_number / new_base)
        if not len(output):
            return 0
        return "".join(reversed(output))

    def __str__(self):
        return str(int(str(self.value), self.base))

    def __add__(self, that):
        return self.value + that.value
        
        
if __name__ == "__main__":
    x = NumberConverter("6C", 16)
    print(x.convert(0))