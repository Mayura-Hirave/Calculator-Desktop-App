import tkinter
import tkinter.messagebox  # Access to standard Tk dialog boxes.
# https://docs.python.org/3/library/tkinter.messagebox.html

import sys
import os


class Calculator:
    def __init__(self):
        self.__main_window = tkinter.Tk()
        self.__main_window.title("Calculator")
        self.__main_window.geometry("350x525")
        self.__main_window.minsize(350, 525)  # width, height
        self.__main_window.maxsize(1500, 525)  # width, height

        os.chdir(sys._MEIPASS)  # remove this line- while running this code in IDE
        self.__main_window.wm_iconbitmap("icon.ico")

        self.__expression = tkinter.StringVar()
        self.__textarea = tkinter.Entry(self.__main_window, textvariable=self.__expression, font="lucida 40 bold")
        self.__textarea.pack(fill=tkinter.X, padx=10, pady=10, ipadx=8)

        frame = tkinter.Frame(self.__main_window)
        numbers = (("7", "8", "9", "+"), ("4", "5", "6", "-"), ("1", "2", "3", "*"), ("C", "0", ".", "/"))
        num_frame = tkinter.Frame(frame)
        for nums in numbers:
            button_frame = tkinter.Frame(num_frame)
            for num in nums:
                self.__create_button(button_frame, num)
            button_frame.pack()
        num_frame.pack()
        frame.pack(padx=10)

        button = tkinter.Button(self.__main_window, text="=", font="lucida 20 bold", bg="red")
        button.bind(sequence="<Button-1>", func=lambda event: self.__click(event))
        button.pack(fill=tkinter.X, pady=5)

    def __click(self, event):
        # event -> object of <ButtonPress event num=1 x=50 y=50>
        # event.widget => .!frame.!button3
        text = event.widget.cget("text")
        if text == "=":
            ans = self.__expression.get()
            if not self.__expression.\
                    get().isdigit():
                try:
                    ans = eval(self.__expression.get())
                except Exception as e:
                    print(e)
                    tkinter.messagebox.showerror("Error", "Invalid Expression")
                    ans = ""
            self.__expression.set(ans)
        elif text == "C":
            self.__expression.set("")
        else:
            self.__expression.set(self.__expression.get() + text)
        self.__textarea.update()

    def __create_button(self, root, text):
        button = tkinter.Button(root, text=text, font="lucida 20 bold", padx=20, pady=20)
        button.bind(sequence="<Button-1>", func=lambda event: self.__click(event))
        button.pack(side=tkinter.LEFT)

    def run(self):
        self.__main_window.mainloop()


if __name__ == '__main__':
    app = Calculator()
    app.run()