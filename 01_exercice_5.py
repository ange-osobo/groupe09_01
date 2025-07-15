class CalculVitesse:
    def run(self):
        dist = float(input("Distance (km) : "))
        temps = float(input("Temps (h) : "))
        v_kmh = dist / temps
        v_ms = v_kmh * 1000/3600
        print(f"Vitesse : {v_kmh:.2f} km/h ({v_ms:.2f} m/s)")
