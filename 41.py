import pandas as pd
from matplotlib.style.core import available

df=pd.read_csv("hotels.csv",dtype=str)
df_cards=pd.read_csv("cards.csv",dtype=str).to_dict(orient='records')
df_security_cards=pd.read_csv("card_security.csv",dtype=str)

class Hotel:
    def __init__(self,id):
        self.hotel_id=id
        self.name=df.loc[df["id"]==self.hotel_id,"name"]
    def book(self):
        availability=df.loc[df["id"]==self.hotel_id,"available"]="no"
        df.to_csv("hotel_csv",index=False)


    def available(self):
        availability=df.loc[df["id"]==self.hotel_id,"available"].squeeze()
        if availability=="yes":
            return True
        else:
            return False
        pass

class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name=customer_name
        self.hotel=hotel_object


    def generate(self):
        content=f""" 
        Thank you for reservation 
        here are you booking data:
        name:{self.customer_name}
        hotel name:{self.hotel.name}"""
        return content


class CreditCard:

    def __init__(self,number):
        self.number=number

    def validate(self,expiration,cvc,holder):
        cards_data={"number":self.number,"expiration":expiration,"holder":holder,"cvc":cvc}
        if cards_data in df_cards:
            return True
        else:
            return False

class SecureCards(CreditCard):
    def authenticate(self,given_password):
        passwords=df_security_cards.loc[df_security_cards["number"]==self.number,"password"].squeeze()
        if passwords== given_password:
            return True


print(df )
hotels_id=input("enter your input")
hotel=Hotel(hotels_id)
if hotel.available():
    credits_card=SecureCards(number="1234")
    if credits_card.validate(expiration="12/26",cvc="123",holder="JOHN SMITH"):
        if credits_card.authenticate("mypass"):
            hotel.book()
            name=input("enter your name")
            reservation_ticket=ReservationTicket(name,hotel)
            print(reservation_ticket.generate())
        else:
            print("credit card authentication is failed ")
    else:
        print("there is problem on credit cards")

else:
    print("hotel ticket is not free")