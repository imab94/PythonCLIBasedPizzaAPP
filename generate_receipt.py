from totalorder import OrderDetails

class Receipt:
    def __init__(self):
        self.receipt = OrderDetails()
        self.central_gst,self.state_gst,self.total = self.receipt.apply_gst()
        print("**********************************************************")
        print("subTot  ",self.total)
        print("CGST @ 9% ",self.central_gst)
        print("SGST/UTGST @ 9% ",self.state_gst)
        print("---"*6)
        print("Total Rs  ",(self.state_gst+self.central_gst+self.total))
        print("Rounding off in Rs ",round((self.state_gst+self.central_gst+self.total)))


rc = Receipt()
