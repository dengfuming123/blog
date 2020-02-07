from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from pic.models import PicTest

def image_field(request):
    if request.method == 'GET':
        return render(request, 'pic/image_field.html')
    elif request.method == 'POST':
        user = request.user
        pic = request.FILES.get('pic')
        pictest = PicTest()
        pictest.user = user
        pictest.goods_pic = pic
        pictest.save()
    return HttpResponse("成功保存")
def show_imgs(request):
    pics = PicTest.objects.all()
    return render(request, 'pic/show_imgs.html', {'pics': pics})

