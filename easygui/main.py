import easygui as eg

def greet(app):
    name = app.get_data("name_field")
    app.msg(f"Hello, {name}!")

# Define the UI Blueprint
with eg.args(title="My First App", theme="Dark") as bp:
    bp.add("label", "Welcome to easygui-tk", font=("Arial", 16, "bold"))
    bp.add_spacer(10)
    
    bp.add("label", "Enter your name:")
    bp.add("inputbox", id="name_field")
    
    bp.add("button", "Say Hello", command=greet)

# Launch the Window
mw = eg.window(bp)
mw()