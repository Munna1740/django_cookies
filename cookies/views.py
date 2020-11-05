from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def setcookie(request):
    response = render(request, 'cookies/setcookie.html')
    response.set_cookie('name','Munna', expires = datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):
    name = request.COOKIES.get('name')
    return render(request, 'cookies/getcookie.html', {'name':name})
    
def delcookie(request):
    response = render(request, 'cookies/delcookie.html')
    response.delete_cookie('name')
    return response

#another way to set get and delete cookies

# def setcookie(request):
#     response = render(request, 'cookies/setcookie.html')
#     response.set_signed_cookie('name','Munna', salt='nm' expires = datetime.utcnow()+timedelta(days=2))
#     return response

# def getcookie(request):
#     name = request.get_signed_cookie('name', salt='nm')
#     return render(request, 'cookies/getcookie.html', {'name':name})
    
# def delcookie(request):
#     response = render(request, 'cookies/delcookie.html')
#     response.delete_cookie('name')
#     return response