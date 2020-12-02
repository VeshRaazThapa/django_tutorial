from django.shortcuts import render
from first_app import views
from first_app.models import Topic,Webpage,AccessRecord

def index(request):
    # my_dict = {'insert_content':"Hello Im from FirstApp!"}
    # return render(request,'first_app/index.html',context=my_dict)
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)


def help(request):
    my_insert = {'insert_help':'i am khan'}
    return render(request,'first_app/help.html',context=my_insert)