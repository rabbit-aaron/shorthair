from typing import Type


class LookupProxyMeta(type):
    def __init__(self: Type["LookupProxy"], *args, **kwargs):
        super().__init__(*args, **kwargs)

        # keep a singleton proxy object for when KeyError
        self.NONE = self(obj=None)


class LookupProxy(metaclass=LookupProxyMeta):
    NONE: "LookupProxy"  # = LookupProxy(obj=None)

    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, key):
        try:
            if isinstance(self.obj, (dict, tuple, list)):
                return self.__class__(self.obj[key])
        except LookupError:
            pass
        return self.NONE

    def __call__(self, *args, **kwargs):
        return self.value

    @property
    def value(self):
        return self.obj
