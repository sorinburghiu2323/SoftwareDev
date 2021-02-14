import json

from django.http import HttpResponseNotAllowed, QueryDict
from django.http.multipartparser import MultiPartParser


def handle_methods(request, GET=None, POST=None, PUT=None, PATCH=None, DELETE=None, args=[], kwargs={}):
    """
    REST Method Handler.
    Return the view handleMethods(request)

    Add all allowed methods with their responses. These can either be a Django HttpResponse,
    or a callable function that takes a single request argument and calls it if the request is of the specified type.

    Any requests without a defined type will be returned with a 405 Method Not Allowed
    and a corresponding list of allowed methods.

    The supported methods are GET, POST, PUT, PATCH, and DELETE.

    Example:
    def my_restful_view(request):
        return handleMethods(request,
                             GET=HttpResponse("GET"),
                             POST=HttpResponse("POST"),
                             PUT=HttpResponse("PUT"),
                             PATCH=my_restful_patch_function)
    """

    def method_not_allowed():
        methods = []
        if GET is not None:
            methods += ["GET"]
        if POST is not None:
            methods += ["POST"]
        if PUT is not None:
            methods += ["PUT"]
        if PATCH is not None:
            methods += ["PATCH"]
        if DELETE is not None:
            methods += ["DELETE"]
        return HttpResponseNotAllowed(methods)
    try:
        if request.content_type.lower() == "application/json":
            data = json.loads(request.body)
        elif request.content_type.lower() == "multipart/form-data":
            data = MultiPartParser(request.META, request, request.upload_handlers).parse()[0].dict()
        else:
            data = QueryDict(request.body).dict()
    except Exception:
        data = QueryDict(request.body).dict()
    request.DATA = data
    if request.method == "GET":
        if GET is None:
            return method_not_allowed()
        if callable(GET):
            return GET(request, *args, **kwargs)
        return GET
    if request.method == "POST":
        if POST is None:
            return method_not_allowed()
        if callable(POST):
            return POST(request, *args, **kwargs)
        return POST
    if request.method == "PUT":
        if PUT is None:
            return method_not_allowed()
        if callable(PUT):
            return PUT(request, *args, **kwargs)
        return PUT
    if request.method == "PATCH":
        if PATCH is None:
            return method_not_allowed()
        if callable(PATCH):
            return PATCH(request, *args, **kwargs)
        return PATCH
    if request.method == "DELETE":
        if DELETE is None:
            return method_not_allowed()
        if callable(DELETE):
            return DELETE(request, *args, **kwargs)
        return DELETE
    for method, function in kwargs.items():
        if request.method == method:
            if function is None:
                return method_not_allowed()
            if callable(function):
                kwargs.pop(method)
                return function(request, *args, **kwargs)
            return function
    return method_not_allowed()
