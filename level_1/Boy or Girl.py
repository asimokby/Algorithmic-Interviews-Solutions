def solve():
    s = list(input().strip())
    
    if len(set(s)) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


solve()
