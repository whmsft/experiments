import tkinter as tk
root = tk.Tk()

representatives = "+-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def toggle(chara):
    if btns[chara].cget('bg') == 'white':
        btns[chara].config(bg="black", fg="white")
    else: btns[chara].config(bg="white", fg="black")

def re():
    for btn in btns:
        btns[btn].config(bg="white", fg="black")

def push():
    flush = ""
    for btn in btns:
        if btns[btn]["bg"] == "black":
            flush = flush+btns[btn]["text"]
    print(flush)

btns = {}
idx = -1
row = 0
for char in representatives:
    idx = idx+1
    if idx %8 == 0: row = row+1
    exec("btns[char] = tk.Button(root, text = char,bg='white',command = lambda:toggle('"+char+"'), width=5, height=2)")
    btns[char].grid(column = idx%8, row=row)

re = tk.Button(root, text="re", command=re)
re.grid(row =row+1, column=0)

push = tk.Button(root, text="ph", command=push)
push.grid(row=row+1, column=1)

root.mainloop()

