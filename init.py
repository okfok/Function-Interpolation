from GUI import handler
from GUI.main import app


def init():
    handler.bind_click_actions()
    handler.bind_menu()
    handler.pack()

    app.mainloop()


if __name__ == '__main__':
    init()
