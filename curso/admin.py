from django.contrib import admin
from .models import Modalidade, Curso, Aluno
from django.utils.html import format_html

# Register your models here.

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['nome', 'modalidade', 'vagas', 'inscritos','image_tag']

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'data_nascimento', 'curso']    
    