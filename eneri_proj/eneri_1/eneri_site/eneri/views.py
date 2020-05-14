from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from datetime import datetime


# Create your views here.

# def home(request):
#     return(HttpResponse("Hello, You're at the eneri site!!!!"))


def home(request, instance=''):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    # GSUser.objects.get(user_id=request.user.id)
    # real_user = User.objects.get(username=request.user.username)

    # try: # need to check user has access to the instance
    #     instance = GSInstance.objects.get(name= inst)
    #     if not instance in real_user.gsuser.org.instances.all():
    #         instance= real_user.gsuser.default_instance
    # except:
    #     instance= real_user.gsuser.default_instance

    inst = { 'db_instance': 'hotec',
                 'map_instance': 'Operations_Phase',
                }

    return render(
        request,
        'eneri/index.html',
        {
            'title': 'ENER-i',
            'year': datetime.now().year,
            'instance': 'my instance',
            'capabilities': 'instance.capabilities',
            'caps': 'instance.capabilities.getList()',
            'groups': 'real_user.gsuser.user.groups.all()',
            'org': 'real_user.gsuser.org',
            'instances': 'real_user.gsuser.org.instances.all()',
            # TODO: - what is gs for??
            'gs': True,
        }
    )
