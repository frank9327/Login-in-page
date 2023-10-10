from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("NewLogin.kv")

users= {"bob":"bobpass","billy":"billypass","himothy":"himpass"}

class HomeScreen(Screen):
    def Screen_choice(self,bool):
        if bool:
            self.manager.current = "Create"
        else:
            self.manager.current = "Login"

class CreateScreen(Screen):
    def enter_new_login(self, username,password,newpassword):
        special = "~!@#$%^&*()_+-="
        has_special = False
        numbers = "1234567890"
        has_numbers = False
        has_capital = False
        has_lowercase = False
        for i in password.text:
            if i in special:
                has_special = True
            if i in numbers:
                has_numbers = True
            if i.capitalize() == i:
                has_capital = True
            if i.lower() == i:
                has_lowercase = True
        if (username.text not in users) and (
                password.text == newpassword.text) and has_special and has_numbers and has_capital and has_lowercase and (len(password.text) > 7):
            users[username.text] = password.text
            self.manager.current = "home"
        else:
            self.ids.enter.color = (1,0,0,1)
    def back(self):
        self.manager.current = "Login"


class LoginScreen(Screen):
    def enter_login(self, username,password):
            if username in users and users[username]==password:
                self.manager.current = "NewHome"
            else:
                self.manager.current = "Create"
    def back(self):
        self.manager.current = "home"

class NewHome(Screen):
    def back(self):
        self.manager.current = "home"


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
