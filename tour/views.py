from django.shortcuts import render, redirect
from .models import *  # better to import explicitly
from django.db.models import Q
def landing(request):
    result = Package.objects.filter(is_popular=True)[:3]

    return render(request, 'index.html', {
        "result": result,
        "query": None
    })

def user_c(request):
    return render(request, 'usercreate.html')
def log(reguest):
    return render(reguest,'login.html')
def about(reguest):
    return render(reguest,'about.html')


def user_register(request):
    if request.method == "POST":
        userprofile.objects.create(
            name=request.POST.get('name'),  
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        return redirect("/log") 

    return render(request, 'usercreate.html')

def user_login(request):
    if request.method=="POST":
        name=request.POST.get('name').strip()
        password=request.POST.get('password').strip()
        try:
            user=userprofile.objects.get(name=name)
            if user.password==password:
                return render(request,'about.html',{"login":True,"name":user.name})
            else:
                return render(request,'login.html',{"error":"wrong password"})
        except userprofile.DoesNotExist:
            return render (request,'login.html',{"error":"name does not exit"})
    return render(request,'login.html')


def logout(request):
    request.session.flush()
    return redirect("/")




def search_fild(request):
    
        query = request.POST.get('query')
        result=[]

        if query:
            result = Package.objects.filter(
                Q(destination__d_state__icontains=query) |
                Q(p_name__icontains=query) |
                Q(destination__d_name__icontains=query)
            )



        return render(request, "index.html", {
        "result": result,
        "query": query})


    