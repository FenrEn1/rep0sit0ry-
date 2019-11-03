#class Auto:
#    def __init__(self)
#        self.color = ""
#        self.max_speed = 200
#my_auto = Auto()





#class Auto:

 #   def __init__(self, color = "red", max_speed = 200, model = 'bmv'):
 #       self.color = color
 #       self.max_speed = max_speed
#        self.model = model

 #   def change_color(self, color):
#        self.color = color
        
#    def change_max_speed(self, max_speed):
 #       self.max_speed = max_speed
        
#    def change_model(self, model):
#        self.model = model
        
#    def print_param(self):
#        pass

#    def __str__(self):
#        return "{},{},{}".format(self.color, self.max_speed, self.model)

#auto = Auto()
#auto1 = Auto("black", 201, 'vmb')
#auto2 = Auto("orange", 3, 'mvb')
#auto3 = Auto(color = "green")
#auto4 = Auto(max_speed = 1, model = 'mmm')

#print(auto)




class Auto:
    def __init__ (self, list_wheels = [0 for x in range(4)], win_number = 1):

        if len(list_wheels) != 4:
            assert

        self.list_wheels = list_wheels
        self._win_numder = win_number

    def set_wheels(self, number, wheel):
        if number > 3:
            print("Столько нет")
        else:
            self.list_wheels[number] = wheel


#    def change_list_wheels(self, list_wheels):
#       self.list_wheels = list_wheels







