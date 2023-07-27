from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Добавляем текст в определенные места на странице
        self.set_font('helvetica', size=14)
        self.set_xy(20, 20)  # Устанавливаем текущую позицию (x=50, y=100)
        self.multi_cell(0, 7,
                        # 'LLC «Grafo Impex» \nulitsa Masterkova, dom 4, etage 2, \npomesheniye I, office 102 \n115280 Moscow \nRUSSISCHE FÖDERATION',
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


# Создаем экземпляр класса PDF
pdf = PDF(orientation='L')  # Устанавливаем альбомную ориентацию (L - landscape)
pdf.add_page()
pdf.top_right()
pdf.end_right()
# Добавляем содержимое и картинки
pdf.contour()
pdf.add_content('0000382622', '31 kg', '05.07.2023', '6462 VL', )
# Сохраняем PDF-файл
pdf.output('a4_output.pdf')
