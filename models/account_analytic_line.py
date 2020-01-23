# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    #@api.model
    #def create(self, values):
        # print(vals)
        # vals['employee_id'] = self.env.uid
        # print('vals', vals)
        # super(AccountAnalyticLine, self).create(vals)
        # return {"type": "ir.actions.act_window_close"}
        # if not values.get('employee_id') and values.get('project_id'):
        #     if values.get('user_id'):
        #         ts_user_id = values['user_id']
        #     else:
        #         ts_user_id = self._default_user()
        #     values['employee_id'] = self.env['hr.employee'].search([('user_id', '=', ts_user_id)], limit=1).id

        # values = self._timesheet_preprocess(values)
        # result = super(AccountAnalyticLine, self).create(values)
        # if result.project_id:  # applied only for timesheet
        #     result._timesheet_postprocess(values)
        # return result