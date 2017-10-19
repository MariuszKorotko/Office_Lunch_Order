import datetime


def footer_cp(request):
    """Display data time and first and last name of the owner."""
    context = {
                "now": datetime.datetime.now(),
                "owner": "Mariusz Korotko",
              }
    return context
