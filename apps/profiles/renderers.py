import json
from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self,data,accepted_media_types=None,render_context=None):
        errors = data.get('errors',None)

        if errors is None:
            return super(ProfileJSONRenderer,self).render(data)
        return json.dumps({"profile":data})