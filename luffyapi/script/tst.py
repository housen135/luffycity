import os,django,sys
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffyapi.settings.dev")

django.setup()

from django.conf import settings
print(os.getcwd())
from utils.logging import logger

logger.info('12323')
logger.debug('456')