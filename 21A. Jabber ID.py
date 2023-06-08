import re

def is_jabber_id(s):
    pattern = r'^[A-Za-z0-9_]{1,16}@[A-Za-z0-9_]{1,16}(\.[A-Za-z0-9_]{1,16}){0,31}(/[A-Za-z0-9_]{1,16})?$'
    return re.match(pattern, s) is not None

# Read the input
jabber_id = input().strip()

# Check if the Jabber ID is valid
if is_jabber_id(jabber_id):
    print('YES')
else:
    print('NO')