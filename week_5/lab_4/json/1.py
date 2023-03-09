import json


with open("D:\PP2-1\week_5\lab_4\json/file1.json", "r") as read_file:
    data = json.load(read_file)

print("""Interface Status
================================================================================""")
print("""DN                                             Description          Speed                      MTU """)
for i, k in data["imdata"][0]["l1PhysIf"]["attributes"].items():
    if i == 'DN':
        print(k, end="                          ")
    if i == 'Speed':
        print(k, end="                                         ")
    if i == 'MTU':
        print(k, end="                   ")