from alipay import AliPay


# app_private_key_string = open("/path/to/your/private/key.pem").read()
# alipay_public_key_string = open("/path/to/alipay/public/key.pem").read()

app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAhpAhConucmHn19aNcMMyq3S8OXOj5+H4liT3VKWFrMgCUuI10ggeEN88S8z2u/B1LBKb2TSQCLkPmxpohi4iwiah6v3guuCivYpiur9HxbRk0aMxVxL/oRdwGB9+5pOoK3s979FHgyYf/FXekNapSKzhY7XhNO+/Tsl3aC499ldQKu2xhO6Ey9JJylP4A8ZrU/9ewxJzVbZhNwD/rbdLuGjDta4GRsMjSSmufGeag2ii6kMpB3h8bNvMHYWHaaZqkIcyvn90JIudIRIKkjg/XkXkaxk4DeYBM1m28ChRmtv8Rg4FASPW1R4uA+KwIdbfI3gDHLfMwBoT/Y2vNTy3lwIDAQABAoIBAGuuEoK4ddOafUi/LFg8G+QQej8PRu5caezcj/9wpVPqidGBq8fzLvwZZ8rQrfEfLuShz400/r28ObzImTQm3zG2cIP3vUpOUGyUvQTr5KdVAAiyKt2fGmjytITZT1d8eWqyKJIsSqmsbJQkswH8hWLe1U5RUXJnGBQYLDF2L6dccJYak+nOQh8ybMljKBjzW5Sel2AurwcalG0fUWxrJ7d16pcBzfOimZXnC0/HRECrsnePVMcfqCHY4+DAVv/b9yA8I8PyPuiqAI/4q17qo1T7UhvpcaANjHy+/5rvW2XQvucT53jfDCQaV3m99P4Pdz4L9OvQuYKEnuyWK7DG/AECgYEA4ou1zXCpWGPfEmSPWQSep1mwWXS2g0o1HExYyqEXlJw89uZRZlRP8kOAyLtuBm31T9aboZblu9dvVV6lReC/O3cPe4ru/i9pC7Srp5/zH7soeeFif+E8tGf/QjEZzFuQQvE51x9k7jx+SOq1XPXpsmDUikCDn5SBd9bRriXyRYECgYEAmA7jpc9pkcubIvSFGNr6IbNhke90aDdaAWsJ/5vrW1O2ovFQnKPlVQZcDvBj1iif9tdtwE5IwQGDKeeG93kmpahrBiSZDsAoXHXdJPRjdJNJRmtaiBhb1t48soQOMlr7fWN/lPkgBh9+yBU509NbLPe7iF1WiPa63s5HM2He+RcCgYEAloLFrZD9IZlwuhKPXlAAbCTdUgGFxKJHuN5MW4s9VGGc61hHmlnHp6gLZtGHnsPtKDbnvSq4xNyzvh8cZNmVk5dddPHwKHYtLzbAmKRe7aT1lkwUmet13lH9t+dRQYFPzfngOLlF4DXWnPE6v2Et+3Hzo0qLaDlM7uaM9kuFs4ECgYAELlSgGIXkll6bpXGLb2n1R0Nlidn/i5YT9+d8ecMM7c5VyKDYzcDeh6A8YOu91bwgQ2gnI3/onqwGmPEjGNexMmJO9u6mcy4o7Ky5+WZKrEoVf5orp8/OpqmwluT1CX9kwTme1QLGaFNKGRtP8b3ODLnBVB+vAGm++pkGlqhU3QKBgQC30W5XJS3A3U7gCjJU2S+KnvmJ+cVaNASmnnNjex4YlXjvmoqnxeNWddiODDFoA5JDwtvfhsUH6h/MlW0ULDcn451eGV6gv/x0vAKN1LEL6H8SjGJOVHQq5J0Z4penldLoiJvOnwjOthLvBfvqPrY12jFCcWkL9JDqKcvlDY2GDg==
-----END RSA PRIVATE KEY-----"""

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhqqeR3BbrjEGBK4huBiqAoKq7d4IIkjEKgTaAlpmAyKzcbw4cswFUSVBp4+6MnJGwmmU1fnb/NoiyJCXIfGMqNiYa7C2WdhjUsQNhMPhQicEicJgj1GXpygzCgEvOD8t93JGjmDkc1s+SOswN3WY+43NAQ/pziL/RbVw8x5TZwoCcCEcInD2g8F+2m+KDH0o2EixHu9QjpaUPOe/KphZA6BPO3tywu7WXLnxHD8vtxd7+B3WRSiNEFtY6yV0ChOpL7q9iUioCx/9MiNByrgjub1/CC6+9fbfot72iCs4mcr7ikiWjQsmMmuRyBuJ5XgL+pA397265VD0b7y4x+Y2qwIDAQAB
-----END PUBLIC KEY-----"""

alipay = AliPay(
    appid="2021000118628578",
    app_notify_url=None,  # 该通知接口一般都设置None
    # 应用私钥
    app_private_key_string=app_private_key_string,
    # 阿里pay公钥
    alipay_public_key_string=alipay_public_key_string,
    # 签名算法，采用RSA2
    sign_type="RSA2", # RSA or RSA2
    # 是否是沙箱环境
    debug=True
)

prefix_url = 'https://openapi.alipaydev.com/gateway.do'

import time
order_string = alipay.api_alipay_trade_page_pay    (
    out_trade_no='%s' % time.time(),
    total_amount=50000,
    subject='小飞机',
    return_url="http://localhost:8080",  # 同步回调的前台接口
    notify_url="https://example.com/notify" # 异步回调的后台接口
)

pay_url = prefix_url + '?' + order_string
print(pay_url)