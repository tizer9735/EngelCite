
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Flashcard
from .forms import FlashcardForm


def home(request):
    return render(request, 'flashcards/home.html')


def add_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flashcards_list')
    else:
        form = FlashcardForm()

    return render(request, 'flashcards/add_flashcard.html', {'form': form})


class FlashcardListView(ListView):
    model = Flashcard
    template_name = 'flashcards/flashcards_list.html'
    context_object_name = 'flashcards'
    ordering = ['-created_at']
    paginate_by = 10


def practice(request):
    flashcards = Flashcard.objects.order_by('knowledge_level')[:5]
    if not flashcards:
        return redirect('add_flashcard')

    context = {
        'flashcards': flashcards,
    }
    return render(request, 'flashcards/practice.html', context)


def update_knowledge(request, pk):
    if request.method == 'POST':
        flashcard = get_object_or_404(Flashcard, pk=pk)
        knowledge_level = int(request.POST.get('knowledge_level', 0))

        if 0 <= knowledge_level <= 5:
            flashcard.knowledge_level = knowledge_level
            flashcard.save()
        return redirect('practice')

