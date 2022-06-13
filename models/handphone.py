from odoo import api, fields, models


class Handphone(models.Model):
    _name ='toko.handphone'
    _description = 'New Description'
    name = fields.Char(string='name')
    
   
   
    
    merk = fields.Char(string='Merk HP')
    tipe = fields.Char(string='Tipe HP')
    spesifikasi = fields.Char(string='Spesifikasi')
    harga_hp = fields.Integer(string='Harga HP')
    stok_hp = fields.Integer(string='Stok HP')
    transaksi_id = fields.Many2one(comodel_name='toko_hp.transaksi', string='transaksi')
   
    
    
    
    
    

    
    
    
    
    