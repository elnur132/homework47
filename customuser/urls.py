from django.urls import path, include
from .views import DashBoard, CreateUserView, DetailUserView, Mistake, UserLogin, UserLogoutView

urlpatterns = [
    path('', DashBoard.as_view(), name='dashboard'),
    path('createuser/', CreateUserView.as_view(), name='createuser'),
    path('<int:user_id>', DetailUserView.as_view(), name='detail_user'),
    path('mistake/', Mistake.as_view(), name='mistake'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
