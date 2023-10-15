from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Hotel,Orders# , Record
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from math import ceil

def go(request):
	hotels = Hotel.objects.all()
	context = {
		'hotels' : hotels
	}
	return render(request, 'go.html', context)


def home(request):
	#records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('index')
		else:
			messages.success(request, "There Was An Error Logging In, Probably You Do Not Register Yet...")
			return redirect('home')
	else:
		return render(request, 'home.html') #, {'records':records}
	
class CustomLoginView(LoginView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('index')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	
def Hom(request):
	return render(request, 'Hom.html')

def bb(request):
	return render(request, 'bb.html')

def explore(request):
	return render(request, 'explore.html')

def homePage(request):
	return render(request, 'homePage.html')

def contact(request):
	return render(request, 'contact.html')

def rooms(request):
	return render(request, 'rooms.html')

def index(request):
	return render(request, 'index.html')

def main(request):
	# hotels = Hotel.objects.all()
	# print(hotels)
	# n = len(hotels)
	# nSlides = n//4 + ceil((n/4)-(n//4))

	allHotel = []
	cityHotel = Hotel.objects.values('city', 'id')
	cats = {item['city'] for item in cityHotel}
	
	for cat in cats:
		prod = Hotel.objects.filter(city=cat)
		n = len(prod)
		nSlides = n // 4 + ceil((n / 4) - (n // 4))
		allHotel.append([prod, range(1, nSlides), nSlides])

	# params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': hotels}
	# allHotel = [[hotels, range(1, nSlides), nSlides],
	#             [hotels, range(1, nSlides), nSlides]]
	params = {'allHotel':allHotel}
	#image_urls = get_unsplash_images(query='hotel-rooms'),{'image_urls': image_urls}
	return render(request, 'main.html', params)
			
    



def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id':id})
    return render(request, 'checkout.html')

import requests
from django.shortcuts import render



def get_unsplash_images(query):
    # Replace 'YOUR_CLIENT_ID' with your actual Unsplash API key
    api_key = 'YOUR_CLIENT_ID'
    unsplash_url = f'https://api.unsplash.com/search/photos/?query={hotel-rooms}&client_id={O4yviB4Yeh_HZy0wIdPOlRr2Fx6Wpy_OetItrESRyJ0}'
    response = requests.get(unsplash_url)
    data = response.json()
    
    images = []
    for result in data['results']:
        images.append(result['urls']['regular'])
    
    return images

def your_view(request):
    hotel_images = get_unsplash_images('hotel-rooms')
    return render(request, 'main.html', {'hotel_images': hotel_images})


def get_images(request):
    access_key = 'your_access_key'
    url = f'https://api.unsplash.com/users/samuelzeller/photos&client_id=O4yviB4Yeh_HZy0wIdPOlRr2Fx6Wpy_OetItrESRyJ0&per_page=30'
    response = requests.get(url)
    images = response.json()
    return render(request, 'image.html', {'images': images})

    
