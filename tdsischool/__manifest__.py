# -*- coding: utf-8 -*-
{
    'name': "TDSISCHOOL",

    'summary': """
        TDSISCHOOL""",

    'description': """
        Gestion des cours dispensés dans une école d'ingénieur, 
        ainsi que les personnes qui interviennent dans ces cours.En Particulier TDSI
    """,
    "company": "TDSI",
    'author': "Birame NDIAYE",
    'website': "https://biramend.github.io/NdiayeCV/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'TDSI',
    "version": "13.0.1",

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/cours_views.xml',
        'views/intervenant_views.xml',
        'views/bureau_views.xml',
        'views/specialite_views.xml',
        'report/tdsischool_report_templates.xml',
        'report/tdsischool_report.xml',
        'views/level_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
    #'images': ['static/description/banner.png'],
    "auto_install": False,
    "application": False,
    "license": "AGPL-3",
}