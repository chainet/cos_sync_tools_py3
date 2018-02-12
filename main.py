from qcloud_cos_py3 import CosBucket

# import config as conf

cos = CosBucket(
    conf.QCLOUD_APP_ID,
    conf.QCLOUD_SECRET_ID,
    conf.QCLOUD_SECRET_KEY,
    conf.QCLOUD_BUCKET
)