# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.5, generator: @autorest/python@6.4.11)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, cast

from azure.core.pipeline.transport import HttpRequest


def _convert_request(request, files=None):
    data = request.content if not files else None
    request = HttpRequest(method=request.method, url=request.url, headers=request.headers, data=data)
    if files:
        request.set_formdata_body(files)
    return request


def _format_url_section(template, **kwargs):
    components = template.split("/")
    while components:
        try:
            return template.format(**kwargs)
        except KeyError as key:
            # Need the cast, as for some reasons "split" is typed as list[str | Any]
            formatted_components = cast(List[str], template.split("/"))
            components = [c for c in formatted_components if "{}".format(key.args[0]) not in c]
            template = "/".join(components)
