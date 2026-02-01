from django.shortcuts import render, get_object_or_404
from .models import Tank, Nation, TankClass
from news.models import Article


def tank_list(request):

    tanks = Tank.objects.select_related('nation', 'tank_class')

    tier = request.GET.get('tier')
    class_slug = request.GET.get('tank_class')
    nation_slug = request.GET.get('nation')
    premium = request.GET.get('premium')

    if nation_slug:
        tanks = tanks.filter(nation__slug=nation_slug)

    if tier and tier.isdigit():
        tanks = tanks.filter(tier=int(tier))

    if class_slug:
        tanks = tanks.filter(tank_class__slug=class_slug)

    if premium == "1":
        tanks = tanks.filter(is_premium=True)

    context = {
        'tanks': tanks,
        'nations': Nation.objects.all(),
        'tank_classes': TankClass.objects.all(),

        'selected_tier': tier,
        'selected_class': class_slug,
        'selected_nation': nation_slug,
        'selected_premium': premium == "1",
    }

    return render(request, 'tanks/tank_list.html', context)



def tank_detail(request, slug):
    tank = get_object_or_404(
        Tank.objects.select_related('nation', 'tank_class'),
        slug=slug
    )
    return render(request, 'tanks/tank_detail.html', {
        'tank': tank
    })


# 🔥 MANA SHU OLDINGI XATONI HAL QILADI
def tanks_by_nation(request, slug):
    nation = get_object_or_404(Nation, slug=slug)
    tanks = Tank.objects.select_related('nation', 'tank_class').filter(nation=nation)

    context = {
        'tanks': tanks,
        'nation': nation,
        'nations': Nation.objects.all(),
        'tank_classes': TankClass.objects.all(),

        'selected_nation': slug,
    }

    return render(request, 'tanks/tank_list.html', context)
def home(request):
    latest_news = Article.objects.filter(published=True).order_by('-created_at')[:3]

    return render(request, 'home.html', {
        'latest_news': latest_news
    })

def home(request):
    latest_news = Article.objects.filter(published=True).order_by('-created_at')[:3]
    return render(request, 'home.html', {
        'latest_news': latest_news
    })