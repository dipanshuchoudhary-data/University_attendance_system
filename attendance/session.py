from datetime import datetime

class Class_Session:
    def __init__(self,subject,start_time,end_time):
        """
        subject: str
        strat_time : str 'HH:MM
        end_time:str 'HH:MM
        """

        self.subject = subject
        self.start_time = start_time
        self.end_time = end_time
        self.date = datetime().strftime("%Y-%m-%d")


    def session_id(self):
        return f"{self.subject}_{self.date}_{self.start_time}-{self.end_time}"