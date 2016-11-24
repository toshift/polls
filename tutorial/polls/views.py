from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("ビューのインデックス関数のレスポンス")

def detail(request, question_id):
    return HttpResponse("あなたは %s 番のQuestionを見ています" % question_id)

def results(request, question_id):
    response = "あなたは %s 番のQuestionの結果を見てる"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("あなたは %s 番目のQuestionに投票する" % question_id)
