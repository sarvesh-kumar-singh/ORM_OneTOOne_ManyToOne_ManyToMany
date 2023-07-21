from django.shortcuts import render,HttpResponse

from .models import User,Page,Post,Song

def Home_page(request):
     return render(request,'orm_all/home.html')
    
    

def User_function(request):
    data1=User.objects.all()
    data2=User.objects.filter(email='sarveshsk888@gmail.com')
    data3=User.objects.filter(page__page_cat='vahical')
    data4=User.objects.filter(post__post_publish_date='2023-07-21')
    data5=User.objects.filter(song__song_publish_date='2023-07-21')

    return render(request,'orm_all/user.html', 
    {'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})

def Page_function(request):
    data1=Page.objects.all()
    data2=Page.objects.filter(page_name='Hero')
    data3=Page.objects.filter(page_cat='vahical')
    

    return render(request,'orm_all/page.html', 
    {'data1':data1,'data2':data2,'data3':data3})



def Post_function(request):
    data1=Post.objects.all()
    data2=Post.objects.filter(post_name='Amazon')
    data3=Post.objects.filter(post_cat="Guard")
    data4=Post.objects.filter(post_publish_date="2023-07-11")

    return render(request,'orm_all/post.html', 
    {'data1':data1,'data2':data2,'data3':data3,'data4':data4})
    


def Song_function(request):
    data1=Song.objects.all()
    data2=Song.objects.filter(song_title='Yaa Rabba')
    data3=Song.objects.filter(song_cat="New")
    data4=Song.objects.filter(song_publish_date="2023-07-21")

    return render(request,'orm_all/song.html', 
    {'data1':data1,'data2':data2,'data3':data3,'data4':data4})





