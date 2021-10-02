import json

from shorthair.proxy import LookupProxy

__all__ = ["ProxyDecoder", "load", "loads"]


class ProxyDecoder(json.JSONDecoder):
    def decode(self, *args, **kwargs):
        ret = super().decode(*args, **kwargs)
        return LookupProxy(ret)


def _adapt_func(func):
    def wrapped(*args, **kwargs):
        func.__doc__ = (
            f"function `json.{func.__name__}` "
            f"with the `cls` argument set to `ProxyDecoder`"
        )
        kwargs["cls"] = kwargs.get("cls", ProxyDecoder)
        return func(*args, **kwargs)

    return wrapped


load = _adapt_func(json.load)
loads = _adapt_func(json.loads)
