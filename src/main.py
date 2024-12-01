import flet as ft


def main(page: ft.Page):
    page.title = "Adventcalendar"
    page.adaptive = True
    buttons = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
    ]
    for row in buttons:
        row_controls = []
        btn = ft.Column(controls=[ft.Text(row)], expand=1)
        row_controls.append(btn)
        page.add(
            ft.SafeArea(
                ft.Row(
                    controls=row_controls,
                    expand=1,
                )
            )
        )


ft.app(main)
