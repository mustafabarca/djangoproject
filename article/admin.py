from django.contrib import admin

# Register your models here.
''' 3 numaralı açıklama'''
from .models import Article

@admin.register(Article) # artık admin panelinde Article modelimiz görünecek.
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title", "author", "created_date"] # article lsitesinde başlık, yazar ve created_date lerin görünmesini sağlar.
    list_display_links = ["title","author", "created_date"] # diğer özelliklerinde link özelliğine sahip olmasını sağlar.
    search_fields = ["title"] # sadece title bilgisi ile arama bölümü olşutururuz.
    list_filter = ["created_date"]
    class Meta:
        model = Article # class Meta django tarafından öngörülüyor. Artık Article modeline göre özelleştirme yapılıyor.