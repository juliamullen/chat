from django.shortcuts import render

def chat_list(request):
    return render(request, 'chat/post_list.html', {})
