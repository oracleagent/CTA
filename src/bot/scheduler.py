from apscheduler.schedulers.background import BackgroundScheduler
from trader import Trader
from db.models import create_tables, Trade, Order, Configuration, session
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
        try:
            # Schedule the trader run method to execute every minute
            self.scheduler.add_job(self.trader.run, 'interval', minutes=1)

            # Add more scheduled jobs if needed here
            self.scheduler.start()
            logging.info("Scheduler started, running jobs.")
        except Exception as e:
            logging.error(f"Error starting scheduler: {e}")

    def shutdown(self):
        """
        Shut down the scheduler when the app is stopping.
        """
        try:
            self.scheduler.shutdown()
            logging.info("Scheduler shut down.")
        except Exception as e:
            logging.error(f"Error shutting down scheduler: {e}")

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    create_tables()  # Ensure the database tables are created

    # Initialize your trading client and strategy
    client = None  # Replace with actual trading client initialization
    strategy = None  # Replace with actual trading strategy initialization

    trader = Trader(client, strategy)
    sched = Scheduler(trader)
    
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        sched.shutdown()
