from django.shortcuts import render
from django.views.generic import View
from book_app.models import Bookmodel
# Create your views here.
class Createbook(View):
    def get(self,request):
        return render(request,"create.html")
    
    def post(self,request):
        print(request.POST)
        Bookmodel.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email")
        )
        return render(request,"create.html")
    
class Readbook(View):
    def get(self,request):
        data=Bookmodel.objects.all()
        return render(request,"read.html",{"data":data})
    
class Updatebook(View):
    def get(self,request,**kwargs):
        update_id = kwargs.get("pk")
        book = Bookmodel.objects.get(id=update_id)
        return render(request,"update.html",{"book":book})
    
    def post(self,request,**kwargs):
        update_id = kwargs.get("pk")
        book = Bookmodel.objects.get(id=update_id)
        print(request.POST)
        book.name=request.POST.get("name")
        book.phone=request.POST.get("phone")
        book.email=request.POST.get("email")
        book.save()
        return render(request,"update.html")
    
class Deletebook(View):
    def get(self,request,**kwargs):
        delete_id=kwargs.get("pk")
        book=Bookmodel.objects.get(id=delete_id)
        book.delete()
        return render(request,"create.html")   


        