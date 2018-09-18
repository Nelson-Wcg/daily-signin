from app import App


class Jianshu(App):

    def __init__(self):
        App.__init__(self, "jianshu", "com.jianshu.haruki", "com.baiji.jianshu.ui.splash.SplashScreenActivity", 950, 1850)
        self.set_sigin(950, 500)

    def run(self):
        self.open()
        self.click_my()
        self.sign_in()
        self.close()
