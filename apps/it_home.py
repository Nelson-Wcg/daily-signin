from app import App


class Ithome(App):

    def __init__(self):
        App.__init__(self, "it", "com.ruanmei.ithome", ".MainActivity1", 950, 1850)
        self.set_sigin_btn(1000, 200)

    def run(self):
        self.open()
        self.click_my()
        self.click_sign()
        self.close()
