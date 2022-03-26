from odoo import models, fields, api


class Specialite(models.Model):
    _name = "tdsischool.level"
    _description = "Amphie"

    nom = fields.Char(string="Amphi", required=True)
    nombreetu = fields.Char(string="Nombre Etudiant", required=True)
    cours_ids = fields.Many2many(
        "tdsischool.cours",
        string="Cours"
    )
    _sql_constraints = [
        ('nom_uniq', 'unique (nom)', "Le nom existe déja !")
    ]

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s-%s" % (record.nom, record.nombreetu)
            result.append((record.id, rec_name))
        return result
