a = int(input())
bonus = 0

if a < 100:
    bonus = 5
elif a > 100:
    bonus = 0.2 * a
elif a > 1000:
    bonus = 0.1 * a
if a / 2:
    bonus = bonus + 1
elif a / 5:
    bonus = bonus + 2

print(bonus)
print(a + bonus)
