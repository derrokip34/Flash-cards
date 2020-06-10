from django.shortcuts import render,redirect
from .models import FlashCard
from .forms import PostFlashCard

# Create your views here.
def home(request):

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
