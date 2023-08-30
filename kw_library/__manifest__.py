{
    'name': 'Library',
    'summary': '',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.2',

    'depends': [
        'base',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',

        'views/menu.xml',
        'views/book.xml',
        'views/author.xml',
    ],
    'demo': [
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

}
