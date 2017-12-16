from django.shortcuts import render, get_object_or_404, redirect
from pynstagram.models import Photograph, User, Comment
from pynstagram.forms import AddCommentForm, SearchUsersForm, MailUserForm
from django.core.mail import send_mail


def homepage(request):
    photos = Photograph.objects.all()
    photos_ordered = photos.order_by('-created')
    return render(request, "index.html", {'photos': photos_ordered})


def header(request):
    return render(request, "header.html")


def photo_index(request, photo_id):
    photo = get_object_or_404(Photograph, pk=photo_id)
    comments = Comment.objects.filter(photograph=photo_id)
    comment_form = AddCommentForm()
    return render(request, "photo_index.html", {'photo': photo, 'comments': comments, 'comment_form': comment_form})


def add_comment(request, photo_id):
    photo = get_object_or_404(Photograph, pk=photo_id)
    if request.method == 'POST':
        comment_form = AddCommentForm(request.POST)
        if comment_form.is_valid():
            comment_author = comment_form.cleaned_data['author']
            comment_text = comment_form.cleaned_data['text']
            comment = comment_form.save(commit=False)
            comment.photograph = photo
            comment.author = comment_author
            comment.text = comment_text
            comment.save()
            comment_form.save_m2m()
    return redirect('photo_index', photo_id)


def user_index(request):
    if request.method == 'POST':
        form = SearchUsersForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            users = User.objects.filter(name__istartswith=name)
        else:
            users = None
    else:
        users = User.objects.all()
        form = SearchUsersForm()
    return render(request, "user_index.html", {'users': users, 'search_users': form})


def user(request, user_id):
    user_instance = get_object_or_404(User, pk=user_id)
    photos = Photograph.objects.filter(owner=user_instance)
    mail_form = MailUserForm()
    return render(request, "user.html", {'user': user_instance, 'photos': photos, 'mail_form': mail_form})


def send_email(request, user_id):
    user_instance = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        mail_form = MailUserForm(request.POST)
        if mail_form.is_valid():
            sender = mail_form.cleaned_data['sender']
            email = mail_form.cleaned_data['email']
            text = mail_form.cleaned_data['mail_text']
            send_mail(
                'Message from .pyNSTAGRAM by ' + sender,
                text,
                email,
                [user_instance.email],
                fail_silently=False
            )
            success = True
        else:
            success = False
    else:
        success = False
    return render(request, "email_success.html", {'success': success})

