from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("LoginPage.kv")




class Question1Screen(Screen):
    def answer_question(self,bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "incorrect"
    pass

class Question2Screen(Screen):
    def answer_question(self,bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "error"
    pass

class QuizPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass

class CorrectScreen(Screen):
    def advance(self):
        self.manager.current = "Question 2"
    pass

class IncorrectScreen(Screen):
    pass


QuizPageApp().run()
