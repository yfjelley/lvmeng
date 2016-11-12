import os, sys
sys.path.append("../lvmeng")

import django
from django.conf import settings
from lvmeng import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lvmeng.settings")
django.setup()

from erp.models import Agent

if __name__=="__main__":
    agents = Agent.objects.all()
    # agents = Agent.objects.filter(id=4)
    for agent in agents:
        try:
            if agent.user:
                username = agent.business.business_num + str(agent.agent_num)
                user = agent.user
                user.username = username
                user.save()
        except:
            pass