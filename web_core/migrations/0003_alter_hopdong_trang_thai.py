# Generated by Django 4.0.4 on 2023-06-03 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_core', '0002_alter_hanghoa_ten_hang_hoa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hopdong',
            name='trang_thai',
            field=models.CharField(blank=True, choices=[('Chờ phê duyệt', 'Chờ phê duyệt'), ('Đã duyệt', 'Đã duyệt'), ('Đang có hiệu lực', 'Đang có hiệu lực'), ('Đã hết hạn', 'Đã hết hạn')], default='Chờ phê duyệt', max_length=100, null=True, verbose_name='Trạng thái hợp đồng'),
        ),
    ]
