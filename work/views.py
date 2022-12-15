from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed


def index(request):
    return render(request, 'work/index.html')

def predict(request):
    return render(request, 'work/predict.html')

def result(request):
    import numpy as np
    import pickle

    sc = pickle.load(open('sc.pkl', 'rb'))
    model = pickle.load(open('diabetes_model.pkl', 'rb'))

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    input_features = np.array([val1, val2, val3, val4, val5, val6, val7, val8])
    pred = model.predict(sc.transform(input_features.reshape(1, -1)))

    result1 = pred
    if pred == [1]:
        result1 = "당뇨병 같은데, 의사선생님께 문의하세요!"
    else:
        result2 = "건강하신거 같은데, 의사선생님께 확인하세요!"

    return render(request, 'work/result.html', {"result_pred":result1})

def heart(request):
    return render(request, 'work/heart.html')

def run(request):
    import numpy as np
    import pickle

    sc = pickle.load(open('heart_sc.pkl', 'rb'))
    model = pickle.load(open('heart_model.pkl', 'rb'))

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])
    val13 = float(request.GET['n13'])

    input_features = np.array([val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13])
    re = model.predict(sc.transform(input_features.reshape(1, -1)))

    result1 = re
    if re == [1]:
        result1 = "심장마비 증세가 보이는데, 의사선생님께 문의하세요!"
    else:
        result2 = "심장마비 증세는 보이지 않아요! 그래도 의사선생님께 확인하세요!"

    return render(request, 'work/run.html', {"run_result":result1})

def hospital(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'work/hospital.html', context)


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)#Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'work/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('question', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'work/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('hospital')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'work/question_form.html', context)