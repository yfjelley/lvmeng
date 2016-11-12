from django.shortcuts import render
from django.shortcuts import render_to_response
from erp.models import *
from api.models import *

# Create your views here.
def Product_Detail(request):
    if request.method == "GET":
        product_id = request.GET.get("product_id", 0)

        try:
            product_detail = Product.objects.get(id=product_id)
        except:
            product_detail = None

        if product_detail:
            return render_to_response("mobi/product_detail.html", locals())
        else:
            return render_to_response("mobi/product_not_found.html")


def News_Detail(request):
    if request.method == "GET":
        news_id = request.GET.get("news_id", 0)

        try:
            news = Headline.objects.get(id=news_id)
        except:
            news = None

        if news:
            return render_to_response("mobi/news_detail.html", locals())
        else:
            return render_to_response("mobi/news_not_found.html")