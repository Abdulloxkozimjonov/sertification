from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exlude = ('password',)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Room
        fields = "__all__"


class StolSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Stol
        fields = "__all__"


class Tarixiy_joylarSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Tarixiy_joylar
        fields = "__all__"


class MexmonxonaSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Mexmonxona
        fields = "__all__"


class Konferentsiya_markaziSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Konferentsiya_markazi
        fields = "__all__"


class ShifoxonaSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Shifoxona
        fields = "__all__"


class AvtoturargohSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Avtoturargoh
        fields = "__all__"


class Turar_joySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Turar_joy
        fields = "__all__"


class DokonSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Dokon
        fields = "__all__"


class RestoranlarSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Restoranlar
        fields = "__all__"


class Kutqaruv_tibiy_xizmatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kutqaruv_tibiy_xizmat
        fields = "__all__"


class CategoryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryLocation
        fields = "__all__"


class CategoryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryLocation
        fields = "__all__"


class SubCategoryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategoryLocation
        fields = "__all__"


class Ovqat_zakasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ovqat_zakas
        fields = "__all__"


class Changi_uchun_maydonSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Changi_uchun_maydon
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = "__all__"


class Bolalar_clubiSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Bolalar_clubi
        fields = "__all__"


class Texnik_spetsifikatsiyalarSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Texnik_spetsifikatsiyalar
        fields = "__all__"


class Dam_olish_maskaniSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Dam_olish_maskani
        fields = "__all__"


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Operator
        fields = "__all__"

class Yetkazib_berishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Yetkazib_berish
        fields = "__all__"


class GitSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = models.Git
        fields = "__all__"