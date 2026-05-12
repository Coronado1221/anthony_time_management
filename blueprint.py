class ProductivityEntry:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        self.current = 0
        self.improved = 0

    def set_task(self, new_task):
        self.task = new_task

    def set_scores(self, current, improved):
        self.current = current
        self.improved = improved

    def get_summary(self):
        return f"User: {self.name}\nTask: {self.task}\nCurrent Productivity: {self.current}%\nImproved Productivity: {self.improved}%"