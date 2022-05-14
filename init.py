from GUI import handler
from GUI import window as w


def init():
    handler.bind_click_actions()
    handler.bind_menu()
    handler.pack()

    w.window.mainloop()


if __name__ == '__main__':
    init()
