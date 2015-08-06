from django.shortcuts import render

# Create your views here.
def startpage(request):
	return render(request, "quiz/quizkampenstartsida.html")

def quiz(request):
	return render(request, "quiz/quizkampen.html")

def question(request):
	return render(request, "quiz/fragesida.html")

def completed(request):
	return render(request, "quiz/resultatsida.html")