
import pandas
signal_monitoring = pandas.read_csv("signal_monitoring.csv")
signal_monitoring["event_date_time"] = pandas.to_datetime(signal_monitoring["event_date_time"])
signal_monitoring["event_end_date_time"] = signal_monitoring["event_date_time"].shift(-1)
signal_monitoring["outage_lenght"] = signal_monitoring["event_end_date_time"] - signal_monitoring["event_date_time"]
# Převedu typ datetimedelta na sekundy = číslo
signal_monitoring["outage_lenght"] = signal_monitoring["outage_lenght"].dt.total_seconds()
# Vybírám řádky, kde je ve sloupci event_type hodnota signal lost
signal_monitoring = signal_monitoring[signal_monitoring["event_type"] == "signal lost"]
print(signal_monitoring["outage_lenght"].mean())