# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json


class JsSettings(object):
    """
    Provides API methods to get and set values on the ``js_settings`` object.
    """
    # TODO(sthzg) Make it a singleton available through complete req/resp cycle.
    def __init__(self, request):
        try:
            self.js_settings = request.js_settings
        except AttributeError:
            self.js_settings = dict()
            request.__setattr__('js_settings', self.js_settings)

        if not self.js_settings.get('ready_actions'):
            self.js_settings['ready_actions'] = list()

        self.js_ready_actions = self.js_settings.get('ready_actions')


    def get_jssetting(self, keys, lookup_dict=None):
        """
        Returns the value for a setting or None.

        Ex:

            jss = JsSettings(request)

            jss.get_jssetting('foo')
            # Returns request.js_settings['foo']

            jss.get_jssetting('foo.bar.bam.baz')
            # Returns request.js_settings['foo']['bar']['bam']['baz']

        :param keys: Keys in string notation, separated by ., e.g. foo.bar.
        :param lookup_dict: Defaults to ``request.js_settings``.
        :return: *, None
        """
        if not lookup_dict:
            lookup_dict = self.js_settings

        try:
            if "." in keys:
                key, rest = keys.split(".", 1)
                return self.get_jssetting(rest, lookup_dict[key])
            else:
                return lookup_dict[keys]

        except KeyError:
            return None

    def set_jssetting(self, keys, value, lookup_dict=None):
        """
        Sets value in ``request.js_settings.``

        Ex:

            jss = JsSettings(request)

            jss.set_jssetting('foo', 'hello world')
            jss.get_jssetting('foo')
            # hello world

            jss.set_jssetting('one.two.three', 'checkpot')
            jss.get_jssetting('one.two.three')
            # checkpot

            jss.set_jssetting('one.two.three', 'checkpot')
            jss.get_jssetting('one.two')
            # {'three': 'checkpot'}

        :param keys:
        :param value:
        :param lookup_dict:
        :return:
        """
        if lookup_dict is None:
            lookup_dict = self.js_settings

        if "." in keys:
            key, rest = keys.split(".", 1)
            if key not in lookup_dict:
                lookup_dict[key] = {}
            self.set_jssetting(rest, value, lookup_dict[key])

        else:
            lookup_dict[keys] = value

    def register_ready_action(self, action):
        """
        Registers an action to be executed on the ready event.

        :param action: String of action to be performed on ready event.
        """
        self.js_ready_actions.append(action)
                
    def dumps(self):
        """
        Returns ``request.js_settings`` as json'ified string.

        :return: ``request.js_settings`` as JSON.
        """
        return json.dumps(self.js_settings)
