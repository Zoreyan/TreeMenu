from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'



class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True, help_text="URL или name для reverse")

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def get_absolute_url(self):
        try:
            return reverse(self.url)
        except NoReverseMatch:
            return self.url

    def __str__(self):
        return self.title