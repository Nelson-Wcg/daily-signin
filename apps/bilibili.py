from app import App


class Bilibili(App):

    def __init__(self):
        App.__init__(self, "bilibili", "tv.danmaku.bili", ".ui.splash.SplashActivity", 400, 1450)
        self.set_sigin_btn(400, 1450)
        self.set_sigin(990, 520)

    def run(self):
        self.open()
        self.swipe(0, 1000, 900, 1000)
        self.click_sign()
        self.sign_in()
        self.close()
