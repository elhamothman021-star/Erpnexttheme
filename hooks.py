# ---------------------------------------------------------------------------
# YOU Telecom | Enterprise Digital Transformation
# edt_ui - Shared UI Foundation / Design System
# 
# Author   : Anwar Taha Mohammed Al-Hitar
# Role     : Applications Developer Specialist - 2H | CEO Office
# Contact  : eyaalhitar@you.com.ye
# Created  : October 2026
# Version  : 20261021f
# ---------------------------------------------------------------------------

"""hooks.py for edt_ui

This file registers the edt_ui app with Frappe and injects the shared design-system
assets (CSS design tokens, component overrides, Vue component bundle, and utils bundle)
across all sites.

The edt_overrides.css file maps Frappe/ERPNext existing component classes (buttons,
inputs, cards, tables, modals, alerts, badges, sidebar) to edt_ui CSS design tokens,
so the standard Frappe UI automatically uses the shared design system.

Domain apps (hr_transformation, finance_transformation, etc.) inject edt_ui via their own
hooks.py using app_include_css / app_include_js, OR consume these globals directly.
"""

app_name = "edt_ui"
app_title = "edt_ui"
app_publisher = "YOU - Head Office"
app_description = "Enterprise Digital Transformation UI - Shared UI Foundation / Design System"
app_email = "eyaalhitar@you.com.ye"
app_license = "MIT"

# ---------------------------------------------------------------------------
# Asset injection across all sites (global include)
# ---------------------------------------------------------------------------
# These are loaded on every Desk page so the design tokens and shared components
# are available enterprise-wide without each app duplicating them.
# Order matters: tokens first, then overrides, then JS bundles.

EDT_UI_VERSION = "20261021f"

app_include_css = [
    "/assets/edt_ui/css/edt_design_tokens.css?v=" + EDT_UI_VERSION,
    "/assets/edt_ui/css/edt_overrides.css?v=" + EDT_UI_VERSION,
]

app_include_js = [
    "/assets/edt_ui/js/edt_utils.bundle.js?v=" + EDT_UI_VERSION,
    "/assets/edt_ui/js/edt_components.bundle.js?v=" + EDT_UI_VERSION,
]

# ---------------------------------------------------------------------------
# Web template / page includes (optional, for custom pages)
# ---------------------------------------------------------------------------
# web_include_css = ["/assets/edt_ui/css/edt_design_tokens.css", "/assets/edt_ui/css/edt_overrides.css"]
# web_include_js = ["/assets/edt_ui/js/edt_components.bundle.js"]

# ---------------------------------------------------------------------------
# Home page / role home page (optional)
# ---------------------------------------------------------------------------
# home_page = "login"
# role_home_page = {
#     "Manager": "dashboard",
# }

# ---------------------------------------------------------------------------
# Website user home page (by role)
# ---------------------------------------------------------------------------
# website_user_home_page = {
#     "HR Manager": "hr-dashboard",
#     "Finance Manager": "finance-dashboard",
# }

# ---------------------------------------------------------------------------
# Generators (optional)
# ---------------------------------------------------------------------------
# website_generators = ["Web Page"]

# ---------------------------------------------------------------------------
# Installation / before hooks (optional)
# ---------------------------------------------------------------------------
# before_install = "edt_ui.install.before_install"
# after_install = "edt_ui.install.after_install"

# ---------------------------------------------------------------------------
# Notifications (optional)
# ---------------------------------------------------------------------------
# notification_config = "edt_ui.notifications.get_notification_config"

# ---------------------------------------------------------------------------
# Permissions (optional)
# ---------------------------------------------------------------------------
# permission_query_conditions = {
#     "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
# has_permission = {
#     "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# ---------------------------------------------------------------------------
# DocType events (optional)
# ---------------------------------------------------------------------------
# doc_events = {
#     "*": {
#         "on_update": "method",
#         "on_cancel": "method",
#         "on_trash": "method",
#     }
# }

# ---------------------------------------------------------------------------
# Scheduled tasks (optional)
# ---------------------------------------------------------------------------
# scheduler_events = {
#     "all": [
#         "edt_ui.tasks.all"
#     ],
#     "daily": [
#         "edt_ui.tasks.daily"
#     ],
# }

# ---------------------------------------------------------------------------
# Testing (optional)
# ---------------------------------------------------------------------------
# before_tests = "edt_ui.install.before_tests"

# ---------------------------------------------------------------------------
# Overriding methods / whitelisted overrides (optional)
# ---------------------------------------------------------------------------
# override_whitelisted_methods = {
#     "frappe.desk.doctype.event.event.get_events": "edt_ui.event.get_events"
# }
# override_doctype_dashboards = {
#     "Task": "edt_ui.task.get_dashboard_data"
# }

# ---------------------------------------------------------------------------
# UI / Desk overrides (optional)
# ---------------------------------------------------------------------------
# override_doctype_class = {
#     "ToDo": "edt_ui.override.CustomToDo"
# }

# ---------------------------------------------------------------------------
# Document events / JS / CSS per doctype (optional)
# ---------------------------------------------------------------------------
# doctype_js = {
#     "Sales Invoice": "public/js/sales_invoice.js"
# }
# doctype_list_js = {
#     "Sales Invoice": "public/js/sales_invoice_list.js"
# }
# doctype_tree_js = {
#     "Sales Invoice": "public/js/sales_invoice_tree.js"
# }
# doctype_calendar_js = {
#     "Sales Invoice": "public/js/sales_invoice_calendar.js"
# }

# ---------------------------------------------------------------------------
# Fixtures (optional) - data to ship with the app
# ---------------------------------------------------------------------------
# fixtures = [
#     {"dt": "Custom Field", "filters": [...]},
# ]
