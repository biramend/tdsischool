from odoo import models, fields, api


class Specialite(models.Model):
    _name = "tdsischool.specialite"
    _description = "Spécialité"

    speciality = fields.Char(string="Spécialité", required=True)
    domaine = fields.Char(string="Domaine", required=True)
    intervenant_ids = fields.Many2many(
        "tdsischool.intervenant",
        string="Intervenant"
    )
    _sql_constraints = [
        ('speciality_domaine_uniq', 'unique (speciality, domaine)', "Cette spécialité existe déja dans le domaine !")
    ]
