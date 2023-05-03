import data_load

class Pizza:

    def __init__(self):
        self.ordered_items = []
        self.price = 0
        self.pizza_menu = data_load.DataPreprocessing().pizza_menu()
        print(self.pizza_menu)
        self.n = list(map(int,input("Please Enter your choice from above Menu ").split()))
        self.row = [list(data_load.DataPreprocessing().pizza_details(i)) for i in self.n] # (1,2,3,4,......)
        self.order_list = ""
        for i in range(len(self.row)):
            self.order_list += self.row[i][0] + ", "
        print("you have selected these pizza's ",self.order_list)
        try:
            for pz in range(len(self.row)):
                self.pizza_size = int(input(f"please Select size for {self.row[pz][0]}\nPress 1 for Regular {self.row[pz][1]}\nPress 2 for Medium {self.row[pz][2]}\nPress 3 for Large {self.row[pz][3]}\n"))
                if self.pizza_size == 1:
                    self.price = self.row[pz][1]
                if self.pizza_size == 2:
                    self.price= self.row[pz][2]
                if self.pizza_size == 3:
                    self.price = self.row[pz][3]
                self.ordered_items.append(self.price)
        except ValueError:
            print("Please Enter valid input")

    def return_pizza_total(self):
        return self.ordered_items



