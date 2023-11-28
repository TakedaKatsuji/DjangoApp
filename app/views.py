from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.views.generic import TemplateView
from .forms import TestForm

# Create your views here.
def index(request):
    return HttpResponse('文字だけアプリ')

class TestView(TemplateView):

    def __init__(self):
        self.params = {
                'message': 'テストの点数を入力し、計算ボタンを押して下さい。',
                'average': '',
                'form': TestForm(),
            }

    def get(self, request):
        return render(request, 'app/index.html', self.params)

    def post(self, request):
        goal = request.POST['goal']
        ko_score = int(request.POST['kokugo'])
        sa_score = int(request.POST['sannsuu'])
        ri_score = int(request.POST['rika'])
        sya_score = int(request.POST['syakai'])
        ave = (ko_score+sa_score+ri_score+sya_score) / 4
        if goal == '':
            msg = '目標平均点が未入力です。'
        elif int(goal) > ave:
            msg =  '残念！目標平均点は（' + str(goal) + '点）です。'
        else:
            msg =  '目標達成！目標平均点は（' + str(goal) + '点）です。'
        self.params['average'] = ave
        self.params['message'] = msg
        self.params['form'] = TestForm(request.POST)
        return render(request, 'app/index.html', self.params)