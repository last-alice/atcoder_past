snk = input()

snk = snk.replace("1", "a").replace("9", "b")
print(int(snk.replace("a", "9").replace("b", "1")))