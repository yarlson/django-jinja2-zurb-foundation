django-jinnja2-zurb-foundation 5.1.1
============================

Django Zurb Foundation 5 package.

Version of this package is equal to the version of Zurb Foundation it provides.

Usage
=====

- Add `foundation-jinja2` to your `INSTALLED_APPS`.
- If you want to use the provided base template, extend from `foundation-jinja2/base.jinja`. If you want to write one from scratch, see the example template.
- If you want to test if foundation works, include `foundation.urls` in your urls.py and visit the path. You should see the Foundation test page.

Including Foundation js/css/vendor files
=============================================

To include specific Foundation js files, you can use `foundation_js` tag.

For example, to include `abide` library use:

    {% foundation_js('abide') %}

Depending on your static url, it will replace the previous tag with something like `<script src="/static/foundation/js/foundation/foundation.abide.js"></script>`.
Same works for Foundation css and vendor files, but in that case use the `foundation_css` or `foundation_vendor` tag the same way.

Note that if you call `foundation_js` without any parameters, it will include `foundation.min.js` file.

Foundation icons
================

The latest Foundation icons set is now included in this package.
The icons are not enabled by default. To enable them use something like this in your template:

    {% block css %}
        {% foundation_css('foundation-icons') %}
    {% endblock css %}

If you have added `foundation.urls` to your urls.py visit `icons/` on that path to see them.

