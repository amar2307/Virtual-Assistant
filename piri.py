import wx
import wikipedia
import wolframalpha
import pyttsx

engine = pyttsx.init()
engine.say("Welcome!")
engine.runAndWait()
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Piri")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello, I am Piri, your Python assistant! How can I help you?")
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

        try:
            #wolframalpha
            app_id = "EX89W4-2H9WYUHH2Q"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print(answer)
            # engine = pyttsx.init()
            # engine.say(answer)
            # engine.runAndWait()
        except:
            #wikipedia
            # input=input.split(" ")
            # input=" ".join(input[2:])
            print(wikipedia.summary(input))
            # engine = pyttsx.init()
            # engine.say("Searching for "+input)
            # engine.runAndWait()


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()