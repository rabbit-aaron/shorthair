from shorthair import LookupProxy


def test_same_proxy_object_is_returned_when_key_error():
    assert LookupProxy({})["a"]["b"] is LookupProxy({})["b"]["a"]


def test_resolves_to_none_when_key_error():
    proxy = LookupProxy({})
    assert proxy["a"]["b"].value is None
    assert LookupProxy({})["a"]["b"]() is None

    assert LookupProxy({"a": []})["a"][0]() is None


def test_resolves_to_correct_value_when_key_exists():
    proxy = LookupProxy({"a": {"b": {"c": [0, 1, 2]}}})
    assert proxy["a"]["b"]["c"][0]() == 0
    assert proxy["a"]["b"]["c"][1]() == 1
    assert proxy["a"]["b"]["c"][2]() == 2
