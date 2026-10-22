from odoo import models


class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    def _build_wkhtmltopdf_args(self, *args, **kwargs):
        command_args = super()._build_wkhtmltopdf_args(*args, **kwargs)

        if "--encoding" not in command_args:
            command_args.extend(["--encoding", "utf-8"])

        return command_args