from django.urls import path
from . import views

urlpatterns = [
    path('mexmonxona-all/', views.Mexmonxona_all.as_view()),
    path('room-all/', views.Room_all.as_view()),
    path('stol-all/', views.Stol_all.as_view()),
    path('tarixiy_joylar-all/', views.Tarixiy_joylar_all.as_view()),
    path('konferentsiya_markazi-all/', views.Konferentsiya_markazi_all.as_view()),
    path('shifoxona-all/', views.Shifoxona_all.as_view()),
    path('avtoturargoh-all/', views.Avtoturargoh_all.as_view()),
    path('turar_joy-all/', views.Turar_joy_all.as_view()),
    path('dokon-all/', views.Dokon_all.as_view()),
    path('restoranlar-all/', views.Restoranlar_all.as_view()),
    path('category_by_addre-all/', views.Category_by_address.as_view()),
    path('changi_uchun_mayd-all/', views.Changi_uchun_maydon.as_view()),
    path('address-all/', views.Address_all.as_view()),
    path('bolalar_clubi-all/', views.Bolalar_clubi_all.as_view()),
    path('texnik_spetsifikatsiyal-all/', views.Texnik_spetsifikatsiyalar.as_view()),
    path('dam_olish_maskani-all/', views.Dam_olish_maskani_all.as_view()),
    path('Yetkazib_berish-all/', views.Yetkazib_berish_all.as_view()),
    path('Kutqaruv_tibiy_xizmat-all/', views.Kutqaruv_tibiy_xizmat_all.as_view()),
    path('Operator-all/', views.Operator_all.as_view()),
    path('Ovqat_zakas-all/', views.Ovqat_zakas_all.as_view()),
    path('git-all/', views.Git_all.as_view()),
    path('SubCategoryLocation-all/', views.SubCategoryLocation.as_view()),
    path('get-mexmonxona_by_name/', views.mexmonxona_by_name),
    path('get-mexmonxona_by_room/', views.mexmonxona_by_room),
    path('get-room_by_name/', views.room_by_name),
    path('get-stol_by_name/', views.stol_by_name),
    path('get-stol_by_xajmi/', views.stol_by_xajmi),
    path('get-tarixiy_joylar_by_name/', views.tarixiy_joylar_by_name),
    path('get-address_by_name/', views.address_by_name),
    path('get-avtoturargox_by_name/', views.avtoturargox_by_name),
    path('get-avtoturargox_by_address/', views.avtoturargox_by_address),
    path('get-konfirentsiya_markazi_by_name/', views.konfirentsiya_markazi_by_name),
    path('get-konfirentsiya_markazi_by_address/', views.konfirentsiya_markazi_by_address),
    path('get-shifoxona_by_name/', views.shifoxona_by_name),
    path('get-shifoxona_by_address/', views.shifoxona_by_address),
    path('get-restoranlar_by_name/', views.restoranlar_by_name),
    path('get-restoranlar_by_description/', views.restoran_by_dascription),
    path('get-restoran_by_address/', views.restoran_by_address),
    path('get-turar_joy_by_name/', views.turar_joy_by_name),
    path('get-turar_joy_by_address/', views.turar_joy_by_address),
    path('get-dokon_by_name/', views.dokon_by_name),
    path('get-dokon_by_address/', views.dokon_by_address),
    path('get-kutqaruv_tibiy_xizmat_by_name/', views.kutqaruv_tibiy_xizmat_by_name),
    path('get-bolalar_clubi_by_address/', views.bolalar_clubi_by_address),
    path('get-bolalar_clubi_by_name/', views.bolalar_clubi_by_name),
    path('get-address_by_name/', views.address_by_name),
    path('get-dam_olish_maskani_by_name/', views.dam_olish_maskani_by_name),
    path('get-dam_olish_maskani_by_address/', views.dam_olish_maskani_by_address),
    path('get-texnik_spetsifikatsiyalar_by_name/', views.texnik_spetsifikatsiyalar_by_name),
    path('get-texnik_spetsifikatsiyalar_by_address/', views.texnik_spetsifikatsiyalar_by_address),
    path('get-operator_by_name/', views.operator_by_name),
    path('get-operator_by_user/', views.operator_by_user),
    path('get-operator_by_address/', views.operator_by_address),
    path('get-changi_uchun_maydon_by_name/', views.changi_uchun_maydon_by_name),
    path('get-changi_uchun_maydon_by_address/', views.changi_uchun_maydon_by_address),
    path('get-yetkazib_berish_by_name/', views.yetkazib_berish_by_name),
    path('get-yetkazib_berish_by_address/', views.yetkazib_berish_by_address),
    path('get-Yetkazib_berish_by_buyurtma_raqami/', views.Yetkazib_berish_by_buyurtma_raqami),
    path('get-Category_by_address_by_name/', views.Category_by_address_by_name),
    path('get-Ovqat_zakas_by_name/', views.Ovqat_zakas_by_name),
    path('get-git_by_name/', views.git_by_name),
]