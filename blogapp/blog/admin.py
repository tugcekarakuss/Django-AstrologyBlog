from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe #html etiketlerini yazı olarak görmesin diye yaptık

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug","selected_categories") # admin sayfasında title,active ve anasayfada mı gibi özellikelri detaya girmeden görebilmek için yapıldı
    list_editable = ("is_active","is_home",) # admin sayfasında editlenmek istenen özellikleri yazdık
    search_fields = ("title","description",) #admin panelinde arama barı ekler ve hangi özellikler içerisinde aranması gerektiğini ister.
    readonly_fields = ("slug",) #sadece okunabilir yapmak için.
    list_filter = ("is_active","is_home","categories",)
    
    def selected_categories(self, obj):
        html = "<ul>"
        
        for category in obj.categories.filter():
            html += "<li>" + category.name + "</li> " 
        
        html += "</ul>"
        return mark_safe(html)
    
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)