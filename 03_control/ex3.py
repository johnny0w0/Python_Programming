# for문

# for (int i = 0; i < 10; i++)
# for i in iterable 객체:

for i in range(5):
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5까지
for i in range(1, 6):
    print(i, end=" ")
print()

# 0 ~ 10중에 짝수 출력
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# 5 4 3 2 1 출력
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11, 1):
    tot += i
else:
    print(f"sum = {tot}")

print(sum(range(1, 11)))

s = "hi12!@한글韓契🏅"

for c in s:
    print(c, end=" ")

print(len(s))

# 구구단 출력
# 2 * 1 = 2  2 * 2 = 4  ..  2 * 9 = 18
# ..
# 9 * 1 = 9  9 * 2 = 18 ..  9 * 9 = 81

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j:<5d}", end="")
    print()
else:
    print("End")
