from django.shortcuts import render
from django.http import HttpResponseRedirect
from webtunesapp.models import Entry
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your views here.
from django.http import HttpResponse
# Imaginary function to handle an uploaded file.


def index(request):
    return render(request, 'webtunesapp/home.html')

def upload(request):
    return render(request, 'webtunesapp/upload.html')

def success(request):
    if request.method != "POST":
        return HttpResponseRedirect('/')

    try:
        song_name = request.POST['song_name']
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name,file)
        uploaded_file_url = fs.url(filename)
        print("The song name is: " + filename)

        E = Entry.objects.create(unique_number=0,set_to_expire="n",file_name=song_name, audio_file=file)
        song_id = E.id
        print("The song id is: " + str(song_id))
        return render(request, 'webtunesapp/success.html', {'song_id': song_id})
    except:
        return HttpResponseRedirect('/error')


def retrieve(request):
    return render(request, 'webtunesapp/retrieve.html')

def play(request):
    if request.method != "POST":
        return HttpResponseRedirect('/')

    try:
        code_number = request.POST['code_number']

        print("The code number is " + code_number)

        song_entry = list(Entry.objects.filter(id=code_number))
        print(song_entry)

        return render(request, 'webtunesapp/play.html', {'song_entry': song_entry})
    except:
        #return HttpResponseRedirect('/error')
        return render(request, 'webtunesapp/play.html', {'song_entry': song_entry})


def error(request):
    return render(request, 'webtunesapp/error.html')