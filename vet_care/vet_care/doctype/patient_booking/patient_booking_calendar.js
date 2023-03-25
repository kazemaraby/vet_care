frappe.views.calendar['Patient Booking'] = {
  gantt: true,
  order_by: 'appointment_date',
  get_events_method: 'vet_care.vet_care.doctype.patient_booking.patient_booking.get_events',
  field_map: {
    'start': 'start',
    'end': 'end',
    'id': 'name',
    'title': 'title',
    'allDay': 'allDay',
    'eventColor': 'color'
  },
  options: {
    minTime: '08:00:00',
    maxTime: '23:00:00',
    slotDuration: '00:15:00',
    slotLabelInterval: 15,
    slotLabelFormat: 'h(:mm)a',
    slotMinutes: 15,
  }
};
