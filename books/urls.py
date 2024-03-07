from django.urls import path
from . import views
from .views import DetailBookView, BorrowBookList, BookReturnView, buy_now





urlpatterns = [
    
    path('book/<int:id>/', views.DetailBookView.as_view(), name='detailbookview'),
    path('buy_now/<int:id>/',views.buy_now.as_view(), name='buy_now'),
    path('borrowbook/', BorrowBookList.as_view(), name='borrow_book_lists'),
    path('return/<int:id>/', BookReturnView.as_view(), name='returnbook'),
    
]