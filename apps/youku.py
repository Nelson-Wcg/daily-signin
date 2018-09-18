from app import App


class Youku(App):

    def __init__(self):
        App.__init__(self, "youku", "com.youku.phone", ".ActivityWelcome", 950, 1850)
        self.set_sigin_btn(160, 575)
        self.set_sigin(900, 220)

    def run(self):
        self.open()
        self.click_my()
        # self.click_sign()
        self.sign_in()
        self.close()
