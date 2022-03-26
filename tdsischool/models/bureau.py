from odoo import models, fields, api


class Bureau(models.Model):
    _name = "tdsischool.bureau"
    _description = "Bureau"

    numbureau = fields.Integer(string="Numéro du bureau", required=True, max=10000)
    batiment = fields.Selection(
        [('A', 'A'),
         ('B', 'B'),
         ('C', 'C'),
         ('D', 'D'),
         ('E', 'E'),
         ('F', 'F'),
         ('G', 'G'),
         ('H', 'H'),
         ('I', 'I'),
         ('J', 'J'),
         ('K', 'K'),
         ('L', 'L'),
         ('M', 'M'),
         ('N', 'N'),
         ('O', 'O'),
         ('P', 'P'),
         ('Q', 'Q'),
         ('R', 'R'),
         ('S', 'S'),
         ('T', 'T'),
         ('U', 'U'),
         ('V', 'V'),
         ('W', 'W'),
         ('X', 'X'),
         ('Y', 'Y'),
         ('Z', 'Z'),
         ],
        'Batiment', default="A"
        , required=True)
    centre = fields.Selection(
        [('R', 'R'),
         ('BF', 'BF'),
         ('PG', 'PG'),
         ],
        'Centre', default="R"
        , required=True)
    intervenant_list = fields.One2many("tdsischool.intervenant", "bureau_id", string="Intervenant")

    _sql_constraints = [
        ("nombre", "CHECK(numbureau <= 1000)", " Le Numéro du bureau doit etre inférieure à ou égale à 1000 ")
    ]

    def name_get(self):
        buro = []
        for record in self:
            rec_name = "%s-%s-%s" % (record.numbureau, record.batiment, record.centre)
            buro.append((record.id, rec_name))
        return buro
