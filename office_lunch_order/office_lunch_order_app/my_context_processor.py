from datetime import datetime

def footer_cp(request):
    """Display data time and name of application"""
    context = {
        "now": datetime.now(),
        "application": "Lunch time",
        "version": "1.0"
    }
    return context