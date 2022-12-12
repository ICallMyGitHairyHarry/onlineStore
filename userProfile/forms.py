from django import forms

from catalogue.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pr_name', 'desc', 'ingreds', 'img', 'pr_cost', 'pr_price', 'pr_left']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['pr_name'].label = 'Название'
        self.fields['desc'].label = 'Описание'
        self.fields['ingreds'].label = 'Состав'
        self.fields['img'].label = 'Изображение'
        self.fields['pr_cost'].label = 'Затраты'
        self.fields['pr_price'].label = 'Цена'
        self.fields['pr_left'].label = 'Количество на складе'

        self.fields['desc'].widget.attrs.update(rows=3, maxlength=1000)
        self.fields['ingreds'].widget.attrs.update(rows=3, maxlength=1000)

        self.fields['pr_name'].widget.attrs.update(onChange="correct_field('id_pr_name')")
        self.fields['desc'].widget.attrs.update(onChange="correct_field('id_desc')")
        self.fields['ingreds'].widget.attrs.update(onChange="correct_field('id_ingreds')")
