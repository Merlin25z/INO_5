class Theater:
    def __init__(self, current_show):
        self.current_show = current_show

    def start_show(self):
        print(f"На театральной площадке начинается представление: {self.current_show}")