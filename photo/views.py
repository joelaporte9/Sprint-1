from django.shortcuts import render

def gallery(request):
    return render(request, 'photos/gallery.html')

def viewPhoto(request, pk):
    return render(request, 'photos/photos.html')

def add(request):
    return render(request, 'photos/add.html')