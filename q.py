from pythainlp.transliterate import pronunciate as pro
from re import findall

with open("thai.txt", "r") as f:
    words = f.readlines()
prefix = {}

words.sort(key=lambda x: -len(x))
# print(words)
s = "คำ\tนับวรรค\tไม่นับวรรค\tพยัญชนะ\tสระ\tวรรณยุกต์\tการันต์\n".encode(encoding='cp874')
for i in words:
    t = i.strip().replace("...", "_")
    #do = i[:-1].isalpha()

    """for c in "โไใำปฝฟฎฏฐศสชซฤฦญฮฬ":
        if c in i:
            do = False
            break"""

    if True:
        s += f"{i[:-1]}\t{len(t)}\t{len(t) - t.count(" ")}\t{len(findall("[ก-ฮ]", i))}\t{len(findall("[ฤฦะ-ๅ็]", i))}\t{len(findall("[่-๋]", i))}\t{len(findall("์", i))}\n".encode(encoding='cp874')
        
        print(i)
    # print(sorted(words, key=lambda x: x[::-1]))
print(s[:20])

with open("l.txt", "wb") as f:
    f.write(s)
