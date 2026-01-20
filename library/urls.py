from django.urls import path
from.import views

urlpatterns=[
    path('',views.registrationform,name='registrationform'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login_view/',views.login_view,name='login_view'),
    path('log_out/',views.log_out,name='logout'),
    path('add_book/',views.add_book,name='add_book'),
    path('manage_book',views.manage_book,name='manage_book'),
    path('edit_book/<int:bid>/',views.edit_book,name='edit_book'),
    path('delete_book/<int:bid>',views.delete_book,name='delete_book'),
    path('manage_user/',views.manage_user,name='manage_user'),
    path('delete_user/<int:uid>',views.delete_user,name='delete_user'),
    path('profile/',views.profile,name='profile'),
    path('favorite_books/',views.favorite_books,name='favorite_books'),
    path('Add_favorite/<int:fid>',views.Add_favorite,name='Add_favorite'),
    path('remove_favorite/<int:fid>',views.remove_favorite,name='remove_favorite')
]