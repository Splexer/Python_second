import json, pyaudio, os
from vosk import Model, KaldiRecognizer

model = Model("E:/Programming/VOSK_Speech/vosk-model-small-ru-0.22")  # Загружаем модель для русского языка
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()

Stream = p.open(format= pyaudio.paInt16, channels=1, rate = 16000, input=True,frames_per_buffer=8000)
Stream.start_stream()

def listen():
    while True:

        data = Stream.read(4000, exception_on_overflow=False)
        if(rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']
for text in listen():
    if text == "сценарий":
        os.startfile('E:\\Creative\\text\\A_Scenario\\Content_warning.docx')
    print(text)
# def on_key_press(event):
#     print(event.name)
#
# keyboard.on_press(on_key_press)
#
# keyboard.wait('esc')  # Ждем нажатия клавиши Esc для завершения программыususwwwwwwwww