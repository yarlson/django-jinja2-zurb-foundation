from django.templatetags.static import static
from django_jinja import library

lib = library.Library()


@lib.global_function
def foundation_js(js_name=None):
    js_path = "foundation/js/foundation/foundation.{0}.js".format(js_name)
    if js_name is None:
        js_path = "foundation/js/foundation.min.js".format(js_name)

    return '<script src="{0}"></script>'.format(static(js_path))


@lib.global_function
def foundation_vendor(vendor_name):
    vendor_path = "foundation/js/vendor/{0}.js".format(vendor_name)
    return '<script src="{0}"></script>'.format(static(vendor_path))


@lib.global_function
def foundation_css(css_name):
    css_path = "foundation/css/{0}.css".format(css_name)
    return '<link rel="stylesheet" href="{0}"/>'.format(static(css_path))
