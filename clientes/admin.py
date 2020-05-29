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

from django.contrib import admin

from encomendas.models import *
from .models import *

# Configurações


admin.site.site_header = 'GER-Clientes'
admin.site.site_title = 'GER-Clientes'
admin.site.index_title = 'Administração do GER-Clientes'


# Inline's


class ChamadasInline(admin.TabularInline):
    model = ChamadaTelefonica


class EncomendasInline(admin.StackedInline):
    model = Encomenda


# Páginas da administração


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [
        ChamadasInline,
        EncomendasInline,
    ]
    fieldsets = (
        ('Dados Pessoais', {
            'classes': ('wide',),
            'fields': ('nome', 'email', 'telefone', 'data_nascimento', 'cartao_cidadao', 'metodo_pagamento', 'numero_parceiro')
        }),
        ('Morada', {
            'classes': ('wide',),
            'fields': ('morada', 'codigo_postal', 'localidade', 'pais'),
        }),
        ('Redes Sociais', {
            'classes': ('collapse',),
            'fields': ('perfil_facebook',),
        })
    )
    list_display = ('nome', 'email', 'telefone', 'numero_parceiro')
    list_filter = ('metodo_pagamento',)
    list_per_page = 30
    list_select_related = True


@admin.register(ChamadaTelefonica)
class ChamadaTelefonicaAdmin(admin.ModelAdmin):
    fields = ('cliente', 'data', 'hora', 'motivo', 'observacoes')
    list_display = ('cliente', 'data', 'hora')
    list_filter = ('motivo',)
    list_per_page = 30
    list_select_related = True


admin.site.register(MetodoPagamento)
admin.site.register(MotivoChamadaTelefonica)
