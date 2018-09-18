from app import App
import time

class Oneplus(App):

    def __init__(self):
        App.__init__(self, "oneplus", "com.oneplus.bbs", ".ui.activity.PreStartActivity", 400, 720)
        self.set_sigin(400, 720)

    def run(self):
        self.open()
        self.sign_in()
        self.click(70, 160)
        self.click(940, 720)
        for num in range(0, 10):
            self.click(540, 640)
            time.sleep(2)
            self.back()
        self.close()
