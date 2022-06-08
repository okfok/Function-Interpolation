from GUI import gui_init
from GUI.app import app


def main():
    gui_init.pack()
    gui_init.bind_menu()
    gui_init.bind_click_actions()

    app.mainloop()


if __name__ == '__main__':
    main()
