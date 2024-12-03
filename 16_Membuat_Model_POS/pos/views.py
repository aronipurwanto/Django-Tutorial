from django.shortcuts import render, redirect

from pos.forms import ProductForm
from pos.models import Category, Product


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/post/product/')
        else:
            return redirect('/post/product/add')
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)

def categoryList(request):
    categories = Category.objects.all()
    context = {
        'title':'Category List',
        'data': categories,
    }
    return render(request, 'category_list.html', context)