# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class Pembelian(models.Model):
    _name = 'ogudang.pembelian' 
    _description = 'Ini adalah pembelian barang'

    name = fields.Char('No Transaksi', store=True)
    
    tgl = fields.Date(default=fields.Date.today())

    customer_id =  fields.Many2one(comodel_name='res.partner', ondelete='restrict')

    total = fields.Float(store=True)

