# Django Rest Framework Multi-tenant SaaS application

This project uses `django-tenants` and `django-tenant-users` to handle tenant-specific data in separate schemas using PostgreSQL,
while also allowing to have a single global user. For more information on how this project is set up, visit 
[tenant-users](https://github.com/Corvia/django-tenant-users) repository.

## API

This example app is a Restaurant app. It incorporates entities such as Restaurant, Menu, Category and Menu Item.

There are two APIs:
- **Public API**
- **Tenant API**

Public API offers the following:
- Signup
- login
- Retrieve users information and detail
- Retrieve, create, update, delete the restaurant
- CRUD Menus
- CRUD Category
- CRUD product

With Tenant API your can:
- retrieve Menu (With categories)
- retrieve Category (With items)
- retrieve Item 

###### API examples

Login and registration are available at `yourdomain/login` and `yourdomain/register` respectively.

To access data about a menu item, for instance, you can visit 

`yourdomain/api/restaurants/<restaurant_id>/menus/<menu_id>/categories/<category_id>/items/<item_id>`

To list users and view user instances, you can use the following links:

`yourdomain/users/`

`yourdomain/users/<user_id>`

You can list any instances provided above by not including their id in the URL.

To retrieve object details on a subdomain, visit <br>
`tenant_slug.yourdomain/api/menus/<menu_id>` <br>
`tenant_slug.yourdomain/api/categories/<category_id>`<br>
`tenant_slug.yourdomain/api/items/<item_id>`

Notice that the following URL is not present in the public domain.

## Project specific setup

This project uses `python-dotenv` to hide sensitive data. Thus, you have to create a `.env` file in the project's
root directory.

There, specify the following variables (or hardcode them into the project if you really want to)
- `SECRET_KEY` - Django secret key
- `POSTGRES_USER`
- `POSTGRES_PASS`
- `PUBLIC_TENANT_EMAIL` - this is the email for our public tenant
- `PUBLIC_TENANT_DOMAIN` - your domain (`"localhost"` if running locally)

Before populating the database, run [this](restaurant_saas/create_public_tenant.py) script first.

User creation and tenant provisioning (restaurant) can both be done using the public API. You can do so via your browser
as well (thanks DRF)