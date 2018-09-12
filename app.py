import action


class App:

    def __init__(self, name, package, main_class, my_x, my_y):
        self.name = name
        self.main_class = main_class
        self.my_x = my_x
        self.my_y = my_y
        self.package = package

    def set_my_position(self, x, y):
        self.my_x = x
        self.my_y = y

    def click_my(self):
        action.click(self.my_x, self.my_y)

    def open(self):
        action.open_app(self.package, self.main_class)