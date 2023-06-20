from django.shortcuts import render
from django.http import HttpResponse
import datetime

conferences = [
        {
            "id": 1,
            "name": "Africa ceo summit",
            "date": "2024-03-12",
            "location": "radisson blu"
        },
        {
            "id": 2,
            "name": "Ubumuntu Arts Festival",
            "date": "2024-8-12",
            "location": " Arena"
        },
        {
            "id": 3,
            "name": "Transform Africa",
            "date": "2024-05-07",
            "location": "kcev"
        },

        {
            "id": 4,
            "name": "Women @ web ",
            "date": "2023-09-5",
            "location": "Serena Hotel"
        },

        {
            "id": 5,
            "name": "Demo day",
            "date": "2025-07-01",
            "location": "amahoro stadium"
        },
    ]
def conferences_view(request):
    return render(request, 'conference/conferences.html', context={"conferences": conferences})