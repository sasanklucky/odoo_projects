from email.policy import default

from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    ref = fields.Char(string="Reference")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default="male")
    active = fields.Boolean(string="Active", default=True)  # unarchived state

    @api.onchange("age")
    def archive_state(self):
        for record in self:
            if record.age <= 18:
                record.active = False
            else:
                record.active = True
