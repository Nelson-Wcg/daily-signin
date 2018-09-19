from apps.jd import Jd
from apps.jdr import Jdr
from apps.acfun import Acfun
from apps.bilibili import Bilibili
from apps.baidu_map import BaiduMap
from apps.it_home import Ithome
from apps.jianshu import Jianshu
from apps.rrsp import Rrsp
from apps.smzdm import Smzdm
from apps.qq_ac import Ac
from apps.black_box import Box
from apps.one_plus import Oneplus
from apps.youku import Youku
from apps.qiyi import Qiyi


def sign_in():
    jd = Jd()
    jd.run()
    jdr = Jdr()
    jdr.run()
    acfun = Acfun()
    acfun.run()
    bilibili = Bilibili()
    bilibili.run()
    b_map = BaiduMap()
    b_map.run()
    ithome = Ithome()
    ithome.run()
    jianshu = Jianshu()
    jianshu.run()
    rr = Rrsp()
    rr.run()
    smzdm = Smzdm()
    smzdm.run()
    # ac = Ac()
    # ac.run()
    box = Box()
    box.run()
    one_plus = Oneplus()
    one_plus.run()
    youku = Youku()
    youku.run()
    qiyi = Qiyi()
    qiyi.run()


sign_in()
