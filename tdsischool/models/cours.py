from datetime import date, timedelta
from odoo import models, fields, api


class Cours(models.Model):
    _name = "tdsischool.cours"
    _description = "Cours"

    annee = fields.Integer(
        string="Annee",
        required=True
    )
    numero = fields.Integer(string="Numéro du cours", required=True)
    titre = fields.Char(string="Titre du cours")
    typecours = fields.Selection(
        [('C', 'C'),
         ('TD', 'TD'),
         ('TP', 'TP'),
        ],
        'Type', default="C")
    datedebut = fields.Date(string="Date de démarrage cours")
    datefin = fields.Date(string="Date prochain cours", compute="_compute_datefin")
    intervenant_id = fields.Many2one(
        "tdsischool.intervenant",
        string="Intervenant",
    )
    level_ids = fields.Many2many(
        "tdsischool.level",
        string="Classe"
    )

    _sql_constraints = [
        ('annee_numero_uniq', 'unique (annee, numero)', "L'année et le numéro existe déja !")
    ]

    def name_get(self):
        resul = []
        for record in self:
            rec_name = "%s" % (record.titre)
            resul.append((record.id, rec_name))
        return resul

    @api.depends('datedebut', 'datefin')
    def _compute_datefin(self):
        for record in self:
            td = timedelta(5)
            record.datefin = record.datedebut + td



