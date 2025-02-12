from django.urls import path
from .views import CourseList, CourseDetail, CourseCreate, CourseUpdate, CourseDelete, Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('course-list/', CourseList.as_view(), name='course_list'),
    path('course-detail/<int:pk>', CourseDetail.as_view(), name='course_detail'),
    path('course-create/', CourseCreate.as_view(), name='course_create'),
    path('course-update/<int:pk>', CourseUpdate.as_view(), name='course_update'),
    path('course-delete/<int:pk>', CourseDelete.as_view(), name='course_delete'),    
]
