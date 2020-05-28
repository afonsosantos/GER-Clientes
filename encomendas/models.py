#  Copyright 2020 Afonso Santos
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from django.db import models

from clientes.models import Cliente, MetodoPagamento


class EstadoEncomenda(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Estado de Encomenda'
        verbose_name_plural = 'Estados de Encomendas'

    def __str__(self):
        return self.descricao


class Encomenda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    conteudo = models.TextField(verbose_name='Conteúdo')
    valor = models.FloatField(verbose_name='Valor (em Euros)')
    data_hora = models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora')
    metodo_pagamento = models.ForeignKey(MetodoPagamento, on_delete=models.SET_NULL, null=True,
                                         verbose_name='Método de Pagamento')
    estado = models.ForeignKey('EstadoEncomenda', on_delete=models.SET_NULL, null=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Encomenda'
        verbose_name_plural = 'Encomendas'

    def __str__(self):
        return f"Encomenda de {self.cliente.nome} em {self.data_hora} - {self.estado}"
