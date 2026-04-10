from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Director, Product
import json

# Create your views here.

def members(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def vision(request):
    return render(request, 'vision.html')

def board(request):
    directors = Director.objects.all()
    context = {
        'directors': directors
    }
    return render(request, 'board.html', context)

def quality(request):
    return render(request, 'quality.html')

def products(request):
    from .models import Product
    from django.core.paginator import Paginator
    
    # Get all products for pagination
    all_products = Product.objects.all().order_by('-created_at')
    
    # Pagination setup - reduced to 6 per page for better testing
    page = request.GET.get('page', 1)
    per_page = 6  # Show 6 products per page instead of 12
    paginator = Paginator(all_products, per_page)
    
    try:
        products_page = paginator.page(page)
    except:
        products_page = paginator.page(1)
    
    # Get featured products (all products from current page)
    featured_products = products_page.object_list
    
    # Get all products categorized by type
    tablet_products = Product.objects.filter(type='Tablet').order_by('name')[:10]
    injection_products = Product.objects.filter(type='Injection').order_by('name')[:10]
    syrup_products = Product.objects.filter(type__in=['Dry Syrup', 'Syrup']).order_by('name')[:10]
    
    context = {
        'products': products_page,  # Paginated products
        'featured_products': featured_products,
        'tablet_products': tablet_products,
        'injection_products': injection_products,
        'syrup_products': syrup_products,
        'total_products': Product.objects.count(),
        'per_page': per_page,
    }
    return render(request, 'products.html', context)

def add_product(request):
    if request.method == 'POST':
        from django.contrib import messages
        from django.shortcuts import redirect
        
        try:
            # Check if SKU already exists
            sku = request.POST.get('sku', '')
            if sku and Product.objects.filter(sku=sku).exists():
                messages.error(request, f'Product with SKU "{sku}" already exists. Please use a different SKU.')
                return redirect('products_page')
            
            # Create product if no duplicate SKU
            # ... rest of product creation logic
            
        except Exception as e:
            messages.error(request, f'Error creating product: {str(e)}')
            return redirect('products_page')
    
    return render(request, 'admin/products_page.html')

def responsibility(request):
    return render(request, 'responsibility.html')

def company(request):
    return render(request, 'company.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')

def help(request):
    return render(request, 'index.html') 

def logout(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return render(request, 'admin/logout.html') 

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email_id')
        password = request.POST.get('login_password')
        print(email, password,"<---------------------- email and password")
        
        from django.contrib.auth import authenticate, login
        from django.contrib.auth.models import User
        from django.contrib import messages
        
        # Check if user exists and is superuser/staff
        try:
            user = User.objects.get(email=email)
            if user.is_superuser or user.is_staff:
                # Authenticate the user
                authenticated_user = authenticate(request, username=user.username, password=password)
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    # messages.success(request, 'Login successful! Welcome to Admin Dashboard.')
                    return redirect('admin_dash')  # Redirect to admin dashboard
                else:
                    messages.error(request, 'Invalid password. Please try again.')
            else:
                messages.error(request, 'Access denied. Only admin users can login.')
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')
        
    return render(request, 'login.html') 

def service(request):
    return render(request, 'service.html') 

def appoinment(request):
    return render(request, 'appoinment.html') 

def team(request):
    return render(request, 'team.html') 

def contact(request):
    return render(request, 'contact.html') 

def admin_dash(request):
    # Check if user is authenticated and is superuser/staff
    if not request.user.is_authenticated or not (request.user.is_superuser or request.user.is_staff):
        return redirect('login')
    
    import json
    from django.utils import timezone
    from datetime import timedelta
    
    total_directors = Director.objects.count()
    total_products = Product.objects.count()
    
    recent_activities = [
        {'name': 'New Director Added', 'action': f'Director count: {total_directors}', 'time': 'Just now'},
        {'name': 'Product Updated', 'action': f'Total products: {total_products}', 'time': '2 hours ago'},
        {'name': 'Database Sync', 'action': 'All models synchronized', 'time': '5 hours ago'},
        {'name': 'System Check', 'action': 'All systems operational', 'time': '1 day ago'},
    ]
    
    dashboard_stats = json.dumps({
        'directors': total_directors,
        'products': total_products,
        'categories': 5,  # This would come from Product categories
        'active_users': 12,  # This would come from User model
    })
    
    context = {
        'total_directors': total_directors,
        'total_products': total_products,
        'recent_activities': recent_activities,
        'dashboard_stats': dashboard_stats,
        'last_updated': timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
    return render(request, 'admin/admin_dash.html', context) 

def board_of_directors(request):
    # Check if user is authenticated and is superuser/staff
    if not request.user.is_authenticated or not (request.user.is_superuser or request.user.is_staff):
        return redirect('login')
    
    search_query = request.GET.get('search', '')
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 6)
    
    # Validate per_page value
    try:
        per_page = int(per_page)
        if per_page not in [6, 12, 24, 48]:
            per_page = 6
    except (ValueError, TypeError):
        per_page = 6
    
    # Filter directors based on search using Q objects
    if search_query:
        from django.db.models import Q
        directors = Director.objects.filter(
            Q(name__icontains=search_query) |
            Q(role__icontains=search_query) |
            Q(about__icontains=search_query)
        )
    else:
        directors = Director.objects.all()
    
    # Pagination with dynamic per_page
    paginator = Paginator(directors, per_page)
    
    try:
        directors_page = paginator.page(page)
    except PageNotAnInteger:
        directors_page = paginator.page(1)
    except EmptyPage:
        directors_page = paginator.page(paginator.num_pages)
    
    context = {
        'directors': directors_page,
        'search_query': search_query,
        'total_directors': directors.count(),
        'per_page': per_page,
        'per_page_options': [6, 12, 24, 48],
    }
    return render(request, 'admin/board_of_directors.html', context) 

def products_page(request):
    # Check if user is authenticated and is superuser/staff
    if not request.user.is_authenticated or not (request.user.is_superuser or request.user.is_staff):
        return redirect('login')
    
    search_query = request.GET.get('search', '')
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 6)
    
    # Validate per_page value
    try:
        per_page = int(per_page)
        if per_page not in [6, 12, 24, 48]:
            per_page = 6
    except (ValueError, TypeError):
        per_page = 6
    
    # Filter products based on search using Q objects
    if search_query:
        from django.db.models import Q
        products = Product.objects.filter(
            Q(name__icontains=search_query) |
            Q(category__icontains=search_query) |
            Q(type__icontains=search_query) |
            Q(manufacturer__icontains=search_query) |
            Q(brand__icontains=search_query) |
            Q(sku__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    else:
        products = Product.objects.all()
    
    # Pagination with dynamic per_page
    paginator = Paginator(products, per_page)
    
    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)
    
    context = {
        'products': products_page,
        'search_query': search_query,
        'total_products': products.count(),
        'per_page': per_page,
        'per_page_options': [6, 12, 24, 48],
    }
    return render(request, 'admin/products_page.html', context)

@csrf_exempt
@require_POST
def add_director(request):
    """API endpoint to add new director"""
    try:
        name = request.POST.get('name')
        role = request.POST.get('role')
        about = request.POST.get('about')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')
        
        # Basic validation
        if not name or not role or not experience:
            return JsonResponse({
                'success': False,
                'message': 'Name, Role, and Experience are required fields'
            })
        
        # Save to database
        director = Director.objects.create(
            name=name,
            role=role,
            about=about,
            experience=experience,
            image=image
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Director added successfully!',
            'data': {
                'id': director.id,
                'name': director.name,
                'role': director.role,
                'about': director.about,
                'experience': director.experience,
                'image': director.image.url if director.image else None
            }
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        })

@csrf_exempt
@require_POST
def update_director(request, director_id):
    """API endpoint to update director"""
    try:
        director = Director.objects.get(id=director_id)
        
        name = request.POST.get('name')
        role = request.POST.get('role')
        about = request.POST.get('about')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')
        
        # Update fields if provided
        if name:
            director.name = name
        if role:
            director.role = role
        if about:
            director.about = about
        if experience:
            director.experience = experience
        if image:
            director.image = image
        
        director.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Director updated successfully!',
            'data': {
                'id': director.id,
                'name': director.name,
                'role': director.role,
                'about': director.about,
                'experience': director.experience,
                'image': director.image.url if director.image else None
            }
        })
        
    except Director.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Director not found'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        })

@csrf_exempt
@require_POST
def delete_director(request, director_id):
    """API endpoint to delete director"""
    try:
        director = Director.objects.get(id=director_id)
        director.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Director deleted successfully!'
        })
        
    except Director.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Director not found'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        })

@csrf_exempt
def get_director(request, director_id):
    """API endpoint to get single director data"""
    try:
        director = Director.objects.get(id=director_id)
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': director.id,
                'name': director.name,
                'role': director.role,
                'about': director.about,
                'experience': director.experience,
                'image': director.image.url if director.image else None
            }
        })
        
    except Director.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Director not found'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        })

@csrf_exempt
@require_POST
def add_product(request):
    """API endpoint to add new product"""
    try:
        name = request.POST.get('name')
        category = request.POST.get('category')
        product_type = request.POST.get('type')
        strength = request.POST.get('strength')
        mrp_price = request.POST.get('mrp_price')
        trade_price = request.POST.get('trade_price')
        purchase_price = request.POST.get('purchase_price')
        selling_price = request.POST.get('selling_price')
        gst_percentage = request.POST.get('gst_percentage')
        discount_percentage = request.POST.get('discount_percentage')
        stock = request.POST.get('stock')
        reorder_level = request.POST.get('reorder_level')
        min_order_quantity = request.POST.get('min_order_quantity')
        max_order_quantity = request.POST.get('max_order_quantity')
        warehouse_location = request.POST.get('warehouse_location')
        storage_conditions = request.POST.get('storage_conditions')
        shelf_life = request.POST.get('shelf_life')
        manufacturer = request.POST.get('manufacturer')
        brand = request.POST.get('brand')
        sku = request.POST.get('sku')
        batch_number = request.POST.get('batch_number')
        description = request.POST.get('description')
        composition = request.POST.get('composition')
        expiry_date = request.POST.get('expiry_date')
        product_image = request.FILES.get('product_image')
        
        # Basic validation
        if not name or not category or not product_type or not mrp_price or not stock:
            return JsonResponse({
                'success': False,
                'message': 'Name, Category, Type, MRP Price, and Stock are required fields'
            })
        
        # Save to database
        product = Product.objects.create(
            name=name,
            category=category,
            type=product_type,
            strength=strength,
            mrp_price=mrp_price,
            trade_price=trade_price,
            retail_price=purchase_price,
            stock=stock,
            reorder_level=reorder_level,
            min_order_quantity=min_order_quantity,
            max_order_quantity=max_order_quantity,
            warehouse_location=warehouse_location,
            storage_conditions=storage_conditions,
            shelf_life=shelf_life,
            manufacturer=manufacturer,
            brand=brand,
            sku=sku,
            batch_number=batch_number,
            description=description,
            composition=composition,
            expiry_date=expiry_date,
            product_image=product_image
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Product added successfully!',
            'data': {
                'name': name,
                'category': category,
                'type': product_type,
                'strength': strength,
                'mrp_price': mrp_price,
                'trade_price': trade_price,
                'purchase_price': purchase_price,
                'selling_price': selling_price,
                'gst_percentage': gst_percentage,
                'discount_percentage': discount_percentage,
                'stock': stock,
                'reorder_level': reorder_level,
                'min_order_quantity': min_order_quantity,
                'max_order_quantity': max_order_quantity,
                'warehouse_location': warehouse_location,
                'storage_conditions': storage_conditions,
                'shelf_life': shelf_life,
                'manufacturer': manufacturer,
                'brand': brand,
                'sku': sku,
                'batch_number': batch_number,
                'description': description,
                'composition': composition,
                'expiry_date': expiry_date
            }
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        })

@csrf_exempt
@require_POST
def update_product(request, product_id):
    """API endpoint to update product"""
    try:
        product = Product.objects.get(id=product_id)
        
        name = request.POST.get('name')
        category = request.POST.get('category')
        product_type = request.POST.get('type')
        strength = request.POST.get('strength')
        mrp_price = request.POST.get('mrp_price')
        trade_price = request.POST.get('trade_price')
        purchase_price = request.POST.get('purchase_price')
        selling_price = request.POST.get('selling_price')
        stock = request.POST.get('stock')
        reorder_level = request.POST.get('reorder_level')
        min_order_quantity = request.POST.get('min_order_quantity')
        max_order_quantity = request.POST.get('max_order_quantity')
        warehouse_location = request.POST.get('warehouse_location')
        storage_conditions = request.POST.get('storage_conditions')
        shelf_life = request.POST.get('shelf_life')
        manufacturer = request.POST.get('manufacturer')
        brand = request.POST.get('brand')
        sku = request.POST.get('sku')
        batch_number = request.POST.get('batch_number')
        description = request.POST.get('description')
        composition = request.POST.get('composition')
        expiry_date = request.POST.get('expiry_date')
        product_image = request.FILES.get('product_image')
        
        # Update fields if provided
        if name:
            product.name = name
        if category:
            product.category = category
        if product_type:
            product.type = product_type
        if strength:
            product.strength = strength
        if mrp_price:
            product.mrp_price = mrp_price
        if trade_price:
            product.trade_price = trade_price
        if purchase_price:
            product.retail_price = purchase_price
        if selling_price:
            product.retail_price = selling_price
        if stock:
            product.stock = stock
        if reorder_level:
            product.reorder_level = reorder_level
        if min_order_quantity:
            product.min_order_quantity = min_order_quantity
        if max_order_quantity:
            product.max_order_quantity = max_order_quantity
        if warehouse_location:
            product.warehouse_location = warehouse_location
        if storage_conditions:
            product.storage_conditions = storage_conditions
        if shelf_life:
            product.shelf_life = shelf_life
        if manufacturer:
            product.manufacturer = manufacturer
        if brand:
            product.brand = brand
        if sku:
            product.sku = sku
        if batch_number:
            product.batch_number = batch_number
        if description:
            product.description = description
        if composition:
            product.composition = composition
        if expiry_date:
            product.expiry_date = expiry_date
        if product_image:
            product.product_image = product_image
        
        product.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Product updated successfully!',
            'data': {
                'id': product.id,
                'name': product.name,
                'category': product.category,
                'type': product.type,
                'strength': product.strength,
                'mrp_price': product.mrp_price,
                'trade_price': product.trade_price,
                'retail_price': product.retail_price,
                'stock': product.stock,
                'reorder_level': product.reorder_level,
                'min_order_quantity': product.min_order_quantity,
                'max_order_quantity': product.max_order_quantity,
                'warehouse_location': product.warehouse_location,
                'storage_conditions': product.storage_conditions,
                'shelf_life': product.shelf_life,
                'manufacturer': product.manufacturer,
                'brand': product.brand,
                'sku': product.sku,
                'batch_number': product.batch_number,
                'description': product.description,
                'composition': product.composition,
                'expiry_date': product.expiry_date,
                'product_image': product.product_image.url if product.product_image else None
            }
        })
        
    except Product.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Product not found'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        })

@csrf_exempt
@require_POST
def delete_product(request, product_id):
    """API endpoint to delete product"""
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Product deleted successfully!'
        })
        
    except Product.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Product not found'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        })

@csrf_exempt
def get_product(request, product_id):
    """API endpoint to get single product data"""
    try:
        product = Product.objects.get(id=product_id)
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': product.id,
                'name': product.name,
                'category': product.category,
                'type': product.type,
                'strength': product.strength,
                'mrp_price': product.mrp_price,
                'trade_price': product.trade_price,
                'retail_price': product.retail_price,
                'stock': product.stock,
                'reorder_level': product.reorder_level,
                'min_order_quantity': product.min_order_quantity,
                'max_order_quantity': product.max_order_quantity,
                'warehouse_location': product.warehouse_location,
                'storage_conditions': product.storage_conditions,
                'shelf_life': product.shelf_life,
                'manufacturer': product.manufacturer,
                'brand': product.brand,
                'sku': product.sku,
                'batch_number': product.batch_number,
                'description': product.description,
                'composition': product.composition,
                'expiry_date': product.expiry_date,
                'product_image': product.product_image.url if product.product_image else None
            }
        })
        
    except Product.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Product not found'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error: {str(e)}'
        })
