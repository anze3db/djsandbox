import multiprocessing

bind = "unix:djsandbox.sock"
workers = multiprocessing.cpu_count() + 1
threads = multiprocessing.cpu_count() * 2
proc_name = "djsandbox"
# Access log - records incoming HTTP requests
accesslog = "/var/log/gunicorn-djsandbox.access.log"
# Error log - records Gunicorn server goings-on
errorlog = "/var/log/gunicorn-djsandbox.error.log"
# Whether to send Django output to the error log
capture_output = True
# How verbose the Gunicorn error logs should be
loglevel = "info"

pidfile = "gunicorn.pid"
