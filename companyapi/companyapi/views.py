
from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    welcome=['welcome to galgotias university',
             'Thanku for visiting here'
    ]

    return JsonResponse(welcome,safe=False)