from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article


# Create your views here.
def index(request): # web sayfalarına istekte bulunuluyor. request değişkeninin her view fonksiyounda ilk parametre olarak bulunması gerekiyor.
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }

    return render(request,"dashboard.html", context)

def addArticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Oluşturuldu...")
        return redirect("index")
    return render(request, "addarticle.html", {"form":form})

def details(request,id):
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article,id=id)
    return render(request,"detail.html", {"article":article})