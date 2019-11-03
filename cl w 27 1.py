class Auto:

    def __init__(self, color = "red", max_speed = 200, model = 'bmv'):
        self.color = color
        self.max_speed = max_speed
        self.model = model

    def change_color(self, color):
        self.color = color
        
    def change_max_speed(self, max_speed):
        self.max_speed = max_speed
        
    def change_model(self, model):
        self.model = model
        
    def print_param(self):
        pass

    def __str__(self):
        return "{},{},{}".format(self.color, self.max_speed, self.model)

auto = Auto()
auto1 = Auto("black", 201, 'vmb')
auto2 = Auto("orange", 3, 'mvb')
auto3 = Auto(color = "green")
auto4 = Auto(max_speed = 1, model = 'mmm')

print(auto4)
