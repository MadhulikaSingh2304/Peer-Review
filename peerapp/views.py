from django.shortcuts import render, redirect
from django.views import View
from .models import Person, Rating, Team
from django.http import Http404, HttpResponse
from django.db.models import F, FloatField
from django.db.models.functions import Cast, Coalesce
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import re

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        usn = request.POST.get('usn')
        batch = request.POST.get('batch')

        print(name)
        print(usn)

        context = {
            'name': name,
            'usn': usn,
            'batch': batch,
        }
        return render(request, 'index2.html', context)
       

class Review(View):
    def get(self, request, *args, **kwargs):
        batch = request.GET.get('batch')
        name = request.GET.get('name')
        usn = request.GET.get('usn')
        print(name)
        print(usn)
        usn=usn.upper()
        name=name.title()
        try:
            person = Person.objects.get(usn__exact=usn.strip())
            if person.batch.batch == batch:
                teammates = Person.objects.filter(batch__batch=batch).exclude(name__exact=name.strip(), usn__exact=usn.strip())
                context = {
                    'teammates': teammates,
                    'batch': batch,
                }
                return render(request, 'index2.html', context)
            else:
                error_message = 'The provided USN does not belong to the specified batch.'
                return render(request, 'index.html', {'error_message': error_message})
        except Person.DoesNotExist:
            error_message = 'No person found with the provided USN.'
            return render(request, 'index.html', {'error_message': error_message})
        teammates = Person.objects.filter(batch__batch=batch).exclude(name__exact=name.strip(), usn__exact=usn.strip())
        context = {
            'teammates': teammates,
            'batch': batch,
        }
        if teammates.exists():
            return render(request, 'index2.html', context)
    
    def post(self, request, *args, **kwargs):
        batch = request.POST.get('batch')  # Retrieve the batch value from the form
        name = request.POST.get('name')  # Retrieve the name value from the form
        usn = request.POST.get('usn')  # Retrieve the usn value from the form

        # Retrieve the total number of team members for the batch
        total_members = Person.objects.filter(batch__batch=batch).count()

        # Loop through the submitted ratings and update the existing ratings in the database
        for key, value in request.POST.items():
            if key.startswith('rating_'):
                teammate_usn = key.split('rating_')[1]  # Extract the teammate's USN from the key
                rating_value = int(value)  # Convert the rating value to an integer

                # Get the teammate's Rating object or create a new one if it doesn't exist
                rating, created = Rating.objects.get_or_create(usn__usn=teammate_usn, defaults={'rating': 0})

                # Update the rating by adding the newly given rating value
                #rating.rating = F('rating') + rating_value
                #rating.save()
                 # Calculate the remaining rating space available
                remaining_rating = 15 - rating.rating

                # Check if the rating value exceeds the remaining rating space
                if rating_value > remaining_rating:
                    # Handle the error, such as displaying an error message
                    error_message = "The total rating cannot exceed 15."
                    # ... Handle the error, such as displaying it on the form page
                else:
                    # Update the rating by adding the newly given rating value
                    rating.rating = F('rating') + rating_value
                    rating.save()

        # Calculate the average rating for each teammate
        for teammate_usn in request.POST.keys():
            if teammate_usn.startswith('rating_'):
                teammate_usn = teammate_usn.split('rating_')[1]  # Extract the teammate's USN
                teammate_rating = Rating.objects.get(usn__usn=teammate_usn)
                teammate_rating.average_rating = Cast(teammate_rating.rating / (total_members - 1), output_field=FloatField())
                teammate_rating.save()

        return render(request, 'index.html')
        
