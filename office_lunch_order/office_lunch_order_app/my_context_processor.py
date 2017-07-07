from datetime import datetime

def footer_cp(request):
    """Display data time, name of application and application's version"""
    context = {
        "now": datetime.now(),
        "application": "Lunch time",
        "version": "1.0"
    }
    return context