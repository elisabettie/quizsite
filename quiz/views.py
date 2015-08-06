# coding: utf-8
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

quizzes = {
	"klassiker": {
   		"name": u"Klassiska böcker",
	   	"description": u"Hur bra kan du dina klassiker?"
	},
	"fotboll": {
	   	"name": u"Största fotbollslagen",
	   	"description": u"Kan du dina lag?"
	},
	"kanda-hackare": {
	    	"name": u"Världens mest kända hackare",
	    	"description": u"Hackerhistoria är viktigt, kan du den?"	},
}