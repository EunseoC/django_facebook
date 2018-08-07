from django.shortcuts import render, redirect
from facebook.models import Article, Comment
# Create your views here.

def play(request):
    return render(request, 'play.html')
count = 0

def play2(request):
    choiEunseo = '최은서'
    age = 10

    global count
    count = count + 1

    if age>18:
        status = '성인입니다'
    else:
        status = '미성년자입니다'

    diary = [
        '너무 졸려(월)' , '집에 갈래(화)', '쿨쿨쿨(수)'
    ]

    return render(request, 'play2.html', {'name':choiEunseo, 'count':count, 'status':status, 'diary':diary})

def myname(request):
    return render(request, 'myname.html')

def event (request):
    choiEunseo = '최은서'
    global count
    count = count + 1

    if(count == 7):
        status = '당첨입니다!'
    else:
        status = '꽝'

    return render(request, 'event.html', {'name': choiEunseo, 'count': count, 'status': status})

def fail(request):
    return render(request, 'fail.html')
def division(request):

    num1 = 21
    num2 = 22

    K = [num1, num2]

    for i in range (0,1):
        if K[i]%7 == 0:
            status = '은 7의 배수입니다'
        else: status = '은 7의 배수가 아닙니다'

    return render(request, 'division.html', {'number':K[i], 'status': status})

def newsfeed(request):
    #db에서 글을 꺼내오는 작업
    articles = Article.objects.all()

    return render(request, 'newsfeed.html', { 'articles':articles })

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST' :
        Comment.objects.create(
            article = article,
            author = request.POST['author'],
            text = request.POST['text'],
            password = request.POST['password']
        )
        return redirect(f'/feed/{article.pk}')
    return render(request, 'detail_feed.html', { 'post':article  })

def new_feed(request):
    #받은 데이터 등록
    if request.method == 'POST':
        #여기에 코드 작성 예정
        post = Article.objects.create(
            author = request.POST['writer'],
            title = request.POST['title'],
            text = request.POST['content'],
            password = request.POST['pw']
        )

        #방금 쓴 페이지의 자세히보기 페이지로 이동을 하라
        return redirect(f'/feed/{post.pk}')

    return render(request, 'new_feed.html')

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['pw'] == article.password:
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.author =request.POST['writer']
            article.save()

            return redirect(f'/feed/{article.pk}')

    return render(request, 'edit_feed.html', {'feed': article})

def remove_feed(request, pk):
    # 받은 데이터 등록
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        if request.POST['pw'] ==  article.password:
                article.delete()
                return redirect('/')
    return render(request, 'remove_feed.html')
