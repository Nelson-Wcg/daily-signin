from app import App


class Acfun(App):

    def __init__(self):
        App.__init__(self, "acfun", "tv.acfundanmaku.video", "tv.acfun.core.view.activity.SplashActivity", 950, 1850)
        # self.set_sigin_btn(160, 575)
        self.set_sigin(900, 650)

    def run(self):
        self.open()
        self.click_my()
        self.sign_in()
        self.close()
