from apscheduler.schedulers.background import BackgroundScheduler
from trader import Trader
import logging

class Scheduler:
    def __init__(self, trader: Trader):
        self.trader = trader
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_jobstore('sqlalchemy', url='sqlite:///jobs.sqlite')

    def start(self):
        """
        Start the scheduler with predefined jobs.
        """
        # Schedule the trader run method to execute every minute
        self.scheduler.add_job(self.trader.run, 'interval', minutes=1)

        # Add more scheduled jobs if needed here
        self.scheduler.start()
        logging.info("Scheduler started, running jobs.")

    def shutdown(self):
        """
        Shut down the scheduler when the app is stopping.
        """
        self.scheduler.shutdown()
        logging.info("Scheduler shut down.")

# Example usage
if __name__ == "__main__":
    client = None  # Initialize your trading client
    strategy = None  # Initialize your trading strategy
    trader = Trader(client, strategy)
    sched = Scheduler(trader)
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        sched.shutdown()
