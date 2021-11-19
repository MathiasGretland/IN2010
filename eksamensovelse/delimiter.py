def main():
    _ = input()
    s = input()
    chars = {"[": 0, "{": 0, "(": 0}
    lastOpened = []
    closers = {"]": "[", "}": "{", ")": "("}

    for i in range(len(s)):
        c = s[i]
        if c == " ":
            continue
        if c in chars:
            chars[c] += 1
            lastOpened.append(c)
        else:
            if not lastOpened:
                print(c, i)
                return
            if closers[c] != lastOpened[-1]:
                print(c, i)
                return
            else:
                chars[closers[c]] -= 1
                lastOpened.pop()

    print("ok so far")

main()
