from .forms import SignupForm, LoginForm, CreateproductForm, BlogForm
from .models import CreateProduct, Blog
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import  check_password
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def Profile(request):
    return render(request, 'profile.html')

def Login(request):
    error = ""
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Email or Password is incorrect')
                return redirect('Login')
        except User.DoesNotExist: 
            messages.error(request, 'Email or Password is incorrect')
            return redirect('Login')

    return render(request, 'Login.html', {'error': error})

def Signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():

            user = form.save()
            login(request, user)
            return redirect('/')
    return render(request, 'signup.html', {'form': form})

def Createproductviews(request):
    if request.method == 'POST':
        form = CreateproductForm(request.POST)
        if form.is_valid():
            comment = form.save()
            created_post_id = comment.id
            return redirect('/')  
    else:
        form = CreateproductForm()

    return render(request, 'createproduct.html', {'form': form})

#def Home(request):
 #   comments = CreateProduct.objects.all()
  #  return render(request, 'home.html', {'comments': comments})

def Product(request, post_id):
    post = get_object_or_404(CreateProduct, id=post_id)
    return render(request, 'product.html', {'post': post})

@login_required
def toggle_like(request, comment_id, source):
    comment = get_object_or_404(CreateProduct, pk=comment_id)
    user = request.user

    if user in comment.likes.all():
        comment.likes.remove(user)
        liked = False
    else:
        comment.likes.add(user)
        liked = True

    response_data = {
        'liked': liked,
        'likes_count': comment.likes.count()
    }

    return JsonResponse(response_data)

def Bag(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        try:
            product = CreateProduct.objects.get(id=product_id)
            total_price += product.price * quantity
            cart_items.append({
                'id': product.id,
                'title': product.title,
                'price': product.price,
                'quantity': quantity
            })
        except CreateProduct.DoesNotExist:
            continue

    return render(request, 'bag.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        cart[str(product_id)] = cart.get(str(product_id), 0) + 1
        request.session['cart'] = cart

        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'}, status=400)

def Like(request):
    liked_posts = CreateProduct.objects.filter(likes=request.user)
    
    return render(request, 'like.html', {'comments': liked_posts})

def Catalog(request):
    return render(request,'catalog.html')

def catalog_by_category(request, category):
    products = CreateProduct.objects.filter(section=category)
    
    return render(request, 'catalog_by_category.html', {'products': products, 'category': category})

def Aboutus(request):
    return render(request,'aboutus.html') 

def Blog_views(request):
    blogs = Blog.objects.all()
    
    if request.method == 'POST':
        if 'delete' in request.POST:
            blog_id = request.POST.get('delete')
            blog = get_object_or_404(Blog, id=blog_id)
            blog.delete()
            return redirect('Blog_views')
        
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blog_views')
    else:
        form = BlogForm()
    
    return render(request, 'blog.html', {'blogs': blogs, 'form': form})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('Blog_views')

def Contact(request):
    return render(request,'contact.html')

def Shipping(request):
    return render(request,'shipping.html')

def Home(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'date') 

    if search_query:
        comments = CreateProduct.objects.filter(title__icontains=search_query)
    else:
        comments = CreateProduct.objects.all()

    if sort_by == 'popularity':
        comments = comments.annotate(like_count=Count('likes')).order_by('-like_count')
    elif sort_by == 'date':
        comments = comments.order_by('-created_at')

    return render(request, 'home.html', {'comments': comments})

def Search(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        posts = CreateProduct.objects.filter(title__icontains=search_query)
    else:
        posts = CreateProduct.objects.all()
    
    return render(request, 'search.html', {'comments': posts})

@login_required
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    user = request.user

    if user in blog.like.all():
        blog.like.remove(user)
    else:
        blog.like.add(user)

    return redirect('Blog_views')

def Homedecor(request):
    return render(request,'homedecor.html')

def clear_cart(request):
    if request.method == 'POST':
        request.session['cart'] = {}
        return redirect('Bag')
    return redirect('Bag')