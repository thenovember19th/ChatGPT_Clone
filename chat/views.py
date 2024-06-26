from django.shortcuts import render
from openai import OpenAI
from .models import QuestionAnswer


def chatGpt(request):
    api_key = "Your OpenAI API Key"
    
    question=''
    if request.method=='POST':
        client = OpenAI(api_key=api_key)
        question=request.POST.get('question')

        # hamro_response=QuestionAnswer.objects.filter(question__icontains=question).first()
        # if hamro_response:
        #     return render(request, 'answer.html', {'chat':hamro_response})
        # else:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "chat with openai"
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.7,
            max_tokens=150
        )
        print(response)
        content=response.choices[0].message.content
        data=QuestionAnswer.objects.create(question=question, answer=content)
        return render(request,'answer.html',{'question':question, 'answer':content})

    return render(request,'index.html')

