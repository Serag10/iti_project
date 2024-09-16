from django.urls import path
# from . import views
from library.views import index , add_book , view_books , view_students, issue_book , view_issued_book ,student_issued_books ,profile,edit_profile ,student_registration,change_password ,student_login ,admin_login , Logout, delete_book, delete_student ,delete_issuedbook, issue_book_admin
urlpatterns = [
    path("", index, name="index"),
    path("add_book/", add_book, name="add_book"),
    path("view_books/", view_books, name="view_books"),
    path("view_students/", view_students, name="view_students"),
    path("issue_book/", issue_book, name="issue_book"),
    path("issue_book_admin/", issue_book_admin, name="issue_book_admin"),
    path("view_issued_book/", view_issued_book, name="view_issued_book"),
    path("student_issued_books/", student_issued_books, name="student_issued_books"),
    path("profile/", profile, name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),

    path("student_registration/", student_registration, name="student_registration"),
    path("change_password/", change_password, name="change_password"),
    path("student_login/", student_login, name="student_login"),
    path("admin_login/", admin_login, name="admin_login"),
    path("logout/", Logout, name="logout"),

    path("delete_book/<int:myid>/", delete_book, name="delete_book"),
    path("delete_student/<int:myid>/", delete_student, name="delete_student"),
    path("delete_issuedbook/<int:myid>/", delete_issuedbook, name="delete_issuedbook"),
] 