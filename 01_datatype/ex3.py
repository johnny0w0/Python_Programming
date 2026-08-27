# 불리언(bool)

a = True
print(a, type(a))

print(2 < 3)
print(2 > 3)
print(2 == 3)
print(2 != 3)

print("apple" > "banana")  # 사전 순. b가 뒤에 있으므로 더 큼
# \n print("뽀로로" > "크롱")

# bool()
print(bool(3))
print(bool(0))
print(bool("hello"))
print(bool(""))  # 비어있음
print(bool([10]))
print(bool([]))

# None 자료형
a = None  # 아직 값이 정해지지 않은 자료형
print(a, type(a))
print(bool(a))

if a is None:
    print("값이 없습니다.")
