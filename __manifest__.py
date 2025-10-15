{
    'name': 'Custom Purple Theme',
    'version': '17.0.1.0.0',
    'category': 'Hidden',
    'summary': 'Custom Dark Purple Theme for Odoo',
    'description': """
Custom Dark Purple Theme
========================
This module provides a custom dark purple theme for Odoo including:
- Dark purple color scheme
- Custom login page styling
- Modern UI elements
- Responsive design
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['web'],
    'data': [],
    'assets': {
        'web.assets_common': [
            'custom_theme/static/src/css/login.css',
        ],
        'web.assets_backend': [
            'custom_theme/static/src/css/backend.css',
            'custom_theme/static/src/css/login.css',
        ],
        'web.assets_frontend': [
            'custom_theme/static/src/css/login.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}