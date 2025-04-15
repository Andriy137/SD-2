from django.shortcuts import render

from .forms import RegistrationForm
from .models import Question

def question_list(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'question_list.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:question_list')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
