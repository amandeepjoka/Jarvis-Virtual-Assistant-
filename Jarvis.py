import wx
import wikipedia
import wolframalpha
from gtts import gTTS
import os
import speech_recognition as sr

tts = gTTS(text='Hello Sir! Jarvis at your service', lang='en')
tts.save("good.mp3")
os.system("good.mp3")
os.remove("good.mp3")
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Jarvis")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello Sir! How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        if input == '':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
                input = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        try:
            #wolframalpha
            app_id = "Your Wolframalpha app id goes here."
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print answer
            tts = gTTS(text="It turns out to be"+answer, lang='en')
            tts.save("g.mp3")
            os.system("g.mp3")
        except:
            #wikipedia
            input1 = input
            tts = gTTS(text="Ok, Let me find about"+input, lang='en')
            tts.save("m.mp3")
            os.system("m.mp3")
            input = input.split(' ')
            input = " ".join(input[2:])
            if input:
                tts = gTTS(text=wikipedia.summary(input), lang='en')
                tts.save("k.mp3")
                os.system("k.mp3")
                print wikipedia.summary(input)
            else :
                tts = gTTS(text=wikipedia.summary(input1), lang='en')
                tts.save("k.mp3")
                os.system("k.mp3")
                print wikipedia.summary(input1)

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
