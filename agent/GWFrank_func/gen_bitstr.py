from random import randint
import json

bit_strs = dict()
for i in range(64):
    bit_strs[f"-1{i}"] = randint(0, 2**64-1)
    bit_strs[f"1{i}"] = randint(0, 2**64-1)

jdata = json.dumps(bit_strs)
with open('bitstr.json', 'w') as f:
    f.write(jdata)
