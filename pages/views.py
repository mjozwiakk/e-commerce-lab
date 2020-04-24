from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})
    
def contact_view(request, *args, **kwargs):
    my_context = {
        "title": "contact page text",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [123, 312, 1221, 123, "abc"],
        "my_html": "<h1>Hello World!</h1>",
    }
    return render(request, 'contact.html', my_context)
    