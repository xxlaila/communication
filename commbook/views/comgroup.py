# -*- coding: utf-8 -*-
"""
@File    : comgroup.py
@Time    : 2021/9/15 4:50 下午
@Author  : xxlaila
@Software: PyCharm
"""
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from ..forms.comgroup import *
from django.shortcuts import (
    render, redirect
)

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
        return redirect('commbook:comgroup-list')