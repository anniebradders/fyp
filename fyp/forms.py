from django import forms

class PredictionForm(forms.Form):
    #field1 = forms.CharField(label='Race Progress', max_length=100)
    #field2 = forms.CharField(label='Remaining pit stops', max_length=100)
    #field3 = forms.CharField(label='Location', max_length=100)
    #field4 = forms.CharField(label='Fufilled second pitstop', max_length=100)
    #field5 = forms.CharField(label='Number of avaliable compounds', max_length=100)

        # Slider field for percentage (0.00 to 1.00)

        # Dropdown for locations
    model_choices = [
        ('./models/RNN_model.h5', 'RNN'), ('./models/LSTM_model.h5', 'LSTM'), ('./models/ANN_model.h5', 'ANN'),
        ('./models/CNN_model.h5', 'CNN'), ('./models/ANN_hyper_model.h5', 'ANN Hyper Tuned Model')
    ]
    field6 = forms.ChoiceField(choices=model_choices, label='Select Model')
    
    field1 = forms.FloatField(widget=forms.NumberInput(attrs={
        'type': 'range', 
        'step': '0.01', 
        'min': '0', 
        'max': '1', 
        'id': 'percentage_slider',  # Javascript ID
    }), label='Race Progress')
    
    # Dropdown for selecting 1, 2, or 3
    field2 = forms.ChoiceField(choices=[(0, '0'),(1, '1'), (2, '2'), (3, '3')], label='Remaining pit stops')
    
    # Dropdown for locations
    location_choices = [
        ('Melbourne', 'Melbourne'), ('KualaLumpur', 'Kuala Lumpur'), ('Sakhir', 'Sakhir'),
        ('Shanghai', 'Shanghai'), ('Catalunya', 'Catalunya'), ('MonteCarlo', 'Monte Carlo'),
        ('Montreal', 'Montreal'), ('Spielberg', 'Spielberg'), ('Silverstone', 'Silverstone'),
        ('Hockenheim', 'Hockenheim'), ('Budapest', 'Budapest'), ('Spa', 'Spa'),
        ('Monza', 'Monza'), ('Singapore', 'Singapore'), ('Sochi', 'Sochi'),
        ('Austin', 'Austin'), ('SaoPaulo', 'Sao Paulo'), ('YasMarina', 'Yas Marina'),
        ('Suzuka', 'Suzuka'), ('MexicoCity', 'Mexico City'), ('Baku', 'Baku'),
        ('LeCastellet', 'Le Castellet')
    ]
    field3 = forms.ChoiceField(choices=location_choices, label='Select Location')
    
    # Boolean choice field (True/False)
    field4 = forms.BooleanField(required=False, label='Fufilled second pitstop')
    
    # Dropdown for selecting from 1 to 5
    field5 = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)], label='Number of avaliable compounds')