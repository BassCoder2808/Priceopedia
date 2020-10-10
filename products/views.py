from django.shortcuts import render
from .models import Product,History
from django.contrib.auth.decorators import login_required
import json
from statistics import mean

# Create your views here.
@login_required
def laptops(request):
    contexts = Product.objects.filter(category_id__category_name = 'Laptops')
    history = History.objects.filter(category_id__category_name = 'Laptops').order_by('date')
    data = []
    labels = []
    for item in history:
        print(item)
        data.append(float(item.curr_price))
        labels.append(item.date.strftime("%m/%d/%Y"))
    print(data,labels)
    min_price = [min(data)]*len(data)
    max_price = [max(data)]*len(data)
    avg_price = [int(mean(data))]*len(data)
    print(min_price,max_price,avg_price)
    return render(request,'products/laptops.html',{'products':contexts,'history':history,'data':data,'labels':json.dumps(labels),'min_data':min_price,'max_data':max_price,'avg_data':avg_price})

@login_required
def phones(request):
    contexts = Product.objects.filter(category_id__category_name = 'Mobile Phones')
    history = History.objects.filter(category_id__category_name = 'Mobile Phones').order_by('date')
    data = []
    labels = []
    for item in history:
        print(item)
        data.append(float(item.curr_price))
        labels.append(item.date.strftime("%m/%d/%Y"))
    print(data,labels)
    min_price = [min(data)]*len(data)
    max_price = [max(data)]*len(data)
    avg_price = [int(mean(data))]*len(data)
    print(min_price,max_price,avg_price)
    return render(request,'products/phones.html',{'products':contexts,'history':history,'data':data,'labels':json.dumps(labels),'min_data':min_price,'max_data':max_price,'avg_data':avg_price})

@login_required
def headphones(request):
    contexts = Product.objects.filter(category_id__category_name = 'Headphones')
    history = History.objects.filter(category_id__category_name = 'Headphones').order_by('date')
    data = []
    labels = []
    for item in history:
        print(item)
        data.append(float(item.curr_price))
        labels.append(item.date.strftime("%m/%d/%Y"))
    print(data,labels)
    min_price = [min(data)]*len(data)
    max_price = [max(data)]*len(data)
    avg_price = [int(mean(data))]*len(data)
    print(min_price,max_price,avg_price)
    return render(request,'products/headphones.html',{'products':contexts,'history':history,'data':data,'labels':json.dumps(labels),'min_data':min_price,'max_data':max_price,'avg_data':avg_price})

@login_required
def tablets(request):
    contexts = Product.objects.filter(category_id__category_name = 'Tablets')
    history = History.objects.filter(category_id__category_name = 'Tablets').order_by('date')
    data = []
    labels = []
    for item in history:
        print(item)
        data.append(float(item.curr_price))
        labels.append(item.date.strftime("%m/%d/%Y"))
    print(data,labels)
    min_price = [min(data)]*len(data)
    max_price = [max(data)]*len(data)
    avg_price = [int(mean(data))]*len(data)
    print(min_price,max_price,avg_price)
    return render(request,'products/tablets.html',{'products':contexts,'history':history,'data':data,'labels':json.dumps(labels),'min_data':min_price,'max_data':max_price,'avg_data':avg_price})


