from django.shortcuts import render, redirect, get_object_or_404
from . models import Note
from . forms import NoteModelForm

def create(request):
	form = NoteModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		return redirect("/")

	context = {
		"form":form,
	}
	return render(request,"note/create.html",context)

def listView(request):
	note = Note.objects.all()
	context = {
		"obj_list": note
	}
	return render(request,"note/list.html", context)

def deleteView(request,abc):
	to_delete = Note.objects.filter(id=abc)
	if to_delete.exists():
		if request.user == to_delete[0].user:
			to_delete[0].delete()
	return redirect("/list")

def updateView(request,id):
	unique_note = get_object_or_404(Note,id=id)
	form = NoteModelForm(request.POST or None, request.FILES or None, instance=unique_note)
	if form.is_valid():
		form.instance.user = request.user 
		form.save()
		return redirect("/list")
	context = {
		"form":form,
	}
	return render(request,"note/create.html", context)	