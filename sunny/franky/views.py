from django.shortcuts import render

# Create your views here.

from .models import TestUserMessage


def getform(request):
    message = None

    all_messages = TestUserMessage.objects.filter(name='bobbytest')

    if all_messages:
        message = all_messages[0]

    # all_messages.delete()
    # for message in all_messages:
    #     message.delete()
        # print(message.name)

    # if request.method == "POST":
    #     name = request.POST.get('name','')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = TestUserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.save()
    #
    #
    return render(request,'test_form.html',{'my_message':message})