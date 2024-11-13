# views.py
from django.shortcuts import render
import pandas as pd
from .models import Session

def session_list(request):
    # Read CSV file
    df = pd.read_csv('sessions.csv')
    
    # Convert to list of dictionaries
    sessions = df.to_dict('records')
    return render(request, 'sessions/session_list.html', {'sessions': sessions})