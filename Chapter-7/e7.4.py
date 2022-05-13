#E-7.4: Your own module with several parameters

#Problem: The fourth exercise in this module elaborates on the idea applied in the last exercise.
#In the exercise the idea is once again to create a module for an existing main program.
#The module tests the feasibility of different user-given inputs for a password.
#The existing code which uses the module is as follows:

                            #import inspector
                            #while True:
                                #userinput = input("Give a string for testing: ")
                                #tulos = inspector.testme(userinput)
                                #if tulos == True:
                                    #print("This string fits for a password!")
                                    #break
                                #else:
                                    #print("The module says no.")

#The idea is to create the module inspector and the function testme which receives the user-given candidate for a password.
#If the given input is shorter than 6 characters,
#contains only letters or only numbers,
#the module should reject the candidate and return False.
#If the input is longer than 6 characters and has both numbers and letters,
#it should be accepted.In this case the module should return True.
#When the program works correctly, it prints the following:

                            #>>>
                            #Give a string for testing: Test
                            #The module says no.
                            #Give a string for testing: 234234
                            #The module says no.
                            #Give a string for testing: Youhavetobekiddingme1234
                            #This string fits for a password!
                            #>>>

#Solution:

