# -*- coding: utf-8 -*-

from odoo import api, models, fields
class L10nBoNotes(models.Model):
    _name = 'l10n.bo.notes' 
    _description = 'Notas internas'

    #no es obligaroeio pero si es necesario (-> display name)
    name = fields.Char(
        string='nombre',
        required=True,
        default='Nota interna'
         
    )
    
    check = fields.Boolean(
        string='validar',
        default=True
    )
    
    company_id = fields.Many2one(
        string='Compañia', 
        comodel_name='res.company', 
        required=True, 
        default=lambda self: self.env.company #lo veremos despues
    )
    
    
    purchase_id = fields.Many2one(
        string='Compra',
        comodel_name='purchase.order',
        ondelete='restrict',
    )
    
    
    sale_id = fields.Many2one(
        string='ventas',
        comodel_name='sale.order',
        ondelete='restrict',
    )
    

    #char
    #boolean
    #integer
    #fload
