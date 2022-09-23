{
    'name': 'Library',
    'summary': '',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': [
        'base',
    ],

    'external_dependencies': {'python': ['pyisbn', ], },

    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',

        'views/menu.xml',
        'views/book.xml',
        'views/author.xml',
        'views/category.xml',
        'views/book_instance.xml',
    ],
    'demo': [
        'demo/author.xml',
        'demo/category.xml',
        'demo/book.xml',
        'demo/book_instance.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'EUR',

}
