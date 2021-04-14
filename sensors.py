from sense_hat import SenseHat


class Weather:

    def __init__(self):
        self.sense = SenseHat()

    @staticmethod
    def get_temp(sense: SenseHat):
        temp_hum = sense.get_temperature_from_humidity()
        temp_pre = sense.get_temperature_from_pressure()
        avg_c = temp_hum / temp_pre
        return (avg_c * 1.8) + 32

    def get_weather_info(self):
        humidity = self.sense.get_humidity()
        pressure = self.sense.get_pressure()
        temp_f = self.get_temp(sense=self.sense)
        return {"humidity": humidity, "pressure": pressure, "temperature": temp_f}
