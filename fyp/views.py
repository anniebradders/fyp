from django.http import HttpResponse
from .fyp import make_prediction 
from django.shortcuts import render, redirect
from .forms import PredictionForm

def fyp(request):
    # Extract user parameters from request
    # For simplicity, let's assume parameters are passed as query parameters
    param1 = request.GET.get('param1')
    param2 = request.GET.get('param2')
    
    # Convert parameters as needed, then make prediction
    prediction = make_prediction(param1, param2)
    
    # Return prediction as HTTP response
    return HttpResponse(f'The prediction is: {prediction}')

def prediction_view(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Call make_prediction with the cleaned data
            result = make_prediction(form.cleaned_data['field1'], form.cleaned_data['field2'], form.cleaned_data['field3'], form.cleaned_data['field4'], form.cleaned_data['field5'], form.cleaned_data['field6'])
            print("Result:", result)
            # Pass the result to your template
            return render(request, './home.html', {'form': form, 'result': result})
    else:
        form = PredictionForm()
    return render(request, './home.html', {'form': form})