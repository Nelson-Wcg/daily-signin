from app import App


class Ac(App):

    def __init__(self):
        App.__init__(self, "qqac", "com.qq.ac.android", ".view.activity.SplashActivity", 950, 1850)
        self.set_sigin(1000, 1600)

    def run(self):
        self.open()
        self.sign_in()
        self.close()
