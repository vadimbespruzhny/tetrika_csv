import os
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import CsvUpload, SortedCsv
from .forms import CsvUploadForm
import csv
# Create your views here.


class ListCsvView(ListView):
    template_name = "success.html"
    model = SortedCsv
    context_object_name = "file"


class UploadCsvView(TemplateView):
    template_name = "upload.html"

    def get_context_data(self, **kwargs):
        context = {"form": CsvUploadForm}
        return context

    def post(self, request):
        form = CsvUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            get_file_data()
            return redirect("success")
        context = {"form": form}
        return render(request, "upload.html", context)


def get_file_data():
    with open("media/Tutors.csv", "r") as f:
        data = list(csv.reader(f, delimiter=","))
        temp_data_list = []
        for data_list in data:
            for inner_list in data_list[:1]:
                temp_data_list.append(inner_list)
        result_list = sorted([int(i) for i in temp_data_list[1:]])
        for rank in result_list:
            obj = SortedCsv(rank=rank)
            obj.save()
    return obj

