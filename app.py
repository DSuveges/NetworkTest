from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

# Importing custom modules:
from modules.db_connection import db_connection
from modules.db_tools import db_handler
from modules.ping import Ping
from configuration import properites

app = Flask(__name__)

# cron = Scheduler(daemon=True)
# # Explicitly kick off the background thread
# cron.start()
#
# # Shutdown the scheduler web process is stopped
# atexit.register(lambda: cron.shutdown())
#
#
# @cron.interval_schedule(seconds=1)


def ping_servers(pingObj, IDs, dbh):
    responses = pingObj.ping()
    mapped_responses = list(map(lambda x, y: (x[1], y), IDs, responses))
    dbh.add_ping_response(mapped_responses)


# The following endpoint serves testing purposes only to demonstrate the flexibility of the template generation.
@app.route('/network_test')
def template_test():
    return render_template('index.html')


def main():

    # Extract properties from config file:
    servers = properites.Configuration.server_list
    db_file = properites.Configuration.db_file
    ping_time = properites.Configuration.ping_interval

    # Connect to db:
    connection = db_connection(db_file)
    dbh = db_handler(connection.conn)

    # Add servers to db:
    IDs = dbh.add_servers(servers)

    # Initialize ping object:
    pingObj = Ping([x[0] for x in servers])

    # Start pinging:
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=ping_servers, trigger="interval", seconds=ping_time, args=[pingObj, IDs, dbh])
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

    app.run(debug=False)


if __name__ == '__main__':
    main()
