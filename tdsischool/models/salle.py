from odoo import models, fields, api


class Salle(models.Model):
    _name = "tdsischool.salle"
    _description = "Salle"

    nom = fields.Char(string="Nom Salle")
    nombreplace = fields.Char(string="Nombre de place")

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s-%s" % (record.nom, record.nombreplace)
            result.append((record.id, rec_name))
        return result
