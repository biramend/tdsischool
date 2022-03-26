from odoo import models, fields, api


class Intervenant(models.Model):
    _name = "tdsischool.intervenant"
    _description = "Intervenant"

    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom")
    telephone = fields.Integer(string="Téléphone")
    telephone1 = fields.Integer(string="Téléphone Secondaire")
    telephone2 = fields.Integer(string="Téléphone Fixe")
    cours_ids = fields.One2many(
        "tdsischool.cours",
        "intervenant_id",
        string="Cours",
    )
    specialite_ids = fields.Many2many(
        "tdsischool.specialite",
        string="Specialite"
    )
    bureau_id = fields.Many2one("tdsischool.bureau", string="Bureau")

    _sql_constraints = [
        ('nom_uniq', 'unique (nom)', 'Le nom existe déja !')
    ]

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s-%s" % (record.prenom, record.nom)
            result.append((record.id, rec_name))
        return result
