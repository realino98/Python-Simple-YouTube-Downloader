from pytube import YouTube 
import PySimpleGUI as sg

SAVE_PATH = r"Downloads/"  
link="https://www.youtube.com/watch?v=igeBnwymK5o"

yt = YouTube(link)

layout = [
    [sg.Text("Insert Link : "), sg.InputText(link)],
    [sg.ProgressBar(100, orientation='h', s=(10,20), k='-PBAR-')],
    [sg.Text("Status : "), sg.Text("", k="-status-")],
    [sg.Button("Download"), sg.Button("Exit")],
    [sg.Multiline(s=(15,2), k="-log-"), ]
]

window = sg.Window('YouTube Downloader', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Download":
        if event[0] != "":
            window['-PBAR-'].update(0)                                                     # Show 30% complete on ProgressBar
            print("Downloading", yt.title)
            window['-PBAR-'].update(10)                                                     # Show 30% complete on ProgressBar
            window['-status-'].update("Downloading " + yt.title)
            yt = YouTube(link)
            window['-PBAR-'].update(40)                                                     # Show 30% complete on ProgressBar
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH + yt.title + ".mp4")
            window['-PBAR-'].update(70)                                                     # Show 30% complete on ProgressBar
            window['-status-'].update("Download Complete!")                                                     # Show 30% complete on ProgressBar
            window['-PBAR-'].update(100)                                                     # Show 30% complete on ProgressBar
            print(yt.title, "Downloaded")
            window['-log-'].update(yt.title + " Downloaded Successfully")
    
window.close()