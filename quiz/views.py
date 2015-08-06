# coding: utf-8
from django.shortcuts import render

# Create your views here.
quizzes = {
	"klassiker": {
   		"name": u"Great!",
	   	"description": u"One person didn't live at the same time as two others. Do you know who?"
	},
}

def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/quizkampenstartsida.html", context)

def quiz(request,slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
	}
	return render(request, "quiz/quizkampen.html", context)

def question(request, slug, number):
	context = {
		"question_number": number,
	    	"question": u"Who didn't live at the same time?",
		"answer1": u"12",
	   	"answer2": u"66 400",
	    	"answer3": u"7 428 954",
	    	"quiz_slug": slug,
	}
	return render(request, "quiz/fragesida.html", context)

def completed(request, slug):
	context = {
	    	"correct": 12,
	    	"total": 20,
			"quiz_slug": slug,
	}
	return render(request, "quiz/resultatsida.html", context)