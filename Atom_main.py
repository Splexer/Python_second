import json, pyaudio, os, time, keyboard
from vosk import Model, KaldiRecognizer
from time import time

listening: bool = False  # Состояние прослушивания, False - прослушивание не происходит в данный момент

model = Model("E:/Programming/VOSK_Speech/vosk-model-small-ru-0.22")  # Загружаем модель для русского языка
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()

Stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=16000)
Stream.start_stream()

print('Конец выполнения основного кода')


def listen():
    global listening
    listening = True
    print('мы зашли в функцию')
    start_time = time()
    one_frame_time = start_time + 6
    while start_time < one_frame_time:
        start_time = time()

        data = Stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']
    listening = False


def check():
    for text in listen():
        print(text)
        if text == "сценарий":
            os.startfile('E:\\Creative\\text\\A_Scenario\\Content_warning.docx')

        if text == "сайт":
            url = 'https://www.youtube.com'
            os.system(f'start {url}')


def on_key_press(event):
    global listening, processing_key_press
    if event.name == 'pause' and not listening:
        check()



if listening is False:
    keyboard.on_press(on_key_press)
    keyboard.wait('esc')  # Ждем нажатия клавиши Esc для завершения