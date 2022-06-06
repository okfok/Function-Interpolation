from GUI import gui_init
from GUI.app import app


def main():
    gui_init.bind_click_actions()
    gui_init.bind_menu()
    gui_init.pack()

    app.mainloop()


if __name__ == '__main__':
    main()
