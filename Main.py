from pytube import YouTube 
import PySimpleGUI as sg

SAVE_PATH = r"Downloads/"  
link="https://www.youtube.com/watch?v=igeBnwymK5o"

yt = YouTube(link)

layout = [
    [sg.Text("YouTube Link : "), sg.InputText(link, k='-link-'), sg.Button("Check")],
    [sg.Text("Video Available : ", k='-video_title_status-', visible=False), sg.Text("", k="-video_title-", visible=False)],
    [sg.Text("Status : "), sg.Text("", k="-status-")],
    [sg.ProgressBar(100, orientation='h', s=(55,15), k='-progress_bar-')],
    [sg.Multiline(k="-log-", s=(100, 20))],
    [sg.Button("Download"), sg.Button("Exit")]
]

window = sg.Window('YouTube Downloader', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':                       
        break
    if event == "Check":
        if values["-link-"] != "":
            yt = YouTube(values["-link-"])
            window['-video_title_status-'].update(visible=True)
            window['-video_title-'].update(yt.title, visible=True)
    if event == "Download":
        if values["-link-"] != "":
            yt = YouTube(values["-link-"])
            window['-progress_bar-'].update(0)                                                     # Show 30% complete on ProgressBar
            print("Downloading", yt.title)
            window['-progress_bar-'].update(10)                                                     # Show 30% complete on ProgressBar
            window['-status-'].update("Downloading " + yt.title)
            window['-progress_bar-'].update(40)                                                     # Show 30% complete on ProgressBar
            window['-progress_bar-'].update(70)                                                     # Show 30% complete on ProgressBar
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
            window['-status-'].update("Download Complete!")                                                     # Show 30% complete on ProgressBar
            window['-link-'].update("")                                                     # Show 30% complete on ProgressBar
            window['-progress_bar-'].update(100)                                                     # Show 30% complete on ProgressBar
            window['-log-'].update(yt.title + " Downloaded Successfully")
        else:
            window['-log-'].update("Invalid Link")

    
window.close()