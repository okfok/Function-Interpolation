from GUI import handler
from GUI import prog


def init():
    handler.bind_click_actions()
    handler.bind_menu()
    handler.pack()

    prog.window.mainloop()


if __name__ == '__main__':
    init()
