import action


class App(object):

    def __init__(self, name, package, main_class, my_x, my_y):
        self.name = name
        self.main_class = main_class
        self.my_x = my_x
        self.my_y = my_y
        self.package = package

    def click_my(self):
        action.click(self.my_x, self.my_y)

    def set_sigin_btn(self, sign_x, sign_y):
        self.sign_btn_x = sign_x
        self.sign_btn_y = sign_y

    def set_sigin(self, sigin_x, sigin_y):
        self.sigin_x = sigin_x
        self.sigin_y = sigin_y

    def open(self):
        action.open_app(self.package, self.main_class)

    def click_sign(self):
        action.click(self.sign_btn_x, self.sign_btn_y)

    def sign_in(self):
        action.click(self.sigin_x, self.sigin_y, 3)

    def close(self):
        action.close(self.package)

    def swipe(self, x, y, x1, y1):
        action.swipe(x, y, x1, y1, 500)

    def run_no_click(self):
        self.open()
        self.close()

    def click(self, x, y):
        action.click(x, y)

    def jump(self, x, y):
        action.click(x, y)

    def back(self):
        action.back()
