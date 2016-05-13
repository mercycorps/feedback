#from django.contrib.sites.models import Site


def base_context_processor(request):
    """
    This allows for getting the absolute and full URL for a given object in templates
    Usage:
        <a href="{{ BASE_URL }}{{ obj.get_absolute_url }}">Object Name</a>
    """
    """
    return {
        'BASE_URL': "http://%s" % Site.objects.get_current().domain
    }
    """
    # or if you don't want to use 'sites' app
    return {
        'BASE_URL': request.build_absolute_uri("/").rstrip("/")
    }
