from django.shortcuts import render,redirect
from myapp.models import acc_details
from myapp.forms import *
from django.http import HttpResponse
def bank_view(request):
    r=registerform()
    if request.method=='POST':
        n=registerform(request.POST)
        if n.is_valid():
            name=n.cleaned_data['name']
            account_num=n.cleaned_data['account_num']
            ifsc=n.cleaned_data['ifsc']
            mob_no=n.cleaned_data['mob_no']
            location=n.cleaned_data['location']
            amount=n.cleaned_data['amount']
            acc_details.objects.create(name=name,account_num=account_num,ifsc=ifsc,mob_no=mob_no,location=location,amount=amount)
            #return HttpResponse('Sucessfully Register')
            return redirect('/response4')
    return render(request,'myapp/register.html',{'r':r})
def login_view(request):
    l=loginform()
    if request.method=='POST':
        s=loginform(request.POST)
        if s.is_valid():
            account_num=s.cleaned_data['account_num']
            mob_no=s.cleaned_data['mob_no']
            user=acc_details.objects.get(account_num=account_num)
            if user.account_num==account_num and user.mob_no==mob_no:
                return redirect('/response3')

    return render(request,'myapp/login.html',{'l':l})
def transction(request):
    a=transactionform()
    if request.method=='POST':
        f=transactionform(request.POST)
        if f.is_valid():
            acc_holder=f.cleaned_data['your_acc_no']
            acc_no=f.cleaned_data['acc_no']
            amount=f.cleaned_data['amount']
            user=acc_details.objects.get(account_num=acc_no)
            user1=acc_details.objects.get(account_num=acc_holder)
            user.amount+=amount
            user1.amount-=amount
            user.save()
            user1.save()
            return HttpResponse('your transction completed')
    return render(request,'myapp/transaction.html',{'f':a})
def detail(request):
    s=acc_details.objects.all()
    return render(request,'myapp/show.html',{'d':s})

def delete(request,id):
    n=acc_details.objects.get(id=id)
    n.delete()
    return HttpResponse('record deleted')

def update(request,name):
    n=acc_details.objects.get(name=name)
    f=updateform(instance=n)
    if request.method=='POST':
        s=updateform(request.POST,instance=n)
        if s.is_valid():
            s.save()
            return HttpResponse('your record updated')
    return render(request,'myapp/update.html',{'form':f})
