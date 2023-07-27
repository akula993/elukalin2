from fpdf import FPDF
import flet as ft
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)


class LableElukalinA4(FPDF):
    def header(self):
        # Добавляем текст в определенные места на странице
        self.set_font('helvetica', size=14)
        self.set_xy(20, 20)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(0, 7,
                        'LLC «Grafo Impex»\nKovrovy micro-district, 37/3\nTownship Kotelniki\n140054 Moscow region\nRUSSISCHE FÖDERATION',
                        align="L")

    def footer(self):
        # Добавляем номер страницы внизу каждой страницы
        self.set_y(-10)
        self.set_font('helvetica', 'B', 20)
        self.set_text_color(255, 255, 255)
        self.cell(0, 0, "Made in Germany", align="C")

    def add_content(self, charge, nettogewicht, versanddatum, number):
        # Добавляем текст в определенные места на странице
        self.set_font('helvetica', 'B', 16)
        self.set_xy(20, 85)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Charge:', align="L")
        self.set_xy(70, 85)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{charge}', align="L")
        self.set_xy(20, 93)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Nettogewicht:', align="L")
        self.set_xy(70, 93)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{nettogewicht}', align="L")
        self.set_xy(20, 101)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Versanddatum:', align="L")
        self.set_xy(70, 101)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{versanddatum}', align="L")
        self.set_font('helvetica', 'B', 65)
        self.set_xy(20, 124)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{number}', align="L")

    def top_right(self):
        # Добавляем картинки справа на странице
        self.set_xy(170, 20)  # Устанавливаем текущую позицию (x=50, y=100)
        self.image('ic.png', h=24)
        self.set_font('helvetica', 'B', 16)
        self.set_xy(170, 50)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(0, 5, 'SPEZIAL-KLEBSTOFF FABRIK GMBH', align="L")
        self.set_line_width(1)
        self.set_draw_color(165)
        self.line(x1=170, y1=60, x2=265, y2=60)

        self.set_font('helvetica', size=14)
        self.set_xy(175, 65)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(0, 7,
                        'Ernst-Abbe-Str. 10\n52249 Eschwieler\nTelefon +49 (0) 2403-6450-0\nTelefon +49 (0) 2403-6450-26\nEmail eukalin@eukalin.de\nwww.eukalin.de',
                        align="L")
        self.line(x1=170, y1=60, x2=170, y2=105)
        self.set_xy(205, 85)  # Устанавливаем текущую позицию (x=50, y=100)
        self.image('ring.png', w=73, )

    def end_right(self):
        # Добавляем картинки справа на этикетке 1
        self.add_font(fname='font/DejaVuSansCondensed.ttf')
        self.set_font('DejaVuSansCondensed', size=9)

        self.set_xy(170, 160)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(190, 3,
                        'EUH208 Содержит reaction mass of: 5-chloro-2-methyl-4-isothiazolin-\n'
                        '3-one EC no. 247-500-7 and 2-methyi-2H-isothiazol-3-one\n'
                        'EC no. 220-239-6 (3:1), Polyethylene lmine. Может вызвать аллергическую\n'
                        'реакцию, EUH210 Карта безопасности/паспорт безопасности\n'
                        'можно получить по требованию',
                        align="L")

    def contour(self):
        self.set_line_width(20)
        self.set_draw_color(150)
        self.set_draw_color(165)
        self.line(x1=15, y1=200, x2=282, y2=200)
        self.rect(1, 1, 295, 205, style="D")


class LableElukalinA5(FPDF):
    def header(self):
        # Добавляем текст в определенные места на этикетке 1
        self.set_font('helvetica', size=12)
        self.set_xy(15, 15)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(0, 7,
                        'LLC «Grafo Impex»\nKovrovy micro-district, 37/3\nTownship Kotelniki\n140054 Moscow region\nRUSSISCHE FÖDERATION',
                        align="L")

        # Добавляем текст в определенные места на этикетке 2
        self.set_font('helvetica', size=12)
        self.set_xy(15, 165)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(0, 7,
                        'LLC «Grafo Impex»\nKovrovy micro-district, 37/3\nTownship Kotelniki\n140054 Moscow region\nRUSSISCHE FÖDERATION',
                        align="L")

    def footer(self):
        # Добавляем номер страницы внизу этикетки 1
        self.set_y(141)
        self.set_font('helvetica', 'B', 15)
        self.set_text_color(255, 255, 255)
        self.cell(0, 0, "Made in Germany", align="C")
        # Добавляем номер страницы внизу этикетки 2
        self.set_y(293)
        self.set_font('helvetica', 'B', 15)
        self.set_text_color(255, 255, 255)
        self.cell(0, 0, "Made in Germany", align="C")

    def add_content(self, charge, nettogewicht, versanddatum, number):
        # Добавляем текст в определенные места на этикетке 1
        self.set_font('helvetica', 'B', 10)
        self.set_xy(15, 65)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Charge:', align="L")
        self.set_xy(45, 65)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{charge}', align="L")
        self.set_xy(15, 70)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Nettogewicht:', align="L")
        self.set_xy(45, 70)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{nettogewicht}', align="L")
        self.set_xy(15, 75)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Versanddatum:', align="L")
        self.set_xy(45, 75)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{versanddatum}', align="L")
        self.set_font('helvetica', 'B', 40)
        self.set_xy(15, 90)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{number}', align="L")

        # Добавляем текст в определенные места на этикетке 2
        self.set_font('helvetica', 'B', 10)
        self.set_xy(15, 215)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Charge:', align="L")
        self.set_xy(45, 215)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{charge}', align="L")
        self.set_xy(15, 220)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Nettogewicht:', align="L")
        self.set_xy(45, 220)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{nettogewicht}', align="L")
        self.set_xy(15, 225)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, 'Versanddatum:', align="L")
        self.set_xy(45, 225)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{versanddatum}', align="L")
        self.set_font('helvetica', 'B', 40)
        self.set_xy(15, 240)  # Устанавливаем текущую позицию (x=50, y=100)
        self.cell(0, 1, f'{number}', align="L")

    def top_right(self):
        # Добавляем картинки справа на этикетке 1
        self.set_xy(122, 15)  # Устанавливаем текущую позицию (x=50, y=100)
        self.image('ic.png', h=18)
        self.set_font('helvetica', 'B', 12)
        self.set_xy(121, 35)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(0, 5, 'SPEZIAL-KLEBSTOFF FABRIK GMBH', align="L")
        self.set_line_width(1)
        self.set_draw_color(165)
        self.line(x1=122, y1=42, x2=202, y2=42)
        self.set_font('helvetica', size=10)
        self.set_xy(125, 45)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(0, 5,
                        'Ernst-Abbe-Str. 10\n52249 Eschwieler\nTelefon +49 (0) 2403-6450-0\nTelefon +49 (0) 2403-6450-26\nEmail eukalin@eukalin.de\nwww.eukalin.de',
                        align="L")
        self.line(x1=122, y1=42, x2=122, y2=75)
        self.set_xy(145, 60)  # Устанавливаем текущую позицию (x=50, y=100)
        self.image('ring.png', w=50, )

        # Добавляем картинки справа на этикетке 2
        self.set_xy(122, 165)  # Устанавливаем текущую позицию (x=50, y=100)
        self.image('ic.png', h=18)
        self.set_font('helvetica', 'B', 12)
        self.set_xy(121, 185)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(0, 5, 'SPEZIAL-KLEBSTOFF FABRIK GMBH', align="L")
        self.set_line_width(1)
        self.set_draw_color(165)
        self.line(x1=122, y1=192, x2=202, y2=192)
        self.set_font('helvetica', size=10)
        self.set_xy(125, 195)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(0, 5,
                        'Ernst-Abbe-Str. 10\n52249 Eschwieler\nTelefon +49 (0) 2403-6450-0\nTelefon +49 (0) 2403-6450-26\nEmail eukalin@eukalin.de\nwww.eukalin.de',
                        align="L")
        self.line(x1=122, y1=192, x2=122, y2=225)
        self.set_xy(145, 210)  # Устанавливаем текущую позицию (x=50, y=100)
        self.image('ring.png', w=50, )

    def end_right(self):
        # Добавляем картинки справа на этикетке 1

        # self.set_font('helvetica', 'B', 6)
        self.add_font(fname='font/DejaVuSansCondensed.ttf')
        self.set_font('DejaVuSansCondensed', size=6)
        self.set_xy(125, 105)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(90, 3,
                        'EUH208 Содержит reaction mass of: 5-chloro-2-methyl-4-isothiazolin-\n'
                        '3-one EC no. 247-500-7 and 2-methyi-2H-isothiazol-3-one\n'
                        'EC no. 220-239-6 (3:1), Polyethylene lmine. Может вызвать аллергическую\n'
                        'реакцию, EUH210 Карта безопасности/паспорт безопасности\n'
                        'можно получить по требованию',
                        align="L")
        # pdf.add_font(fname='font/DejaVuSansCondensed.ttf')
        # pdf.set_font('DejaVuSansCondensed', size=6)
        self.set_xy(125, 260)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(90, 3,
                        'EUH208 Содержит reaction mass of: 5-chloro-2-methyl-4-isothiazolin-\n'
                        '3-one EC no. 247-500-7 and 2-methyi-2H-isothiazol-3-one\n'
                        'EC no. 220-239-6 (3:1), Polyethylene lmine. Может вызвать аллергическую\n'
                        'реакцию, EUH210 Карта безопасности/паспорт безопасности\n'
                        'можно получить по требованию',
                        align="L")

    def contour(self):
        # Контур этикетки 1
        self.set_line_width(10)
        self.set_draw_color(150)
        self.set_draw_color(165)
        # self.line(x1=15, y1=193, x2=282, y2=193)
        # self.line(x1=15, y1=197, x2=282, y2=197)
        self.rect(1, 1, 210, 140, style="D")

        # Контур этикетки 2
        self.set_line_width(10)
        self.set_draw_color(150)
        self.set_draw_color(165)
        self.rect(1, 152, 210, 140, style="D")


def main(page: ft.Page):
    page.title = 'Этикетка ELUKALIN'  # Название
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    # Размер окна
    page.window_width = 400  # ширина окна равна 200 пикселям
    page.window_height = 700  # высота окна равна 200 пикселям
    page.window_resizable = False  # размер окна не поддается изменению

    page.update()
    # Добавление картинки
    img = ft.Image(src=f'ic.png', fit=ft.ImageFit.CONTAIN)
    page.add(img)
    img2 = ft.Image(src=f'DoubleV.jpg', fit=ft.ImageFit.CONTAIN)

    # Open directory dialog
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled!"
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()
    # скрыть все диалоговые окна в overlay
    page.overlay.extend([get_directory_dialog, ])

    open_path = Row([ElevatedButton("Куда сохранить", icon=icons.FOLDER_OPEN,
                                    on_click=lambda _: get_directory_dialog.get_directory_path(), disabled=page.web, ),
                     directory_path, ])

    def button_a4():
        # Создаем экземпляр класса PDF
        pdf = LableElukalinA4(orientation='L')  # Устанавливаем альбомную ориентацию (L - landscape)
        pdf.add_page()
        pdf.top_right()
        pdf.end_right()
        # Добавляем содержимое и картинки
        pdf.contour()
        pdf.add_content(charge.value, nettogewicht.value, versanddatum.value, number.value)
        # Сохраняем PDF-файл
        pdf.output(f'{directory_path.value}\{str(number.value)}.pdf')
        page.update()

    def button_a5():
        # Создаем экземпляр класса PDF
        pdf = LableElukalinA5()  # Устанавливаем альбомную ориентацию (L - landscape)
        pdf.add_page()
        pdf.top_right()
        pdf.end_right()
        # Добавляем содержимое и картинки
        pdf.contour()
        pdf.add_content(charge.value, nettogewicht.value, versanddatum.value, number.value)
        # Сохраняем PDF-файл
        pdf.output(f'{directory_path.value}\{str(number.value)}.pdf')
        page.update()

    def button_event(e):
        if dd.value == 'A4':
            t.value = f"Выбран размер {dd.value}"
            button_a4()
        else:
            t.value = f"Выбран размер {dd.value}"
            button_a5()
        page.update()

    t = ft.Text()

    dd = ft.Dropdown(options=[ft.dropdown.Option("A4"), ft.dropdown.Option("A5")], )

    charge = ft.TextField(label="Введите номер партии", hint_text="номер партии")
    nettogewicht = ft.TextField(label="Введите вес нетто", hint_text="вес нетто")
    versanddatum = ft.TextField(label="Введите дату отгрузки", hint_text="дату отгрузки")
    number = ft.TextField(label="Введите номер", hint_text="номер")
    b = ft.ElevatedButton(text="Создать", on_click=button_event)
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    print(open_path)

    page.add(dd, t, charge, nettogewicht, versanddatum, number, file_picker, open_path, b, img2)


ft.app(target=main)
