import time

def main():
    seconds = 0
    minutes = 0
    hours = 0

    while True:
        try:
            seconds += 1
            time.sleep(1)

            if seconds == 60:
                seconds = 0
                minutes += 1
            
            if minutes == 60:
                minutes = 0
                hours += 1

            if len(str(seconds)) == 2:
                prnt = f"0{hours}:0{minutes}:{seconds}"
                if len(str(minutes)) == 2:
                    prnt = f"0{hours}:{minutes}:{seconds}"
                    if len(str(hours)) == 2:
                        prnt = f"{hours}:{minutes}:{seconds}"
                    else:
                        prnt = f"0{hours}:{minutes}:{seconds}"
                else:
                    prnt = f"0{hours}:0{minutes}:{seconds}"
            else:
                prnt = f"0{hours}:0{minutes}:0{seconds}"
            print(prnt, end='\r')

        except KeyboardInterrupt:
            raise SystemExit

if __name__ == "__main__":
    main()