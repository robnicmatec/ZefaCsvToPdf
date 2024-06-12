import pandas as pd
import pdfkit
from pathlib import Path

# install and provide path of executable https://wkhtmltopdf.org/downloads.html
wkhtmltopdf_path = '/usr/bin/wkhtmltopdf'
csv_path = "./mai.csv"
pdf_path = f"{Path(csv_path).stem}.pdf"
options = {    'page-size': 'A4',
    'orientation':'Landscape',
    'encoding': 'UTF-8',
    'margin-top': '8mm',
    'margin-right': '8mm',
    'margin-bottom': '8mm',
    'margin-left': '8mm'
}

df = pd.read_csv(csv_path, sep=";")

df.drop(columns=['System_ID', 'Status', 'Tätigkeitsbeschreibung', 'Kostenstelle Buchungspunkt',
       'Debitor', 'Produkt', 'Kostenstelle Bestellung'], inplace=True)

html_table = df.to_html()

pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
pdfkit.from_string(html_table, pdf_path, options=options)

