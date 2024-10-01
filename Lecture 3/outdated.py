months={
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}
def main():
    corrected=mordernize("Date:")
    print(corrected)

def mordernize(date):
    while True:
        try:
            outdate=str.strip(input(date))
            if len(outdate.split(" "))!=3 and len(outdate.split("/"))!=3:
                pass
            if outdate.split(" ")[0] in months:
                MM,DD,YYYY=outdate.split(" ")
                if DD.endswith(","):
                    MM=months[MM]
                    DD=DD.removesuffix(",")
                    update=[YYYY,MM,f"{int(DD):02}"]
                else:
                    pass
            else:
                MM,DD,YYYY=outdate.split("/")
                update=[YYYY,f"{int(MM):02}",f"{int(DD):02}"]
            if 0<int(DD)<32 and 0<int(MM)<13:
                return "-".join(update)
            else:
                pass
        except (KeyError,ValueError,UnboundLocalError):
            pass


main()
