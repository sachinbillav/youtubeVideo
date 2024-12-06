from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from pytubefix import YouTube
# Create your views here.
from django.template import loader
from .logic import downloadLogic, viewLogic
def index(request):
    if request.method == 'POST':
        # Get the value of a specific field
        name = request.POST.get('youtube_link')
        #print("type",request.POST.get('action'))
        if request.POST.get('action') == "view":
            array = viewLogic(name)
            template = loader.get_template('home.html')
            context = {
            'title': array[0],
            'link' : name,
            'thumbnail': array[1]
                        }
            if array == "ERROR":
                context = {
                'title': "Video Not Found",
                'link' : "",
                'thumbnail': "https://img.icons8.com/ios/50/nothing-found.png"
                        }
            return HttpResponse(template.render(context, request))
        if request.POST.get('action') == "download":
            #print("downlaoding")
            return FileResponse(open(YouTube(name).streams.first().download(skip_existing=True),'rb'), as_attachment=True)
    else:
        # Render the initial form
        return render(request, 'home.html')




