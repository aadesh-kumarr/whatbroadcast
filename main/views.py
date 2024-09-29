from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django import forms
from .forms import logdat, login_page,msg
from .models import logdata
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm



# from .views import person


# Create your views here.


# @login_required(login_url='main')
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def getacoffee(request):
    return render(request, "getacoffe.html")





def login(request):
    print(1)
    if request.method=='POST':
       form=AuthenticationForm(request,request.POST)
       print('form created')
       if form.is_valid():
          print('valid')
          username=request.POST['username']
          pw=request.POST['password']
          user=authenticate(username=username,password=pw)
          if user is not None:
             messages.success(request,'login successfull')
             print('user found')
             return redirect('main')

       else:
             print('user not found2')
             form=AuthenticationForm()  
             messages.error(request,'invalid credentials')
             return render(request, "login.html",{'form':form})
       
             
    else:
       print('formin get')
       messages.warning(request,'an error occured please try again')
       form=AuthenticationForm()  
       return render(request, "login.html",{'form':form})


def signup(request):
    from django.contrib.auth import get_user_model
    User=get_user_model()
    context = {}
    context["form"] = logdat()
    if request.method == "POST":
        form = logdat(request.POST)
        print("form created")
        if form.is_valid():

            try:

                print(1)
                fname = request.POST["fname"]
                lname = request.POST["lname"]
                email = request.POST["email"]
                pw = request.POST["password"]
                username = request.POST["username"]
                user = User.objects.create(username=username, email=email, password=pw)

                user.save()
                user.first_name = fname
                user.last_name = lname
                user.save()

                messages.success(request, "account successfully created")
                return redirect("main")
            except IntegrityError:
                messages.error(request,"username already exist")

                #   popup error message to be added
                print("intigrity error")
                return render(request,"signup.html",context)

        else:
            print(2)
    else:
        print(3)
        return render(request, "signup.html", context)






def usepage(request):
    context={}
    context['data']=User.objects.all()
    print(context['data'])
    context['form']=msg()
        
    if request.method=='get':
        print('form created')
        form=msg(request.GET)
        if form.is_valid():
            global mesg,img,excel
            mesg=request.GET.get["txt"]
            img=request.GET.get["image"]
            speed=request.GET.get["speed"]
            excel=request.GET.get['excelfile']
            # print(mesg,speed,img)
        else:
            pass
    else:
        pass
            
            
    return render(request,'usepage.html',context)

def selectfile(request):
    from pandas import read_excel
    
    a=read_excel(excel)
    for i in range(len(excel)-1,0,-1):
        if(excel[i]=='/'):
            newpath=a[0:i]
            break
        else:
            pass
    global d
    d=newpath+'/namesfromexcel.txt' 
    excel=a.to_string(index=False).lstrip()
    c=excel.split('     ')
    print(c)
    file=open(d,'w+',encoding='utf-8')
    file.writelines(c)
    file.close()
# new text file created
# creating and opening browser 



def strt(request):
    if 'd' in globals():
        from selenium import webdriver
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        browser=webdriver.Edge()
        browser.maximize_window()
        browser.get('https://web.whatsapp.com/')
        
    # open and read contacts directory (new built)

        with open(d,'r',encoding='utf-8') as f:
            global contacts
            contacts=[group.strip() for group in f.readlines()]


    # sleep timer for whatsp qr code scan 
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.wait import WebDriverWait
        checkk=By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
        
    # whatsp login wait 
        from time import sleep
        from selenium.webdriver.support import expected_conditions as ec
        WebDriverWait(browser,600).until(ec.presence_of_element_located(checkk))
        
        
    # sleep for loading whatsp details 
        sleep(3)
    # ---------------------------
        
        from pyperclip import copy
        from selenium.webdriver.common.keys import Keys
        
        for group in contacts:
            serchbox=browser.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
            cp=By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
            copy(group)

    #sending name to search box
            serchbox.send_keys(Keys.SHIFT,Keys.INSERT)
            sleep(3)
            try:
                browser.find_element(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[2]/div')
                serchbox.send_keys(Keys.ENTER)
                
                # sleep to enter in chat 
                sleep(0.2)
    # entered in chat
                    
                textbox=browser.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                textbox.send_keys(mesg)
                textbox.send_keys(Keys.ENTER)
    # text message sent

                attatch=browser.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')
                attatch.click()
                
                return render(request,"usepage.html")
                
                
            # incomplete
            # incomplete
    # attatch step 2 executed
            # incomplete
            # incomplete
            except Exception as e:
                serchbox.clear()
                
            
        return render(request,'home.html')
    else:
        messages.error(request,'please select an excel file')
        return render(request,"usepage.html")













# def check(request):
#     if request.method == "POST":
#         name = request.POST("name", default="")
#         email = request.POST("email", default="")
#         pw = request.POST("password", default="")
#         contact = request.POST("contact", default="")
#         print(1)

#         print(name, email, pw, contact)
#         user = User.objects.create_user(name, email, pw, contact)
#         user.save()