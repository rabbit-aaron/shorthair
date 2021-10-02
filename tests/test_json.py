import json
from io import StringIO

from shorthair import json as shorthair_json, LookupProxy


def make_json_file(obj):
    stream = StringIO()
    stream.write(json.dumps(obj))
    stream.seek(0)
    return stream


def test_func_proxy_obj_returned():
    assert type(shorthair_json.load(make_json_file({}))) is LookupProxy
    assert type(shorthair_json.loads("{}")) is LookupProxy
