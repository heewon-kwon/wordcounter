from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1
    
    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()})

def result2(request):
    text2 = request.GET['fulltext2']
    words2 = text2.split()
    word_dictionary2 = {}

    for word2 in words2:
        if word2 in word_dictionary2:
            #increase
            word_dictionary2[word2]+=1
        else:
            #add to dictionary
            word_dictionary2[word2]=1
    
    return render(request, 'result2.html', {'full2': text2, 'total2': len(words2), 'dictionary2': word_dictionary2.items()})