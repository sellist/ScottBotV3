- Needs following environment variables:
  - DB_NAME={{Name of desired DB to connect to}}
  - DB_USER={{User name of db client}}
  - DB_PASS={{Password of user of db client}}
  - TOKEN={{Discord bot token}}

- Needs POSTGRESQL database, can use the provided `db/create.sh` to create one.

To run locally, use command `nohup python main.py &` to run persistently, and to kill,
`ps -ef | grep main.py` and then `kill [PID]`. Otherwise, just `python main.py`.