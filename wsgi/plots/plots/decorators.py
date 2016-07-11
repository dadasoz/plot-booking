from django.http import HttpResponseRedirect


def is_logged_in(function):
    def wrap(request, *args, **kwargs):
        if request.user:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/auth/login/')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
