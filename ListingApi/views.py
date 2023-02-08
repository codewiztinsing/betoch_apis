from django.shortcuts import render






def LandingView(request):
	return render(request,'index.html',{})