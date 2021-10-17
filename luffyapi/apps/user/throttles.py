from rest_framework.throttling import  SimpleRateThrottle

class SMSThrottle(SimpleRateThrottle):
    scope = 'sms_throttle'
    def get_cache_key(self, request, view):
        mobile = request.data.get('mobile')
        if mobile:
            return 'sms_throttle_%s'%mobile