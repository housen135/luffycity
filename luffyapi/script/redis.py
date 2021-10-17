
import os,sys
print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffyapi.settings.dev")
django.setup()


from django.core.cache import cache
cache.set('name120', 'bob', 20)
print(cache.get('name120'))


