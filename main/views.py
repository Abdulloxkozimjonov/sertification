from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers


class Mexmonxona_all(ListAPIView):
    queryset = models.Mexmonxona.objects.all()
    serializer_class = serializers.MexmonxonaSerializer


class Room_all(ListAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class Stol_all(ListAPIView):
    queryset = models.Stol.objects.all()
    serializer_class = serializers.StolSerializer


class Tarixiy_joylar_all(ListAPIView):
    queryset = models.Tarixiy_joylar.objects.all()
    serializer_class = serializers.Tarixiy_joylarSerializer


class Konferentsiya_markazi_all(ListAPIView):
    queryset = models.Konferentsiya_markazi.objects.all()
    serializer_class = serializers.Konferentsiya_markaziSerializer


class Git_all(ListAPIView):
    queryset = models.Git.objects.all()
    serializer_class = serializers.GitSerializer


class Shifoxona_all(ListAPIView):
    queryset = models.Shifoxona.objects.all()
    serializer_class = serializers.ShifoxonaSerializer


class Avtoturargoh_all(ListAPIView):
    queryset = models.Avtoturargoh.objects.all()
    serializer_class = serializers.AvtoturargohSerializer


class Turar_joy_all(ListAPIView):
    queryset = models.Turar_joy.objects.all()
    serializer_class = serializers.Turar_joySerializer


class Dokon_all(ListAPIView):
    queryset = models.Dokon.objects.all()
    serializer_class = serializers.DokonSerializer


class Restoranlar_all(ListAPIView):
    queryset = models.Restoranlar.objects.all()
    serializer_class = serializers.RestoranlarSerializer


class Category_by_address(ListAPIView):
    queryset = models.CategoryLocation.objects.all()
    serializer_class = serializers.CategoryLocationSerializer


class SubCategoryLocation(ListAPIView):
    queryset = models.SubCategoryLocation.objects.all()
    serializer_class = serializers.SubCategoryLocationSerializer


class Changi_uchun_maydon(ListAPIView):
    queryset = models.Changi_uchun_maydon.objects.all()
    serializer_class = serializers.Changi_uchun_maydonSerializer


class Address_all(ListAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class Bolalar_clubi_all(ListAPIView):
    queryset = models.Bolalar_clubi.objects.all()
    serializer_class = serializers.Bolalar_clubiSerializer


class Texnik_spetsifikatsiyalar(ListAPIView):
    queryset = models.Texnik_spetsifikatsiyalar.objects.all()
    serializer_class = serializers.Texnik_spetsifikatsiyalarSerializer


class Dam_olish_maskani_all(ListAPIView):
    queryset = models.Dam_olish_maskani.objects.all()
    serializer_class = serializers.Dam_olish_maskaniSerializer


class Yetkazib_berish_all(ListAPIView):
    queryset = models.Yetkazib_berish.objects.all()
    serializer_class = serializers.Yetkazib_berishSerializer


class Kutqaruv_tibiy_xizmat_all(ListAPIView):
    queryset = models.Kutqaruv_tibiy_xizmat.objects.all()
    serializer_class = serializers.Kutqaruv_tibiy_xizmatSerializer


class Operator_all(ListAPIView):
    queryset = models.Operator.objects.all()
    serializer_class = serializers.OperatorSerializer


class Ovqat_zakas_all(ListAPIView):
    queryset = models.Ovqat_zakas.objects.all()
    serializer_class = serializers.Ovqat_zakasSerializer


@api_view(["GET"])
def mexmonxona_by_name(request):
    name = request.GET.get("name")
    mexmonxona = models.Mexmonxona.objects.filter(name = name)
    ser = serializers.MexmonxonaSerializer(mexmonxona, many=True)
    return Response(ser.data)


@api_view(["GET"])
def mexmonxona_by_room(request):
    room = request.GET.get("room")
    mexmonxona = models.Mexmonxona.objects.filter(room = room)
    ser = serializers.MexmonxonaSerializer(mexmonxona, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_name(request):
    name = request.GET.get("name")
    room = models.Room.objects.filter(name = name)
    ser = serializers.RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def stol_by_name(request):
    name = request.GET.get("name")
    stol = models.Stol.objects.filter(name = name)
    ser = serializers.StolSerializer(stol, many=True)
    return Response(ser.data)


@api_view(["GET"])
def stol_by_xajmi(request):
    xajmi = request.GET.get("xajmi")
    stol = models.Stol.objects.filter(xajmi = xajmi)
    ser = serializers.StolSerializer(stol, many=True)
    return Response(ser.data)


@api_view(["GET"])
def tarixiy_joylar_by_name(request):
    name = request.GET.get("name")
    tarixiy_joylar = models.Tarixiy_joylar.objects.filter(name = name)
    ser = serializers.Tarixiy_joylarSerializer(tarixiy_joylar, many=True)
    return Response(ser.data)


@api_view(["GET"])
def address_by_name(request):
    name = request.GET.get("name")
    address = models.Address.objects.filter(name = name)
    ser = serializers.AddressSerializer(address, many=True)
    return Response(ser.data)


@api_view(["GET"])
def avtoturargox_by_name(request):
    name = request.GET.get("name")
    avtoturargox = models.Avtoturargoh.objects.filter(name = name)
    ser = serializers.AvtoturargohSerializer(avtoturargox, many=True)
    return Response(ser.data)


@api_view(["GET"])
def avtoturargox_by_address(request):
    address = request.GET.get("address")
    avtoturargox = models.Avtoturargoh.objects.filter(address = address)
    ser = serializers.AvtoturargohSerializer(avtoturargox, many=True)
    return Response(ser.data)


@api_view(["GET"])
def konfirentsiya_markazi_by_name(request):
    name = request.GET.get("name")
    konfirentsiya = models.Konferentsiya_markazi.objects.filter(name = name)
    ser = serializers.Konferentsiya_markaziSerializer(konfirentsiya, many=True)
    return Response(ser.data)


@api_view(["GET"])
def konfirentsiya_markazi_by_address(request):
    address = request.GET.get("address")
    konfirentsiya = models.Konferentsiya_markazi.objects.filter(address = address)
    ser = serializers.Konferentsiya_markaziSerializer(konfirentsiya, many=True)
    return Response(ser.data)


@api_view(["GET"])
def shifoxona_by_name(request):
    name = request.GET.get("name")
    shifoxona = models.Shifoxona.objects.filter(name = name)
    ser = serializers.ShifoxonaSerializer(shifoxona, many=True)
    return Response(ser.data)


@api_view(["GET"])
def shifoxona_by_address(request):
    address = request.GET.get("address")
    shifoxona = models.Shifoxona.objects.filter(address = address)
    ser = serializers.ShifoxonaSerializer(shifoxona, many=True)
    return Response(ser.data)


@api_view(["GET"])
def restoranlar_by_name(request):
    name = request.GET.get("name")
    restoranlar = models.Restoranlar.objects.filter(name = name)
    ser = serializers.RestoranlarSerializer(restoranlar, many=True)
    return Response(ser.data)


@api_view(["GET"])
def restoran_by_dascription(request):
    description = request.GET.get("name")
    restoranlar = models.Restoranlar.objects.filter(description = description)
    ser = serializers.RestoranlarSerializer(restoranlar, many=True)
    return Response(ser.data)


@api_view(["GET"])
def restoran_by_address(request):
    address = request.GET.get("address")
    restoran = models.Restoranlar.objects.filter(address = address)
    ser = serializers.RestoranlarSerializer(restoran, many=True)
    return Response(ser.data)


@api_view(["GET"])
def turar_joy_by_name(request):
    name = request.GET.get("name")
    turar_joy = models.Turar_joy.objects.filter(name = name)
    ser = serializers.Turar_joySerializer(turar_joy, many=True)
    return Response(ser.data)


@api_view(["GET"])
def turar_joy_by_address(request):
    address = request.GET.get("address")
    turar_joy = models.Turar_joy.objects.filter(address = address)
    ser = serializers.Turar_joySerializer(turar_joy, many=True)
    return Response(ser.data)


@api_view(["GET"])
def dokon_by_name(request):
    name = request.GET.get("name")
    dokon_by_name = models.Dokon.objects.filter(name = name)
    ser = serializers.DokonSerializer(dokon_by_name, many=True)
    return Response(ser.data)


@api_view(["GET"])
def dokon_by_address(request):
    address = request.GET.get("address")
    dokon = models.Dokon.objects.filter(address = address)
    ser = serializers.DokonSerializer(dokon, many=True)
    return Response(ser.data)

@api_view(["GET"])
def kutqaruv_tibiy_xizmat_by_name(request):
    name = request.GET.get("name")
    kutqaruv_tibiy_xizmat = models.Kutqaruv_tibiy_xizmat.objects.filter(name = name)
    ser = serializers.Kutqaruv_tibiy_xizmatSerializer(kutqaruv_tibiy_xizmat, many=True)
    return Response(ser.data)


@api_view(["GET"])
def bolalar_clubi_by_address(request):
    address = request.GET.get("address")
    bolalar = models.Bolalar_clubi.objects.filter(address = address)
    ser = serializers.Bolalar_clubiSerializer(bolalar, many=True)
    return Response(ser.data)


@api_view(["GET"])
def bolalar_clubi_by_name(request):
    name = request.GET.get("name")
    bolalar = models.Bolalar_clubi.objects.filter(name = name)
    ser = serializers.Bolalar_clubiSerializer(bolalar, many=True)
    return Response(ser.data)


@api_view(["GET"])
def address_by_name(request):
    name = request.GET.get("name")
    address = models.Address.objects.filter(name = name)
    ser = serializers.AddressSerializer(address, many=True)
    return Response(ser.data)


@api_view(["GET"])
def dam_olish_maskani_by_name(request):
    name = request.GET.get("name")
    Dam_olish_maskani = models.Dam_olish_maskani.objects.filter(name = name)
    ser = serializers.Dam_olish_maskaniSerializer(Dam_olish_maskani, many=True)
    return Response(ser.data)


@api_view(["GET"])
def dam_olish_maskani_by_address(request):
    address = request.GET.get("address")
    Dam_olish_maskani = models.Dam_olish_maskani.objects.filter(address = address)
    ser = serializers.Dam_olish_maskaniSerializer(Dam_olish_maskani, many=True)
    return Response(ser.data)


@api_view(["GET"])
def texnik_spetsifikatsiyalar_by_name(request):
    name = request.GET.get("name")
    Texnik_spetsifikatsiyalar = models.Texnik_spetsifikatsiyalar.objects.filter(name = name)
    ser = serializers.Texnik_spetsifikatsiyalarSerializer(Texnik_spetsifikatsiyalar, many=True)
    return Response(ser.data)


@api_view(["GET"])
def texnik_spetsifikatsiyalar_by_address(request):
    address = request.GET.get("address")
    Texnik_spetsifikatsiyalar = models.Texnik_spetsifikatsiyalar.objects.filter(address = address)
    ser = serializers.Texnik_spetsifikatsiyalarSerializer(Texnik_spetsifikatsiyalar, many=True)
    return Response(ser.data)


@api_view(["GET"])
def operator_by_name(request):
    name = request.GET.get("name")
    operator = models.Operator.objects.filter(name = name)
    ser = serializers.OperatorSerializer(operator, many=True)
    return Response(ser.data)


@api_view(["GET"])
def operator_by_user(request):
    user = request.GET.get("user")
    operator = models.Operator.objects.filter(user = user)
    ser = serializers.OperatorSerializer(operator, many=True)
    return Response(ser.data)


@api_view(["GET"])
def operator_by_address(request):
    address = request.GET.get("address")
    operator = models.Operator.objects.filter(address = address)
    ser = serializers.OperatorSerializer(operator, many=True)
    return Response(ser.data)


@api_view(["GET"])
def changi_uchun_maydon_by_name(request):
    name = request.GET.get("name")
    operator = models.Changi_uchun_maydon.objects.filter(name = name)
    ser = serializers.Changi_uchun_maydonSerializer(operator, many=True)
    return Response(ser.data)


@api_view(["GET"])
def changi_uchun_maydon_by_address(request):
    address = request.GET.get("address")
    operator = models.Changi_uchun_maydon.objects.filter(address = address)
    ser = serializers.Changi_uchun_maydonSerializer(operator, many=True)
    return Response(ser.data)


@api_view(["GET"])
def yetkazib_berish_by_name(request):
    name = request.GET.get("name")
    Yetkazib_berish = models.Yetkazib_berish.objects.filter(name = name)
    ser = serializers.Yetkazib_berishSerializer(Yetkazib_berish, many=True)
    return Response(ser.data)


@api_view(["GET"])
def yetkazib_berish_by_address(request):
    address = request.GET.get("address")
    Yetkazib_berish = models.Yetkazib_berish.objects.filter(address = address)
    ser = serializers.Yetkazib_berishSerializer(Yetkazib_berish, many=True)
    return Response(ser.data)


@api_view(["GET"])
def Yetkazib_berish_by_buyurtma_raqami(request):
    buyurtma_raqami = request.GET.get("buyurtma_raqami")
    Yetkazib_berish = models.Yetkazib_berish.objects.filter(buyurtma_raqami = buyurtma_raqami)
    ser = serializers.Yetkazib_berishSerializer(Yetkazib_berish, many=True)
    return Response(ser.data)


@api_view(["GET"])
def Category_by_address_by_name(request):
    name = request.GET.get("name")
    Category = models.CategoryLocation.objects.filter(name = name)
    ser = serializers.CategoryLocationSerializer(Category, many=True)
    return Response(ser.data)


@api_view(["GET"])
def Ovqat_zakas_by_name(request):
    name = request.GET.get("name")
    Ovqat = models.Ovqat_zakas.objects.filter(name = name)
    ser = serializers.Ovqat_zakasSerializer(Ovqat, many=True)
    return Response(ser.data)


@api_view(["GET"])
def git_by_name(request):
    first_name = request.GET.get("first_name")
    git = models.Git.objects.filter(first_name = first_name)
    ser = serializers.GitSerializer(git, many=True)
    return Response(ser.data)