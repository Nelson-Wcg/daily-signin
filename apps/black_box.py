from app import App


class Box(App):

    def __init__(self):
        App.__init__(self, "black_box", "com.max.xiaoheihe", ".SplashActivity", 950, 1850)

    def run(self):
        self.open()
        self.close()
