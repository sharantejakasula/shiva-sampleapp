from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt  # Disabling CSRF for demonstration purposes, use appropriate CSRF handling in production
def index(request):
    return render(request, 'index.html')

@csrf_exempt  # Disabling CSRF for demonstration purposes, use appropriate CSRF handling in production
def vendor(request):
    return render(request, 'Vendor.html')

@csrf_exempt  # Disabling CSRF for demonstration purposes, use appropriate CSRF handling in production
def handle_button_click(request):
    if request.method == 'POST':
        button_type = request.POST.get('type')

        # Perform actions based on button type
        # Example actions:
        if button_type == 'vendor':
            pass
        elif button_type == 'support':
            # Perform SAP support team-related actions
            pass
        elif button_type == 'user':
            # Perform business user-related actions
            pass

        # Return JSON response (if needed)
        return JsonResponse({'message': f'Button clicked: {button_type}'})
    else:
        return JsonResponse({'error': 'Invalid request method'})