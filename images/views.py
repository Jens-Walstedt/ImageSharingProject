from django.shortcuts import render


def pics_list_view(request):
    return render(request, "pics/pics_list.html", {})
