from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # Set the Header
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
    #pdf.line(10, 20, 200, 20)
    for inc in range(20, 300, 10):
        pdf.line(10, inc, 200, inc)


    #Set the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='R', ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align='R', ln=1)
        # or j in pdf.:

        for inc in range(10, 300, 10):
            pdf.line(10, inc, 200, inc)

pdf.output("output.pdf")
