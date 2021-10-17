BANNER_COUNT =2

SMS_EXP =600000

SMS_CACHE_KEY ='sms_%s'

# 后台http根路径
# BASE_URL = 'http://127.0.0.1:8000'
BASE_URL = 'http://120.55.63.84:8000'
# 前台http根路径
# LUFFY_URL = 'http://127.0.0.1:8080'
LUFFY_URL = 'http://120.55.63.84:8080'
# 订单支付成功的后台异步回调接口
NOTIFY_URL = BASE_URL + '/order/success'

# 订单支付成功的前台同步回调接口
RETURN_URL = LUFFY_URL + '/pay/success'


