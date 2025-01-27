from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact

# Create your views here.

def frontpage(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)



        if form.is_valid():

            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            contact = Contact(name=name, number=number, email=email, content=content)
            contact.save()

            message = '''

                Name: {}

                New Message: {}

                Number: {}

                From: {}


            '''.format(name, content, number, email)


            send_mail("Message", message, 'a.paryani@adeptaiagents.com', ['a.paryani@adeptaiagents.com'])

            return redirect('frontpage')
        else:
            return redirect('contact')

    else:
        form = ContactForm()
    return render(request, 'website/frontpage.html', {

        'form': form,}
        )

def about(request):
    return render(request, 'website/about.html')

def we_do(request):
    return render(request, 'website/we_do.html')

def portfolio(request):
    return render(request, 'website/portfolio.html')

def llm_based_ai_agents(request):
    return render(request, 'website/llm_based_ai_agents.html')

def basic_ai_enabled_chatbots(request):
    return render(request, 'website/basic_ai_enabled_chatbots.html')

def deep_learning_nlp(request):
    return render(request, 'website/deep_learning_nlp.html')

def web_development(request):
    return render(request, 'website/web_development.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)



        if form.is_valid():

            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            contact = Contact(name=name, number=number, email=email, content=content)
            contact.save()

            message = '''

                Name: {}

                New Message: {}

                Number: {}

                From: {}


            '''.format(name, content, number, email)


            send_mail("Message", message, 'a.paryani@adeptaiagents.com', ['a.paryani@adeptaiagents.com'])

            return redirect('contact')
        else:
            return redirect('contact')

    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {
        'form': form,
    })

def handler404(request):
    return render(request, 'website/404.html')