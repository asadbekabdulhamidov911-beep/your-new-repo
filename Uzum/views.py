from django.shortcuts import render, get_object_or_404
from .models import *

def navigation(request):
    kategoriyalar = Category.objects.all()
    return render(request, "navigation.html", {"kategoriyalar": kategoriyalar})

def footer(request):
    return render(request, "footer.html")

def home(request):
    kategoriyalar = Category.objects.all()
    mahsulotlar = Product.objects.all()
    return render(request, "home.html", {
        "kategoriyalar": kategoriyalar,
        "mahsulotlar": mahsulotlar
    })

def kategoriya_mahsulotlari(request, slug):
    kategoriya = get_object_or_404(Category, slug=slug)
    kategoriyalar = Category.objects.all()
    mahsulotlar = Product.objects.filter(kategoriya=kategoriya)
    return render(request, "home.html", {
        "kategoriyalar": kategoriyalar,
        "mahsulotlar": mahsulotlar,
        "tanlangan_kategoriya": kategoriya
    })

def topshirish_punkiti(request):
    kategoriyalar = Category.objects.all()
    return render(request, "topshirish_punkiti.html", {"kategoriyalar": kategoriyalar})

def detail(request, id):
    mahsulot = Product.objects.get(id=id)
    kategoriyalar = Category.objects.all()
    context = {
        "mahsulot": mahsulot,
        "kategoriyalar": kategoriyalar
    }
    return render(request, "detail.html", context)

def sotuvchi_bolish(request):
    kategoriyalar = Category.objects.all()
    return render(request, "sotuvchi_bolish.html", {"kategoriyalar": kategoriyalar})

def sotuv(request):
    kategoriyalar = Category.objects.all()
    return render(request, "sotuv.html", {"kategoriyalar": kategoriyalar})

def savol(request):
    kategoriyalar = Category.objects.all()
    return render(request, "savol.html", {"kategoriyalar": kategoriyalar})

def sotuvchilik(request):
    kategoriyalar = Category.objects.all()
    return render(request, "sotuvchilik.html", {"kategoriyalar": kategoriyalar})

def splash(request):
    kategoriyalar = Category.objects.all()
    return render(request, 'splash.html', {"kategoriyalar": kategoriyalar})