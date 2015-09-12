from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.mail import EmailMultiAlternatives
from django.views.generic import FormView

from coming_soon.forms import ClientForm


class ComingSoon(FormView):

    template_name = "coming_soon/main_page.html"
    form_class = ClientForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user = self.object.email_address
        context = Context({"name": user})
        content = loader.get_template('coming_soon/email.html')
        html_content = content.render(context)
        x = EmailMultiAlternatives("Welcome to hoardingswale.com", "", 'noreply@hoardingswale.com', [user])
        x.attach_alternative(html_content, "text/html")
        x.send()

        #self.object.save()
        return HttpResponseRedirect(reverse_lazy("coming_soon:soon"))

