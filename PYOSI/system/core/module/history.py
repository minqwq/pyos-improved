def write():
    tmp_f = open("../data/cache/history.txt", "w+", encoding="utf-8")
    tmp_f.write("\n" + input)
    tmp_f.close()
def clear():
    tmp_f2 = open("../data/cache/history.txt", "w", encoding="utf-8")
    tmp_f2.write("")
    tmp_f2.close
