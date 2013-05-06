from notes.models import Note, NoteForm, Tag
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext


#View index: the home logic. Creates a form for input notes, and render notes/index.html
#template, passing all the tags to show as filter hashes.
def index(request):
    all_tags = Tag.objects.all()
    form = NoteForm()
    return render_to_response('notes/index.html', {'tags_list': all_tags, 'form': form}, context_instance=RequestContext(request))


#View get_list_notes: receives a request, and retrieves the corresponding notes.
#in the POST is sent tags[], an array of string with the hashes to filter.
def get_list_notes(request):
    tags = request.POST.getlist('tags[]')
    if not tags:
        notes = Note.objects.all().order_by('-created_at')
    else:
        notes = Note.objects.filter(tags__in=Tag.objects.filter(tag__in=tags)).distinct().order_by(-'created_at')
    return render_to_response('notes/listnotes.html', {'notes_list': notes}, context_instance=RequestContext(request))


#View add: receives a request with POST data of a new note to add.
#if the POST is not in the request just render notes/add.html for debug.
def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        form.save()
        return redirect("/")
    else:
        form = NoteForm()
        return render(request, "notes/add.html", {"form": form})
