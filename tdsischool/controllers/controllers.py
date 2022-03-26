# -*- coding: utf-8 -*-
from odoo import http

# class Tdscschool(http.Controller):
#     @http.route('/tdscschool/tdscschool/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tdscschool/tdscschool/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tdscschool.listing', {
#             'root': '/tdscschool/tdscschool',
#             'objects': http.request.env['tdscschool.tdscschool'].search([]),
#         })

#     @http.route('/tdscschool/tdscschool/objects/<model("tdscschool.tdscschool"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tdscschool.object', {
#             'object': obj
#         })