import functions as fn
import PySimpleGUI as sg
import time

clock = sg.Text('', key='clock')
label = sg.Text("Enter a TODO")
input_text = sg.InputText(tooltip="Enter todo",
                          key='todo')
add_butt = sg.Button('add', size=10)

list_box = sg.Listbox(values=fn.get_todo()
                      , enable_events=True,
                      key='todos', size=[45, 10])
edit_but = sg.Button('edit', size=10)
complete_but = sg.Button('complete', size=10)
exit_but = sg.Button('exit', size=7)
sg.theme('LightBlue5')
window = sg.Window("my todo-list",
                   layout=[[clock],
                           [label],
                           [input_text, add_butt],
                           [list_box, edit_but, complete_but],
                           [exit_but]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))

    match event:
        case 'add':
            todos = fn.get_todo()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fn.write_todo(todos)
            window['todos'].update(values=todos)
        case 'edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = fn.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                fn.write_todo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select a todo first.', font=('Helvetica', 12))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'complete':
            try:
                todos = fn.get_todo()
                index = todos.index(values['todos'][0])
                todos.pop(index)
                fn.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select a todo first.', font=('Helvetica', 12))

        case 'exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
