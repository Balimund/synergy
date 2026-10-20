from django.shortcuts import redirect, render

from .forms import NameForm
from .models import UserName


def index(request):
    """Главная страница: форма ввода имени и приветствие."""
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect после успешной отправки - защита от повторной отправки формы
            return redirect("index")
    else:
        form = NameForm()

    last_user = UserName.objects.order_by("-id").first()
    return render(request, "greetings/index.html", {"form": form, "last_user": last_user})
