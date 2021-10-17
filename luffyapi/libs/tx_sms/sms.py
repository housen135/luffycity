import random

from qcloudsms_py import SmsSingleSender
from . import settings
from utils.logging import logger


sender = SmsSingleSender(settings.appid, settings.appkey)


def send_sms(mobile, code, exp):
    try:
        response = sender.send_with_param(
            86,
            mobile,
            settings.template_id,
            params=(code, exp),
            sign=settings.sms_sign,
            extend='',
            ext='',
        )
        if response and response.get('result') == 0:
            return True
        msg = response.get('result')
    except Exception as msg:
        pass
    logger.error('短信发送失败:%s' % msg)
    return False

def get_code():
    code =''
    for i in range(3):
        code += str(random.randint(0,9))
    return code
