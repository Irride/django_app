from django.shortcuts import render, redirect
from datetime import datetime
from core.models import Feedback_new, Subject, Author
from core.forms import ContactUsForm



def landing_page_view(request):
    # message = request.Get.get('message') 

    # if message:
    #     pass 

    return render(request, "landing_page.html", 
    context = {"name": "iryna", "now": datetime.now(), 
    # "message": message
     })

# def landing_page_view_about(request):
#     return render(request, "landing_page_about.html", 
#     context = {"name": "iryna", "now": datetime.now(), 
#     "Information_about_yourself": {"city": "Rivne", "birthday": "06 of July"},
#      })

def landing_page_view_about(request):
    return render(request, "landing_page_about.html", 
    context = {"name": "iryna", "city": "Rivne", "birthday": "06 of July", "now": datetime.now()
     })


def contact_us_view(request):
    LAST_MESSAGE = "DEFAULT"
    LAST_NAME = "DEFAULT"

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():

            print('PerFECT')
            LAST_MESSAGE = request.POST.get("message22")
            LAST_NAME = request.POST.get("name22")
            
            feedback = Feedback_new.objects.create(name_m=LAST_NAME, text_m=LAST_MESSAGE)  #as in models

            response = redirect('feedbacks')
            response['Location'] += '?from=contact-us'
            return response

            #return redirect('/feedbacks/') # після контакт ас перенапрявляє зразу на фідбекс


    else:
        print('GET method')
        form = ContactUsForm()

    
    # print("Ira")
    return render(
        request,
        "contact_us.html",
        context={
            "message44": LAST_MESSAGE,
            "name44": LAST_NAME,
            'form': form
        },
    )

def feedbacks_view(request):
    has_contacted = bool(request.GET.get('from') == 'contact-us')
    #feedbacks = Feedback_new.objects.all()# показує всі фідбеки
    feedbacks = Feedback_new.objects.filter(is_active=True) # показувати фідбеки тільки по фільтру

    return render(
        request,
        "feedbacks_page.html",
        context={
            "feedbacks": feedbacks,
            "has_contacted": has_contacted
        
        },
    )


def subjects_view(request):
    author_name = (request.GET.get('author'))

    if author_name:
        author_obj = Author.objects.filter(name = author_name).first()
        subjects = Subject.objects.filter(is_active = True, author = author_obj)
        # subjects = Subject.objects.all()

    else:
        subjects = Subject.objects.filter(is_active = True)
        
    return render(
        request,
        "subjects.html",
        context={
            "subjects": subjects
            
        
        },
    )

def subject_item_view(request, subject_name):
    subject_item = Subject.objects.filter(is_active = True, name_bot = subject_name).first()


    return render(
        request,
        "bot.html",
        context={
            "bot": subject_item
            
        
        },
    )