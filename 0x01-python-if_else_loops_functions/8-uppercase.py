
Executable File·7 lines (7 loc) · 204 Bytes
#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{0}".format(char), end="")
    print("")

