# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class Barang(models.Model):
    _name = 'ogudang.barang' 
    _description = 'Ini adalah master produk'


    name = fields.Char('Nama Barang', required=True)

    kode_barang = fields.Char(string="Kode Barang")

    stok = fields.Integer(required=True)

    harga = fields.Float(required=True)

    berat = fields.Float(default=0)

    state = fields.Selection(string='Status', selection=[
        ('available', 'Tersedia'),
        ('unavailable', 'Tidak Tersedia'),
    ])