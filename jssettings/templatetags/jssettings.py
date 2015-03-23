# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from django import template

register = template.Library()


@register.simple_tag
def jss_settings(request):
    if not hasattr(request, 'js_settings'):
        return '{}'

    return json.dumps(request.js_settings)

register.simple_tag(jss_settings)


@register.simple_tag
def jss_ready_actions(request):
    if not request.js_settings.get('ready_actions'):
        return ''

    actions = request.js_settings.get('ready_actions')

    return READY_ACTIONS.format('\r\n'.join(actions))

READY_ACTIONS = '''
<script type="text/javascript">
(function ($) {{
    $(document).ready(function() {{
        {0}
    }});
}})(django.jQuery || Suit || jQuery);
</script>
'''

register.simple_tag(jss_ready_actions)
