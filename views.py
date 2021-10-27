from django.shortcuts import render
from . import stories


def home_page(request):
    for story in stories.stories:
        story['desc'] = story['text'][:120]

    return render(request, 'index.html', {'stories': stories.stories})
