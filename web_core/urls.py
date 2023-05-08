from django.urls import path

from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', lambda request: redirect('dspr', permanent=False), name='home'),
    # path('', views.dskb, name='home'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('dshh/', views.dshh, name='quanli_dshh'),

    path('dspr/', views.dspr, name='quanli_dspr'),
    path('them_pr/', views.add_pr, name='quanli_them_pr'),
    path('xem_pr/<str:ma_PR>', views.view_pr, name='quanli_xem_pr'),

    path('ca_nhan/dspr/', views.dspr_canhan, name='canhan_dspr'),
    path('ca_nhan/them_pr/', views.add_pr, name='canhan_them_pr'),
    path('ca_nhan/xem_pr/<str:ma_PR>', views.view_pr_canhan, name='canhan_xem_pr'),
    path('ca_nhan/sua_pr/<str:ma_PR>-<str:ma_HH>', views.edit_pr_canhan, name='canhan_sua_pr'),

    path('phancong_pr/<str:ma_PR>', views.phancong_pr, name='quanli_phancong_pr'),

    path('dspo/', views.dspo, name='quanli_dspo'),
    path('xem_po/<str:ma_PO>', views.view_po, name='quanli_xem_po'),
    path('ca_nhan/dspo/', views.dspo_canhan, name='canhan_dspo'),
    path('ca_nhan/xem_po/<str:ma_PO>', views.view_po_canhan, name='canhan_xem_po'),
    path('ca_nhan/capnhat_po/<str:ma_PO>', views.update_po_status, name='canhan_capnhat_po'),

    path('them_po/<str:ma_PR>-<str:ma_HH>', views.add_po, name='canhan_them_po'),
    path('them_po_2/', views.add_po_2, name='canhan_them_po_2'),
    path('sua_po/<str:ma_PO>', views.edit_po, name='canhan_sua_po'),
    path('duyet_po/<str:ma_PO>', views.duyet_po, name='quanli_duyet_po'),

    path('dsncc/', views.dsncc, name='quanli_dsncc'),
    path('them_ncc/', views.add_ncc, name='quanli_them_ncc'),
    path('xem_ncc/<str:ma_NCC>', view=views.view_ncc, name='quanli_xem_ncc'),


    path('ca_nhan/dsncc/', views.dsncc_canhan, name='canhan_dsncc'),
    path('ca_nhan/xem_ncc/<str:ma_NCC>', view=views.view_ncc_canhan, name='canhan_xem_ncc'),
    path('ca_nhan/sua_ncc/<str:ma_NCC>', view=views.edit_ncc, name='canhan_sua_ncc'),

    path('dshd/', views.dshd, name='quanli_dshd'),
    path('them_hd/', views.add_hd, name='quanli_them_hd'),
    path('xem_hd/<str:ma_HD>', view=views.view_hd, name='quanli_xem_hd'),
    path('duyet_hd/<str:ma_HD>', views.duyet_hd, name='quanli_duyet_hd'),

    path('ca_nhan/dshd/', views.dshd_canhan, name='canhan_dshd'),
    path('ca_nhan/xem_hd/<str:ma_HD>', view=views.view_hd_canhan, name='canhan_xem_hd'),
    path('ca_nhan/sua_hd/<str:ma_HD>', view=views.edit_hd, name='canhan_sua_hd'),
    # path('dsbn', views.dsbn, name='quanli_dsbn'),
    # path('sua_bn/<str:id>', views.edit_benhnhan, name='quanli_sua_benhnhan'),
    # path('xoa_bn/<str:id>', views.del_benhnhan, name='quanli_xoa_benhnhan'),

    # path('xuathoadon', views.xuathoadon, name='quanli_xuathoadon'),
    # path('hoadon/<str:pk>/', views.hoadon, name='quanli_xuathoadon_hoadon'),

    # path('lsk',views.lsk, name='quanli_lsk'),

    # path('dspk',views.dspk, name='quanli_dspk'),
    # path('them_pk', views.add_phieukham, name='quanli_them_phieukham'),
    # path('sua_pk/<str:id>', views.edit_phieukham, name='quanli_sua_phieukham'),
    # path('xoa_pk/<str:id>', views.del_phieukham, name='quanli_xoa_phieukham'),

    # path('lapbaocao/', views.lap_bao_cao, name='quanli_lapbaocao'),
    # path('lapbaocao/doanhthuthang/', views.baocao_doanhthuthang, name='quanli_lapbaocao_bcdtt'),
    # path('lapbaocao/sudungthuoc/', views.baocao_sudungthuoc, name='quanli_lapbaocao_bcsdt'),

    # path('thaydoi/', views.thaydoi_quydinh, name='quanli_thaydoi'),
    # path('thaydoi/soluongbenhnhan', views.thaydoi_slbn, name='quanli_thaydoi_slbn'),
    # path('thaydoi/tienkham', views.thaydoi_tienkham, name='quanli_thaydoi_tienkham'),

    # path('thaydoi/loaibenh', views.thaydoi_loaibenh, name='quanli_thaydoi_loaibenh'),
    # path('thaydoi/loaibenh/them', views.thaydoi_loaibenh_them, name='quanli_thaydoi_loaibenh_them'),
    # path('thaydoi/loaibenh/xoa/<str:id>', views.thaydoi_loaibenh_xoa, name='quanli_thaydoi_loaibenh_xoa'),

    # path('thaydoi/donvitinh', views.thaydoi_dvt, name='quanli_thaydoi_dvt'),
    # path('thaydoi/donvitinh/them', views.thaydoi_dvt_them, name='quanli_thaydoi_dvt_them'),
    # path('thaydoi/donvitinh/xoa/<str:id>', views.thaydoi_dvt_xoa, name='quanli_thaydoi_dvt_xoa'),

    # path('thaydoi/cachdung', views.thaydoi_cachdung, name='quanli_thaydoi_cachdung'),
    # path('thaydoi/cachdung/them', views.thaydoi_cachdung_them, name='quanli_thaydoi_cachdung_them'),
    # path('thaydoi/cachdung/xoa/<str:id>', views.thaydoi_cachdung_xoa, name='quanli_thaydoi_cachdung_xoa'),

    # path('thaydoi/thuoc', views.thaydoi_thuoc, name='quanli_thaydoi_thuoc'),
    # path('thaydoi/thuoc/them', views.thaydoi_thuoc_them, name='quanli_thaydoi_thuoc_them'),
    # path('thaydoi/thuoc/xoa/<str:id>', views.thaydoi_thuoc_xoa, name='quanli_thaydoi_thuoc_xoa'),
    # path('thaydoi/thuoc/sua/<str:id>', views.thaydoi_thuoc_sua, name='quanli_thaydoi_thuoc_sua'),
]
