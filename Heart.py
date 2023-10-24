class Heart:
    def __init__(self):
        self.usage = None
        self.state = None

    def check_heart_state(self, load_percentage):
        if load_percentage > 70:
            self.state = "high blood pressure"
        else:
            self.state = "feeling good"


class Brain:
    def __init__(self):
        self.usage = None
        self.state = None

    def check_brain_state(self, workload_percentage):
        if workload_percentage > 90:
            self.state = "tired"
        else:
            self.state = "rested"


class Leg:
    def __init__(self, moving_speed):
        self.moving_speed = moving_speed
        self.state = None

    def check_leg_state(self):
        if self.moving_speed > 10:
            self.state = "running"
        elif self.moving_speed > 0:
            self.state = "walking"
        else:
            self.state = "standing"


class Person:
    def __init__(self):
        self.heart = Heart()
        self.brain = Brain()

    def check_health(self, heart_load_percentage, brain_workload_percentage, leg_moving_speed):
        self.heart.check_heart_state(heart_load_percentage)
        self.brain.check_brain_state(brain_workload_percentage)
        leg = Leg(leg_moving_speed)
        leg.check_leg_state()
        return leg.state



person = Person()
heart_load = 75 
brain_workload = 85 
leg_speed = 12  

leg_state = person.check_health(heart_load, brain_workload, leg_speed)
print(f"Heart state: {person.heart.state}")
print(f"Brain state: {person.brain.state}")
print(f"Leg state: {leg_state}")
