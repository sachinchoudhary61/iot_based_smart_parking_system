from django.shortcuts import render, HttpResponse,redirect
from Applicationuser.form import ApplicationuserForm
from .form import *
# Create your views here.
from miscellaneous import otp_sending

def signup(request):
    if request.method == 'POST':
        form = ApplicationuserForm(request.POST)
        f = form.save(commit=False)
        f.first_name = request.POST['firstname']
        # f.last_name = request.POST['lastname']
        # f.email = request.POST['email_id']
        # if request.POST['paswd'] == request.POST['c_pswd']:
        #     f.password = request.POST['paswd']
        # else:
        #     return HttpResponse("<h1> Password and Confirm password is not same</h1>")
        # f.phone_no = request.POST['phone_number']
        # f.city = ''
        # f.address = ''
        # f.otp = otp_sending.otp_sending()
        # f.otp_gen_time = otp_sending.time_gen()
        # f.user_type = request.POST['user_type']
        # f.token = ''
        # f.save()
        # HttpResponse("done")
    return render(request, 'test.html')


def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'imagetest.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
