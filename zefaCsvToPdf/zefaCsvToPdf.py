import pandas as pd
import pdfkit
import datetime

# install and provide path of executable https://wkhtmltopdf.org/downloads.html
wkhtmltopdf_path = 'C:/Program Files/wkhtmltopdf/bin'

your_name = "Christ_Robin" #change
last_month = (datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y-%m")

csv_path = "./november.csv" #change to your file name
pdf_path = f"Monatsliste_ZEFA_{your_name}_{last_month}.pdf"
options = {    'page-size': 'A4',
    'orientation':'Landscape',
    'encoding': 'UTF-8',
    'margin-top': '8mm',
    'margin-right': '8mm',
    'margin-bottom': '8mm',
    'margin-left': '8mm'
}

df = pd.read_csv(csv_path, sep=";")

df.drop(columns=['System_ID', 'Status', 'Tätigkeit', 'Kostenstelle Buchungspunkt',
       'Debitor', 'Produkt', 'Kostenstelle Bestellung'], inplace=True)

html_table = df.to_html()

# Windows: Add wkhtmltopdf_path to windows' env variable PATH, don't pass as argument here
pdfkit.configuration()
# Linux: Pass as argument
# pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

pdfkit.from_string(html_table, pdf_path, options=options)
