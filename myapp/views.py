from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponse
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . models import Details

# Create your views here.

def save(request):
    c = {}
    c.update(csrf(request))

    if request.method == "POST":
        print request.POST
        user = User.objects.create_user( first_name=request.POST.get("fname"),
                                        last_name=request.POST.get("lname"),username=request.POST.get("uname"),
                                        email=request.POST.get("email"),
                                        password=request.POST.get("psw"),)
        user.save()

        return render(request,"afterregister.html")
    else:
        return render(request, "signupform.html", c)


def loginview(request):
    c = {}
    c.update(csrf(request))

    if request.method == "POST":

        username=request.POST.get('uname')
        password=request.POST.get('psw')

        user = authenticate(username=username, password=password)
        print user,"main user"
        if user is not None:
            print user,"hzsdfdgxfhcfgh"
            login(request,user)

            return render(request, "afterlogin.html")

            # Redirect to a success page.

        else:
            return render(request, "login.html", c)
            # Return an 'invalid login' error message.



    else:
        return render(request,"login.html",c)

def logout_view(request):
    logout(request)


def forget_password(request):

    if request.method =="POST":
         username=request.POST['uname']
         password=request.POST['psw']

         u = User.objects.get(username=username)
         u.set_password(password)
         u.save()
         return HttpResponse("hello")
    else:
        return  render(request,"forgetpassword.html")

def update_profile(request):
    c = {}
    c.update(csrf(request))
    if request.method == "POST":
        address = request.POST.get("add")
        bday = request.POST.get("bday")
        mobile = request.POST.get("mob")
        myfile = request.FILES['myfile']
        print request.FILES

        fs = FileSystemStorage()

        filename = fs.save(myfile.name, myfile)

        uploaded_file_url = fs.url(filename)
        current_user = request.user
        l=current_user.id





        p=Details(user=l,location=address,birth_date=bday,mobile=mobile,image_path=uploaded_file_url)

        p.save()
        print uploaded_file_url, "dsfsdf"
        print p.image_path

        u = Details()
        print u.image_path,"after pathhhh"

        return HttpResponse("sdfdgdg")

    else:
        return render(request,"profile.html",c)

