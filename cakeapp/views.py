from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import ContactForm
# Create your views here.



# Base views

def index(request):
    home1 = Index_start.objects.all()
    home2 = About.objects.all()
    home3 = Birthday.objects.all()
    home4 = Wedding.objects.all()
    home5 = Custom.objects.all()
    home6 = Service.objects.all()
    home7 = Team.objects.all()
    home8 = Offer.objects.all()
    home9 = Client.objects.all()
    context = {
        'home1' : home1,
        'home2' : home2,
        'home3' : home3,
        'home4' : home4,
        'home5' : home5,
        'home6' : home6,
        'home7' : home7,
        'home8' : home8,
        'home9' : home9,
    }
    return render(request, 'index.html', context=context)


def about(request):
    about = About.objects.all()
    context = {
        'about' : about
    }
    return render(request, 'about.html', context=context)

def menu(request):
    menu1 = Birthday.objects.all()
    menu2 = Wedding.objects.all()
    menu3 = Custom.objects.all()
    menu4 = Offer.objects.all()
    context = {
        'menu1' : menu1,
        'menu2' : menu2,
        'menu3' : menu3,
        'menu4' : menu4
    }
    return render(request, 'menu.html', context=context)

def team(request):
    team = Team.objects.all()
    context = {
        'team' : team
    }
    return render(request, 'team.html', context=context)

def service(request):
    service = Service.objects.all()
    context = {
        'service' : service
    }
    return render(request, 'service.html', context=context)

def client(request):
    client = Client.objects.all()
    context = {
        'client' : client
    }
    return render(request, 'testimonial.html', context=context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h1>Sizning malumotingiz qabul qilindi</h1>")
    context = {
        'form': form
    }
    return render(request,'contact.html',context=context)







# Detail views


def detail1(request,home1):
    home1 = get_object_or_404(Index_start, slug=home1)
    context = {
        'home1': home1
    }
    return render(request, 'details/detail1.html', context=context)

def detail2(request,home3):
    home2 = get_object_or_404(Birthday, slug=home3)
    context = {
        'home2': home2
    }
    return render(request, 'details/detail2.html', context=context)

def detail3(request,home4):
    home3 = get_object_or_404(Wedding, slug=home4)
    context = {
        'home3': home3
    }
    return render(request, 'details/detail3.html', context=context)

def detail4(request,home5):
    home4 = get_object_or_404(Custom, slug=home5)
    context = {
        'home4': home4
    }
    return render(request, 'details/detail4.html', context=context)

def detail5(request,home6):
    home5 = get_object_or_404(Service, slug=home6)
    context = {
        'home5': home5
    }
    return render(request, 'details/detail5.html', context=context)

def detail6(request,home7):
    home6 = get_object_or_404(Team, slug=home7)
    context = {
        'home6': home6
    }
    return render(request, 'details/detail6.html', context=context)
    
def detail7(request,home8):
    home7 = get_object_or_404(Offer, slug=home8)
    context = {
        'home7': home7
    }
    return render(request, 'details/detail7.html', context=context)

def detail8(request,home9):
    home8 = get_object_or_404(Client, slug=home9)
    context = {
        'home8': home8
    }
    return render(request, 'details/detail8.html', context=context)


# Change views

class Index_startUpdateView(UpdateView):
    model = Index_start
    fields = ('__all__')
    template_name = 'change/Index_startUpdate.html'
class Index_startDeleteView(DeleteView):
    model = Index_start
    template_name = 'change/Index_startDelete.html'
    success_url = reverse_lazy('index')
class Index_startCreateView(CreateView):
    model = Index_start
    template_name = 'change/Index_startCreate.html'
    fields = "__all__"

class AboutUpdateView(UpdateView):
    model = About
    fields = ('__all__')
    template_name = 'change/AboutUpdate.html'
class AboutDeleteView(DeleteView):
    model = About
    template_name = 'change/AboutDelete.html'
    success_url = reverse_lazy('index')
class AboutCreateView(CreateView):
    model = About
    template_name = 'change/AboutCreate.html'
    fields = "__all__"
    
class BirthdayUpdateView(UpdateView):
    model = Birthday
    fields = ('__all__')
    template_name = 'change/BirthdayUpdate.html'
class BirthdayDeleteView(DeleteView):
    model = Birthday
    template_name = 'change/BirthdayDelete.html'
    success_url = reverse_lazy('index')
class BirthdayCreateView(CreateView):
    model = Birthday
    template_name = 'change/BirthdayCreate.html'
    fields = "__all__"

class WeddingUpdateView(UpdateView):
    model = Wedding
    fields = ('__all__')
    template_name = 'change/WeddingUpdate.html'
class WeddingDeleteView(DeleteView):
    model = Wedding
    template_name = 'change/WeddingDelete.html'
    success_url = reverse_lazy('index')
class WeddingCreateView(CreateView):
    model = Wedding
    template_name = 'change/WeddingCreate.html'
    fields = "__all__"

class CustomUpdateView(UpdateView):
    model = Custom
    fields = ('__all__')
    template_name = 'change/CustomUpdate.html'
class CustomDeleteView(DeleteView):
    model = Custom
    template_name = 'change/CustomDelete.html'
    success_url = reverse_lazy('index')
class CustomCreateView(CreateView):
    model = Custom
    template_name = 'change/CustomCreate.html'
    fields = "__all__"

class ServiceUpdateView(UpdateView):
    model = Service
    fields = ('__all__')
    template_name = 'change/ServiceUpdate.html'
class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'change/ServiceDelete.html'
    success_url = reverse_lazy('index')
class ServiceCreateView(CreateView):
    model = Service
    template_name = 'change/ServiceCreate.html'
    fields = "__all__"

class TeamUpdateView(UpdateView):
    model = Team
    fields = ('__all__')
    template_name = 'change/TeamUpdate.html'
class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'change/TeamDelete.html'
    success_url = reverse_lazy('index')
class TeamCreateView(CreateView):
    model = Team
    template_name = 'change/TeamCreate.html'
    fields = "__all__"

class OfferUpdateView(UpdateView):
    model = Offer
    fields = ('__all__')
    template_name = 'change/OfferUpdate.html'
class OfferDeleteView(DeleteView):
    model = Offer
    template_name = 'change/OfferDelete.html'
    success_url = reverse_lazy('index')
class OfferCreateView(CreateView):
    model = Offer
    template_name = 'change/OfferCreate.html'
    fields = "__all__"

class ClientUpdateView(UpdateView):
    model = Client
    fields = ('__all__')
    template_name = 'change/ClientUpdate.html'
class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'change/ClientDelete.html'
    success_url = reverse_lazy('index')
class ClientCreateView(CreateView):
    model = Client
    template_name = 'change/ClientCreate.html'
    fields = "__all__"

