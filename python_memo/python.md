## enumerate()
for i, name in enumerate(<イテラブルオブジェクト>, <始めるインデックス>):

## 演算子
/ 除算
// 整数除算
** べき乗

## リストの連結
```
a_l = [0, 1, 2]
b_l = [10, 20, 30]
print(a_l + b_l)
# [0, 1, 2, 10, 20, 30]
```

## 繰り返し演算子
```
print(b_l * 3)
# [10, 20, 30, 10, 20, 30, 10, 20, 30]
```

## リスト内包表記
[式 for 任意の変数名 in イテラブルオブジェクト]

```
squares = [i**2 for i in range(5)]
print(squares)
# [0, 1, 4, 9, 16]
```

## ifで分岐したリスト内包表記
[式 for 任意の変数名 in イテラブルオブジェクト if 条件式]

```
odds = [i for i in range(10) if i % 2 == 1]
print(odds)
# [1, 3, 5, 7, 9]
```

## 三項演算子＋リスト内包表記
[真のときの値 if 条件式 else 偽のときの値 for 任意の変数名 in イテラブルオブジェクト]

```
odd_even = ['odd' if i % 2 == 1 else 'even' for i in range(10)]
print(odd_even)
# ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']
```

## リスト、タプル、辞書型、配列
[【Python】リスト型・配列型・タプル型・辞書型の違い・使い方](https://algorithm.joho.info/programming/python/list-tuple-dict-chigai/)

リスト型：要素の書き換え可能
タプル型：要素の書き換え不可
辞書型：キーで要素にアクセス
配列型(Numpy)：同じデータ型の要素のみ・長さ不変・処理が高速
集合型(sets)：重複する要素は無視、順序は保持しない
array型：指定したデータ型の要素のみ・長さ可変