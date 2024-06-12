from django.shortcuts import render,redirect
from .models import hiretuber
from django.contrib import messages
# Create your views here.

def hiretubers(request):
    if request.method == "POST" :
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        user_id = request.POST['user_id']
        state = request.POST['state']
        city = request.POST['city']
        phone = request.POST['phone']
        message = request.POST['message']

        hiretubers = hiretuber(firstname=firstname,
                             lastname=lastname,
                             email=email,
                             tuber_id = tuber_id,
                             tuber_name = tuber_name,
                             user_id = user_id,
                             state=state,
                             city=city,
                             phone=phone,
                             message=message)
        hiretubers.save()
        messages.success(request,"Thanks For Reaching To Us.")
        return redirect("youtubers")