#E-9.4: Inheritance

#Problem: The last exercise in chapter 10,
#and at the same time the course tries out inheritance.
#In this exercise, your task is to define a new class which will be inherited from the class Customer defined in the chapter's theory part.

            #class Customer:
                #name = "John Johnsson"
                #total = 1000
                #paymenttype = "Masterexpress"
                #number = "1234-5678-9012345"

                #def printout(self):
                    #print("Name: ", self.name)
                    #print("Total: ", self.total)
                    #print("Payment type: ", self.paymenttype)
                    #print("Card/Bill number: ", self.number)

#Define a new class called ManageCustomer which has the following abilities:
   #1) A method "addbill", which increases the attribute total by 50, and
   #2) a method "payment" which decreases the attribute total by 100.

#Remember that you only need to write the new inheriting class ManageCustomer.
#The system will test the class,
#but in the submitted answer only the class definition is needed.
#If the class is defined correctly, the program will print the following:

                    #>>>
                    #Name:  Homer Griffin
                    #Total:  850
                    #Payment type:  Masterexpress
                    #Card/Bill number:  1234-5678-9012345
                    #>>>

#Solution:

class Customer:
    name = "John Johnsson"
    total = 1000
    paymenttype = "Masterexpress"
    number = "1234-5678-9012345"


    def printout(self):
        print("Name: ", self.name)
        print("Total: ", self.total)
        print("Payment type: ", self.paymenttype)
        print("Card/Bill number: ", self.number)


class ManageCustomer(Customer):
    def addbill(self):
        self.total += 50

    def payment(self):
        self.total -= 100


def main():
    person = ManageCustomer()
    person.name = "Homer Griffin"
    person.addbill()
    person.payment()
    person.payment()
    person.printout()


if __name__ == '__main__':
    main()



