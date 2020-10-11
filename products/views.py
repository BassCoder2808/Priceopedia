from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,History
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
import json
from statistics import mean

# Create your views here.
@login_required
def laptops(request):
    contexts = Product.objects.filter(category_id__category_name = 'Laptops')
    return render(request,'products/laptops.html',{'products':contexts})

@login_required
def phones(request):
    contexts = Product.objects.filter(category_id__category_name = 'Mobile Phones')
    return render(request,'products/phones.html',{'products':contexts})

@login_required
def headphones(request):
    contexts = Product.objects.filter(category_id__category_name = 'Headphones')
    return render(request,'products/headphones.html',{'products':contexts})

@login_required
def tablets(request):
    contexts = Product.objects.filter(category_id__category_name = 'Tablets')
    return render(request,'products/tablets.html',{'products':contexts})


class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'products/all.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'



def prod_detail(request,pk):
    print(pk)
    prod = Product.objects.filter(product_id = pk)
    prod1 = prod[0]
    print(prod1,type(prod1))
    history = History.objects.filter(product_id = prod1).order_by('date')
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
    return render(request,'products/productDetails.html',{'product':prod1,'history':history,'data':data,'labels':json.dumps(labels),'min_data':min_price,'max_data':max_price,'avg_data':avg_price})

def graph_detail(request,pk,time_frame):
    print(request.path,pk,type(time_frame))
    prod = Product.objects.filter(product_id = pk)
    prod1 = prod[0]
    print(prod1,type(prod1))
    history = History.objects.filter(product_id = prod1).order_by('date')
    data = []
    labels = []
    for item in history:
        data.append(float(item.curr_price))
        labels.append(item.date.strftime("%m/%d/%Y"))
    data = data[len(data)-time_frame:]
    labels = labels[len(labels)-time_frame:]
    print(labels,data)
    min_price = [min(data)]*len(data)
    max_price = [max(data)]*len(data)
    avg_price = [int(mean(data))]*len(data)
    print(len(min_price),len(max_price),len(avg_price),len(data))
    return render(request,'products/productDetails.html',{'product':prod1,'history':history,'data':data,'labels':json.dumps(labels),'min_data':min_price,'max_data':max_price,'avg_data':avg_price})
