from app import App


class Jd(App):

    def __init__(self):
        App.__init__(self, "jd", "com.jingdong.app.mall", ".main.MainActivity", 968, 1864)
        self.set_sigin_btn(330, 800)
        self.set_sigin(530, 340)

    def run(self):
        self.open()
        self.click_sign()
        self.sign_in()
        self.close()
