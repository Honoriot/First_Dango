from django.shortcuts import render
from .models import Mobile, Fruit
# Create your views here.
def product_detail_view(request):
    obj = Mobile.objects.get(id=1)
    obj1 = Fruit.objects.get(id=1)
    # content = {
    #     "title" : obj.title,
    #     "description" : obj.description,
    #     "price" : obj.price,
    #     "summary" : obj.summary,
    #     "title_1" : obj1.title,
    #     "description_1" : obj1.description,
    #     "price_1" : obj1.price,
    #     "summary_1" : obj1.summary,

    # }
    content = {
        "object" : obj,
        "object1" : obj1
    }
    return render(request, "product/detail.html", content)