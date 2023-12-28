from rest_framework.generics import ListCreateAPIView,UpdateAPIView,DestroyAPIView
from main import models
from main import serializers


class CreateMexmonxona(ListCreateAPIView):
    queryset = models.Mexmonxona.objects.all()
    serializer_class = serializers.MexmonxonaSerializer


class UpdateMexmonxona(UpdateAPIView):
    queryset = models.Mexmonxona.objects.all()
    serializer_class = serializers.MexmonxonaSerializer


class DeleteMexmonxona(DestroyAPIView):
    queryset = models.Mexmonxona.objects.all()
    serializer_class = serializers.MexmonxonaSerializer


class CreateRoom(ListCreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class UpdateRoom(UpdateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class DeleteRoom(DestroyAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class CreateStol(ListCreateAPIView):
    queryset = models.Stol.objects.all()
    serializer_class = serializers.StolSerializer


class UpdateStol(UpdateAPIView):
    queryset = models.Stol.objects.all()
    serializer_class = serializers.StolSerializer


class DeleteStol(DestroyAPIView):
    queryset = models.Stol.objects.all()
    serializer_class = serializers.StolSerializer


class CreateTarixiy_joylar(ListCreateAPIView):
    queryset = models.Tarixiy_joylar.objects.all()
    serializer_class = serializers.Tarixiy_joylarSerializer


class UpdateTarixiy_joylar(UpdateAPIView):
    queryset = models.Tarixiy_joylar.objects.all()
    serializer_class = serializers.Tarixiy_joylarSerializer


class DeleteTarixiy_joylar(DestroyAPIView):
    queryset = models.Tarixiy_joylar.objects.all()
    serializer_class = serializers.Tarixiy_joylarSerializer


class CreateSubCategoryLocation(ListCreateAPIView):
    queryset = models.SubCategoryLocation.objects.all()
    serializer_class = serializers.SubCategoryLocationSerializer


class UpdateSubCategoryLocation(UpdateAPIView):
    queryset = models.SubCategoryLocation.objects.all()
    serializer_class = serializers.SubCategoryLocationSerializer


class DeleteSubCategoryLocation(DestroyAPIView):
    queryset = models.SubCategoryLocation.objects.all()
    serializer_class = serializers.SubCategoryLocationSerializer


class CreateKonferentsiya_markazi(ListCreateAPIView):
    queryset = models.Konferentsiya_markazi.objects.all()
    serializer_class = serializers.Konferentsiya_markaziSerializer


class UpdateKonferentsiya_markazi(UpdateAPIView):
    queryset = models.Konferentsiya_markazi.objects.all()
    serializer_class = serializers.Konferentsiya_markaziSerializer


class DeleteKonferentsiya_markazi(DestroyAPIView):
    queryset = models.Konferentsiya_markazi.objects.all()
    serializer_class = serializers.Konferentsiya_markaziSerializer


class CreateShifoxona(ListCreateAPIView):
    queryset = models.Shifoxona.objects.all()
    serializer_class = serializers.ShifoxonaSerializer


class UpdateShifoxona(ListCreateAPIView):
    queryset = models.Shifoxona.objects.all()
    serializer_class = serializers.ShifoxonaSerializer


class DeleteShifoxona(DestroyAPIView):
    queryset = models.Shifoxona.objects.all()
    serializer_class = serializers.ShifoxonaSerializer


class CreateAvtoturargoh(ListCreateAPIView):
    queryset = models.Avtoturargoh.objects.all()
    serializer_class = serializers.AvtoturargohSerializer


class UpdateAvtoturargoh(UpdateAPIView):
    queryset = models.Avtoturargoh.objects.all()
    serializer_class = serializers.AvtoturargohSerializer


class DeleteAvtoturargoh(DestroyAPIView):
    queryset = models.Avtoturargoh.objects.all()
    serializer_class = serializers.AvtoturargohSerializer


class CreateTurar_joy(ListCreateAPIView):
    queryset = models.Turar_joy.objects.all()
    serializer_class = serializers.Turar_joySerializer


class UpdateTurar_joy(UpdateAPIView):
    queryset = models.Turar_joy.objects.all()
    serializer_class = serializers.Turar_joySerializer


class DeleteTurar_joy(DestroyAPIView):
    queryset = models.Turar_joy.objects.all()
    serializer_class = serializers.Turar_joySerializer


class CreateDokon(ListCreateAPIView):
    queryset = models.Dokon.objects.all()
    serializer_class = serializers.DokonSerializer


class UpdateDokon(UpdateAPIView):
    queryset = models.Dokon.objects.all()
    serializer_class = serializers.DokonSerializer


class DeleteDokon(DestroyAPIView):
    queryset = models.Dokon.objects.all()
    serializer_class = serializers.DokonSerializer


class CreateRestoran(ListCreateAPIView):
    queryset = models.Restoranlar.objects.all()
    serializer_class = serializers.RestoranlarSerializer


class UpdateRestoran(UpdateAPIView):
    queryset = models.Restoranlar.objects.all()
    serializer_class = serializers.RestoranlarSerializer


class DeleteRestoran(DestroyAPIView):
    queryset = models.Restoranlar.objects.all()
    serializer_class = serializers.RestoranlarSerializer


class CreateCategoryLocation(ListCreateAPIView):
    queryset = models.CategoryLocation.objects.all()
    serializer_class = serializers.CategoryLocationSerializer


class UpdateCategoryLocation(UpdateAPIView):
    queryset = models.CategoryLocation.objects.all()
    serializer_class = serializers.CategoryLocationSerializer


class DeleteCategoryLocation(DestroyAPIView):
    queryset = models.CategoryLocation.objects.all()
    serializer_class = serializers.CategoryLocationSerializer


class CreateChangi_uchun_maydon(ListCreateAPIView):
    queryset = models.Changi_uchun_maydon.objects.all()
    serializer_class = serializers.Changi_uchun_maydonSerializer


class UpdateChangi_uchun_maydon(UpdateAPIView):
    queryset = models.Changi_uchun_maydon.objects.all()
    serializer_class = serializers.Changi_uchun_maydonSerializer


class DeleteChangi_uchun_maydon(DestroyAPIView):
    queryset = models.Changi_uchun_maydon.objects.all()
    serializer_class = serializers.Changi_uchun_maydonSerializer


class CreateAddress(ListCreateAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class UpdateAddress(UpdateAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class DeleteAddress(DestroyAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class CreateBolalar_clubi(ListCreateAPIView):
    queryset = models.Bolalar_clubi.objects.all()
    serializer_class = serializers.Bolalar_clubiSerializer


class UpdateBolalar_clubi(UpdateAPIView):
    queryset = models.Bolalar_clubi.objects.all()
    serializer_class = serializers.Bolalar_clubiSerializer


class DeleteBolalar_clubi(DestroyAPIView):
    queryset = models.Bolalar_clubi.objects.all()
    serializer_class = serializers.Bolalar_clubiSerializer


class CreateTexnik_spetsifikatsiyalar(ListCreateAPIView):
    queryset = models.Texnik_spetsifikatsiyalar.objects.all()
    serializer_class = serializers.Texnik_spetsifikatsiyalarSerializer


class UpdateTexnik_spetsifikatsiyalar(UpdateAPIView):
    queryset = models.Texnik_spetsifikatsiyalar.objects.all()
    serializer_class = serializers.Texnik_spetsifikatsiyalarSerializer


class DeleteTexnik_spetsifikatsiyalar(DestroyAPIView):
    queryset = models.Texnik_spetsifikatsiyalar.objects.all()
    serializer_class = serializers.Texnik_spetsifikatsiyalarSerializer


class CreateDam_olish_maskani(ListCreateAPIView):
    queryset = models.Dam_olish_maskani.objects.all()
    serializer_class = serializers.Dam_olish_maskaniSerializer


class UpdateDam_olish_maskani(UpdateAPIView):
    queryset = models.Dam_olish_maskani.objects.all()
    serializer_class = serializers.Dam_olish_maskaniSerializer


class DeleteDam_olish_maskani(DestroyAPIView):
    queryset = models.Dam_olish_maskani.objects.all()
    serializer_class = serializers.Dam_olish_maskaniSerializer


class CreateYetkazib_berish(ListCreateAPIView):
    queryset = models.Yetkazib_berish.objects.all()
    serializer_class = serializers.Yetkazib_berishSerializer


class UpdateYetkazib_berish(UpdateAPIView):
    queryset = models.Yetkazib_berish.objects.all()
    serializer_class = serializers.Yetkazib_berishSerializer


class DeleteYetkazib_berish(DestroyAPIView):
    queryset = models.Yetkazib_berish.objects.all()
    serializer_class = serializers.Yetkazib_berishSerializer


class CreateKutqaruv_tibiy_xizmat(ListCreateAPIView):
    queryset = models.Kutqaruv_tibiy_xizmat.objects.all()
    serializer_class = serializers.Kutqaruv_tibiy_xizmatSerializer


class UpdateKutqaruv_tibiy_xizmat(UpdateAPIView):
    queryset = models.Kutqaruv_tibiy_xizmat.objects.all()
    serializer_class = serializers.Kutqaruv_tibiy_xizmatSerializer


class DeleteKutqaruv_tibiy_xizmat(DestroyAPIView):
    queryset = models.Kutqaruv_tibiy_xizmat
    serializer_class = serializers.Kutqaruv_tibiy_xizmatSerializer


class CreateOperator(ListCreateAPIView):
    queryset = models.Operator.objects.all()
    serializer_class = serializers.OperatorSerializer


class UpdateOperator(UpdateAPIView):
    queryset = models.Operator.objects.all()
    serializer_class = serializers.OperatorSerializer


class DeleteOperator(DestroyAPIView):
    queryset = models.Operator.objects.all()
    serializer_class = serializers.OperatorSerializer


class CreateOvqat_zakas(ListCreateAPIView):
    queryset = models.Ovqat_zakas.objects.all()
    serializer_class = serializers.Ovqat_zakasSerializer


class UpdateOvqat_zakas(UpdateAPIView):
    queryset = models.Ovqat_zakas.objects.all()
    serializer_class = serializers.Ovqat_zakasSerializer


class DeleteOvqat_zakas(DestroyAPIView):
    queryset = models.Ovqat_zakas.objects.all()
    serializer_class = serializers.Ovqat_zakasSerializer


class CreateGit(ListCreateAPIView):
    queryset = models.Git.objects.all()
    serializer_class = serializers.GitSerializer


class UpdateGit(UpdateAPIView):
    queryset = models.Git.objects.all()
    serializer_class = serializers.GitSerializer


class DeleteGit(DestroyAPIView):
    queryset = models.Git.objects.all()
    serializer_class = serializers.GitSerializer