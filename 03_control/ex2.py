# 반복문 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    if i == 5:
        break
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
i = 0

while i < len(nums):
    if nums[i] == target:
        print(f"{target}을 찾았다!")
        break
    i += 1
else:
    print(f"{target}을 못찾음")

# 1 ~ 10까지의 합
# sum = 55
i = 1
tot = 0

while i < 10:
    tot += i
    i += 1

print(f"1부터 {i}까지의 합: {tot}")

tot, i = 0, 0

# 1 ~ 10까지 짝수의 합
while i < 10:
    i += 1
    if i % 2 == 1:
        continue
    tot += i

print(f"1부터 {i}까지 짝수의 합: {tot}")
