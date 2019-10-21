from django.db import models




class ModelAdi(models.Model):

    title = models.CharField(verbose_name=u'Başlık', max_length=200,help_text="Sadece baş harfler büyük olacak şekilde giriş yapınız.")

    description = models.CharField(verbose_name=u'Yazı', max_length=1000, blank=True,help_text="Cümle formatında giriş yapınız.")

    link = models.URLField(verbose_name=u"Url", help_text="Link", blank=True, null=True)