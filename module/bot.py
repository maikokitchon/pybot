import sys
sys.path.append('..')
from lib import glibCheckerLib

def reload():
    print("[DEBUG] Bot::reload")
    glibCheckerLib()
    return f"This is a reply from bot::reload."

def test_parameter(args):
    print("[DEBUG] Bot::test_parameter")
    print(args)
    return f"This is a reply from bot::test_parameter."