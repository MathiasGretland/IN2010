import sys
from collections import defaultdict
account = defaultdict(lambda: 0)
account["a"] = 1
account["b"] = 2
print(account["c"])
print(account)