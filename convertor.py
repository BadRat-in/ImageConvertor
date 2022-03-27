import tkinter as tk
from tkinter import ttk, messagebox, filedialog, messagebox
from PIL import ImageTk, Image
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import os



class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Convertor")
        self.geometry("450x650")
        # self.iconbitmap("icon.ico")
        self.configure(bg="#333333")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.create_widgets()

    def create_widgets(self):
        self.optins = [
            "PNG",
            "JPG",
            "GIF",
            "ICO",
            "WEBP",
            ]
        self.comboVariable = tk.StringVar()
        self.comboVariable.set(self.optins[0])
        self.label_1 = tk.Label(self, text="Convertor", font=("Arial", 20), bg="#333333", fg="#ffffff")
        self.label_1.place(x=150, y=10)
        self.label_2 = tk.Label(self, text="Select image file", font=("Arial", 10), bg="#333333", fg="#ffffff")
        self.label_2.place(x=10, y=70)
        self.filepicker = tk.Button(self, text="Browse", command=self.file_picker, bg="#cccccc", fg="#000000")
        self.filepicker.place(x=120, y=65)
        self.label_5 = tk.Label(self, text="To", font=("Arial", 10), bg="#333333", fg="#ffffff").place(x=200, y=70)
        self.combo = ttk.Combobox(self, values=self.optins, textvariable=self.comboVariable, state="readonly", background="#333333", foreground="#ffffff").place(x=225, y=70)
        self.label_4 = tk.Label(self, width=400, height=400 , bg="#222222").place(x=0, y=130)
        self.ConverButton = tk.Button(self, text="Convert", bg="#fafafa", command=self.convert)
        self.ConverButton.place(x=30, y=600)
        self.ExitButton = tk.Button(self, text="Exit", command=self.on_closing, bg="#555", fg="#fafafa")
        self.ExitButton.place(x=350, y=600)
    def file_picker(self):
        self.filename = filedialog.askopenfilename(title="Select image file", filetypes=(("Image files", "*.png *.jpg *.jpeg *.ico *.webp *.gif"), ("All files", "*.*")))
        if self.filename:
            temp = self.filename.split(".")[::-1]
            if temp[0] == "jpg" or temp[0] == "jpeg" or temp[0] == "png" or temp[0] == "gif" or temp[0] == "ico" or temp[0] == "webp":
                self.label_3 = tk.Label(self, text="", font=("Arial", 10), bg="#333333", fg="#ffffff")
                self.label_3.place(x=10, y=100)
                self.label_3.config(text=f"{self.filename} selected")
                temp = self.filename.split(".")[::-1]
                if temp[0] == "pdf":
                    self.PhotoImage = ImageTk.PhotoImage(Image.open("./pdf.jpg").resize((450, 450)))
                else:
                    self.PhotoImage = ImageTk.PhotoImage(Image.open(self.filename).resize((450, 450)))
                self.label_4 = tk.Label(self, image=self.PhotoImage, bg="#aaaaaa", width=450, height=450).place(x=0, y=130)
            else:
                messagebox.showerror("Error", "Please select a valid image file")
        else:
            messagebox.showerror("Error", "No file selected")

    def convert(self):
        if self.comboVariable.get() or self.comboVariable.get() != "":
            type = self.comboVariable.get()
        else:
            messagebox.showerror("Error", "Conversion type not selected")

        if self.filename:
            try:
                temp = self.filename.split(".")[::-1]
                # if temp[0] == "pdf":
                #     temp = temp[1].split("/")
                #     path = ""
                #     for i in range(len(temp) -1):
                #         path += temp[i] + "/"
                #     print(path)
                #     if os.path.isdir(f"{path}Pdf2Image") == False:
                #         folderName = f"{path}Pdf2Image"
                #         os.mkdir(folderName)
                #     images = convert_from_path(self.filename)
                #     print(images)
                #     temp = self.filename.split(".")[0: -1]
                #     # for i, image in enumerate(images):
                #     #     image.save(f"{temp[0]}-{i}.{type.lower()}", type)
                if temp[0] == "jpg" or temp[0] == "jpeg" or temp[0] == "png" or temp[0] == "gif" or temp[0] == "ico" or temp[0] == "webp":
                    self.image = Image.open(self.filename)
                    self.temp = self.filename.split(".")[0: -1]
                    self.name = self.temp[0] + "Converted." + type.lower()
                    if type == "JPG":
                        self.image.save(self.name, "JPEG")
                    else:
                        self.image.save(self.name, type)
                    self.label_3.config(text="")
                    self.label_3.config(text=f"{self.name} saved")
                    messagebox.showinfo("Success", "Image converted")
                else:
                    messagebox.showerror("Error", "Please select a valid image file")
            except Exception:
                messagebox.showerror("Error", "Something went wrong")
                raise PDFInfoNotInstalledError
        else:
            messagebox.showerror("Error", "No file selected")



    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


if __name__ == "__main__":
    window = Window()
    window.mainloop()