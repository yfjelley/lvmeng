import os, sys
sys.path.append("../lvmeng")

import django
import datetime
from django.conf import settings
from lvmeng import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lvmeng.settings")
django.setup()

from api.models import Headline

if __name__=="__main__":
    today = datetime.datetime.now().strftime("%F")
    if len(Headline.objects.filter(add_date=today)) >= 20:
        olds = Headline.objects.filter(add_date__lt=today)
        for old in olds:
            old.delete()