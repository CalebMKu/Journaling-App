import tkinter as tk
from tkinter import font

class Window:
    def __init__(self, title, size, color):
        """
        this holds all of the window initializers
        :param title: Title
        :param size: Size
        :param color: Color
        """
        self.root = tk.Tk()

        self.title = title
        self.size = size
        self.color = color

        self.title = self.root.title(self.title)
        self.size = self.root.geometry(self.size)
        self.color = self.root.configure(bg=self.color)

        self.root.resizable(False, False)

    def head(self):
        """
        this is the header you see at the top of the screen when you first open the app
        :return: None
        """
        header = tk.Label(self.root, text="PERSONAL JOURNAL", bg="lightblue", fg="blue", font="Consoles, 45")
        header.pack()

    def body(self):
        """
        this is the entry field and the save button for the persons new journal entry
        :return: None
        """
        self.entry = tk.Text(self.root, width=70, height=20, font="Consoles, 17")
        self.entry.pack()

        def save():
            """
            this saves the persons journal entry to a text file
            :return:
            """
            with open("journal.txt", "w") as my_journal:
                my_journal.write(self.entry.get("1.0", "end-1c"))

            self.root.quit()


        self.save_button = tk.Button(self.root, text="SAVE & EXIT", width=20, height=2, font="Consoles, 14", command=save)
        self.save_button.pack()

    def loop(self):
        """
        this is the tkinter loop that goes with all tkinter applications
        :return: None
        """
        self.root.mainloop()

