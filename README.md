This application serves API for stats.cybergreen.net

# CyberGreen Cubes

---

For development run:

```
# install requirements
$ pip install -r requirements.txt

# Export database url like so
CG_URL=dialect+driver://username:password@host:port/database
# example
DATABASE_URI=postgres://cg_user:SecetPassword@cg-example.jdutoe634ksdk.cg-region-1.rds.amazonaws.com:1234/cg_database

# run server
$ python setup.py
```

visit http://localhost:5000 to see results
