import tkinter as tk
from PIL import Image, ImageTk

class LoginPage(tk.Frame):
	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings

		super().__init__(parent)
		self.configure(bg="black")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, width=self.settings.width, height=self.settings.height, bg="black")
		self.main_frame.pack(expand=True)

		self.label_username = tk.Label(self.main_frame, text="Username", anchor="w" ,font=("Arial", 18, "bold"), bg="black", fg="white")
		self.label_username.pack(fill="both")

		self.var_username = tk.StringVar()
		self.entry_username = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), textvariable=self.var_username)
		self.entry_username.pack(fill="x")

		self.label_password = tk.Label(self.main_frame, text="Password", anchor="w",font=("Arial", 18, "bold"), bg="black", fg="white")
		self.label_password.pack(fill="both")

		self.var_password = tk.StringVar()
		self.entry_password = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), show="*", textvariable=self.var_password)
		self.entry_password.pack(fill="x")

		self.btn_login = tk.Button(self.main_frame, text="LOGIN", font=("Arial", 18, "bold"), command=lambda:self.app.auth_login())
		self.btn_login.pack(pady=5)

