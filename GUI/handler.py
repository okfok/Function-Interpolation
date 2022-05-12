import tkinter as tk

import click_actions as ca
import window as w


def pack():
    w.labelX.pack()
    w.entryX.pack()
    w.labelY.pack()
    w.entryY.pack()

    w.frameX.pack(side=tk.LEFT)
    w.frameY.pack(side=tk.LEFT)

    w.frameCord.pack(side=tk.TOP)

    w.button_add.pack(side=tk.LEFT)
    w.button_remove.pack(side=tk.LEFT)
    w.button_clear.pack(side=tk.LEFT)

    w.labelPoints.pack(side=tk.BOTTOM)

    w.frameCordMenu.pack(side=tk.TOP)
    w.framePoints.pack(side=tk.BOTTOM)

    w.button_open.pack(side=tk.LEFT)
    w.button_save.pack(side=tk.LEFT)

    w.frameInput.pack(side=tk.LEFT)

    w.mainframe.pack()


def bind_click_actions():
    w.button_add.bind("<Button-1>", ca.add_clicked)
    w.button_remove.bind("<Button-1>", ca.remove_clicked)
    w.button_clear.bind("<Button-1>", ca.clear_clicked)
