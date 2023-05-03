from Pizza_shop import Pizza
import re

class OrderDetails:
    def __init__(self):
        self.central_good_service_charge = 0.0
        self.state_good_service_charge = 0.0
        self.final_total = 0
        self.obj = Pizza()
        self.total = self.obj.return_pizza_total()
        for i in self.total:
            self.temp = re.findall(r'\d+',i)
            self.res = sum(list(map(int, self.temp)))
            self.final_total += self.res

    def apply_gst(self):
        self.central_good_service_charge = float((self.final_total*9)/100)
        self.state_good_service_charge = self.central_good_service_charge
        return self.central_good_service_charge,self.state_good_service_charge,self.final_total



