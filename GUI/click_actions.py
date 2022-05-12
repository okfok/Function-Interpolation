from tkinter.filedialog import askopenfilename, asksaveasfilename

import Core
import window as w


def display_input_points():
    w.labelPoints['text'] = str(Core.interp)


def add_clicked(event):
    x = float(w.entryX.get())
    y = float(w.entryY.get())
    Core.interp.add_point(Core.Point(x, y))
    display_input_points()


def remove_clicked(event):
    x = float(w.entryX.get())
    y = float(w.entryY.get())
    Core.interp.remove_point(Core.Point(x, y))
    display_input_points()


def clear_clicked(event):
    Core.interp.clear_points()
    display_input_points()


def open_file():
    """Открываем файл для редактирования"""
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Простой текстовый редактор - {filepath}")


def save_file():
    """Сохраняем текущий файл как новый файл."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Простой текстовый редактор - {filepath}")