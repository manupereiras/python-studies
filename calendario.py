from fpdf import FPDF

# Classe personalizada para o calendário
class PDFCalendar(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 102, 204)
        self.cell(0, 10, 'Paróquia São José Esposo de Maria', align='C', ln=True)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Escala do Mês de Janeiro - 2025', align='C', ln=True)
        self.ln(10)

    def add_calendar(self):
        # Dias da semana
        days = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
        
        # Configuração do espaço de cada célula
        cell_width = 35
        cell_height = 15

        # Título da tabela
        self.set_font('Arial', 'B', 12)
        for day in days:
            self.cell(cell_width, cell_height, day, border=1, align='C')
        self.ln(cell_height)

        # Dados do calendário (dia e escala)
        calendar_data = {
            1: '19:30h - Milena',
            2: '19:30h - Carol',
            3: '19:30h - Valdo',
            7: '19:30h - Kinha',
            8: '19:30h - Carol',
            9: '19:30h - Valdo',
            10: '19:30h - Milena',
            14: '19:30h - Kinha',
            15: '19:30h - Valdo',
            16: '19:30h - Milena',
            17: '19:30h - Carol',
            21: '19:30h - Kinha',
            22: '19:30h - S. Rita',
            23: '19:30h - Valdo',
            24: '19:30h - Milena',
            28: '19:30h - Kinha',
            29: '19:30h - Valdo',
            30: '19:30h - Milena',
            31: '19:30h - Carol'
        }

        # Ajuste inicial para o primeiro dia do mês (1ª quarta-feira de janeiro de 2025)
        start_day = 3  # Quarta-feira (0 = Domingo, 1 = Segunda, ..., 6 = Sábado)

        # Preenchimento do calendário
        day = 1
        max_days = 31

        for week in range(6):  # 6 semanas no mês (no máximo)
            for weekday in range(7):
                if week == 0 and weekday < start_day:
                    # Espaços em branco antes do início do mês
                    self.cell(cell_width, cell_height, '', border=1)
                elif day > max_days:
                    # Espaços em branco após o fim do mês
                    self.cell(cell_width, cell_height, '', border=1)
                else:
                    # Dia do calendário
                    if day in calendar_data:
                        self.set_font('Arial', 'B', 10)
                        self.cell(cell_width, cell_height / 2, str(day), border='LTR', align='C')
                        self.set_font('Arial', '', 9)
                        self.cell(cell_width, cell_height / 2, calendar_data[day], border='LBR', align='C', ln=True)
                    else:
                        self.cell(cell_width, cell_height, str(day), border=1, align='C')
                    day += 1

            self.ln(cell_height)

# Gerar o PDF
pdf = PDFCalendar()
pdf.add_page()
pdf.add_calendar()
pdf.output("Calendario_Janeiro_2025.pdf")

print("Calendário criado com sucesso!")
