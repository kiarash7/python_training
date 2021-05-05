digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(digits))
windows_size = 3
loops = windows_size - 1
for i in range(len(digits) - loops):
    print(digits[i:i+windows_size])
