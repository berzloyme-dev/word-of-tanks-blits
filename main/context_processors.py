from .models import Nation

def nations_processor(request):
    return {
        'nations': Nation.objects.all()
    }
