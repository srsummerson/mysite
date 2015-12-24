from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Question

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]  # returns 5 most recently published questions
	template = loader.get_template('polls/index.html')  # defines template to use for this view
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
		})
	return HttpResponse(template.render(context))

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)  # either the question or a 404 exception error
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
