from frappe import _


def get_data():
    return [
        {
            "label": _("VetCare"),
            "items": [
                {
                    'type': 'doctype',
                    'name': 'Animal Overview'
                },
                {
                    'type': 'doctype',
                    'name': 'Patient Booking'
                },
                {
                    'type': 'doctype',
                    'name': 'Patient Activity'
                },
                {
                    'type': 'report',
                    'name': 'Patient History',
                    'is_query_report': True,
                }
            ]
        },
        {
            "label": _("Healthcare"),
            "items": [
                {
                    'type': 'doctype',
                    'name': 'Patient',
                    'description': _('Patient document')
                },
                {
                    'type': 'doctype',
                    'name': 'Healthcare Practitioner',
                    'description': _('Practitioner document')
                },
                {
                    'type': 'doctype',
                    'name': 'Practitioner Schedule'
                },
                {
                    'type': 'doctype',
                    'name': 'Healthcare Service Unit'
                },
                {
                    'type': 'doctype',
                    'name': 'Inpatient Record'
                },
                {
                    'type': 'doctype',
                    'name': 'Vital Signs'
                }
            ]
        },
        {
            "label": _("Setup"),
            "items": [
                {
                    'type': 'doctype',
                    'name': 'Vetcare Settings',
                    'description': _('Vetcare Settings')
                }
            ]
        }
    ]
