# 挿入ソート
def insert_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]         #挿入データを一時的に記録
        j = i - 1
        while (j >= 0) and (data[j] > tmp):   #挿入データがソート済みデータ内のデータよりも小さく右にある
            data[j + 1] = data[j]       #右へ1つデータを移す
            j -= 1
        data[j + 1] = tmp     #上の操作で移動を終えた所に一時的に記録していた挿入データを代入

    return data

if __name__ == '__main__':
    DATA = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

    sorted_data = insert_sort(DATA.copy())

    print(f"{DATA} → {sorted_data}")