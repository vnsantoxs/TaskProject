import flet as ft
from UserInterface.Authentication import RegisterFrafment, LoginFragment, RecoverFragment


def main(page: ft.Page):
    page.title = "Task app"
    page.window_width = 360
    page.window_height = 640
    register = RegisterFrafment.RegisterFragment()
    login = LoginFragment.LoginFragment()
    recorver = RecoverFragment.RecoverFragment()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Login", font_family="monospace"), bgcolor=ft.colors.SURFACE_VARIANT),
                    login,
                    ft.Row([
                        ft.ElevatedButton("Login", bgcolor=ft.colors.GREY_50, color=ft.colors.BLACK),
                        ft.TextButton("Register", on_click=lambda _: page.go("/register")),
                    ]),
                    ft.Row([
                        ft.TextButton("Recorver", on_click=lambda _: page.go("/recorver"))
                    ]),
                ],
            )
        )
        if page.route == "/register":
            page.views.append(
                ft.View(
                    "/register",
                    [
                        ft.AppBar(title=ft.Text("Register", font_family="monospace"), bgcolor=ft.colors.SURFACE_VARIANT),
                        register,
                        ft.Row([
                            ft.ElevatedButton("Register", bgcolor=ft.colors.GREY_50, color=ft.colors.BLACK,
                                              on_click=lambda _: page.go("/")),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                    ],
                )
            )
        if page.route == "/recorver":
            page.views.append(
                ft.View(
                    "/recorver",
                    [
                        ft.AppBar(title=ft.Text("Recorver"), bgcolor=ft.colors.SURFACE_VARIANT),
                        recorver,
                        ft.Row([
                            ft.ElevatedButton("Recorver", bgcolor=ft.colors.GREY_50, color=ft.colors.BLACK,
                                              on_click=lambda _: page.go("/")),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                    ],
                )
            )
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main)
