import time
import random

print("🤖 Smart Bot Activated")

while True:
    # Simulated sensor readings
    wall_detected = random.choice([True, False])
    human_detected = random.choice([True, False])

    print("\nScanning environment...")

    if human_detected:
        print("👤 Human detected! Pausing...")
        time.sleep(3)
        print("Resuming movement...")

    elif wall_detected:
        direction = random.choice(["left", "right"])
        print(f"🧱 Wall detected! Turning {direction}...")
        time.sleep(1)

    else:
        print("Path clear. Moving forward...")
        time.sleep(1)

    # Stop loop after some cycles (for demo)
    if random.randint(1, 10) == 5:
        print("\n🛑 Stopping bot simulation.")
        break
