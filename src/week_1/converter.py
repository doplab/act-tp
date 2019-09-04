class NumberConverter:
    @staticmethod    
    def to_base_10(value, new_base):
        return int(str(value), new_base)

    def __init__(self, value, base):
        self.base = base
        self.value = self.to_base_10(value, base)

    def convert(self, new_base):
        output = ""
        base_number = self.value
        while base_number >= 1:
            modulo = base_number % new_base
            base_number = int(base_number / new_base)
            output += str(modulo)
        if not len(output):
            return 0
        return int("".join(reversed(output)))

    def __str__(self):
        return str(int(str(self.value), self.base))

    def __add__(self, that):
        return self.value + that.value
        
        
if __name__ == "__main__":
    x = NumberConverter(100, 10)
    y = NumberConverter(1100, 2)
    print(x + y)
    print(y.convert(8))