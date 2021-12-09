m, n, a = map(int, input().split())

if m % a != 0:
    m = m//a + 1
else:
    m = m//a

if n % a != 0:
    n = n//a + 1
else:
    n = n//a

print(m*n)