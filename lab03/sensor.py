a = float(input())
n = int(input())
d = []
d_errors = []
max_value_count = 0
for i in range(n):
    b = input()
    if b == 'error':
        d_errors.append(b)
    else:
        d.append(float(b))
        if float(b) > a: max_value_count += 1
print(len(d)+len(d_errors))
print(len(d_errors))
print(max_value_count)
print(max(d))
print(f'{(sum(d)/len(d)):.1f}')
