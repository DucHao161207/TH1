a1, b1, c1, a2, b2, a3 = map(float, input().split())
average = (a1 + b1 + c1 + (a2 + b2) * 2 + a3 * 3) / 10
print(f"{average:.1f}")