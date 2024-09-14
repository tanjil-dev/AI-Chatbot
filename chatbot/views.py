from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import openai

openai.api_key = settings.API_KEY

def ask_openai(message):
    response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "user", "content": message},
    ],
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7,
    )
    
    answer = response.choices[0].message.content

    return answer

# Create your views here.
def chatbot(request):
    template_name = 'chatbot.html'
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, template_name=template_name)