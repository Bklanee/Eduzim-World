# любое целое число в **5 оканчивается на это же число
# начинать циклы можно с прошлого значения цикла
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                abcd = a**5 + b**5 + c**5 + d**5
                e = int(abcd ** (1 / 5))
                if abcd == e**5:
                    print(a + b + c + d + e)
