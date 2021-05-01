from kivy.app import App
from kivy.uix.gridlayout import GridLayout
class Chooser(GridLayout):
    def selected(self, filename):
        try: self.ids.image.source = filename[0]
        except: pass
class FileChooser(App):
    def __init__(self):
    	App.__init__(self)
    	self.run()
    build = lambda self: Chooser()
if __name__ == '__main__': FileChooser()