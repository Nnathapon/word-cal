for i in range(0x2600, 0x2700):
    print(chr(i), end=" ")
    if i % 16 == 15:
        print(hex(i))
