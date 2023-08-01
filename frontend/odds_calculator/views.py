from django.shortcuts import render
from django.http import JsonResponse
import json

from odds_calculator.utils import calculate_odds


def index(request):
    """
    A view function that reads the uploaded JSON file and compute the odds.
    
    Parameters:
    -----------
        request: request
        
    Returns:
    --------
    Render a view and a dict containing the computed odds, the name of the uploaded
    JSON file and eventually an error message if the uploaded file is invalid.
    """
    odds = None
    data_file = None
    error_message = None
    if request.method == 'POST' and request.FILES.get('data_file'):
        data_file = request.FILES['data_file']
        try:
            data_dict = json.load(data_file)
            odds = calculate_odds(data_dict)
        except:
            error_message = "Invalid file. Please upload a valid JSON file."
            
    return render(request, 'index.html', {'odds': odds, 'data_file': data_file, 'error_message': error_message})


