from datetime import date, datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

from yx_project.spiders.yx import YX

yx = YX()
def test_tick():
    yx.browser.refresh()
    yx.web_monitoring()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(test_tick, 'interval', seconds=60)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
