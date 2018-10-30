from django.shortcuts import render
from .models import Aktiviti
from .forms import AktivitiForm

# Create your views here.

# Home penganjur
def home(request):
	
	# aktivitiid = request.GET['aktivitiid']
	print(request.GET['aktivitid'])
	# List of records
	a = Aktiviti.objects.all()
	for ak in a:
		print(ak.tajuk,ak.tempat,ak.penceramah)

	return render(request,'penganjur/home.html')


# update aktiviti
def update_aktiviti(request,pk):
	#dptkan id aktiviti dan cari rekod
	aktiviti = get_object_or_404(Aktiviti,pk)
	aktiviti = Aktiviti(tajuk='Not Cheddar Update', 
		tempat='Anyplaces Update',
		penceramah='Anybody Update',
		hadpeserta=20,
		)
	aktiviti.save()

	return render(request,'penganjur/home.html')

# tambah aktiviti
def add_aktiviti(request):
	
	# Tambah data setiap kali request 
	akt = Aktiviti(tajuk='Not Cheddar', 
		tempat='Anyplaces',
		penceramah='Anybody',
		hadpeserta=0,
		)
	akt.save()

	return render(request,'penganjur/home.html')

# delete aktiviti
def delete_aktiviti(request,pk):
	
	#dptkan id aktiviti dan cari rekod
	aktiviti = get_object_or_404(Aktiviti,pk)
	
	#confirm delete
	aktiviti.delete()

	return render(request,'penganjur/home.html')


# tambah aktiviti
def addaktiviti(request):
	print(request.method)
	if request.method == "POST":
		pass # temporary kosongkan
		# form = AktivitiForm(request.POST)
		# if form.is_valid():
			

	else:	
		form = AktivitiForm()
		# print(form)
	return render(request,'penganjur/tambahaktiviti.html', { 'form' : form } )