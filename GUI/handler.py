import GUI.click_actions as ca
import GUI.window as w


def pack():
    w.labelX.grid(row=0, column=0, sticky="ew", padx=5)
    w.entryX.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    w.button_add.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    w.button_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
    w.button_open.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

    w.labelY.grid(row=0, column=1, sticky="ew", padx=5)
    w.entryY.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
    w.button_remove.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

    w.button_save.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

    w.labelX0.grid(row=0, column=2, sticky="ew", padx=5)
    w.entryX0.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
    w.button_graph.grid(row=2, column=2, sticky="ew", padx=5, pady=5)

    w.frameInput.grid(row=0, column=0, sticky="ns")
    w.labelPoints.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    w.frameMenu.grid(row=0, column=0, sticky="ns")

    w.labelResult.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
    w.graph.grid(row=1, column=0, sticky="ew", padx=5)

    w.frameOutput.grid(row=0, column=1, sticky="ns")


def bind_click_actions():
    w.button_add.bind("<Button-1>", ca.add_clicked)
    w.button_remove.bind("<Button-1>", ca.remove_clicked)
    w.button_clear.bind("<Button-1>", ca.clear_clicked)

    w.button_graph.bind("<Button-1>", ca.graph_clicked)
