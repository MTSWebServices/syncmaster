# CLI for managing superusers { #manage-superusers-cli }

There are two ways to manage users:

- automatic:

  [REST API Server][server] Docker container entrypoint will automatically create users with `is_superuser=True` in database
  during startup.

  Usernames can be passed via config file:

```yaml title="config.yml"
superusers:
  - user1
  - user2
```

  Or via environment variable:

```bash
export 'SYNCMASTER__SUPERUSERS=["user1", "user2"]'
```

- manual via CLI:
<!-- TODO: fix docstring extraction -->
<!--.. argparse::
   :module: syncmaster.server.scripts.manage_superusers
   :func: create_parser
   :prog: python -m syncmaster.server.scripts.manage_superusers
   -->
