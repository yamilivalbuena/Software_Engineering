from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


#Defining the functionality of each view

#Home page takes all the destination classes
def home(request):
    context = {
        'destinations': Destination.objects.all()
    }
    return render(request, 'app1/home.html', context)

class DestinationListView(ListView):
    model = Destination
    template_name = 'app1/home.html'
    context_object_name = 'destinations'
    ordering = ['schedule']

class DestinationDetailView(DetailView):
    model = Destination

class DestinationCreateView(LoginRequiredMixin, CreateView):
    model = Destination
    fields = ['name', 'schedule']
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

class DestinationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Destination
    fields = ['name', 'schedule']
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        destination = self.get_object()
        if self.request.user == destination.admin:
            return True
        return False

class DestinationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Destination
    success_url = '/'
    def test_func(self):
        destination = self.get_object()
        if self.request.user == destination.admin:
            return True
        return False


#About page does not take any extra information except a title change

def about(request):
    return render(request, 'app1/about.html', {'title': 'About'})

#BookTrip page takes destinations' information

def BookTrip(request):
    context = {
        'destinations': Destination.objects.all()
    }
    return render(request, "app1/test1.html", context)

#DetailTrip page takes the information already selected in BookTrip

def DetailTrip(request):
    names= request.GET['name']
    dates= request.GET['date']
    times= request.GET['time']
    return render(request, "app1/test2.html",{'name':names, 'date':dates, 'time':times})

#Confirmation page does not take any extra parameter

def confirmation(request):
    return render(request, "app1/confirmation.html")
