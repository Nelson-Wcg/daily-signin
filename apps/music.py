from app import App


class Music(App):

    def __init__(self):
        App.__init__(self, "music", "com.netease.cloudmusic", ".activity.LoadingActivity", 950, 1850)
        self.set_sigin_btn(160, 575)
        self.set_sigin(810, 520)

    def run(self):
        self.open()
        # self.click_my()
        # self.click_sign()
        # self.sign_in()
        # self.close()
