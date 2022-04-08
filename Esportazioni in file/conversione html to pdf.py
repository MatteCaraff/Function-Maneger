##  importo libbrerie e funzioni che mi servono ##
import pdfkit                          #esportazione in file html e in file pdf

config = pdfkit.configuration(wkhtmltopdf = r"D:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")   #dove è installata wkhtmltopdf

pdfkit.from_file('exp.html', 'example.pdf', configuration = config) #converto il file presente nella path stessa del codice con quel nome in un pdf con quel nome