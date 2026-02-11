import time
import random


def smart_bot():
    print("Smart Bot Activated")

    cycle = 1

    while True:
        print(f"\n--- Cycle {cycle} ---")
        print("Scanning environment...")

        # Simulated sensor readings
        wall_detected = random.choice([True, False])
        human_detected = random.choice([True, False])

        # Decision-making logic
        if human_detected:
            print("Human detected! Pausing...")
            time.sleep(3)
            print("Resuming movement...")

        elif wall_detected:
            direction = random.choice(["left", "right"])
            print(f"Wall detected! Turning {direction}...")
            time.sleep(1)

        else:
            print("Path clear. Moving forward...")
            time.sleep(1)

        # Stop loop randomly (for demo purpose)
        if random.randint(1, 10) == 5:
            print("\nStopping bot simulation.")
            break

        cycle += 1


# Run the bot
if __name__ == "__main__":
    smart_bot()

