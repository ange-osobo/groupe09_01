class ConversionDuree:
    def run(self):
        h = int(input("Heures : "))
        m = int(input("Minutes : "))
        s = int(input("Secondes : "))
        total = h*3600 + m*60 + s
        print(f"Total : {total} secondes.")
