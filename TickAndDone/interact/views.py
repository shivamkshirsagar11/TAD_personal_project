from django.shortcuts import render,redirect

def index(request):
    try:
        if request.user.is_authenticated and not request.user.is_superuser:
            id = request.user.id
            email = request.user.email
            print(email,id)
            name = request.user.username
            return render(request,'after_login.html',{"name":name,"email":email})
        else:
            return render(request,'home.html')
    except Exception:
        return redirect('/')
