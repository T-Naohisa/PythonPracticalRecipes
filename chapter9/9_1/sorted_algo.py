from operator import itemgetter


seq = [5, 1, 2, 3]
print(seq)
print(sorted(seq, reverse=True))
# 戻り値はNoneになるので、実行の結果はリスト表示されない
print(seq.sort(reverse=True))
print(seq)
data = [(1, 40, 200), (3, 10, 300), (2, 20, 300), (1, 30, 300)]
print(sorted(data))
# index2の項目でソートする
print(sorted(data, key=itemgetter(2)))
# index2の項目でソートする同じ場合はindex0の値でソートする
print(sorted(data, key=itemgetter(2, 0)))

dic = {"a": 2, "c": 1, "b": 3}
print(sorted(dic.items(), key=itemgetter(1)))
