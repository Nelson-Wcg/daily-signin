from app import App


class Rrsp(App):

    def __init__(self):
        App.__init__(self, "rr", "com.zhongduomei.rrmj.society", ".function.launch.activity.LaunchActivity", 950, 1850)
        self.set_sigin(180, 380)

    def run(self):
        self.open()
        self.click_my()
        self.sign_in()
        self.close()
