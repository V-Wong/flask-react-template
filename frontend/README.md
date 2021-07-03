# frontend
## API Reverse Proxy
A reverse proxy is setup to simplify paths to backend. All routes are simply prepended with ``/api`` with no reference to IP address. For example, if you want to access the ``/users`` route, you would use ``/api/users``.