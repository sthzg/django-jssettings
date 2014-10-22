# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from jssettings.jssettings import JsSettings


def javascript_base_settings(request):
    """Provides basic settings to the javascript settings dictionary.

    Prepares a dictionary with all configuration values that were pushed
    to ``JsSettings`` during the request lifecycle. Additionally adds
    the ``STATIC_URL`` and ``MEDIA_URL`` to the settings.

    To make the javascript settings available on the templates:

        <script type="text/javascript">
            window.jss = {% jss_settings request %};
        </script>

    The settings are then available at the ``window.jss`` namespace, e.g:

        console.log(window.jss.media_url);
    """
    jss = JsSettings(request)
    jss.set_jssetting('static_url', settings.STATIC_URL)
    jss.set_jssetting('media_url', settings.MEDIA_URL)

    return dict()