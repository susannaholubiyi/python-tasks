def menu():

	print("""1. Phone book\n2. Messages\n3. Chat\n4. Call Register\n5. Tones \n6. Settings\n7. Call Divert\n8. Games\n9. Calculator\n10. Reminders\n11. Clock\n12. Profiles\n13. SIM services\n""")
	


	
def phone_book():

	print("""\n          Phone book          \n1. Search\n2. Service\n3.Add Name\n4. Erase\n5. Edit
	\n6. Assign tone\n7. Send B' Card\n8. Options\n9. Speed Dials\n10. Voice Tags""")
	


def options():

	print("1. Type of view\n2. Memory status\n")
	phone_book_options = (input("Enter 1 or 2 to select options: "))

	match phone_book_options:
		case '1':
			print("\"Type of view\"")

		case '2':
			print("\"Memory status\"")


def back_button():

	back_to_menu = input("Enter 1 to go back to menu: ")
	while back_to_menu != '1':
		print("Enter 1!")
		back_to_menu = input("Enter 1 to go back to menu: ")

	else:
		menu()


def messages():

	print("""\n          Messages          |\n1.Write messages\n2. Inbox\n3. Outbox\n4. Picture messages
	\n5. Templates\n6. Smileys\n7. Message settings\n8. Info services\n9. Voice mailbox number\n. Service command editor""")
	

def Set1():
	
	print("""1. Message centre number\n2. Messages sent as\n3. Message validity""")
	browse_set1_option = input("Enter any number from 1-3 to browse through set1: ")

	match browse_set1_option:

		case '1':
			print("\"Message centre number\"")

		case '2':
			print("\"Messages sent as\"")

		case '3':
			print("\"Message validity\"")
			
		case _:
			print("Enter a valid number")
			
	back_button()
		

def Common():

	print("""1. Delivery reports\n2. Reply via same centre\n3. Character support""")
	
	browse_common = input("Enter any number from 1-3 to browse through common: ")
	
	match browse_common:
	
		case '1':
			print("\"Delivery reports\"")
			
		case '2':
			print("\"Reply via same centre\"")
			
		case '3':
			print("\"Character support\"")
			
		case _:
			print("Enter a valid number")
			
	back_button()

	

def message_settings():

	print("1. Set 1\n2. Common\n")
	browse_message_settings = input("Enter 1 or two to browse through message settings")
	
	if browse_message_settings == '1':
		Set1()
	
	else:
		Common()
		
		

def call_register():

	print("""1. Missed calls\n2. Received calls\n3. Dialled numbers\n4. Erase recent call lists\n5. Show call duration\n6. Show call costs\n7. Call cost settings\n8. Prepaid credit""")



def show_call_duration():

	print("1. Last call duration\n2. All calls' duration\n3. Received calls' duration\n4. Dialled calls' duration\n5. Clear timers")
	
	browse_call_duration = input("Enter any number from 1-5  to show call duration: ")

	if browse_call_duration == '1':
		print("\"Last call duration\"")
	
	elif browse_call_duration == '2':
		print("\"All calls' duration\"")
		
	elif browse_call_duration == '3':
		print ("\"Received calls' duration\"")

	elif browse_call_duration == '4':
		print ("\"Dialled calls' duration\"")
		
	elif browse_call_duration == '5':
		print ("\"Clear timers\"")
		
	else:
		print("Enter a valid number!")
		
	back_button()
	

def show_call_cost():

	print("1. Last call cost\n2. All calls' cost\n3. Clear counters")
	
	browse_call_cost = input("Enter any number from 1-5  to show call costs: ")

	match browse_call_cost:
	
		case '1':
			print("\"Last call cost\"")
			
		case '2':
			print("\"All calls' cost\"")
			
		case '3':
			print("\"Clear counters\"")
			
		case _:
			print("Enter a valid number!")
			
	back_button()
	
	
	
def call_cost_settings():

	print("1. Call cost limit\n2. Show costs in")	

	browse_cost_settings = input("Enter 1 or 2  to show call costs settings: ")
	
	match browse_cost_settings:
	
		case '1':
			print("\"Call cost limit\"")
			
		case '2':
			print("\"Show costs in\"")
			
		case _:
			print("Enter a valid number!")
			
	back_button()



def tones():
	print("""1. Ringing tone\n2. Ringing volume\n3. Incoming call alert\n4. Composer
	\n5. Message alert tone\n6. Keypad tones\n7. Warning and game tones\n8. Vibrating alert\n9. Screen saver""")
	
	
	
def settings():
	print("1. Call settings\n2. Phone settings\n3. Security settings\n4. Restore factory settings")
	
 
 
def call_settings():
 	print("""1. Automatic redial\n2. Speed dialling\n3. Call waiting options
 	\n4. Own number sending\n5. Phone line in use\n6. Automatic answer""")
 	
 	browse_call_settings = input("Enter any number from 1-5  to browse through call settings: ")
 	
 	match browse_call_settings:
 	
 		case '1':
 			print("\"Automatic redial\"")
 			
 		case '2':
 			print("\"Speed dialling\"")
 			
 		case '3':
 			print("\"Call waiting options\"")
 			
 		case '4':
 			print("\"Own number sending\"")
 			
 		case '5':
 			print("\"Automatic answer\"")
 			
 		case _:
 			print("Enter a valid number!")
 			
 	back_button()
 	
 
 	
def phone_settings():
 	print("""1. Language\n2. Cell info display\n3. Welcome note\n4. Network selection\n5. Lights\n6. Confirm SIM service actions""")
 	
 	browse_phone_settings = input("Enter any number from 1-6 to browse through phone settings: ")
 	
 	match browse_phone_settings:
 	
 		case '1':
 			print("\"Language\"")
 			
 		case '2':
 			print("\"Cell info display\"")
 			
 		case '3':
 			print("\"Welcome note\"")
 			
 		case '4':
 			print("\"Network selection\"")
 			
 		case '5':
 			print("\"Lights\"")
 			
 		case '6':
 			print("\"Confirm SIM service actions\"")
 			
 		case _:
 			print("Enter a valid number!")
 			
 	back_button()

 	
 	
def security_settings():


	print("""1. PIN code request\n2. Call barring service\n3. Fixed dialling\n4. Closed user group
 	\n5. Phone security\n6. Change access codes""")
	browse_security_settings = input("Enter any number from 1-6 to browse through security settings: ")
 	
	match browse_security_settings:
 	
 		case '1':
 			print("\"PIN code request\"")
 			
 		case '2':
 			print("\"Call barring service\"")
 			
 		case '3':
 			print("\"Fixed dialling\"")
 			
 		case '4':
 			print("\"Closed user group\"")
 			
 		case '5':
 			print("\"Phone security\"")
 			
 		case '6':
 			print("\"Change access codes\"")
 			
 		case _:
 			print("Enter a valid number!")
 			
	back_button()




print("Welcome to Nokia 3310 :) \n")

menu()	

browse = (input("\nEnter from 1-13 to browse through the menu: "))


match browse:

	case '1': 
	
		phone_book()
	  
	  
		browse_phone_book = input("Enter any number  from 1-10 to browse through phone book: ")
	  
		match browse_phone_book:

			case '1':
				print("\"Search\"")

			case '2':
				print("\"Service Nos\"")

			case '3':
				print("\"Add name\"")

			case '4':
				print("\"Erase\"")

			case '5':
				print("\"Edit\"")

			case '6':
				print("\"Assign tone\"")

			case '7':
				print("\"Send B' Card\"")


			case '8':
				options()

			case '9':
				print("\"Speed dials\"")

			case '10':
				print("\"Voice tags\"")

			case _ :
				print("Enter a valid number!")


		phonebook_back_to_menu()

	

	case '2':
		
		messages()

		browse_messages = input("Enter any number  from 1-10 to browse through phone book: ")

		match browse_messages:

			case '1':
				print("\"Write messages\"")

			case '2':
				print("\"Inbox\"")

			case '3': 
				print("\"Outbox\"")

			case '4':
				print("\"Picture messages\"")

			case '5':
				print("\"Templates\"")

			case '6':
				print("\"Smileys\"")

			case '7':
				message_settings()
				
			case '8':
				print("\"Info service\"")
				
			case '9':
				print("\"Voice mailbox number\"")
				
			case '10':
				print("\"Service command editor\"")
				
			case _:
				print("Enter a valid number!")
				
				
	case '3':
		print("\"Chats\"")
		
	
	case '4':
		call_register()
		
		browse_call_register = input("Enter any number  from 1-8 to browse through call register: ")
		
		match browse_call_register:
		
			case '1':
				print("\"Missed call\"")
				
			case '2':
				print("\"Received calls\"")
				
			case '3':
				print("\"Dialled numbers\"")
				
			case '4':
				print("\"Erase recent call lists\"")
				
			case '5':
				show_call_duration()
				
			case '6':
				show_call_cost()
				
			case '7':
				call_cost_settings()
				
			case '8':
				print("\"Prepaid credit\"")
				
			case _:
				print("Enter a valid number!")
				
				
	case '5':
		
		tones()
		
		browse_tones = input("Enter any number from 1-8 to browse though tones: ")
		
		match browse_tones:
		
			case '1':
				print("\"Ringing tone\"")
				
			case '2':
				print("\"Ringing volume\"")
				
			case '3':
				print("\"Incoming call alert\"")
				
			case '4':
				print("\"Composer\"")
				
			case '5':
				print("\"Message alert tone\"")
				
			case '6':
				print("\"Keypad tones\"")
				
			case '7':
				print("\"Warning and game tones\"")
				
			case '8':
				print("\"Vibrating alert\"")
				
			case '9':
				print("\"Screen saver\"")
				
			case _:
				print("Enter a valid number!")
				
				
	case '6':
		
		settings()
		
		browse_settings = input("Enter any number from 1-4 to browse though settings: ")
		
		match browse_settings:
		
			case '1':
				call_settings()
				
			case '2':
				phone_settins()
				
			case '3':
				security_settings()
				
			case '4':
				print("\"Restore factory settings\"")
			
				back_button()
			case _:
				print("Enter a valid number!")
				
				settings()
				
		
				
				
	case '7':
		print("\"Call divert\"")
		back_button()
		
	case '8':
		print("\"Games\"")
		back_button()
		
	case '9':
		print("\"Calculator\"")
		back_button()
		
	case '10':
		print("\"Reminders\"")
		back_button()
		
	case '11':
		print("""1. Alarm clock\n2. Clock settings\n3. Date setting\n4. Stopwatch\n5. Countdown timer\n6. Auto update of date and time""")
		
		browse_clock = input("Enter a number from 1-6 to browse through clock: ")
		if browse_clock == '1':
		
			print("\"Alarm clock\"")
			
		elif browse_clock == '2':
		
			print("\"Clock settings\"")
			
		elif browse_clock == '3':
		
			print("\"Date setting\"")
				
		elif browse_clock == '4':
		
			print("\"Stopwatch\"")
			
		elif browse_clock == '5':
		
			print("\"Countdown timer\"")
			
		elif browse_clock =='6':
		
			print("Auto update of date and time\"")
			
		else:
			print("Enter a valid number: ")
			
		back_button()
		
	
	case '12':
		print("\"Profiles\"")
		back_button()
		
	case '13':
		print("\"SIM services\"")
	
		back_button()
			
	
				
	

		
		
				

		
	  	 
                  
                  

             
           
