from django.contrib import admin
from myadmin.models import Notice
# Register your models here.
admin.site.site_header = 'NLJ NOTICES'
admin.site.index_title = 'CSE : 2024'

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id','subject','description','created_at','updated_at']
    search_fields =['subject','description','updated_at']

admin.site.register(Notice,NoticeAdmin)