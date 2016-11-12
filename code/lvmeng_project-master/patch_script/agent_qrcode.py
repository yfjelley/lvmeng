import os, sys
sys.path.append("../lvmeng")

import django
from django.conf import settings
from lvmeng import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lvmeng.settings")
django.setup()

from erp.models import Agent

class Qrcode(object):
    host = 'www.niujidui.com'
    META = {'HTTP_HOST':host}

if __name__=="__main__":
    agents = Agent.objects.all()
    # agents = Agent.objects.filter(id=4)
    for agent in agents:
        if not agent.qrcode:
            request = Qrcode()
            agent.create_qrcode(request)