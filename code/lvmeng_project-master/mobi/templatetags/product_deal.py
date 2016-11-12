#! /usr/bin/env python
#coding:utf-8

from django import template
from PIL import Image

register = template.Library()

@register.filter
def decimal_percent(decimal):
    return ("%.2f" % (decimal*100)) + "%"

@register.filter
def parse_number(yuan):
    if yuan:
        return float(yuan)/10000
    else:
        return u'无'

@register.filter
def risk_preference(product):
    if product.risk_preference:
        return product.get_risk_preference_display()
    else:
        return ' '