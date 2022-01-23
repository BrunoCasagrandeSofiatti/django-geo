import io
from django.http import FileResponse, response
from django.views.generic import View
from reportlab.pdfgen import canvas

# imports do WeasyPrint
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

class IndexView(View):

    def get(self, request, *args, **kwargs):
        # Cria um arquivo para receber os dados e gerar o PDF
        buffer = io.BytesIO()

        # Cria o arquivo pdf
        pdf = canvas.Canvas(buffer)

        # Insere coisas no pdf
        pdf.drawString(100, 100, 'Bruno Sofiatti')

        # quando acabamos de inserir coisa no pdf
        pdf.showPage()
        pdf.save()

        # retornamos o buffer para o inicio do arquivo
        buffer.seek(0)

        # abre o arquivo direto no navegador
        return FileResponse(buffer, filename='relatorio.pdf')
        
        # faz o download do arquivo
        #return FileResponse(buffer, as_attachment=True, filename='arquivo.pdf')

class Index2View(View):

    def get(self, request, *args, **kwargs):
        texto = ['Geek University', 'Bruno', 'Outra Coisa', 'mais uma coisa']

        html_string = render_to_string('relatorio.html', {'texto': texto})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/relatorio2.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio2.pdf') as pdf:
            
            response = HttpResponse(pdf, content_type='application/pdf')
            # faz o download do arquivo
            #response['Content-Disposition'] = 'attachment; filename="relatorio2.pdf"'

            # abre direto no navegador
            response['Content-Disposition'] = 'inline; filename="relatorio2.pdf"'
        return response
