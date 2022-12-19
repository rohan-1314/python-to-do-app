import functions as fn
import PySimpleGUI as sg

label = sg.Text("Enter a TODO")
input_text = sg.InputText(tooltip="Enter todo",
                          key='todo')
add_butt = sg.Button('add')

list_box = sg.Listbox(values=fn.get_todo()
                      , enable_events=True,
                      key='todos', size=[45, 10])
edit_but = sg.Button('edit')
complete_but = sg.Button('complete')
exit_but = sg.Button('exit')
window = sg.Window("my todo-list",
                   layout=[[label],
                           [input_text, add_butt],
                           [list_box, edit_but, complete_but],
                           [exit_but]],
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
            window['todos'].update(values=todos)
        case 'edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'
            todos = fn.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            fn.write_todo(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'complete':
            todos = fn.get_todo()
            index = todos.index(values['todos'][0])
            todos.pop(index)
            fn.write_todo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
