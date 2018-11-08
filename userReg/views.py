from django.shortcuts import render

# Create your views here.

def reg(request):
	return render(request,'index.html')

def add_acc(request):
	if request.method=='POST':
		uname=request.POST.get('username')
		upassword=request.POST.get('password')
		email=request.POST.get('email')
		gender=2
		avatar=request.FILES.get('avatar')

	return HttpResponse('ok')
		