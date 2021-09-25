# -*- coding: utf-8 -*-
"""
@File    : comgroup.py
@Time    : 2021/9/15 4:50 下午
@Author  : xxlaila
@Software: PyCharm
"""
from django.views.generic import TemplateView
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from ..models.tacstsgroup import *
from django.utils import timezone
from ..forms.comgroup import *
from ..forms.contacts import *
from django.shortcuts import (
    render, redirect
)
from django.http import JsonResponse
import logging

class ComgroupListView(TemplateView):
    """
    comgroup list
    """
    template_name = 'commbook/_comgroup_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_lists = Comgroup.objects.all()
        context['group_lists'] = group_lists

        return context

class ComgroupAddView(CreateView):
    model = Comgroup
    template_name = 'commbook/_comgroup_create.html'
    form_class = ComgroupForm
    # success_url = reverse_lazy('commbook:comgroup-list')

class ComgroupUpdateView(UpdateView):
    model = Comgroup
    form_class = ComgroupForm
    template_name = 'commbook/_comgroup_update.html'

    def get(self, request, *args, **kwargs):
        adv_group = Comgroup.objects.get(id=self.kwargs['pk'])
        initial = {'name': adv_group.name, 'comment': adv_group.comment}
        form = self.form_class(initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        adv_group = Comgroup.objects.get(id=self.kwargs['pk'])
        adv_group.name = request.POST.get('name')
        adv_group.comment = request.POST.get('comment')
        adv_group.save()
        return redirect('commbook:comgroup-list')


class ComgroupDeleteView(DeleteView):
    def get(self, request, *args, **kwargs):
        adv_group = Comgroup.objects.get(id=self.kwargs['pk'])
        adv_group.delete()
        t_group = Tacstsgroup.objects.get(group_id=self.kwargs['pk'])
        t_group.delete()
        return redirect('commbook:comgroup-list')

class ComgroupDetailView(DetailView):
    model = Comgroup
    template_name = 'commbook/_comgroup_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ComgroupDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['t_users'] = Tacstsgroup.objects.filter(group_id=self.kwargs['pk'])
        context['c_users'] = Contacts.objects.values_list('id', 'name')
        return context

    def post(self, request, *args, **kwargs):
        u_name = request.POST.get('usergroup')
        u_id = Contacts.objects.filter(name=u_name).first()
        try:
            _name = Tacstsgroup.objects.get(user_id=u_id.id)
            _name.user_id = u_id.id
            _name.save()
            return JsonResponse({"status": "success"})
        except Tacstsgroup.DoesNotExist:
            data = {"group_id": self.kwargs['pk'], "user_id": u_id.id}
            try:
                Tacstsgroup.objects.update_or_create(**data)
                return JsonResponse({"status": "success"})
            except Exception as e:
                # logger.error(e)
                return JsonResponse({"status": "error"})



