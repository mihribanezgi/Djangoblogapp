from django.contrib import admin

from .models import Article,Comment


admin.site.register(Comment)





@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display =["title","author","created_date"] #Articleda makaleyi kaydettiğimizde sayfada bunları gösterir
    list_display_links= ["title","created_date"] #önceden sadece title bastığımızda makaleyi açıyordu şimdi bunlara basıncada açıyor 
    search_fields=["title"] #titlea göre arama oluşur 
    list_filter=["created_date"] #makalelerin oluşturuldukları tarihe göre süzgeç yapar istersek içine titleda yazarız
    class Meta:
        model = Article
