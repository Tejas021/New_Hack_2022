from django.shortcuts import render, redirect
from django.contrib import messages
from mail_templated import send_mail
# from django.core.mail import send_mail
from django.views.generic import ListView, FormView, TemplateView
from main.models import CompanyInfo, StudentForm, SiteConfig
from main.forms import TeamRegForm
from django.template.loader import render_to_string
from django.views.generic import CreateView
from django.urls import reverse_lazy

import datetime
from django.conf import settings
# Create your views here.
# class IndexView(TemplateView):
#     template_name = 'main/index.html'


def IndexView(request):
    # homepage countdown timer
    timer_flag = False
    TWITTER_TIMELINE_SHOW_DATE_TIME = settings.TWITTER_TIMELINE_SHOW_DATE_TIME
    if TWITTER_TIMELINE_SHOW_DATE_TIME > datetime.datetime.now():
        timer_flag = True

    # homepage live upadates section
    try:
        site_cfg = SiteConfig.objects.get(id=1)
        timeline_flag = site_cfg.live_updates_section
        youtube_url = site_cfg.youtube_embed_url
        twitter_url = site_cfg.twitter_embed_url
    except:
        timeline_flag = False
        youtube_url = settings.YT_URL
        twitter_url = settings.TWITTER_URL
        # print("diff",TWITTER_TIMELINE_SHOW_DATE_TIME - datetime.datetime.now() )
    return render(request, 'main/index.html', {'displayTimer': timer_flag, 'displayTimeline': timeline_flag, 'yt_url': youtube_url, 'tw_url': twitter_url})


class CompanyProblemsList(ListView):
    template_name = 'main/problems_list.html'
    model = CompanyInfo
    context_object_name = 'problems'


class StudentFormView(CreateView):
    model = StudentForm
    form_class = TeamRegForm
    template_name = 'main/form.html'
    success_url = reverse_lazy('student_form')

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Please correct the errors in the form.')
        return super(StudentFormView, self).form_invalid(form, *args, **kwargs)

    def form_valid(self, form, *args, **kwargs):
        instance = form.save(commit=False)
        # instance.problem_statement_1 = form.cleaned_data['problem_statement_1']
        # instance.problem_statement_2 = form.cleaned_data['problem_statement_2']
        # instance.problem_statement_3 = form.cleaned_data['problem_statement_3']
        # instance.problem_statement_4 = form.cleaned_data['problem_statement_4']

        arr = ["1","2","3","4","5"]
        # print(type(form.cleaned_data['problem_statement_1_preference']))
        # print(form.cleaned_data['problem_statement_1_preference'])
        for i in range(1,6):
            temp = form.cleaned_data[f'problem_statement_{i}_preference']
            if temp in arr:
                arr.remove(temp)
            # print(arr)
        if len(arr)!=0:
            messages.error(self.request, 'Please make sure you have a unique preference for each problem')
            return super(StudentFormView, self).form_invalid(form, *args, **kwargs)
            # return super(StudentFormView, self).form_invalid(form, *args, **kwargs)
        email_address = form.cleaned_data['team_leader_email']
        # changed from email "vcet.hackathon@vcet.edu.in" -> "hackathon@vcet.me"
        send_mail('email/confirmation.tpl',
                  {'team_leader': form.cleaned_data['team_leader_name']}, 'vcet.hackathon@vcet.edu.in', [email_address, ])
        messages.success(
            self.request, 'Form submitted successfully. We have sent you an email about further details. If you dont see the email, please check the spam folder or contact us.')
        instance.save()
        return super(StudentFormView, self).form_valid(form, *args, **kwargs)


def email(request):
    '''Test email functionality'''
    send_mail('email/confirmation.tpl', {'team_leader': 'Tushar'}, 'vcet.hackathon@vcet.edu.in', ['tushar.192034101@vcet.edu.in',])
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'hackathon@vcet.me',
    #     ['ravilamkoti@gmail.com'],
    #     fail_silently=False,
    # )
    return render(request, 'main/email.html', {})
