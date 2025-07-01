import tkinter as tk


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("Weather App")


if __name__ == "__main__":
    root = tk.Tk()
    mainWindow = MainWindow(master=root)

    mainWindow.mainloop()