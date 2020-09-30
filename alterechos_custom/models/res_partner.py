# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def cron_compute_is_subscriber(self):
        partners = self.search([])
        partners._compute_is_subscriber()
