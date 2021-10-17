from alipay import AliPay

from .settings import *

alipay = AliPay(
    appid = APP_ID,
    app_notify_url= None,
    app_private_key_string = app_private_key_string,
    alipay_public_key_string= alipay_public_key_string,
    sign_type=SIGN,
    debug = DEBUG
)