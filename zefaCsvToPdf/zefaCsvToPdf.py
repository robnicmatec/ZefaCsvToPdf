import pandas as pd
import pdfkit
import datetime

# install and provide path of executable https://wkhtmltopdf.org/downloads.html
wkhtmltopdf_path = 'C:/Program Files/wkhtmltopdf/bin'

your_name = "Christ_Robin" #change
this_month = (datetime.date.today().replace(day=1)).strftime("%Y-%m")
last_month = (datetime.date.today().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y-%m")

csv_path = "./juni.csv" #change to your file name
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

def make_delta(entry):
    h, m = entry.split(':')
    return datetime.timedelta(hours=int(h), minutes=int(m))
def td_to_str(td):
    hours, remainder = divmod(td.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{int(hours):02}:{int(minutes):02}'

deltas = td_to_str(df["Std"].map(lambda entry: make_delta(entry)).sum(min_count=1))

print(deltas)
df.loc[-1] = ["Summe:", f"{deltas}", "", "", "", "", "", ""]
df.index = df.index + 1  # shifting index
df = df.sort_index()


html_table = df.to_html()

# Windows: Add wkhtmltopdf_path to windows' env variable PATH, don't pass as argument here
pdfkit.configuration()
# Linux: Pass as argument
# pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

pdfkit.from_string(html_table, pdf_path, options=options)


