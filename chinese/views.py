from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food, Category
from django.core.files.storage import FileSystemStorage


#def upload(request):
#  fs=FileSystemStorage()
#  uploaded_file = request.FILES['file']
#  name = fs.save(uploaded_file.name, uploaded_file)
#  url = fs.url(name)
#  return HttpResponse('{}에 저장이 잘 되었습니다.'.format(url))

def add_food(request):
  # get(그냥 주소 입력해서 오면) -> 페이지만 보여주고
  # post -> DB에 입력하는 과정을 넣자

  if request.method == 'GET':
    return render(request=request, template_name='chinese/add_food.html')    # 그냥 페이지만 보여주면 됨

  elif request.method == 'POST':
        # Food.objects.create(name='라떼')
        # request.POST['lion_name']

    # html로부터 요청받은 값(category/lion_name/price/description/takeout)을
    # DB에 저장하기위해 변수에 입력받은 값 담기

    # Category 인스턴스의 값을 가져오는 영역
    category = Category.objects.get(name=request.POST['category'])
    food_name = request.POST['lion_name']
    food_price = request.POST['price']
    food_description = request.POST['description']

    # 이미지 저장 및 url 설정 내용
    fs = FileSystemStorage()
    uploaded_file = request.FILES['file']
    name = fs.save(uploaded_file.name, uploaded_file)
    url = fs.url(name)

    # DB에 입력받은 값을 저장하기 위한 메소드
    Food.objects.create(category=category, name=food_name, price=food_price, description=food_description, image_url=url)
    
    return redirect('index')


def food_detail(request, pk):
  object = Food.objects.get(pk=pk)
  context = {
    'object' : object
  }
  return render(request, 'chinese/food_detail.html', context)

def food_delete(request, pk):
  object = Food.objects.get(pk=pk)
  object.delete()
  return redirect('index')