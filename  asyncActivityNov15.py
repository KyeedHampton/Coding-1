
name = "Man"
passcode = "12345"

input_name = "Man"
input_passcode = "12345"


is_authorized = name == input_name and passcode == input_passcode
print("Is the person authorized?", is_authorized)


required_ecgs = 10
received_ecgs = 4

required_oxygen = 6
received_oxygen = 9


ecg_status = "Request more ECG machines" if received_ecgs < required_ecgs else "Send back overflow"
oxygen_status = "Request more oxygen tanks" if received_oxygen < required_oxygen else "Send back overflow"

print("ECG Machine Status:", ecg_status) 
print("Oxygen Tank Status:", oxygen_status) 


user_message = "Hello, how are you?"
recipient_message = user_message 
print("Message sent to recipient:", recipient_message) 


name = "kyeed"
age = "17"
print("My name is " + name + ". I am " + age + " years old.")