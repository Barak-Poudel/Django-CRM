from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from .forms import SignUpForm , AddRecordForm
from .models import Record
# Create your views here.




def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in !!!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")

    # Only show records if user is logged in
    if request.user.is_authenticated:
        records = Record.objects.all()
    else:
        records = None   # or [] 

    return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request,"Successfully logged out.")
    return render(request,'home.html',)

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()

    # One render at the end
    return render(request, 'register.html', {'form': form})

def customer_record(request,id):
    if request.user.is_authenticated:
        #look up records

        customer_record = Record.objects.get(id = id)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You must be logged in to view that page..")
        return redirect('home')


def delete_record(request,id):
    if request.user.is_authenticated:
        delete_it =  Record.objects.get(id = id)
        delete_it.delete()
        messages.success(request,"Successfully deleted a record..")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in to delete a record..")
        return redirect('home')    

def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record added")
                return redirect('home')
        else:
            form = AddRecordForm()

        # One render at the end
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to add a record.")
        return redirect('home')

def update_record(request,id):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = id)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully...")
            return redirect('home')
        return render(request,'update_record.html',{'form':form,'current_record':current_record})
    else:
        messages.error(request, "You must be logged in to update a record.")
        return redirect('home')
        
