from django.shortcuts import render, redirect
import hashlib
from .forms import HashForm
from .models import Hash


def homepage(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf8')).hexdigest()
            try:
                Hash.objects.get(hash=text_hash)
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hash = text_hash
                hash.save()
            # hash = {'text': text, 'hash': text_hash}
            return redirect('hash_detail', hex_digest=text_hash)
    form = HashForm()
    return render(request, 'hashing/index.html', {'form': form})


def hash_detail(request, hex_digest):
    hash = Hash.objects.get(hash=hex_digest)
    return render(request, 'hashing/hash_detail.html', {'hash': hash})
