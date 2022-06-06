from email import message
from urllib import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from .models import Ingredient, Rating, Reception
from .forms import receptionform,Ratingf,ingredientformset
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist


class Home(ListView):
   model = Reception
   template_name = 'home.html'
   ordering = ['-reception_date']
   


class receptionview(DetailView):
   model = Reception
   template_name = 'receptions_det.html'
   

   def get_queryset(self):
      return Reception.objects.order_by('title')

   def get_context_data(self, **kwargs):
      context = super(receptionview, self).get_context_data(**kwargs)
      context['ingredients'] = Ingredient.objects.order_by('nameing')
      return context
 
def Addreception(request):
   if request.method == "GET":
      form = receptionform()
      formset= ingredientformset()
      return render(request,'add_reception.html',{"form":form,"formset":formset})
   elif request.method == "POST":
         form = receptionform(request.POST)
         if form.is_valid():
            recipe = form.save()
            formset = ingredientformset(request.POST, instance=recipe)
            if formset.is_valid():
               formset.save()
            return redirect('/')
         else:
            return render(request, 'add_reception.html', {"form":form})
   #form_class = receptionform
   #template_name = 'add_reception.html'

class deletereception(DeleteView):
   model = Reception
   template_name = 'delete_reception.html'
   success_url = reverse_lazy('home')

def submitrating(request,reception_id):
   url = request.META.get('HTTP_REFERER')
   if request.method == 'POST':
      try:
         ratings = Rating.objects.get(user__id=request.user.id,reception__id=reception_id)
         form = Ratingf(request.POST,instance=ratings)
         form.save()
         message.success(request,'Thank you for this rate!')
         return render(request,"home")
                
      except Rating.DoesNotExist:
         form = Ratingf(request.POST)
         if form.is_valid():
            data = Rating()
            data.rating = form.cleaned_data['rating']
            data.ip = request.META.get('REMOTE_ADDR')
            data.reception_id = reception_id
            data.user_id = request.user.id
            data.save()
            message.success(request,'Thank you for this rate and it is submitted!')
            return render(request,"home")

def ingredienttop(request):
   
   ingredienttopp = Ingredient.objects.annotate(num_ingredients=Count('nameing')).order_by('-num_ingredients')[:5]
   ingredienttopp[0].num_ingredients
   
   return render(request,"ingredient_top.html",{'Ingredient':ingredienttopp})
