import sys
import datetime
from storage import append_csv_row


MORNING_FILE: str = "data/morning.csv"
MORNING_HEADERS: list[str] = (
    ["date", "sleep_hours", "wake_time", "morning_state"]
)


def log_morning() -> None:
    today_is: str = datetime.date.today().isoformat()
    sleep_hours: float = float(input('Sleep hours: '))
    wakeup_time: str = input('Wake up time: ').strip()
    morning_state: int = int(input('Morning state: '))
    if morning_state < 1 or morning_state > 10:
        print('Invalid morning state input!')
        return
    row: list[str | float | int] = (
        [today_is, sleep_hours, wakeup_time, morning_state]
    )
    append_csv_row(MORNING_FILE, MORNING_HEADERS, row)
    print(f'{today_is} - saved')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python main.py morning')
    elif sys.argv[1] == "morning":
        log_morning()
    else:
        print(f"Unknown command: {sys.argv[1]}")
