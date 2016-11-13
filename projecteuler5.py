"""2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

Answer: 232,792,560
"""

answer = []
num = 1
while len(answer) < 1:
    for j in range(1, 21):
        if num % j != 0:
            num += 1
            break
        else:
            if j == 20:
                answer.append((num, j))

print answer


