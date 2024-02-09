import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category

def populate():
    # 创建或更新Python类别
    python_cat = Category.objects.get_or_create(name='Python')[0]
    python_cat.views = 128
    python_cat.likes = 64
    python_cat.save()

    # 创建或更新Django类别
    django_cat = Category.objects.get_or_create(name='Django')[0]
    django_cat.views = 64
    django_cat.likes = 32
    django_cat.save()

    # 创建或更新Other Frameworks类别
    other_cat = Category.objects.get_or_create(name='Other Frameworks')[0]
    other_cat.views = 32
    other_cat.likes = 16
    other_cat.save()

if __name__ == '__main__':
    print("开始执行Rango应用的数据填充脚本...")
    populate()
