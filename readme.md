# Django Easy Metatags


#### Django Easy Metatags is a package for adding meta tags from admin panel to any url of your website.


### Quick start

1. Add "metatags" to your INSTALLED_APPS setting like this::

    ```
    INSTALLED_APPS = [
        ...
        'metatags',
    ]
    ```

2. Run ``python manage.py migrate`` to create the polls models.

3. Load metatags templates tags in base.html::

    ``{% load metatags %}``

4. Add metatags tag in head of body or any page where you want to add meta tags to.

    ```
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {% metatags request.path %}
        <title>Document</title>
    </head>
    ```

5. Visit http://127.0.0.1:8000/admin/metatags/metatag/ to add meta tags.

6. In slug add some unique feature of url.

7. Enjoy!