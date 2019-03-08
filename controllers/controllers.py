# -*- coding: utf-8 -*-
from odoo import http

class LeadWebsite(http.Controller):

    @http.route('/contactus', website=True)
    def lead_website(self, **kw):
        return http.request.render('lead_website.new_lead_form')
