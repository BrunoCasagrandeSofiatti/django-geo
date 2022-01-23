from cProfile import label
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

class IndexView(TemplateView):
    template_name = 'index1.html'

class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        """Retorna 12 labens para a representação do x"""
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]

        return labels

    def get_providers(self):
        """Retorna o nomes dos datasets"""
        datasets = [
            "Programação para leigos",
            "Programação em Java",
            "Progração em python"
        ]
        return datasets
    
    def get_data(self):
        """
        Retorna os datasets para plotar o grafico

        Cada linha representa um dataset
        Cada coluna representa um label.
        """
        dados = []
        for l in range(3):
            for c in range(12):
                dado = [
                    randint(1,100),
                    randint(1,100),
                    randint(1,100),
                    randint(1,100),
                    randint(1,100),
                    randint(1,100),
                    randint(1,100),
                    randint(1,100),
                    randint(1,100),
                    randint(1,100),
                    randint(1,100),
                    randint(1,100)
                ]
            dados.append(dado)
        return dados