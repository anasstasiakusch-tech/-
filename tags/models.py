from django.db import models
from django.utils.text import slugify
from cats.models import Cat


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Тег')
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CatTag(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='cat_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_cats')

    class Meta:
        unique_together = ('cat', 'tag')

    def __str__(self):
        return f'{self.cat.name} - {self.tag.name}'