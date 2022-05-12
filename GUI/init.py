import handler
import window as w


def init():
    handler.pack()
    handler.bind_click_actions()

    w.window.mainloop()


if __name__ == '__main__':
    init()
