from django.shortcuts import render, reverse, get_object_or_404
from .models import Kwitantie
from .forms import KwitantieAanmaken
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, FileResponse
from datetime import date
from .pdf_gen import make_pdf
from .input_fields import tarief_dict
from .gitlab import commit_file


def nieuwe_kwitantie(request):
    if request.method == 'POST':
        form = KwitantieAanmaken(request.POST)
        if form.is_valid():
            form.kwitantie.bedrag = form.data.get('tarief')
            form.kwitantie.dienst = [key for key, value in tarief_dict().items() if str(value) == form.data.get('tarief')][0]
            form.kwitantie.save()
            form.kwitantie.kwitantienummer = '%s-%s%s' % (date.today().year,
                                                          "00" if form.kwitantie.id < 10 else "0",
                                                          form.kwitantie.id)
            form.kwitantie.save()
            return HttpResponseRedirect(reverse("kwitantie-list"))
    else:
        form = KwitantieAanmaken()
        return render(request, 'kwitantie/kwitantie.html', {'form': form})


def get_pdf(request, pk):
    kwitantienummer = make_pdf(get_object_or_404(Kwitantie, pk=pk))
    try:
        commit_file(Kwitantie)
    except:
        pass
    return FileResponse(open('kwitantie-%s.pdf' % kwitantienummer, 'rb'), content_type='application/pdf')


class KwitantieListView(ListView):
    model = Kwitantie
