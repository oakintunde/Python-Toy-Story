class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

   def show_info(self):
    print("Last name - "+self.last_name)
    print("Eye Color - "+self.eye_color)

    def Child(Parent):
        def __init__(self, last_name, eye_color, number_of_toys):
            print("Child constructor called")
            Parent.__init__(self, last_name, eye_color)
            self.number_of_toys = number_of_toys

            billy_cyrus = Child("Cyrus", "Blue")
            billy_cyrus.show_info()
            miley_cyrus = Child("Cyrus", "Blue", 5)
    