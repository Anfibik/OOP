class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):

        seconds = self.__len__()
        if seconds:
            h = seconds // 3600
            m = (seconds - 3600 * h) // 60
            s = seconds - (h * 3600 + m * 60)
            return f"{str(h).rjust(2, '0')}: {str(m).rjust(2, '0')}: {str(s).rjust(2, '0')}"
        return "00: 00: 00"

    def __len__(self):
        time_difference = self.clock1.get_time() - self.clock2.get_time()
        return time_difference if time_difference > 0 else 0


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = self.check_value(hours)
        self.minutes = self.check_value(minutes)
        self.seconds = self.check_value(seconds)

    @staticmethod
    def check_value(value):
        if type(value) == int and value >= 0:
            return value
        return None

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
