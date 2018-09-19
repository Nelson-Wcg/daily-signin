from app import App
import time


class Smzdm(App):

    def __init__(self):
        App.__init__(self, "smzdm", "com.smzdm.client.android", ".activity.HomeActivity", 950, 1850)
        self.set_sigin(790, 620)

    def run(self):
        self.open()
        self.click_my()
        self.sign_in()
        self.click(580, 400)
        time.sleep(2)
        self.close()
