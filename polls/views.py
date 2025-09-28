from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_questions": latest_questions}
    return render(request,"polls/index.html", context)


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/question.html", {"question": question})


def results(request, question_id):
    return HttpResponse("Resultados da pergunta: %s." % question_id)


def votes(request, question_id):
    response = "Votando na pergunta: %s."
    return HttpResponse(response % question_id)
