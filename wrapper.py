def mul(m):
  print("m = ", m)
  def wrapper(n):# 함수를 반환
    print("n = ", n)
    return m*n
  return wrapper

if __name__ == "__main__":
  mul3 = mul(3)
  mul5 = mul(5)
print("mul3 id = ", id(mul3))
print("mul5 id = ", id(mul5))
print(mul3(10))
print(mul5(10))