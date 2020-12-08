from random import randint
with open("bitstr.txt", mode="w") as f:
    for i in range(64):
        f.write(f"({i:2}, -1): {randint(0, 2**64-1)}\n")
        f.write(f"({i:2},  1): {randint(0, 2**64-1)}\n")
print("finish!")