from odoo import api, fields, models


class Transaksi(models.Model):
    _name = 'toko_hp.transaksi'
    _description = 'New Description'

    tanggal = fields.Datetime(string='Tanggal Transaksi',default=fields.Datetime.now)
    jumlah_beli= fields.Integer(string='Jumlah Beli')
    total_harga = fields.Integer(string='Total Harga')
    handphonedetail_ids = fields.One2many(
        comodel_name='toko.handphone', 
        inverse_name='transaksi_id', 
        string='Handphonenya')
    
    
    
    
        
    
    
