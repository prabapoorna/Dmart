'''
Created on 15-May-2019

@author: sudhirk
'''


from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello world')