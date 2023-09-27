from flet import *


class LoginFragment(UserControl):
    def __int__(self):
        super(LoginFragment, self).__init__()
        self.email = TextField(label="email")
        self.password = TextField(label="password")

    def build(self):
        return Container(
                content=Column([
                    Text("Email"),
                    TextField(
                        label="Email",
                        border_color="white",
                        color="white",
                        text_align=TextAlign.CENTER
                    ),
                    Text("Password"),
                    TextField(
                        label="Password",
                        border_color="white",
                        color="white",
                    ),
                ])
        )

