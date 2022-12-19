import functions as fn
import PySimpleGUI as sg

label = sg.Text("Enter a TODO")
input_text = sg.InputText(tooltip="Enter todo",
                          key='todo')
add_butt = sg.Button('add')
window = sg.Window("my todo-list",
                   layout=[[label],
                           [input_text, add_butt]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'add':
            todos = fn.get_todo()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fn.write_todo(todos)
        case sg.WIN_CLOSED:
            break

window.close()