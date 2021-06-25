import sys, os
sys.path.append('..')
from lib import check_if_glib_works

def reload(args):
    print("[DEBUG] Bot::reload")
    check_if_glib_works()
    return f"This is a reply from bot::reload."

def test_parameter(args):
    print("[DEBUG] Bot::test_parameter")
    print(args)
    return f"This is a reply from bot::test_parameter."