import random
import time
import tkinter as tk
from tkinter import ttk
import csv
import pprint

onde_b = "ロンド B スクエア"
biz_ud = "BIZ UDゴシック"

window_size_horizontal = 1024
window_size_vertical = 768
title_main_str = "闇鍋★ショートストーリー"

# CSVファイルを開く
with open(r'D:\30programming\py3\SecretPot.csv', encoding="utf-8") as f:
    reader = csv.reader(f)

    # 行を取得
    l = [row for row in reader]
    print(l)

    # 0番目の行を削除
    l.remove(l[0])
    print(l)

    # 列を取得
    l_T = [list(x) for x in zip(*l)]
    print(l_T)

    # 0番目の列を削除
    l_T.remove(l_T[0])
    print(l_T)

# 各リストへ変換
member = l_T[0]
member_num = len(member)
when = l_T[1]
where = l_T[2]
who = l_T[3]
what = l_T[4]


# GUIの設定
root = tk.Tk()
root.title(title_main_str)
root.geometry(f"{window_size_horizontal}x{window_size_vertical}")

# Textウィジェットの作成
text_widget = tk.Text(root, font=(biz_ud, 16), wrap=tk.WORD)
text_widget.pack(pady=20)

# ランダムな抽選
def RandomChoose():
    global member, when, who, where, what

    selected_member = random.choice(member)
    member.remove(selected_member)

    selected_when = random.choice(when)
    when.remove(selected_when)

    selected_where = random.choice(where)
    where.remove(selected_where)

    selected_who = random.choice(who)
    who.remove(selected_who)

    selected_what = random.choice(what)
    what.remove(selected_what)

    return selected_member, selected_when, selected_who, selected_where, selected_what

def Display(index=0):
    if index < member_num:
        selected_member, selected_when, selected_who, selected_where, selected_what = RandomChoose()

        text = f"{selected_member}："
        text_widget.insert(tk.END, text)
        root.update()
        time.sleep(2)

        text = f"{selected_when}"
        text_widget.insert(tk.END, text)
        root.update()
        time.sleep(2)

        text = f"{selected_where}"
        text_widget.insert(tk.END, text)
        root.update()
        time.sleep(2)
        
        text = f"{selected_who}"
        text_widget.insert(tk.END, text)
        root.update()
        time.sleep(2)        

        text = f"{selected_what}\n"
        text_widget.insert(tk.END, text)
        root.update()
        time.sleep(2)

        root.after(10000, Display, index + 1)  # 0ミリ秒後に次のテキストを表示
    else:
        text_widget.insert(tk.END, "抽選終了\n")

# 最初のテキスト表示をトリガー
Display()

# GUIを表示
root.mainloop()

