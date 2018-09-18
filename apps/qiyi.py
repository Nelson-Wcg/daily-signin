from app import App


class Qiyi(App):

    def __init__(self):
        App.__init__(self, "aiqiyi", "com.qiyi.video", "org.qiyi.android.video.MainActivity", 760, 1850)
        self.set_sigin(730, 260)

    def run(self):
        self.open()
        self.click_my()
        self.sign_in()
        self.close()
