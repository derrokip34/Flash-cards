from django.shortcuts import render,redirect
from .models import FlashCard,Subject
from .forms import PostFlashCard,UpdateFlashCardForm
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger

# Create your views here.
def home(request):
    flashcards = FlashCard.get_all_flashcards()
    paginator = Paginator(flashcards,3)

    try:
        page = request.GET.get('page')
    except ValueError:
        page = 1
    try:
        flashcards = paginator.page(page)
    except (EmptyPage,InvalidPage):
        flashcards = paginator.page(paginator.num_pages)
    return render(request,'index.html',locals())

def post_flash_card(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostFlashCard(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.user = current_user
            flashcard.save()
        return redirect('home')
    else:
        form = PostFlashCard()

    title = 'New Flash Card'
    return render(request,'new_flash_card.html',locals())

def update_flash_card(request,id):
    current_user = request.user
    card = FlashCard.objects.filter(id=id).first()
    if request.method == 'POST':
        form = PostFlashCard(request.POST,instance=card)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.user = current_user
            flashcard.save()
        return redirect('home')
    else:
        form = PostFlashCard(instance=card)

    title = 'Update Flash Card'
    return render(request,'update_flash_card.html',locals())

def subject_cards(request,subject,subject_id):
    subject = Subject.objects.filter(id=subject_id).first()
    subject_cards = FlashCard.objects.filter(subject=subject).all()

    title = f'{subject.subject} cards'
    return render(request,'subject.html',locals())
