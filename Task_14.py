# Create a function greet(name='Guest') that prints 'Hello, <name>!'. If no name is provided, it should greet 'Guest'.
from tkinter.font import names

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alim")
greet()         
