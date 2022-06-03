import GUI.click_actions as ca
from GUI import prog


def pack():
    prog.labelX.grid(row=0, column=0, sticky="ew", padx=5)
    prog.entryX.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    prog.button_add.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    prog.button_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    prog.labelY.grid(row=0, column=1, sticky="ew", padx=5)
    prog.entryY.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
    prog.button_delete.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

    prog.labelX0.grid(row=0, column=2, sticky="ew", padx=5)
    prog.entryX0.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
    prog.button_graph.grid(row=2, column=2, sticky="ew", padx=5, pady=5)

    prog.frameInput.grid(row=0, column=0, sticky="ns")
    prog.scrollbar.grid(row=1, column=0, padx=5, pady=5)
    prog.pointsListBox.grid(row=1, column=0, sticky="ew")

    prog.frameMenu.grid(row=0, column=0, sticky="ns")

    prog.labelResult.pack(padx=5, pady=10)
    prog.graph.get_tk_widget().pack()

    prog.frameOutput.grid(row=0, column=1, sticky="ns")


def bind_click_actions():
    prog.button_add.bind("<Button>", ca.add_clicked)
    prog.button_delete.bind("<Button>", ca.delete_clicked)
    prog.button_clear.bind("<Button>", ca.clear_clicked)
    prog.button_graph.bind("<Button>", ca.graph_clicked)


def bind_menu():
    prog.menu_file.add_command(label='Open', command=ca.open_clicked)
    prog.menu_file.add_command(label='Save', command=ca.save_clicked)
    prog.menu_file.add_command(label='Exit', command=ca.exit_clicked)

    prog.menu.add_cascade(label='File', menu=prog.menu_file)

    prog.menu_examples.add_command(label='Sqrt', command=ca.sqrt_example)
    prog.menu_examples.add_command(label='Quadratic', command=ca.quadratic_example)
    prog.menu_examples.add_command(label='Cubic', command=ca.cubic_example)
    prog.menu_examples.add_command(label='Sin', command=ca.sin_example)
    prog.menu_examples.add_command(label='Cos', command=ca.cos_example)
    prog.menu_examples.add_command(label='Rand', command=ca.rand_example)

    prog.menu.add_cascade(label='Examples', menu=prog.menu_examples)

    prog.window.config(menu=prog.menu)
