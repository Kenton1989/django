# Architecture Notes

# Units
django.utils: tools commonly used by multiple independent modules
django.conf: configurations
django.dispatch: communication based on Observer pattern
django.core: core functionality for running a HTTP server
- management: entry point, directly used by 'manage.py' script, see management.\_\_init\_\_.execute_from_command_line
django.db: things about database
django.urls: URL router
django.http: core functionality of http: parsing request & encoding response, cookie
django.views: http handler
django.middleware: request middleware
django.template: page template, typically html page
django.form: simplify manipulation of html form
django.contrib: add-on functionality