# prime-number.py - 제곱근을 이용한속도최적화버전
import math
print("1부터 100 사이의소수(최적화버전):")
for num in range(2, 101):
    is_prime = True
    # 제곱근까지만나누어떨어지는지확인하여연산속도대폭향상
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")