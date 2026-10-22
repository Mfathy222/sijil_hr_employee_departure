{
    'name': 'Sijil HR Employee Departure',
    'summary': 'Salary Certificate (تعريف بالراتب) letter + payslip report design',
    'description': """
Sijil HR Employee Departure
================

Adds a dynamic Smart Button to the Employee profile for printing official departure documents. To prevent human error, the button is conditionally visible only for departed (archived) employees.

Key Features:

    Conditional Smart Button Visibility: The print button automatically appears at the top of the profile only when the employee's status is set to "Departed" (Archived).

    One-Click PDF Generation: Instant generation of the official clearance or departure document directly from the archived profile.

    Dynamic Content Mapping: Automatically pulls employee core data and pairs it with the specific departure date and reason (Resignation, Termination, Retirement, etc.) from Odoo 19.

    Print-Ready PDF Layout: A clean, corporate-grade PDF template equipped with designated signature blocks for both the Employee and the HR Department.

    Automated Chatter Logging: Keeps a permanent record by automatically posting a copy of the generated PDF to the employee's chatter.
""",
    'version': '19.0.1.0.18',
    'author': 'Sijil Dev Team',
    'category': 'Human Resources/Payroll',
    'depends': ['hr','hr_payroll','l10n_sa_hr_payroll','account',
    ],
    'data': [
        'report/employee_departure.xml',
        'views/hr_employee_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
