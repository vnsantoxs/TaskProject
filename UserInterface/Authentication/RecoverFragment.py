from flet import *


class RecoverFragment(UserControl):
    def __int__(self):
        super(RecoverFragment, self).__init__()
        self.email = TextField(label="email")

    def build(self):
        return Container(
                content=Column([
                    Text("Email"),
                    TextField(
                        label="Email",
                        border_color="white",
                        color="white"
                    ),
                ])
        )
