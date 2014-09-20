# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from django import template

register = template.Library()


@register.simple_tag
def jssettings(request):
    return json.dumps(request.js_settings)

register.simple_tag(jssettings)
