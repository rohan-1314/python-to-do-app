import functions
import PySimpleGUI as sg

label = sg.Text("Enter a TODO")
input_text = sg.InputText(tooltip="Enter todo")
add_butt = sg.Button('add')
window = sg.Window("my todo-list", layout=[[label], [input_text, add_butt]])
window.read()
window.close()