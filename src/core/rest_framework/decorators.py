from functools import wraps
from django.utils.decorators import method_decorator

def template_name(name: str):

    def decorator(view_func):
        @wraps(view_func)
        def _wrapper_view(*args, **kwargs):
            response = view_func(*args, **kwargs)
            response.template_name = name
            return response
        
        return _wrapper_view
    
    return decorator

def viewset_template_name(**kwargs):
    def decorator(viewset):
        for key, value in kwargs.items():
            decorator = method_decorator(template_name(value), name=key)
            decorator(viewset)
        return viewset

    return decorator
