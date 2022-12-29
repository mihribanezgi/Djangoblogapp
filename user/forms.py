from django import forms





class LoginForm(forms.Form): #Kullanıcı Giriş Formu Oluşturdum daha sonra login.html git devam et    
    username = forms.CharField(label = "Kuallnıcı Adı")
    password =forms.CharField(label ="Parola",widget= forms.PasswordInput) 










class RegisterForm(forms.Form): #Kullanıcı Kayıt Formu oluştu

    username = forms.CharField(max_length=50,label ="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    comfirm = forms.CharField(max_length=20,label="Parolayı Doğrula",widget=forms.PasswordInput)
    
    def clean(self): #clean metodu djangonun içinde var zaten şifre doğrulamaya yarar şifreler tutuyormu? 3 tane alanı bu metod ile aldık
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm =self.cleaned_data.get("confirm")

        if password and confirm and (password != confirm):     #parolam ile parola doğrulama alanım eşleşmiyor ?
            raise forms.ValidationError("Parolalar eşleşmiyor ")
    
        
        values = {     
            "username" : username,
            "password" : password,
        }    #sözlük oluşturduk ve anahtar kelimeler oluşturduk bir sonraki sayfada döndürmek için 
        return values 


    

