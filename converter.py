# GUI
import tkinter as tk
# function
from PIL import Image
import glob
import os

# tkインスタンス生成
root = tk.Tk()

# -------関数エリア-------


def btn_click(event):
    """
    ボタンクリックした時の処理
    """
    statusbar['text'] = 'converting...'
    folderPath = input_box.get()
    conv(folderPath, var_origin.get(), var_converted.get())


def conv(folderPath, o, conv) -> None:
    """
    変換処理
    """
    files = glob.glob(folderPath + f'/*.{o}')

    if len(files) == 0:
        statusbar['text'] = 'No webp files were found in the directory.'
        return

    for _ in files:
        im = Image.open(_).convert('RGB')
        rename = os.path.splitext(_)[0] + f'.{conv}'
        im.save(rename)
        os.remove(_)
    statusbar['text'] = 'complete!'


if __name__ == '__main__':

    # -------タイトルラベル-------
    root.title('image converter.exe')
    # -------画面サイズ-------
    root.geometry('500x200')

    # -------拡張子選択（オリジナル）-------
    OptionList = [
        'jpg',
        'webp',
        'png',
        'ico',
        'bmp',
        'gif',
    ]
    var_origin = tk.StringVar(root)
    var_origin.set(OptionList[0])

    lbl_orijinl = tk.Label(text=u'拡張子選択(変換前)')
    lbl_orijinl.place(x=10, y=0)
    original = tk.OptionMenu(root, var_origin, *OptionList)
    original.place(x=10, y=20)
    # -------拡張子選択（変換先）-------
    var_converted = tk.StringVar(root)
    var_converted.set(OptionList[1])

    lbl_converted = tk.Label(text=u'拡張子選択(変換後)')
    lbl_converted.place(x=150, y=0)
    converted = tk.OptionMenu(root, var_converted, *OptionList)
    converted.place(x=150, y=20)

    # -------フォルダパス-------
    lbl = tk.Label(text=u'フォルダのフルパス')
    lbl.place(x=10, y=80)
    input_box = tk.Entry(width=70)
    input_box.place(x=10, y=105)

    # -------実行ボタン-------
    btn = tk.Button(root, text="変換実行")
    btn.place(x=10, y=150)
    btn.bind('<Button-1>', btn_click)

    # -------ステータスバー設置-------
    statusbar = tk.Label(root, text="0/0")
    statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    root.mainloop()
