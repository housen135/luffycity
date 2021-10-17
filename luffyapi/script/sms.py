from qcloudsms_py.httpclient import HTTPError
from qcloudsms_py import SmsSingleSender
appid = 1400580497
appkey = '184518d80def0953b74e40154fb6f208'
template_id = 1146985
sms_sign = '墨水鉴赏'


ssender = SmsSingleSender(appid, appkey)
params = ['888888', '600']
try:
    result = ssender.send_with_param(
        86, '18758526052', template_id, params, sign=sms_sign, extend='', ext='')
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)
