from app import App


class BaiduMap(App):

    def __init__(self):
        App.__init__(self, "map", "com.baidu.BaiduMap", "com.baidu.baidumaps.MapsActivity", 90, 130)
        self.set_sigin(900, 230)

    def run(self):
        self.open()
        self.click_my()
        self.sign_in()
        self.click(550, 380)
        self.close()

