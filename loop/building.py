floors = int(input())
apartments = int(input())

for i in range(floors, 0, -1):
    print()
    for j in range(0, apartments):
        if i % 2 == 1 and i > 1:
            print(f"A{i}{j}", end=" ")
        elif i % 2 == 0 and i > 1:
            print(f"O{i}{j}", end=" ")
        elif i == 1:
            print(f"L{i}{j}", end=" ")

