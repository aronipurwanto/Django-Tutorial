from django.shortcuts import render

from pos.models import Category


# Create your views here.
def categoryList(request):
    categories = Category.objects.all()
    context = {
        'title':'Category List',
        'data': categories,
    }
    return render(request, 'category_list.html', context)