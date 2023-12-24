from . models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User,auth
from django.contrib.auth import  authenticate ,login

#def home(request,c_slug=None):
#    c_page=None
#    prdt=None
#    if c_slug!=None:
##        c_page=get_object_or_404(categ,slug=c_slug)
#        prdt=product.objects.filter(category=c_page,available=True)
        
#    else: 
    

#     prod=product.objects.all()
#     cat=categ.objects.all()     
 
#    return render(request,"home.html",{'pt':prod,'ct':cat})
def home(request,c_slug=None):
    c_page=None
    prdt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prdt=product.objects.filter(category=c_page)
        prod_list=product.objects.all()
        cat=categ.objects.all() 
            
 
        return render(request,"category.html",{'pt':prod_list,'ct':cat,'po':prdt})
        
    else: 
      
    

      prod_list=product.objects.all()
   
      cat=categ.objects.all()
      paginator=Paginator(prod_list,4)
      page_number=request.GET.get('page')
    try:
      finalprod_list=paginator.get_page(page_number)
    except PageNotAnInteger:
      finalprod_list=paginator.page(1)
    except EmptyPage:
      finalprod_list=paginator.page(paginator.num_pages)    
                     
 
    return render(request,"home.html",{'ct':cat,'pf':finalprod_list,'page':page_number})
def cart(request):
    return render(request,"cart.html")

def category(request):
   prod_list=product.objects.all()
   
   cat=categ.objects.all()
   paginator=Paginator(prod_list,1)
   page_number=request.GET.get('page')

   try:
    finalprod_list=paginator.get_page(page_number)
   except PageNotAnInteger:
      finalprod_list=paginator.page(1)
   except EmptyPage:
      finalprod_list=paginator.page(paginator.num_pages)    

  
     
   return render(request,"category.html",{'pt':prod_list,'ct':cat,'pf':finalprod_list,'page':page_number})



def itemdetails(request,name):
   
   if product.objects.filter(name=name).exists():
      cf=product.objects.filter(name=name)
      return render(request,"item.html",{'jk':cf})
   else:
        return render(request,"home.html")
      
   

   

def productdetails(request,c_slug,product_slug):
   
   try:
    print(c_slug)
    pd=product.objects.get(category=c_slug,slug=product_slug)
  
    
   except Exception as e:
      raise e
   return render(request,"item.html",{'pz':pd})
   
   


def touchdisplay(request,id):
   
  ## c=product.objects.filter(category_id=id)

  if(categ.objects.filter(id=id)):
   food=product.objects.filter(category_id=id)
   return render(request,"cart,html",{'ft':food})
  else:
     print("soryy")
     return render(request,"home.html")
  
   

  # instance = get_object_or_404(categ,id=id)
  # food=product.objects.filter(category_id=instance)


  # return render(request, 'cart.html', {'ft': food})
  ## return render(request,"cart.html",{'ft':c})

def searchitems(request):
   itemprdt=None
   query=None
   if 'q' in request.GET:
      query=request.GET.get('q')
      itemprdt=product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query) )
      return render(request,"search.html",{'t':itemprdt,'qr':query})
   else:
      return render(request,"home.html")
   
def c_id(request):
   ct_id=request.session.session_key
   if not ct_id:
      ct_id=request.session.create()
     
      return render(request,"session.html",{'t':ct_id})
   else:
      return render(request,"session.html",{'t':ct_id})
   
#########################################################
   
def one(request):
    ct_id=request.session.session_key
    return ct_id

def two(request):
   ct_id=request.session.create()
    
   return ct_id




 
   
def create_session_key(request):
    # Check if the session key already exists
    if 'my_session_key' not in request.session:
        # If not, generate a new session key (you can use any method you prefer)
        import uuid
        new_session_key = str(uuid.uuid4())
        
        # Store the session key in the session dictionary
        request.session['my_session_key'] = new_session_key
        
    else:
        # If the session key already exists, retrieve and display it
        existing_session_key = request.session['my_session_key']
         
   
def cartdetails(request,ct_items=None,tot=0,count=0,uni=0,cart_items=None):
   try:
    ct=cartlist.objects.get(cartid=User.id)
    
    
    ct_items=items.objects.filter(cart=ct)
    
    for i in ct_items:
       tot +=(i.prdt.price*i.quantity)
       count+=i.quantity
      
   except ObjectDoesNotExist:
      pass
   return render(request,'cartcart.html',{'ci':ct_items,'tr':tot,'cn':count,'unn':uni})


       

   
def addcart(request,product_id):
   prod=product.objects.get(id=product_id)
   c=print(two)  
  ## try:
  ##    ct=cartlist(cartid="qpk9szikac1pu5yz5lgn6dz78xxyo6tz")

   ##   ct=cartlist.objects.get(cartid=one(request))
  ##### except cartlist.DoesNotExist:
      ##ct=cartlist.objects.create(cartid=two(request))
      ##ct.save()

   ct, created = cartlist.objects.get_or_create(cartid= User.id)
   
   ct.save()
   print("saved")   
   try:
      
      c_items=items.objects.get(prdt=prod,cart=ct)
      if c_items.quantity < c_items.prdt.stock:
         c_items.quantity+=1
      c_items.save()
   except items.DoesNotExist:
      c_items=items.objects.create(prdt=prod,quantity=1,cart=ct)
      c_items.save()
   return redirect('cartdetails') 

def testcart(request):
   return render(request,"join.html")

def min(request,product_id):
   ct, created = cartlist.objects.get_or_create(cartid= User.id)
   prdd=get_object_or_404(product,id=product_id)
   c_items=items.objects.get(prdt=prdd,cart=ct)
   if c_items.quantity>1:
      c_items.quantity-=1
      c_items.save()
   else:
      c_items.delete()
   return redirect(cartdetails)

def deleteelement(request,product_id):
    ct, created = cartlist.objects.get_or_create(cartid= User.id)
    prdd=get_object_or_404(product,id=product_id)
    c_items=items.objects.get(prdt=prdd,cart=ct)
    c_items.delete()
    return redirect(cartdetails)




def reg(request):
    if request.method=="POST":

    
        
        user_name = request.POST['name']
        
        password1 = request.POST['password']
       
        email = request.POST['email']
        
        u=User.objects.create_user(username=user_name,password=password1,email=email)
        u.save();
        print("user created")
        return redirect(home)
         
        #messages.info(request,"succesfuly")
    # messages.info(request,"username taken")
       
    else:
        return render(request,"register.html")
    return render(request,"register.html")



def login(request):
    
        
      if request.method=="POST":
       
            
        user_name=request.POST['name']
        password1=request.POST['password']
        
        
        
        user = auth.authenticate(username=user_name,password=password1)
        if user is not None:
            auth.login(request,user)

            return redirect(home)
          
            #return redirect('/')
        else:
            print("sorry")
            return  redirect(login)
      else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    
    return redirect(login)      
    








    




