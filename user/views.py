from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

 
 
 



# Create your views here.

def register(request): #kayıt işlemi
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid(): #is_valid yaparsak clean metodu çağırılıyor alanlarımız doğru mu kontrol ediyor 
            username = form.cleaned_data.get("username")
            password =form.cleaned_data.get("password") #username ve password alanını aldım

            newUser = User(username =username) #yeni bir kullanıcı oluşturdum ama önce yukarda from django.contrib.auth.models import User modelini dahil ettim 
            newUser.set_password(password) #parolamı şifreledim
            newUser.save() #kullanıcıyı veritabanına kaydettim

            login(request,newUser) #user kayıt oldu ve sisteme login sayesinde otomatik giriş yaptı ama önce yukarda from django.contrib.auth import login modelini dahil ettim 
            messages.info(request,"Başarıyla Kayıt Oldunuz...")

            return redirect("index") #yukarda from django.shortcuts import render,redirect yaniii redirect dahi ettim kullanıcı kayıt olduktan sonra blog daki urls.py içinde önceden verdiğimiz namei index olan anasayfaya gidecek
        context = {
            "form" : form
        }
        return render(request,"register.html",context)    #formum isvalid olmadığında döner


    else: #post request yani kayıt işlemi olmamış tekrar kayıt sayfası context ile açıır
        form = RegisterForm()
        context = {
            "form" :form
        }
        return render(request,"register.html",context)
    
def loginUser(request): #giriş işlemi
    form = LoginForm(request.POST or None)
    
    context = {
        "form":form
    }
    if form.is_valid(): #is_valid yaparsak clean metodu çağırılıyor alanlarımız doğru mu kontrol ediyor 
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password) #kullanıcı var mı yok mu varsa bilgisini döner otantikeyt yoksa none
        
        if user is None: #böyle bir kullanıcı yoksa eğer;
            messages.info(request,"Kullanıcı adı veya parola hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla giriş yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)  #localhost:8000/user/login sayfasına tıkladığımızda ilk bu çıkar 

    
def logoutUser(request): #çıkış işlemi
   logout(request)
   messages.success(request,"Başarıyla çıkış yaptınız...")
   return redirect("index")
   