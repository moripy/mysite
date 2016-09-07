
from .models import Question
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger,InvalidPage
from django.shortcuts import render_to_response


def index(request):
    latest_question_list = Question.objects.all()
    paginator = Paginator(latest_question_list,4)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        latest_question_list = paginator.page(page)
    except (InvalidPage, EmptyPage):
        latest_question_list = paginator.page(paginator.num_pages)
    return render_to_response("polls/index.html", dict(latest_question_list=latest_question_list, user=request.user))



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


