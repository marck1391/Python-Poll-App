from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Question

def index(request):
	questions = Question.objects.order_by('-pub_date')[:5]
	data = {
		'question_list': questions
	}
	return render(request, 'polls/index.html', data)

def detail(request, question_id):
	question = get_object_or_404(Question, id=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	return HttpResponse("Question results: %s"%question_id)

def vote(request, question_id):
	return JsonResponse({'test':'json'})