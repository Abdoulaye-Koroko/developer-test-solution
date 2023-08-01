from django.shortcuts import render
from django.http import JsonResponse
from .utils import calculate_odds

def index(request):
    odds = None
    data_file = None
    error_message = None

    if request.method == 'POST':
        data_file = request.FILES.get('data_file')
        if data_file is not None and is_valid_file(data_file):
            odds = calculate_odds(data_file)
        else:
            error_message = "Invalid file. Please upload a valid JSON file."

    return render(request, 'index.html', {'odds': odds, 'data_file': data_file, 'error_message': error_message})

def is_valid_file(file):
    
    return file.name.endswith('.json') 
