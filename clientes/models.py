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

from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django_countries.fields import CountryField


# Validação de campos
def validar_data_nascimento(data):
    hoje = date.today()
    idade = hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day))
    if idade < 18:
        raise ValidationError('O cliente não pode ser menor de idade.')


class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(max_length=150, verbose_name='Email')
    telefone = models.CharField(max_length=13, verbose_name='Telefone')
    data_nascimento = models.DateField(validators=[validar_data_nascimento], verbose_name='Data de Nascimento')
    cartao_cidadao = models.CharField(max_length=15, blank=True, verbose_name='Cartão de Cidadão')
    morada = models.CharField(max_length=200, verbose_name='Morada (Rua, Avenida, ...)')
    codigo_postal = models.CharField(max_length=8, verbose_name='Código-Postal')
    localidade = models.CharField(max_length=50, verbose_name='Localidade')
    pais = CountryField(blank_label='Selecionar um país...')
    metodo_pagamento = models.ForeignKey('MetodoPagamento', on_delete=models.SET_NULL, null=True,
                                         verbose_name='Método de Pagamento')
    perfil_facebook = models.CharField(max_length=100, blank=True, verbose_name='Perfil no Facebook')
    numero_parceiro = models.CharField(max_length=15, blank=True, verbose_name='Número de Parceiro')
    registado_em = models.DateTimeField(auto_now_add=True, verbose_name='Registado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-registado_em']

    def __str__(self):
        return self.nome


class MetodoPagamento(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Método de Pagamento'
        verbose_name_plural = 'Métodos de Pagamento'
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


class ChamadaTelefonica(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, verbose_name='Cliente')
    data = models.DateField(verbose_name='Data')
    hora = models.TimeField(verbose_name='Hora')
    motivo = models.ForeignKey('MotivoChamadaTelefonica', on_delete=models.CASCADE, verbose_name='Motivo')
    observacoes = models.TextField(verbose_name='Observações')

    class Meta:
        verbose_name = 'Chamada Telefónica'
        verbose_name_plural = 'Chamadas Telefónicas'
        ordering = ['-data']

    def __str__(self):
        return f"Chamada para {self.cliente.nome} em {self.data} às {self.hora}"


class MotivoChamadaTelefonica(models.Model):
    descricao = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Motivo de Chamada Telefónica'
        verbose_name_plural = 'Motivos de Chamadas Telefónicas'
        ordering = ['-descricao']

    def __str__(self):
        return self.descricao
