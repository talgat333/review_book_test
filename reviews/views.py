from django.shortcuts import render
from reviews.forms import ReviewForm
from django.shortcuts import redirect
from reviews.models import Review
from django.views import View

# Create your views here.

class ReviewsView(View):

    def get(self, request):
        form = ReviewForm()
        reviews = Review.objects.all()

        return render(request, 'reviews.html', {'form': form, 'reviews': reviews})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')

            Review.objects.create(name=name, email=email, review=review, rating=rating)
            return redirect('reviews')

        form = ReviewForm()
        reviews = Review.objects.all()
        return render(request, 'reviews.html', {'form': form, 'reviews': reviews})

def reviews_before_classes(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            Review.objects.create(name=name, email=email, review=review, rating=rating)

            return redirect('reviews')


    form = ReviewForm()
    #review_1 = Review.objects.get(id=1)
    #print(review_1.name)
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'form': form, 'reviews': reviews})
    #return render(request, 'reviews.html', {'form': form})



def reviews_before_db(request):
    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'reviews.html', {'form': form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            with open('data.csv', 'a') as file:
                file.write(f'{name}|{email}|{review}|{rating}\n')
            print(data)
            return redirect('reviews')

    else:
        form = ReviewForm()
        return render(request, 'reviews.html', {'form': form})

    with open('data.csv') as file:
        reviews = file.readlines()
        if len(reviews) > 0:
            review_data_1 = reviews[0]
            name_1 = review_data_1.split('|')[0]
            email_1 = review_data_1.split('|')[1]
            review_1 = review_data_1.split('|')[2]
        else:
            name_1 = ""
            email_1 = ""
            review_1 = ""

    form = ReviewForm()
    return render(request, 'reviews.html', {'form': form, 'name_1': name_1, 'email_1': email_1, 'review_1': review_1})

def reviews_hw(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            with open('data.csv', 'a') as file:
                file.write(f'{name}|{email}|{review}|{rating}\n')
                return redirect('reviews')
    with open('data.csv') as file:
        reviews = file.readlines()
        if len(reviews) > 0:
            review_data_1 = reviews[0]
            name_1 = review_data_1.split('|')[0]
            email_1 = review_data_1.split('|')[1]
            review_1 = review_data_1.split('|')[2]
        else:
            name_1 = ""
            email_1 = ""
            review_1 = ""

    form = ReviewForm()
    return render(request, 'reviews.html', {'form': form, 'name_1': name_1, 'email_1': email_1, 'review_1': review_1})

def reviews_old(request):
    # name_1 = "Вася"
    # email_1 = "vasya@example.com"
    # review_1 = "Все понравилось, обязательно приду еще!"
    name_1 = request.GET.get('name')
    email_1 = request.GET.get('email')
    review_1 = request.GET.get('review')
    return render(request, 'reviews.html',{'name_1': name_1, 'email_1': email_1, 'review_1': review_1, 'form':form})
    #return render(request, 'reviews.html')