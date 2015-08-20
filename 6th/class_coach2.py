def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + "." + secs


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted(set(sanitize(t) for t in self.times))[0:3]

    def add_time(self, time):
        self.times.append(time)

    def add_times(self, times):
        self.times.extend(times)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(",")
            return Athlete(templ.pop(0), templ.pop(0), templ)
    except IOError as err:
        print("File error : " + str(err))
        return None


sarah = get_coach_data("sarah2.txt")
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

james = get_coach_data("james2.txt")
print(james.name + "'s fastest times are: " + str(james.top3()))
