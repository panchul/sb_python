# pip install pysimplegui
# pip install psutil

import PySimpleGUI as sg
import psutil

print("Opening a window using PySimpleGUI. If there is no window open, something is wrong.")

sg.theme("Dark")
mylayout = [[sg.Text('meter')], # no 'key', so just static text
        [sg.Text(size=(16,4),
                 font=('Helvetica',24),
                 justification='center',
                 key="-text-")],  # has 'key' - we can change it using update()
        [sg.Exit(button_text="Done",
                 button_color=('white',
                               'firebrick4'),
                               size=(10,1))],
          [sg.Exit(button_text="NotDone",
                   button_color=('white',
                                 'firebrick4'),
                   size=(10,1))]
        ]

mywindow = sg.Window("My window title",
                   mylayout,
                   no_titlebar=False,
                   grab_anywhere=True,
                   finalize=True)

while True:
    event, values = mywindow.read(timeout=10)
    if event in (sg.WIN_CLOSED, "Done"):
        break
    cpu_percent = psutil.cpu_percent(interval=1)
    mywindow['-text-'].update(f"cpu {cpu_percent:02.0f}%")

mywindow.close()
