from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required   # this is used to check that either user is logged in or not
from .models import Product   # for making object of Product
from django.utils import timezone  # for current time

def home(request):
    return render(request,'products/home.html') 

def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product} )


@login_required # create futn can only be accesed if the person is logged in unless redirects it to homepage.
def create(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['title'] and request.POST['body'] and request.POST['url']and request.POST['summary']: 
            product = Product()
            product.name = request.POST['name']
            product.title = request.POST['title']
            product.url = request.POST['url']
            product.summary = request.POST['summary']
            product.body = request.POST['body']
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
    else:
        return render(request, 'products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    event_list=Product.objects.all()    
    args={'product': product,'event_list':event_list}
    return render(request, 'products/detail.html', args)         

# def home(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     event_list=Product.objects.all()    
#     args={'product': product,'event_list':event_list}
#     return render(request, 'products/home.html', args)        
