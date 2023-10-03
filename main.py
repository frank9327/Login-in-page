from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("NewLogin.kv")

class HomeScreen(Screen):
    def answer_question(self,text):
        if text.lower() == "two":
            self.manager.current = "correct"
        else:
            self.manager.current = "incorrect"


class Question1Screen(Screen):
    def answer_question(self,bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "incorrect"
    pass

class Question2Screen(Screen):
    def answer_question(self,text):
        if text.lower() == "two":
            self.manager.current = "correct"
        else:
            self.manager.current = "incorrect"

class QuizPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass


class CorrectScreen(Screen):

    cur_question = 1

    def advance(self):
        self.cur_question += 1
        self.manager.current = "question"+str(self.cur_question)

class IncorrectScreen(Screen):

    cur_question = 1

    def advance(self):
        self.cur_question += 1
        self.manager.current = "question"+str(self.cur_question)


QuizPageApp().run()
