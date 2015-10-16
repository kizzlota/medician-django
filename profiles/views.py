from django.shortcuts import render
from models import User, UserAddress
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import User
from forms import RegisterForm, RegisterFormSecond
# from profiles.mailing import send_email
# Create your views here.

def registration(request):
	if request.method == 'POST':
		id_user = request.POST.get('username')
		reg_form = RegisterForm(request.POST)
		if reg_form.is_valid():
			data = reg_form.cleaned_data
			user = User.objects.create_user(username=data['username'], email=data['email'])
			user.set_password(data['password'])
			# reg_form.save_m2m()
			user.save()
			loginuser = authenticate(username=data['username'], password=data['password'])
			login(request, loginuser)
			# send_email(user, prefix='signup_email')

			return HttpResponseRedirect('profiles/secondstep/')
	else:
		reg_form = RegisterForm()
	return render(request, 'profiles/index.html', {'reg_form': reg_form, 'registration': True})
