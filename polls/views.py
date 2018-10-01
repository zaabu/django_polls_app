from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic




# Create your views here.

#from django.http import HttpResponse
#from django.template import loader 

from .models import Question, Choice

#FUNCTION-BASED VIEWS

#django views return either an HttpResponse or an http exception e.g 404

# def index(request):
#     #return HttpResponse("Hello World, You are at the polls index")
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]

#     #display raw data
#     '''
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
#     '''
#     #loading data using loader - method 1
#     '''
#     #get template
#     template = loader.get_template('polls/index.html')
#     #get data
#     context = {
#         'latest_question_list': latest_question_list,
#     }
    
#     #pass data into template
#     return HttpResponse(template.render(context, request))
#     '''
#     # using render - method 2
#     context = {'latest_question_list': latest_question_list}
#     # request, template file, data to display inside template
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     #return HttpResponse("You're looking at question %s." %question_id)
#     '''
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#     '''
#     #get object or return 404 error
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     # response = "You are looking at the results of question %s." 
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     #return HttpResponse("You're voting on question %s." %question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.

#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five oublished questions. """
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question 
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." %question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


