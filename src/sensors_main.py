# -*- coding: utf-8 -*-
import datetime, time
from apscheduler.schedulers.blocking import BlockingScheduler
from src.sensors.sensors1_text import sonde1
from src.sensors.sensors2_piechart import sonde2
from src.sensors.sensors3_linechart import sonde3
from src.sensors.sensors4_cumulativeflow import sonde4
from src.sensors.sensors5_simplepercentage import sonde5
from src.sensors.sensors6_listing import sonde6
from src.sensors.sensors7_barchart import sonde7
from src.sensors.sensors8_fancylisting import sonde8
from src.sensors.sensors9_bigvalue import sonde9
from src.sensors.sensors10_justvalue import sonde10
from src.sensors.sensors11_advancedplot import sonde11
# from src.sensors.sensorsjs2_piechart import sonde12
from src.sensors.utils import end


def launch_sensors():
    sonde1()
    sonde3()
    sonde4()
    sonde5()
    sonde6()
    sonde7()
    sonde8()
    sonde9()
    sonde10()
    sonde11()
    # sonde12()


def scheduleYourSensors():
    scheduler = BlockingScheduler()
    scheduler.add_job(sonde1, 'interval', minutes=42)
    scheduler.add_job(sonde2, 'interval', minutes=42)
    scheduler.add_job(sonde3, 'interval', minutes=42)
    scheduler.add_job(sonde4, 'interval', minutes=42)
    scheduler.add_job(sonde5, 'interval', minutes=42)
    scheduler.add_job(sonde6, 'interval', minutes=42)
    scheduler.add_job(sonde7, 'interval', minutes=42)
    scheduler.add_job(sonde8, 'interval', seconds=20)
    scheduler.add_job(sonde8, 'interval', hours=1, minutes=30, seconds=20)
    scheduler.add_job(sonde9, 'interval', hours=1, minutes=30)
    scheduler.add_job(sonde10, 'interval', hours=1)
    scheduler.add_job(sonde11, 'interval', days=1, next_run_time=datetime.datetime.now())
    print(f"(+) Tipboard starting schedul task", flush=True)
    scheduler.start()
    return True


if __name__ == "__main__":
    print(f"(+) Tipboard  sensors initialisation", flush=True)
    start_time = time.time()
    launch_sensors()
    end(title="startUp", start_time=start_time)
    # scheduleYourSensors() If you need actualized data :)
    end(title="scheduled sensors ", start_time=start_time)
