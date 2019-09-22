from django.http import HttpResponse
from django.shortcuts import render
def convert(s): 
    if(len(s) == 0): 
        return
    s1 = '' 
    s1 += s[0].upper() 
    for i in range(1, len(s)): 
        if (s[i] == ' '): 
            s1 += s[i + 1].upper() 
            i += 1
        elif(s[i - 1] != ' '): 
            s1 += s[i]  
    return(s1)

def index(request):
    return render(request,'index.html')

def form(request):
    inputText=request.POST.get('text','default')
    upper=request.POST.get('uppercase','off')
    lower=request.POST.get('lowercase','off')
    capital=request.POST.get('capitalize','off')
    camel=request.POST.get('camelcase','off')
    analyzed=""
    if upper!='off':
        purpose="Upper Case"
        analyzed=inputText.upper()
    elif lower!='off':
        purpose="Lower Case"
        analyzed=inputText.lower()
    elif capital!='off':
        purpose="First Case"
        analyzed=inputText.capitalize()
    elif camel!='off':
        purpose="Camel Case"
        analyzed=convert(inputText)
    params={'purposed':purpose,'analyzed_text':analyzed}
    return render(request,'analyze.html',params)