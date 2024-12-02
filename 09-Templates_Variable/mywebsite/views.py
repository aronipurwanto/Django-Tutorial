from django.shortcuts import render

def index(request):
	context = {
		'judul':'Belajar Django Asyik',
		'kontributor':'Lutfi',
		'durasi':'5 Hari Bro'
	}
	return render(request,'index.html', context)
