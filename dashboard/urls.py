from django.urls import path
from . import views

urlpatterns = [
    path('create-mexmonxona/', views.CreateMexmonxona.as_view()),
    path('update-mexmonxona/<int:pk>/', views.UpdateMexmonxona.as_view()),
    path('delete-mexmonxona/<int:pk>/', views.DeleteMexmonxona.as_view()),

    path("create-room/", views.CreateRoom.as_view()),
    path("update-room/<int:pk>/", views.UpdateRoom.as_view()),
    path("delete-room/<int:pk>/", views.DeleteRoom.as_view()),

    path('create-stol/', views.CreateStol.as_view()),
    path('update-stol/<int:pk>/', views.UpdateStol.as_view()),
    path('delete-stol/<int:pk>/', views.DeleteStol.as_view()),

    path('create-tar-joy/', views.CreateTarixiy_joylar.as_view()),
    path('update-tar-joy/<int:pk>/', views.UpdateTarixiy_joylar.as_view()),
    path('delete-tar-joy/<int:pk>/', views.DeleteTarixiy_joylar.as_view()),

    path('create-Konferentsiya_markazi/', views.CreateKonferentsiya_markazi.as_view()),
    path('update-Konferentsiya_markazi/<int:pk>/', views.UpdateKonferentsiya_markazi.as_view()),
    path('delete-Konferentsiya_markazi/<int:pk>/', views.DeleteKonferentsiya_markazi.as_view()),

    path('create-Shifoxona/', views.CreateShifoxona.as_view()),
    path('update-Shifoxona/<int:pk>/', views.UpdateShifoxona.as_view()),
    path('delete-Shifoxona/<int:pk>/', views.DeleteShifoxona.as_view()),

    path('create-Avtoturargoh/', views.CreateAvtoturargoh.as_view()),
    path('update-Avtoturargoh/<int:pk>/', views.UpdateAvtoturargoh.as_view()),
    path('delete-Avtoturargoh/<int:pk>/', views.DeleteAvtoturargoh.as_view()),

    path('create-Turar_joy/', views.CreateTurar_joy.as_view()),
    path('update-Turar_joy/<int:pk>/', views.UpdateTurar_joy.as_view()),
    path('delete-Turar_joy/<int:pk>/', views.DeleteTurar_joy.as_view()),

    path('create-Dokon/', views.CreateDokon.as_view()),
    path('update-Dokon/<int:pk>/', views.UpdateDokon.as_view()),
    path('delete-Dokon/<int:pk>/', views.DeleteDokon.as_view()),

    path('create-Restoran/', views.CreateRestoran.as_view()),
    path('update-Restoran/<int:pk>/', views.UpdateRestoran.as_view()),
    path('delete-Restoran/<int:pk>/', views.DeleteRestoran.as_view()),

    path('create-Category_by_address/', views.CreateCategoryLocation.as_view()),
    path('update-Category_by_address/<int:pk>/', views.UpdateCategoryLocation.as_view()),
    path('delete-Category_by_address/<int:pk>/', views.DeleteCategoryLocation.as_view()),

    path('create-Changi_uchun_maydon/', views.CreateChangi_uchun_maydon.as_view()),
    path('update-Changi_uchun_maydon/<int:pk>/', views.UpdateChangi_uchun_maydon.as_view()),
    path('delete-Changi_uchun_maydon/<int:pk>/', views.DeleteChangi_uchun_maydon.as_view()),

    path('create-Address/', views.CreateAddress.as_view()),
    path('update-Address/<int:pk>/', views.UpdateAddress.as_view()),
    path('delete-Address/<int:pk>/', views.DeleteAddress.as_view()),

    path('create-Bolalar_clubi/', views.CreateBolalar_clubi.as_view()),
    path('update-Bolalar_clubi/<int:pk>/', views.UpdateBolalar_clubi.as_view()),
    path('delete-Bolalar_clubi/<int:pk>/', views.DeleteBolalar_clubi.as_view()),

    path('create-Texnik_spetsifikatsiyalar/', views.CreateTexnik_spetsifikatsiyalar.as_view()),
    path('update-Texnik_spetsifikatsiyalar/<int:pk>/', views.UpdateTexnik_spetsifikatsiyalar.as_view()),
    path('delete-Texnik_spetsifikatsiyalar/<int:pk>/', views.DeleteTexnik_spetsifikatsiyalar.as_view()),

    path('create-Dam_olish_maskani/', views.CreateDam_olish_maskani.as_view()),
    path('update-Dam_olish_maskani/<int:pk>/', views.UpdateDam_olish_maskani.as_view()),
    path('delete-Dam_olish_maskani/<int:pk>/', views.DeleteDam_olish_maskani.as_view()),

    path('create-Yetkazib_berish/', views.CreateYetkazib_berish.as_view()),
    path('update-Yetkazib_berish/<int:pk>/', views.UpdateYetkazib_berish.as_view()),
    path('delete-Yetkazib_berish/<int:pk>/', views.DeleteYetkazib_berish.as_view()),

    path('create-Kutqaruv_tibiy_xizmat/', views.CreateKutqaruv_tibiy_xizmat.as_view()),
    path('update-Kutqaruv_tibiy_xizmat/<int:pk>/', views.UpdateKutqaruv_tibiy_xizmat.as_view()),
    path('delete-Kutqaruv_tibiy_xizmat/<int:pk>/', views.DeleteKutqaruv_tibiy_xizmat.as_view()),

    path('create-Operator/', views.CreateOperator.as_view()),
    path('update-Operator/<int:pk>/', views.UpdateOperator.as_view()),
    path('delete-Operator/<int:pk>/', views.DeleteOperator.as_view()),

    path('create-Ovqat_zakas/', views.CreateOvqat_zakas.as_view()),
    path('update-Ovqat_zakas/<int:pk>/', views.UpdateOvqat_zakas.as_view()),
    path('delete-Ovqat_zakas/<int:pk>/', views.DeleteOvqat_zakas.as_view()),

    path('create-Git/', views.CreateGit.as_view()),
    path('update-Git/<int:pk>/', views.UpdateGit.as_view()),
    path('delete-Git/<int:pk>/', views.DeleteGit.as_view()),

    path('create-SubCategoryLocation/', views.CreateSubCategoryLocation.as_view()),
    path('update-SubCategoryLocation/<int:pk>/', views.UpdateSubCategoryLocation.as_view()),
    path('delete-SubCategoryLocation/<int:pk>/', views.DeleteSubCategoryLocation.as_view()),
]
