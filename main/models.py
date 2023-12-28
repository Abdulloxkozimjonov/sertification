from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify


class User(AbstractUser):
    foto = models.ImageField(upload_to='foto/')
    phone_number=models.CharField(max_length=13,null=True,blank=True,validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message = 'Invalide phone number',
            code = 'Invalid number'
        )
    ])
    bio = models.CharField(max_length=13, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable= 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Employee(models.Model):
    user = models.ForeignKey(to="User", on_delete=models.PROTECT)


class Mexmonxona(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    room = models.ForeignKey(to="Room", on_delete=models.CASCADE)
    description = models.TextField()
    # qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    #
    # def save(self, *args, **kwargs):
    #     qr = qrcode.QRCode(
    #     version=1,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=8,
    #     border=4,
    # )
    # qr.add_data(f"Your data to encode in the QR code: {self.Mexmonxona.name}")
    # qr.make(fit=True)
    # img = qr.make_image(fill_color="black", back_color="white")
    # buffer = BytesIO()
    # img.save(buffer)
    # buffer.seek(0)
    #
    # self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

    # super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Room(models.Model):
    user = models.ForeignKey(to="User", on_delete=models.CASCADE)
    STATUS = (
        ('luxury','Luxury'),
        ('economy','Economy')
    )
    name = models.CharField(max_length=100, choices=STATUS, default='luxury')
    description = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Stol(models.Model):
    user = models.ForeignKey(to="User", on_delete=models.PROTECT)
    ovqat_zakas = models.ForeignKey(to="Ovqat_zakas", on_delete=models.PROTECT)
    name = models.CharField(max_length=55)
    xajmi = models.IntegerField(blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tarixiy_joylar(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Avtoturargoh(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     qr = qrcode.QRCode(
    #     version=1,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=8,
    #     border=4,
    # )
    # qr.add_data(f"Your data to encode in the QR code: {self.address.name}")
    # qr.make(fit=True)
    # img = qr.make_image(fill_color="black", back_color="white")
    # buffer = BytesIO()
    # img.save(buffer)
    # buffer.seek(0)
    #
    # self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
    #
    # super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Konferentsiya_markazi(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Shifoxona(models.Model):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    name = models.CharField(max_length=100)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.car_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Restoranlar(models.Model):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    name = models.CharField(max_length=255)
    description = models.TextField()
    stol = models.ForeignKey(to="Stol", on_delete=models.PROTECT)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.address.name}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Turar_joy(models.Model):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    name = models.CharField(max_length=100)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Dokon(models.Model):
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    name = models.CharField(max_length=100)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Kutqaruv_tibiy_xizmat(models.Model):
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Bolalar_clubi(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Dam_olish_maskani(models.Model):
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    name = models.CharField(max_length=125)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.address.name}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Texnik_spetsifikatsiyalar(models.Model):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    name = models.CharField(max_length=100)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.car_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Operator(models.Model):
    ADMIN = (
        (1,'Boshlik'),
        (2,'Admin'),
        (3,'odiy user'),
    )
    user1 = models.IntegerField(default=0, choices=ADMIN, null=True, blank=True)
    user = models.ForeignKey(to="User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(to="Address", on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Changi_uchun_maydon(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.car_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Yetkazib_berish(models.Model):
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    name = models.CharField(max_length=100)
    buyurtma_raqami = models.IntegerField()
    address = models.ForeignKey(to = "Address", on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.car_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CategoryLocation(models.Model):
    name = models.CharField(max_length=255)

    def str(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategoryLocation(models.Model):
    location_category = models.ForeignKey(to='CategoryLocation', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def str(self):
        return self.name


class Ovqat_zakas(models.Model):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    name = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.car_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Git(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=13, blank=True, null=True, verbose_name='Telefon_raqam', unique=True, validators=[
            RegexValidator(
                regex='^[\+]9{2}8{1}[0-9]{9}$',
                message='Invalide phone number',
                code='Invalid number'
                )
    ])
    img = models.ImageField(upload_to='git_img/')


