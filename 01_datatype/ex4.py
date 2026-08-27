# 문자열(str)
# "", ''

a = "python"
print(a, type(a))

print("I'll be back")
print("I'll be back")  # 역실래쉬로 대체 가능

# 여러줄 문자열
a = """
멀티라인 문자열. 
이건 여러줄 문자열임. 
코드 포함됨.
"""
print(a)


# docstring
def func():
    # 반드시 함수 1번째 줄에 doc string 작성
    """
    func() 함수에 대한 설명 작성하는 식으로 멀티라인 문자열 사용
    """
    pass


print(func.__doc__)  # doc에 함수 내에서 작성한 멀티라인 문자열이 들어감

# 문자열 연결
print("Hello" + " Python")

# 문자열 반복
print("Hello\n" * 10)
print("_" * 50)

# 문자열 연산시 주의사항
# print("Hello" + 3)
print("Hello" + str(3))

print("10" + "2")
print(int("10") + int("2"))

# 문자열 포맷팅 (f-string)
name = "pororo"
age = 23

print(f"이름: {name}, 나이: {age}")
print(f"내년 나이: {age + 1}살")
print(f"{name.upper()}")

pi = 3.141592

print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")

print(f"{num:15,d}")
print(f"{num:<15,d}")

print(f"{num:015,d}")
print(f"{num:<015,d}")
