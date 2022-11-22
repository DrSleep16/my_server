from django.shortcuts import render

def myhome(r):
    return render(r, 'myhome.html')

def reverse(request):
    user_text = request.GET['username']
    reversed_text = user_text[::-1]
    return render(request,
                  'reverse.html',
                  {'word': reversed_text}
                  )
