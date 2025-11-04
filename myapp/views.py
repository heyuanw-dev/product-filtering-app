from django.shortcuts import render
from .models import Category, Tag, Product
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def product_list(request):
    category_slug = request.GET.get("category")
    tag_slugs = request.GET.getlist("tags")
    description_query = request.GET.get("q", "").strip()

    # Fetch products with related category and tags to minimize queries
    products = Product.objects.select_related("category").prefetch_related("tags").all()

    if category_slug:
        products = products.filter(category__slug=category_slug)

    if tag_slugs:
        for slug in tag_slugs:
            products = products.filter(tags__slug=slug)
        products = products.distinct()

    if description_query:
        # Split the query into words and filter products containing any words in the description
        query_words = description_query.split()
        query = Q()
        for word in query_words:
            query |= Q(description__icontains=word)
        products = products.filter(query)

    paginator = Paginator(products, 12)
    page_obj = paginator.get_page(request.GET.get("page"))


    context = {
        "page_obj": page_obj,
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "selected_category": category_slug,
        "selected_tags": tag_slugs,
        "q": description_query,
    }

    querydict = request.GET.copy()
    if "page" in querydict:
        querydict.pop("page")
    context["query_string"] = querydict.urlencode()
    
    return render(request, "index.html", context)
