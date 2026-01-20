from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from.models import Collections,Category,Profile,FavoriteBooks
from.forms import BookForm,UserForm,ProfileForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def registrationform(request):
    return render(request,"registrationform.html")

def signup(request):
    if request.method == "POST":
        user_type=request.POST.get("user_type")
        user_name=request.POST.get("username")
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.create_user(
            username=user_name,
            email=email,
            password=password
        )
        login(request,user)
        return redirect('home')
    return redirect('signup')
    

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)    
            return redirect('home')
        else:
            return redirect('login_view')            
    return render(request,'registrationform.html')     

def log_out(request):
    logout(request)
    return redirect('login_view')

def home(request):
    categories=Category.objects.prefetch_related('books').all()
    context={
        'categories':categories,
    }
    return render(request,'home.html',context)    
 
def add_book(request):
    if request.method == "POST":
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form= BookForm()
    return render(request,'add_book.html',{'form':form})    

@staff_member_required    
def manage_book(request):
    books=Collections.objects.all()
    return render(request,'manage_book.html',{'books':books})

@staff_member_required 
def edit_book(request,bid):
    books=get_object_or_404(Collections,id=bid)
    if request.method =="POST":
        form=BookForm(request.POST,request.FILES,instance=books)
        if form.is_valid():
            form.save()
            return redirect('manage_book')
    else:
        form=BookForm(instance=books)
    return render(request,'edit_book.html',{'form':form})  

@staff_member_required 
def delete_book(request,bid):
    books=get_object_or_404(Collections,id=bid)
    if request.method == "POST":
        books.delete()
        return redirect('manage_book')
    return redirect('manage_book')    

@staff_member_required         
def manage_user(request):
    users=User.objects.filter(is_staff=False,is_superuser=False)
    return render(request,'manage_user.html',{'users':users})

def delete_user(request,uid):
    user=get_object_or_404(User,id=uid)
    if request.method == "POST":
        user.delete()
        return redirect('manage_user')
    return redirect('manage_user')  

def profile(request):
    profile,created=Profile.objects.get_or_create(user=request.user)
    user_form=UserForm(instance=request.user)
    profile_form=ProfileForm(instance=profile)
    if request.method == 'POST':
        user_form=UserForm(request.POST,instance=request.user)
        profile_form=ProfileForm(request.POST,request.FILES,instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    return render(request,'profile.html',{'user_form':user_form,'profile_form':profile_form})        

def favorite_books(request):
    bitems=FavoriteBooks.objects.filter(user=request.user).all()
    return render(request,'favorite_books.html',{'bitems':bitems})

def Add_favorite(request,fid):
    book=get_object_or_404(Collections,id=fid)
    favorite=FavoriteBooks.objects.filter(user=request.user,book=book).first()
    if favorite:
        favorite.delete()
    else:
        FavoriteBooks.objects.create(user=request.user,book=book)
    return redirect (request.META.get('HTTP_REFERER','home'))        

def remove_favorite(request,fid):
    f_delete=FavoriteBooks.objects.filter(id=fid)
    f_delete.delete()
    return redirect('favorite_books')
