# Function to get the date of an event
def get_event_date(event):
    return event.date

# Function to process events and determine current users on each machine
def current_users(events):
    # Sort events by date
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        # Initialize a set for each machine if not already present
        if event.machine not in machines:
            machines[event.machine] = set()
        # Add user to the machine's set if it's a login event
        if event.type == "login":
            machines[event.machine].add(event.user)
        # Remove user from the machine's set if it's a logout event
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

# Get the current users on each machine
users = current_users(events)
print(users)

# Generate the report
generate_report(users)
