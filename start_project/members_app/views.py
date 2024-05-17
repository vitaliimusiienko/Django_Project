from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm

 

def index(request):
    return render(request, 'members_app/index.html')

def new_notes(request):
    
    error = '' 
    
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all notes')
        
        else:
            error = 'Try again'  
            
    form = NotesForm()
    notes_dict = { 
             'form' : form,
             'error': error
    }   
    return render(request, 'members_app/new_notes.html', notes_dict)

def all_notes(request):
    notes = Notes.objects.all()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    return render(request, 'members_app/all_notes.html', context={'notes': notes, 'num_visits': num_visits})


