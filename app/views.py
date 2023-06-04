from django.shortcuts import render
<<<<<<< HEAD
from django.http import JsonResponse, HttpResponse
from .functions import fnBuildBrain, fnAskQuestion, handle_uploaded_file
# Create your views here.
answer = ""
=======
from django.http import JsonResponse
from .functions import fnBuildBrain, fnAskQuestion, handle_uploaded_file
# Create your views here.
>>>>>>> main
def fnBuildSecondBrain(request):
    if request.method == "POST":
        try:
            api_key = request.POST["api-key"]
            if api_key == "":
                return render(request, "index.html", context={"error":"API Key is Blank"})
        except:
            return render(request, "index.html", context={"error":"API Key is Blank"})
        try:
            f = request.FILES['file']
        except:
            return render(request, "index.html", context={"error":"You didn't upload file", "api_key":api_key})

        input_text = handle_uploaded_file(f)
<<<<<<< HEAD
        print("input_text", input_text)
=======
>>>>>>> main
        result = fnBuildBrain(api_key, input_text)
        if result == False:
            return render(request, "index.html", context={"error":"This API Key can't work now. Please use other api key"})
        return render(request, "index.html", context={"data":"Second Brain is trained", "api_key":api_key})
    return JsonResponse({"response":"success"})

def fnQA(request):
<<<<<<< HEAD
    global answer
=======
>>>>>>> main
    if request.method == "POST":    
        chunks = 10000
        try:
            api_key = request.POST["api-key_hidden"]
            if api_key == "":
                return render(request, "index.html", context={"error":"API Key is Blank", "chunk":chunks})
        except:
            return render(request, "index.html", context={"error":"API Key is Blank", "chunk":chunks})
        try:
            chunks = int(request.POST["chunk_size"])
        except:
            return render(request, "index.html", context={"error":"Please input chunks size", "api_key":api_key, "chunk":chunks})
        try:
            question = request.POST["question"]
            if question == "":
                return render(request, "index.html", context={"error":"Question is Blank", "api_key":api_key, "chunk":chunks})
        except:
            return render(request, "index.html", context={"error":"Please input question", "api_key":api_key})
        answer = fnAskQuestion(api_key, question, chunk_size=chunks)
<<<<<<< HEAD
        if answer == "":
            return render(request, "index.html", context={"error":"This API Key can't work now. Please use other api key"})
        return render(request, "index.html", context={"result":answer, "api_key":api_key, "question":question, "chunk":chunks})
    return JsonResponse({"response": "success"})

def download_text(request):
    global answer
    try:
        # Create the HttpResponse object with the generated text file
        response = HttpResponse(answer, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="generated_text.txt"'
        answer = ""
    except:
        response = HttpResponse(generated_text, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="blank.txt"'
    return response
=======
        if answer == False:
            return render(request, "index.html", context={"error":"This API Key can't work now. Please use other api key"})
 
        return render(request, "index.html", context={"result":answer, "api_key":api_key, "question":question, "chunk":chunks})
    return JsonResponse({"response": "success"})
>>>>>>> main
