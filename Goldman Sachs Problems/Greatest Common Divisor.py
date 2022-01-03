def gcdOfStrings(str1: str, str2: str) -> str:
    l = [""]

    if (len(str1) < len(str2)):
        for j in range(0, len(str1) + 1):
            req = str1[0:j]
            copy2 = str2.replace(req, '')
            copy1 = str1.replace(req, '')
            if len(copy1) == 0 and len(copy2) == 0:
                l.append(req)
    else:
        for j in range(0, len(str2) + 1):
            req = str2[0:j]
            copy2 = str2.replace(req, '')
            copy1 = str1.replace(req, '')
            if len(copy1) == 0 and len(copy2) == 0:
                l.append(req)
    return l[-1]

i0=input()
i1=input()
print(gcdOfStrings(i0,i1))
