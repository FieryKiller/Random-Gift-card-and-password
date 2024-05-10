# Random-Gift-card-and-password
import random

# Possible characters for the gift card code
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


# Function to generate a fake gift card code
def generate_gift_card_code():
  code = ''
  for i in range(16):
    code += random.choice(characters)
  return code


# Function to generate a 4-digit password
def generate_password():
  password = ''
  for i in range(4):
    password += str(random.randint(0, 9))
  return password


# Generate a gift card code
gift_card_code = generate_gift_card_code()

# Generate a 4-digit password
password = generate_password()

# Print the generated gift card code and password
print('Generated Gift Card Code:', gift_card_code)
print('Generated 4-Digit Password:', password)
