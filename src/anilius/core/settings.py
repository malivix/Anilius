"""
Settings and configuration for Django.

Read values from the module specified by the DJANGO_SETTINGS_MODULE environment
variable, and then from django.conf.global_settings; see the global_settings.py
for a list of all possible variables.
"""

import importlib
from importlib.util import find_spec


class Settings(object):
    """
    A lazy proxy for either global Django settings or a custom settings object.
    The user can manually configure settings prior to using them. Otherwise,
    Django uses the settings module pointed to by DJANGO_SETTINGS_MODULE.
    """

    def __init__(self):
        """
        Load the settings module pointed to by the environment variable. This
        is used the first time settings are needed, if the user hasn't
        configured settings manually.
        """
        settings_module = "settings"

        if find_spec(settings_module):
            mod = importlib.import_module(settings_module)

            self._explicit_settings = set()
            for setting in dir(mod):
                if setting.isupper():
                    setting_value = getattr(mod, setting)
                    setattr(self, setting, setting_value)
                    self._explicit_settings.add(setting)

    def get(self, key, default=None):
        if hasattr(self, key):
            return getattr(self, key)

        return default

    def set(self, key, value):
        self.__setattr__(key, value)

    def __setattr__(self, name, value):
        """
        Set the value of setting. Clear all cached values if _wrapped changes
        (@override_settings does this) or clear single values when set.
        """
        super().__setattr__(name, value)

    def __delattr__(self, name):
        """Delete a setting and clear it from cache if needed."""
        super().__delattr__(name)


settings = Settings()
