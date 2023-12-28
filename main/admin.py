from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from . import models

@admin.register(models.User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('bio','phone_number','foto',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(models.Mexmonxona)
admin.site.register(models.Room)
admin.site.register(models.Stol)
admin.site.register(models.Tarixiy_joylar)
admin.site.register(models.Konferentsiya_markazi)
admin.site.register(models.Shifoxona)
admin.site.register(models.Avtoturargoh)
admin.site.register(models.Turar_joy)
admin.site.register(models.Dokon)
admin.site.register(models.Restoranlar)
admin.site.register(models.CategoryLocation)
admin.site.register(models.SubCategoryLocation)
admin.site.register(models.Changi_uchun_maydon)
admin.site.register(models.Address)
admin.site.register(models.Bolalar_clubi)
admin.site.register(models.Texnik_spetsifikatsiyalar)
admin.site.register(models.Dam_olish_maskani)
admin.site.register(models.Yetkazib_berish)
admin.site.register(models.Ovqat_zakas)
admin.site.register(models.Kutqaruv_tibiy_xizmat)
admin.site.register(models.Operator)
admin.site.register(models.Git)
