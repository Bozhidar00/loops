destination = input()
limit = 20
total = 0

while total < limit:
    amount = int(input())
    total += amount
    if total >= limit:
        print(f"Going to {destination}")
        break
