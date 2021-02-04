from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html

from toys.services.send_email_salary import send_email
from .models import *

@admin.register(Toy)
class ToyAdmin(ModelAdmin):
    list_display = ( 'name', 'user', 'description')
    search_fields =('name',)
    list_display_links = None
    #list_editable = ('description',)
    autocomplete_fields = ('user',)


    def get_list_display(self, request):
        ld = ['name', 'user', 'description']
        if request.user.is_superuser:
            ld += ['created_at']
        return ld

class UserToysInline(admin.TabularInline):
    model = Toy

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('firstname', 'lastname', 'email','phone', 'age')
    search_fields = ('firstname', 'lastname')
    list_display_links = ('firstname','lastname')
    readonly_fields = ('password_change_link',)
    #exclude = ('age',)
    #fields = ('firstname', 'lastname', 'email','phone', 'age')
    fieldsets = (('Asosiy ma\'lumotlar',{
        'fields':(('firstname', 'lastname'),'email'),
        'classes':('wide',),
    }),
    ('Qo\'shimcha ma\'lumotlatr',{
        'fields':('phone','age',),
        'description':'Kiritilishi majburiy emas!',
    })
                 )
    inlines = [UserToysInline]

    def password_change_link(self,obj):
        return format_html('<a href="/admin/toys/user/{0}/password/">Change password</a>'.format(obj.pk))

@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'description')
#    list_editable = ('name','description',)
    search_fields = ('^name',)
    empty_value_display = '---'




@admin.register(Addres)
class AdresAdmin(ModelAdmin):
    fields = (('street', 'city'), 'zip_code', 'country')
    list_display = ('street', 'city', 'zip_code', 'country')
    readonly_fields = ('zip_code',)
    search_fields = ('city', 'country')

class EmployeInline(admin.StackedInline):
    model = Employee



@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    list_display = ('name',)
    inlines = [EmployeInline,]
    actions = ('send_email_salary_report',)

    def send_email_salary_report(self,request, query):
        send_email()
        self.message_user(request,'Message yuborildi.')
    send_email_salary_report.short_description = 'send_email_salary_report'









