from applications.accounts.models import User
from applications.products_framework.models import ProductType, Category, Attribute
from django.db import IntegrityError

def create_users():
    print('Creating users')
    user = User(email='koos@example.com', username='Koos', is_staff=True)
    user.set_password('MeatCo.1')
    user.save()
    print('Created user "Koos"')

    user = User(email='jan@example.com', username='Jan')
    user.set_password('MeatCo.1')
    user.save()
    print('Create user "Jan"')

    print('Done creating users')

def create_product_types():
    print('Creating product types')
    for name in ['Animals', 'Vehicles', 'Real Estate']:
        pt = ProductType(name=name)
        pt.save()
        print('Created {}'.format(name))
    print()

def create_categories():
    print('Creating Categories')
    categories_dict = {
        'Vehicles': ['Cars', 'Trucks'],
        'Animals': ['Dogs', 'Cats'],
        'Real Estate': ['Residential', 'Commercial'],
    }
    product_types = ProductType.objects.all()
    for type in product_types:
        if type.name in categories_dict.keys():
            for cat_name in categories_dict[type.name]:
                cat = Category(name=cat_name, product_type=type)
                cat.save()
                print('Created category: {}: {}'.format(type.name, cat_name))

def create_attributes():
    print('Creating Attributes')
    categories_dict = {
        'Vehicles': [('Manufacturer', True, 'STRING'), ('Model', True, 'STRING'), ('Colour', True, 'STRING'), ('Kilometers', False, 'INTEGER')],
        'Animals': [('Colour', True, 'STRING'), ('Age', False, 'INTEGER'), ('Breed', False, 'STRING')],
        'Real Estate': [('Plot Size (sqm)', True, 'INTEGER'), ('No of Bedrooms', False, 'INTEGER'), ('No of Bathrooms', False, 'INTEGER')],
    }
    product_types = ProductType.objects.all()
    for type in product_types:
        if type.name in categories_dict.keys():
            for attr_name, required, d_type in categories_dict[type.name]:
                try:
                    attr = Attribute(name=attr_name, product_type=type, required=required, data_type = d_type)
                    attr.save()
                    print('Created category: {}: {}'.format(type.name, attr, required))
                except IntegrityError as err:
                    pass

def create_all():
    create_users()
    create_product_types()
    create_attributes()

if __name__ == '__main__':
    create_users()
    create_product_types()

