from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    param={'name':'Mohit'}
    return render(request,'index.html',param) #render templates
    #return HttpResponse('<a href="http://127.0.0.1:8000/about">About</a><a href="http://127.0.0.1:8000/help">Help</a>')

def about(request):
    #get the text message
    d_text=request.POST.get('text','default')
    #Check checkbox values
    analyze=request.POST.get('analyze','off')
    count_char=request.POST.get('count_char','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    capital=request.POST.get('capital','off')
    newlineremover=request.POST.get('newlineremover','off')
    #if checkbox is on
    if analyze=="on":
        remove_a='a'
        a_text=""
        for char in d_text:
            if char not in remove_a:
                a_text=a_text+char
        param={'analyze_data':'Data','a_text':a_text}
        d_text=a_text
        #return render(request,'analyze.html',param)

    if capital=="on":
        a_text=""
        for char in d_text:
            a_text=a_text+char.upper()
        param={'analyze_data':'changed in Uppercase','a_text':a_text}
        d_text=a_text
        #return render(request,'analyze.html',param)

    if count_char=="on":
        count=0
        for char in d_text:
            if not(char==' '):
                count=count+1
        param={'analyze_data':'Total no. of character','a_text':count}
        #return render(request,'analyze.html',param)

    if extraspaceremover=="on":
        a_text=""
        for index,char in enumerate(d_text):
            if not(d_text[index]==' ' and d_text[index+1]==' '):
                a_text=a_text+char
        param={'analyze_data':'have remove extra space ','a_text':a_text}

    if extraspaceremover!="on" and count_char!="on" and capital!="on":
        return HttpResponse("Please select any option and try again")

    return render(request,'analyze.html',param)

def help(request):
    return HttpResponse('What can i help you Search in <a href="https://www.google.com">Google</a>'
                        ' Log in <a href="https://www.facebook.com">Facebook</a>'
                        '<a href="/">back</a>')


