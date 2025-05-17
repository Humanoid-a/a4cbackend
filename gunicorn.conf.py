# gunicorn.conf.py

import multiprocessing
import os

# 1. Where to bind: a UNIX socket or an IP:port
bind = os.getenv("GUNICORN_BIND", "unix:/run/gunicorn.sock")
# bind = os.getenv("GUNICORN_BIND", "0.0.0.0:8080")

# 2. Number of worker processes
# A common formula: (2 × $num_cores) + 1
workers = int(3)

# 3. Worker class: sync, gevent, uvicorn.workers.UvicornWorker, etc.
worker_class = os.getenv("GUNICORN_WORKER_CLASS", "sync")

# 4. Maximum requests per worker before restart (memory-leak mitigation)
max_requests = int(os.getenv("GUNICORN_MAX_REQUESTS", 1000))
max_requests_jitter = int(os.getenv("GUNICORN_MAX_REQUESTS_JITTER", 50))

# 5. Timeouts (in seconds)
timeout = int(os.getenv("GUNICORN_TIMEOUT", 30))
keepalive = int(os.getenv("GUNICORN_KEEPALIVE", 2))

# 6. Logging
accesslog = os.getenv("GUNICORN_ACCESS_LOG", "-")   # “-” → stdout
errorlog  = os.getenv("GUNICORN_ERROR_LOG",  "-")
loglevel  = os.getenv("GUNICORN_LOG_LEVEL",  "info")

# 7. Preload app (loads application code before forking workers)
preload_app = os.getenv("GUNICORN_PRELOAD", "false").lower() in ("1", "true", "yes")

# 8. Change working directory
chdir = os.getenv("GUNICORN_CHDIR", "/a4cbackend")

# Optionally: user/group to run as
# uid = os.getenv("GUNICORN_UID", "www-data")
# gid = os.getenv("GUNICORN_GID", "www-data")