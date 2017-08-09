from datetime import datetime

def footer_cp(request):
    """Display data time, name of application and application's version"""
    context = {
                "now": datetime.now(),
                "owner" : "Mariusz Korotko"
              }
    return context