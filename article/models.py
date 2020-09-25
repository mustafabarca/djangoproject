from django.db import models

# Create your models here.
'''2 numaralı açıklama'''
class Article(models.Model): 
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name= "Yazar") # django içerisindeki hazır kullanıcı (user) modelini kullanıyoruz. bu nedenle o tabloya atıfta bulunmak için foreinKey yazıyoruz. bu alanımız user tablosunu işaret ediyor. on_delete = models.CASCADE yazarak kullanıcının silinmesi halinde o kullanıcınun içerikleride silinecek.
    title = models.CharField(max_length=50, verbose_name="Başlık") # 
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi") # auto_now_add = True ile veritabanına herhangi bir veri eklendiği zaman o anki tarihi created date'e atacak.
    def __str__(self):
        return self.title #admin panelinde makaleler bölümünde makalenin başlık ile görünmesini sağlar(eski hali articleobject 1), create_date veya author şeklinde de gösterebiliriz.



