 
# Create your views here.
from django.shortcuts import render, redirect
from .forms import EmployeeSurveyForm

def survey_view(request):
    if request.method == 'POST':
        form = EmployeeSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'survey/thank_you.html')
    else:
        form = EmployeeSurveyForm()
    return render(request, 'survey/survey_form.html', {'form': form})
