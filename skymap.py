import sys
import math

commands = ["-help", "-h", "-skymap", "get-ha", "calculate-all", "get-j2000",
            "-year", "-month", "-day", "-time_utc", "-lat", "-long", "-ra", "-dec"]
help_flag = False
print("\n\n\n\n\n\nhelp: \npython skymap.py help not all function work it is alfa version\n\n\n\n\n\n")


class SkyMap:
    hour = 0

    day = 22
    min = 0
    sec = 0
    year = 2021
    month = 9
    time_utc = 22
    longitude = 0
    latitude = 0
    Ra = 0
    Dec = 0
    Star_az = 0
    Star_alt = 0
    j2000 = 0
    declination = 0
    right_ascension = 0
    ha = 0.00
    lst = 0.00

    def __init__(self,  lattitude=0,  longitude=0,  declination=0,  right_ascension=0,  year=0,  month=0,  day=0,  time_utc=0):
        self.latitude = lattitude
        self.longitude = longitude
        self.declination = declination
        self.right_ascension = right_ascension
        self.year = year
        self.month = month
        self.day = day
        self.time_utc = time_utc
        if self.latitude != 0 and self.longitude != 0:
            self.Calculate_all()

    def deg2rad(self, deg):
        return deg * 3.14159265358979 / 180

    def rad2deg(self, rad):
        return rad * 180 / 3.14159265358979

    def my_location(self, lattitude=0,  longitude=0):
        self.latitude = lattitude
        self.longitude = longitude

    def star_ra_dec(self, right_ascension=0,  declination=0):
        self.right_ascension = right_ascension
        self.declination = declination

    def Hh_mm_ss2UTC(self, hhh,  mmm,  sss,  your_timezone_offset=0):
        self.hour = hhh
        self.min = mmm
        self.sec = sss
        self.timezone_offset = your_timezone_offset

    def DateTime(self, year, month, day, utc):
        self.year = year
        self.month = month
        self.time_utc = utc
        self.day = day

    def J2000(self, Y=0,  M=0,  D=0,  TIME=0):

        if (Y != 0 and M != 0 and D != 0 and TIME != 0):

            jd = (367 * Y - math.floor(7 * (Y + math.floor((M + 9) / 12)) / 4) - math.floor(3 *
                                                                                            (math.floor((Y + (M - 9) / 7) / 100) + 1) / 4) + math.floor(275 * M / 9) + D + 1721028.5 + TIME / 24)
            self.j2000 = jd - 2451545
            return self.j2000
        else:
            jd = (367 * self.year - math.floor(7 * (self.year + math.floor((self.month + 9) / 12)) / 4) - math.floor(3 * (math.floor(
                (self.year + (self.month - 9) / 7) / 100) + 1) / 4) + math.floor(275 * self.month / 9) + self.day + 1721028.5 + self.time_utc / 24)
            self.j2000 = jd - (2451545)

            return self.j2000

    def Local_Sidereal_Time(self, j2000=0,  time_utc=0,  longitude=0):

        if (j2000 != 0 and time_utc != 0 and longitude != 0):

            lst = 100.46 + 0.985647 * j2000 + longitude + 15 * time_utc
            if (lst < 0):

                lst += 360

            elif (lst > 360):

                lst -= 360

            return lst

        else:

            _lst = 100.46 + 0.985647 * self.j2000 + self.longitude + 15 * self.time_utc
            if (_lst < 0):

                _lst += 360

            elif (_lst > 360):
                _lst -= 360

            self.lst = _lst
            return _lst

    def Hour_Angle(self, LST=0,  right_ascension=0):

        if (LST != 0 and right_ascension != 0):

            self.ha = LST - right_ascension
            if (self.ha < 0):

                self.ha += 360

            elif (self.ha > 360):

                self.ha -= 360

            return self.ha

        else:
            self.ha = self.lst - self.right_ascension
            if (self.ha < 0):
                self.ha += 360
            elif (self.ha > 360):
                self.ha -= 360
            return self.ha

    def calculate_AZ_alt(self, hour_angle=0,  declination=0,  lattitude=0):
        sinDEC = math.sin(self.deg2rad(declination))
        sinHA = math.sin(self.deg2rad(hour_angle))
        sinLAT = math.sin(self.deg2rad(lattitude))
        cosDEC = math.cos(self.deg2rad(declination))
        cosHA = math.cos(self.deg2rad(hour_angle))
        cosLAT = math.cos(self.deg2rad(lattitude))
        sinALT = (sinDEC * sinLAT) + (cosDEC * cosLAT * cosHA)
        self.ALT = math.asin(sinALT)
        cosALT = math.cos((self.ALT))
        cosA = (sinDEC - sinALT * sinLAT) / (cosALT * cosLAT)
        self.A = math.acos(cosA)
        self.A = self.rad2deg(self.A)
        self.ALT = self.rad2deg(self.ALT)

        if (sinHA > 0):
            self.AZ = 360 - self.A
        else:
            self.AZ = self.A
        self.Star_alt = self.ALT
        self.Star_az = self.AZ
        return self.ALT, self.AZ

    def Calculate_all(self):
        self.J2000()
        self.Local_Sidereal_Time()
        self.Hour_Angle()
        self.calculate_AZ_alt(self.ha, self.declination, self.latitude)

    def update(self, lattitude=0,  longitude=0,  declination=0,  right_ascension=0,  year=0,  month=0,  day=0,  time_utc=0):
        self.latitude = lattitude
        self.longitude = longitude
        self.declination = declination
        self.right_ascension = right_ascension
        self.year = year
        self.month = month
        self.day = day
        self.time_utc = time_utc
        self.Calculate_all()

    def get_azymuth(self):
        return self.Star_az

    def get_alt(self):
        return self.Star_alt


class my_location:
    latitude = 34.052235
    longitude = -118.243683


class star:

    altitude = 0.0
    azymuth = 0.0
    declination = -16.7424
    right_ascension = 101.52


class input_date_time:
    year = 2021
    month = 9
    day = 4
    UTC_TIME = 16


def caluclating_star_location():
    #global help_flag
    tracked_star = star()
    mylocation = my_location()
    datetime = input_date_time()
    skymap = SkyMap()
    correct_input_length = False
    if(sys.argv[1] == commands[4] and len(sys.argv) > 9 and help_flag == False):
        correct_input_length = True
    if correct_input_length:
        sys.argv[2] = mylocation.latitude
        sys.argv[3] = mylocation.longitude
        sys.argv[4] = tracked_star.declination
        sys.argv[5] = tracked_star.right_ascension
        sys.argv[6] = datetime.year
        sys.argv[7] = datetime.month
        sys.argv[8] = datetime.day
        sys.argv[9] = datetime.UTC_TIME
        skymap.my_location(mylocation.latitude, mylocation.longitude)
        skymap.DateTime(datetime.year, datetime.month,
                        datetime.day, datetime.UTC_TIME)
        skymap.star_ra_dec(tracked_star.right_ascension,
                           tracked_star.declination)
        skymap.Calculate_all()
        tracked_star.azymuth = skymap.get_azymuth()
        tracked_star.altitude = skymap.get_alt()
        print(
            f"data provided by you\nyour location:\nlat: {mylocation.latitude} long: {mylocation.longitude}\nday and time: {datetime.year}-{datetime.month}-{datetime.day} time:{datetime.UTC_TIME}\nlooking for:Star RA : {tracked_star.right_ascension},Dec : {tracked_star.declination}\n")
        print("\n---------------------------------------------------------Results---------------------------------------------------------\n")
        if(tracked_star.altitude > 0):
            print("Visibility : STAR IS VISIBLE")
        else:
            print("Visibility : STAR IS not VISIBLE")
        print(
            f"your star is located at azymuth:{tracked_star.azymuth} altitude:{tracked_star.altitude}\n")
        print("\n---------------------------------------------------------Results---------------------------------------------------------\n")

        print("program finished")

        sys.exit()
    else:
        print("number of input arguments is incorrect")
        sys.exit()


def main():

    if len(sys.argv) == 1:
        print("python skymap.py -h\ncopy line above to get -help")
    else:

        for command in commands:

            if sys.argv[1] == command:

                for args in sys.argv:
                    if args == commands[1]:
                        help_flag = True
                    else:
                        help_flag = False
                        if sys.argv.count("-h") == 0:
                            caluclating_star_location()

                if help_flag == True and len(sys.argv) == 3:
                    if sys.argv[1] == commands[4] or sys.argv[2] == commands[4]:
                        print(
                            "example:\npython skymap.py calculate-all [latitude] [longitude] [Dec] [Ra] [year] [month] [day] [utc]\n ")
                        print(
                            "example below show how to calculate position of star on sky in example below we observe sirius at los angeles on 4th of september 2021 time :20UTC\nif you dont know star RA and dec search for right ascension and declination of star you are looking for on internet :)")
                        print(
                            "\nlos angeles and sirius example:\npython skymap.py calculate-all 34.052235 -118.243683 -16.7424 101.52 2021 9 4 20\n")
                    else:
                        print(f"command is not valid\nall commands:{commands}")
                else:
                    print(
                        "you are not using help properly\nexample:\npython skymap.py calculate-all -h\n\nor\n\npython skymap.py -h calculate-all\n\n")


main()
