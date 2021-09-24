# -*- coding: utf-8 -*-


"""
@File    : contacts.py
@Time    : 2021/9/15 4:50 下午
@Author  : xxlaila
@Software: PyCharm
"""
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.urls import reverse_lazy
from ..models.contacts import *
from ..models.comgroup import *
from ..models.tacstsgroup import *
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from ..forms.contacts import *
from django.shortcuts import (
    render, redirect
)
from django.http import JsonResponse


class ContactsListView(TemplateView):
    """
    contacts list
    """
    template_name = 'commbook/_contacts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts_lists = Contacts.objects.all()
        context['contacts_lists'] = contacts_lists

        return context

class ContactsAddView(CreateView):
    model = Contacts
    template_name = 'commbook/_contacts_create.html'
    form_class = ContactsForm

class ContactsUpdateView(UpdateView):
    model = Contacts
    form_class = ContactsForm
    template_name = 'commbook/_contacts_update.html'

    def get(self, request, *args, **kwargs):
        adv_user = Contacts.objects.get(id=self.kwargs['pk'])
        initial = {'name': adv_user.name, 'sex': adv_user.sex, 'mobile': adv_user.mobile, 'birthday': adv_user.birthday,
                   'appellative': adv_user.appellative, 'qq': adv_user.qq, 'email': adv_user.email,
                   'units': adv_user.units, 'address': adv_user.address, 'comment': adv_user.comment}
        form = self.form_class(initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        adv_user = Contacts.objects.get(id=self.kwargs['pk'])
        adv_user.name = request.POST.get('name')
        adv_user.comment = request.POST.get('comment')
        adv_user.save()
        return redirect('api-commbook:contact-list:')

class ContactsDeleteView(DeleteView):
    def get(self, request, *args, **kwargs):
        adv_user = Contacts.objects.get(id=self.kwargs['pk'])
        adv_user.delete()
        return redirect('api-commbook:contact-list:')

class ContactsDetailView(DetailView):
    model = Contacts
    template_name = 'commbook/_contacts_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            adv_id = Tacstsgroup.objects.filter(user_id=self.kwargs['pk']).values_list('id','group__name')
            if adv_id:
                context['groups'] = adv_id
        except Tacstsgroup.DoesNotExist:
            raise ValidationError("None")
        context['new_groups'] = Comgroup.objects.values_list('id', 'name')
        return context

    def post(self, request, *args, **kwargs):
        # g_name = request.POST['usergroup']
        g_name =request.POST.get('usergroup')
        g_id = Comgroup.objects.filter(name=g_name).first()
        try:
            u_group = Tacstsgroup.objects.get(user_id=self.kwargs['pk'])
            u_group.group_id = g_id.id
            u_group.save()
            return JsonResponse({"status": "success"})
        except Tacstsgroup.DoesNotExist:
            data = {"group_id": g_id.id, "user_id": self.kwargs['pk']}
            try:
                Tacstsgroup.objects.update_or_create(**data)
                return JsonResponse({"status": "success"})
            except Exception as e:
                return JsonResponse({"status": "error"})