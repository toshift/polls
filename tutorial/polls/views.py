from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html' ,{ 'questin':question })

def results(request, question_id):
    response = "あなたは %s 番のQuestionの結果を見てる"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("あなたは %s 番目のQuestionに投票する" % question_id)

