from django.http import HttpResponseRedirect


def index(request):
    if request.user.is_authenticated():
        url = "/{0}/".format(request.user.user_category.slug)
        return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect("/auth/login/")
