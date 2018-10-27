from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'misperris/post_list.html', {})