from django.contrib import admin

# Register your models here.
from django.contrib import admin

from django.contrib import admin
from .models import   Categorys, お菓子UZAWA, お菓子FUKUCHI, お菓子, 半生お菓子, チーズ, 洋日配, 飲料, お酒



admin.site.register(Categorys)

class お菓子UZAWAAdmin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 
                 ]
    list_display = ('商品名','category','賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    list_editable = ['category']
    search_fields = ['商品名']
    ordering = ('dis_date',)
admin.site.register(お菓子UZAWA, お菓子UZAWAAdmin)

class お菓子FUKUCHIAdmin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 ]
    list_display = ('商品名','category','賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    search_fields = ['商品名']
    list_editable = ['category']
    ordering = ('dis_date',)
admin.site.register(お菓子FUKUCHI, お菓子FUKUCHIAdmin)

class お菓子Admin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 ]
    list_display = ('商品名','category', '賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    search_fields = ['商品名']
    list_editable = ['category']
    ordering = ('dis_date',)
admin.site.register(お菓子, お菓子Admin)

class 半生お菓子Admin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 ]
    list_display = ('商品名','category','賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    search_fields = ['商品名']
    list_editable = ['category']
    ordering = ('dis_date',)
admin.site.register(半生お菓子, 半生お菓子Admin)

class 洋日配Admin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 ]
    list_display = ('商品名','category','賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    search_fields = ['商品名']
    list_editable = ['category']
    ordering = ('dis_date',)
admin.site.register(洋日配, 洋日配Admin)

class チーズAdmin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 ]
    list_display = ('商品名','category','賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    search_fields = ['商品名']
    list_editable = ['category']
    ordering = ('dis_date',)
admin.site.register(チーズ, チーズAdmin)


class 飲料Admin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 ]
    list_display = ('商品名','category','賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    search_fields = ['商品名']
    list_editable = ['category']
    ordering = ('dis_date',)
admin.site.register(飲料, 飲料Admin)

class お酒Admin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 ]
    list_display = ('商品名','category','賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    search_fields = ['商品名']
    list_editable = ['category']
    ordering = ('dis_date',)
admin.site.register(お酒, お酒Admin)
