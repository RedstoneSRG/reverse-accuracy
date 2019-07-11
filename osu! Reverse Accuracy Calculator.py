import PySimpleGUI as sg
import sys

# GUI setup
layout = [
    [sg.Text("Input desired accuracy and max 300s:")],
    [sg.Text('Accuracy (to nearest hundredth): '), sg.Input(size=(10, 1))],
    [sg.Text('300s: '), sg.Input(size=(10, 1))],
    [sg.Text('100s: '), sg.Input(size=(10, 1))],
    [sg.Text('50s: '), sg.Input(size=(10, 1))],
    [sg.Text('Miss: '), sg.Input(size=(10, 1))],
    [sg.OK(), sg.Exit()]
]
window = sg.Window('osu! Reverse Accuracy Calculator').Layout(layout)


def process(three):
    hundred, maximum = 0, three
    while True:
        testacc = round(((100 * hundred + 300 * three) /
                         (300 * (hundred + three))) * 100, 2)
        if testacc <= acc:
            break
        three -= 1
        hundred += 1
    if maximum > three and testacc != acc:
        three += 1
        hundred -= 1
        testacc = round(((100 * hundred + 300 * three) /
                         (300 * (hundred + three))) * 100, 2)
    sg.Popup(str(three) + "/" + str(hundred) + "/0/0" + " for " + str(acc) + "% if FC (" + str(testacc) + "%)")


while True:
    while True:
        event, (acc, threehundred, onehundred, fifty, miss) = window.Read()
        if event is None or event == "Exit":
            sys.exit()
        try:
            acc, threehundred, onehundred, fifty, miss =\
                float(acc), int(threehundred), int(onehundred), int(fifty), int(miss)
            threehundred = threehundred + onehundred + fifty + miss
            if 0 <= float(acc) <= 100:
                break
            else:
                sg.Popup("That is an invalid input.")
        except ValueError:
            sg.Popup("ERROR", "That is an invalid input.")
    process(threehundred)
