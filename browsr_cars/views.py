from django.shortcuts import render
from .models import Cars
from django.core.paginator import Paginator

# Create your views here.

def All_car(request):

   all_car = Cars.objects.all()

   paginator = Paginator(all_car, 9)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   context = {'all':page_obj}

   return render(request, './Cars/Browse_carsn.html', context)




def car_detiles(request, id):
    job_lists = Cars.objects.get(id=id)
    all_car = Cars.objects.all()


    return render(request, './Cars/car_detelis.html', {'all':job_lists, 'all_car':all_car})




