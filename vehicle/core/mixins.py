from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import AccessMixin


class LoggedInUserRedirectMixin(AccessMixin):
    template_name = 'frontend/index.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user:
                return HttpResponseRedirect('/home/')
            else:
                return super(LoggedInUserRedirectMixin, self).dispatch(
                    request, *args, **kwargs)
        else:
            return super(LoggedInUserRedirectMixin, self).dispatch(
                request, *args, **kwargs)
