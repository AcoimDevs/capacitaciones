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
        default=False
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

    
    contact = fields.Char(
        string='contactos',
    )
    
    
    employers = fields.Boolean(
        string='empleados',
        default=False
    )

    
   
    
    expense = fields.Boolean(
        string='Gastos',
        default=False 
    )
    
    def saludar(self):
        for record in self:
            record.check = True
            record.employers = True
            record.expense=True


    def cancelar(self):
        for record in self:
            record.check = False
            record.employers = False
            record.expense=False


    state= fields.Selection(
       string='Estado',
       selection=[('draft', 'Borrador'), 
               ('validated', 'validado'),
               ('cancel','cancelado')],
               
        default='draft',
    )

   
    

    
 



    #char
    #boolean
    #integer
    #fload
