from app import App


def sign_in():
    print(1)
    app = App("market", "com.oppo.market", ".activity.MainActivity", 1, 1)
    # app.click_my()
    app.open()


sign_in()
