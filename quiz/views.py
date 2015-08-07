# coding: utf-8
from quiz.models import Quiz
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
#quizzes = {
#	"klassiker": {
#   		"name": u"Great!",
#	   	"description": u"One person didn't live at the same time as two others. Do you know who?"
#	},
#}

def startpage(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/quizkampenstartsida.html", context)

def quiz(request,slug):
	context = {
		"quiz": Quiz.objects.get(slug=slug),
	}
	return render(request, "quiz/quizkampen.html", context)

def question(request, slug, number):
	number = int(number)
	quiz = Quiz.objects.get(slug=slug)
	questions = quiz.questions.all()
	if number > questions.count():
		return redirect("completed_page", quiz.slug)
	question = questions[number - 1]
	context = {
    		"question_number": number,
    		"question": question.question,
	    	"answer1": question.answer1,
    		"answer2": question.answer2,
	    	"answer3": question.answer3,
	    	"quiz": quiz,
	}
	return render(request, "quiz/fragesida.html", context)

def completed(request, slug):
	context = {
	    	"correct": 12,
	    	"total": 20,
			"quiz_slug": slug,
	}
	return render(request, "quiz/resultatsida.html", context)