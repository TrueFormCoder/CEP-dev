from scripts.check_schema_compatibility import is_compatible

def test_compat_same_version():
    assert is_compatible("v2.1.1","v2.1.1") is True
