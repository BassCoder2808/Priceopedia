from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,History
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,DeleteView
import json
from statistics import mean

# Create your views here.
@login_required
def laptops(request):
    contexts = Product.objects.filter(category_id__category_name = 'Laptops')
    for product in contexts:
        history = History.objects.filter(product_id = product).order_by('date')
        data = []
        labels = []
        avg_price = []
        for item in history:
            data.append(float(item.curr_price))
            labels.append(item.date.strftime("%m/%d/%Y"))
            avg_price.append(int(sum(data)/len(data)))
        product.price = data[len(data)-1]
    return render(request,'products/laptops.html',{'products':contexts})

@login_required
def phones(request):
    contexts = Product.objects.filter(category_id__category_name = 'Mobile Phones')
    for product in contexts:
        history = History.objects.filter(product_id = product).order_by('date')
        data = []
        labels = []
        avg_price = []
        for item in history:
            data.append(float(item.curr_price))
            labels.append(item.date.strftime("%m/%d/%Y"))
            avg_price.append(int(sum(data)/len(data)))
        product.price = data[len(data)-1]
    return render(request,'products/phones.html',{'products':contexts})

@login_required
def headphones(request):
    contexts = Product.objects.filter(category_id__category_name = 'Headphones')
    curr_price = []
    for product in contexts:
        history = History.objects.filter(product_id = product).order_by('date')
        data = []
        labels = []
        avg_price = []
        for item in history:
            data.append(float(item.curr_price))
            labels.append(item.date.strftime("%m/%d/%Y"))
            avg_price.append(int(sum(data)/len(data)))
        product.price = data[len(data)-1]
    return render(request,'products/headphones.html',{'products':contexts,'current_price':curr_price})

@login_required
def tablets(request):
    contexts = Product.objects.filter(category_id__category_name = 'Tablets')
    for product in contexts:
        history = History.objects.filter(product_id = product).order_by('date')
        data = []
        labels = []
        avg_price = []
        for item in history:
            data.append(float(item.curr_price))
            labels.append(item.date.strftime("%m/%d/%Y"))
            avg_price.append(int(sum(data)/len(data)))
        product.price = data[len(data)-1]
    return render(request,'products/tablets.html',{'products':contexts})


@login_required
def productDetailView(request):
    contexts = Product.objects.all()
    for product in contexts:
        history = History.objects.filter(product_id = product).order_by('date')
        data = []
        labels = []
        avg_price = []
        for item in history:
            data.append(float(item.curr_price))
            labels.append(item.date.strftime("%m/%d/%Y"))
            avg_price.append(int(sum(data)/len(data)))
        product.price = data[len(data)-1]
    return render(request,'products/all.html',{'products':contexts})


# class ProductListView(LoginRequiredMixin,ListView):
#     model = Product
#     template_name = 'products/all.html'
#     context_object_name = 'products'


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
    avg_price = []
    for item in history:
        data.append(float(item.curr_price))
        labels.append(item.date.strftime("%m/%d/%Y"))
        avg_price.append(int(sum(data)/len(data)))
    print(data,labels)
    min_price = [min(data)]*len(data)
    max_price = [max(data)]*len(data)
    curr_price = data[len(data)-1]
    average_price = avg_price[len(avg_price)-1]
    minimum_price = min_price[len(min_price)-1]
    maximum_price = max_price[len(max_price)-1]
    #avg_price = [int(mean(data))]*len(data)
    print(labels)
    return render(request,'products/productDetails.html',{'product':prod1,'history':history,'data':data,'labels':json.dumps(labels),'min_data':min_price,'max_data':max_price,'avg_data':avg_price,'current_price':curr_price,'average_price':average_price,'minimum_price':minimum_price,'maximum_price':maximum_price})

def graph_detail(request,pk,time_frame):
    print(request.path,pk,type(time_frame))
    prod = Product.objects.filter(product_id = pk)
    prod1 = prod[0]
    print(prod1,type(prod1))
    history = History.objects.filter(product_id = prod1).order_by('date')
    data = []
    labels = []
    avg_price = []
    for item in history:
        data.append(float(item.curr_price))
        labels.append(item.date.strftime("%m/%d/%Y"))
        avg_price.append(int(sum(data)/len(data)))
    data = data[len(data)-time_frame:]
    labels = labels[len(labels)-time_frame:]
    print(labels,data)
    min_price = [min(data)]*len(data)
    max_price = [max(data)]*len(data)
    curr_price = data[len(data)-1]
    #avg_price = [int(mean(data))]*len(data)
    print(labels)
    print(len(min_price),len(max_price),len(avg_price),len(data))
    return render(request,'products/productDetails.html',{'product':prod1,'history':history,'data':data,'labels':json.dumps(labels),'min_data':min_price,'max_data':max_price,'avg_data':avg_price,'current_price':curr_price})


class ProductDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False
