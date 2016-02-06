from django.http import HttpResponse
import json

from ..models import Expert, Office, Project, Agency
from ..utils import serialize, JSONEncoderPlus, prefetch_constraints
from ..views import MandelbrotView, ExpertView, ExpertsView


class APIView(MandelbrotView):
    json_cls = JSONEncoderPlus

    def get(self, request, *args, **kwargs):
        data = self.lookup(request, *args, **kwargs)
        return HttpResponse(json.dumps(
            serialize(self.fields, data),
            cls=self.json_cls,
        ))


class ExpertView(APIView, ExpertView):
    fields = (
        'id', 'name', 'photo_url', 'title', 'bio', 'active',
        'start_date', 'end_date',

        'interests.name'

        'buddy.id', 'buddy.name',

        'contact_details.type', 'contact_details.value',
        'contact_details.label', 'contact_details.note',

        'memberships.project.id', 'memberships.project.name',
        'memberships.project.active', 'memberships.start_date',
        'memberships.end_date', 'memberships.roles.name',
        'memberships.part_time',

        'badges.badge.id', 'badges.badge.title', 'badges.awarded_on',
        'badges.awarded_by.id', 'badges.awarded_by.name',
    )

class ExpertsView(APIView, ExpertsView):
    fields = (
        'id', 'name', 'photo_url', 'title', 'active',
        'start_date', 'end_date',

        'contact_details.type', 'contact_details.value',
        'contact_details.label', 'contact_details.note',
    )


# vim: foldmethod=marker
