from django.shortcuts import render
from .models import QuestionAnswer


def chatGpt(request):
    question=''
    if request.method=='POST':
        question=request.POST.get('question')
        response=QuestionAnswer.objects.filter(question=question).first()
        return render(request, 'answer.html', {'chat':response})
    return render(request,'index.html')

