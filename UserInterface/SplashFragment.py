import flet
from flet import (
    Page,
    colors,
    Row
)


def splashFragment(page: Page):
    return Row(
            [
                flet.Icon(flet.icons.TASK_ALT, size=100)
            ],
            alignment=flet.MainAxisAlignment.CENTER,
        )

