from bot.models import MessagesCount
from django.shortcuts import render, redirect
import telegram
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decouple import config


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            usernam = request.POST['username']
            passwd = request.POST['password1']
            confirm_password = request.POST['password2']
            if User.objects.filter(username=usernam).exists():
                messages.error(
                    request, "Username already exists! Try something else")
                return redirect('register')

            if passwd == confirm_password:
                user = User.objects.create_user(
                    username=usernam, password=passwd)
                user.save()
                messages.success(request, "User successfully registered")
                return redirect('home')
            else:
                messages.error(request, "Password doesn't match!")

        return render(request, 'register.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            usernam = request.POST['username']
            passwd = request.POST['password']
            user = authenticate(request, username=usernam, password=passwd)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or Password')
                return redirect('login_view')

        return render(request, 'login.html')


@login_required(login_url='login/')
def home(request):
    count_table = MessagesCount.objects.all()
    context = {
        'count': count_table,
    }
    return render(request, 'home.html', context)


stupid_joke = '''What do you call a pig that does karate?
A pork chop.'''
dump_joke = '''Why are teddy bears never hungry?
They are always stuffed.'''
fat_joke = '''
Yo momma is so fat,
I took a picture of her last Christmas
and it’s still printing. —The Laugh Factory'''


def telegram_post(request, data):
    telegram_settings = settings.TELEGRAM

    bot = telegram.Bot(token=telegram_settings['bot_token'])

    if MessagesCount.objects.filter(user=request.user).exists():
        count = MessagesCount.objects.get(user=request.user)
        if data == 'stupid':
            count.stupid_count += 1
            count.save()
            message = stupid_joke
        if data == 'dump':
            count.dump_count += 1
            count.save()
            message = dump_joke
        if data == 'fat':
            count.fat_count += 1
            count.save()
            message = fat_joke
    else:
        if data == 'stupid':
            count = MessagesCount(user=request.user, stupid_count=1)
            message = stupid_joke
        if data == 'dump':
            count = MessagesCount(user=request.user, dump_count=1)
            message = dump_joke
        if data == 'fat':
            count = MessagesCount(user=request.user, fat_count=1)
            message = fat_joke
        count.save()

    bot.send_message(chat_id=config('CHAT_ID'), text=message,
                     parse_mode=telegram.ParseMode.HTML)
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('login_view')
