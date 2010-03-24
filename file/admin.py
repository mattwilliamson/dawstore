from django.contrib import admin
from file.models import Account, File

class FileInline(admin.TabularInline):
	model = File

class FileAdmin(admin.ModelAdmin):
	list_display = ('name', 'added_date', 'key',)

class AccountAdmin(admin.ModelAdmin):
	inlines = (FileInline,)
	list_display = ('name', 'public_key')

admin.site.register(Account, AccountAdmin)
admin.site.register(File, FileAdmin)
