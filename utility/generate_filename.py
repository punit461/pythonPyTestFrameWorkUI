import datetime


def date_time():
    date = "%d-%m-%Y"
    time = "%H-%M-%S"
    return date, time


def generate_report_filename():
    date, time = date_time()
    current_time = datetime.datetime.now().strftime(date + "_" + time)
    return f"Test_Execution_Report_{current_time}.html"


def generate_ss_filename():
    date, time = date_time()
    current_time = datetime.datetime.now().strftime(date + "_" + time)
    return f"_{current_time}.png"


def generate_ss_folder():
    date, time = date_time()
    current_date = datetime.datetime.now().strftime(date)
    return f"Test_Execution_{current_date}"
