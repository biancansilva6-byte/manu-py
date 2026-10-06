import customtkinter as ctk

app = ctk.CTk()
app.geometry("250x150")

ctk.CTkButton(app, text="Clique", command=lambda: print("OK")).pack(pady=40)

app.mainloop()