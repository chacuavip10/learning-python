# type
# String, single/double quote
print("======================Some string function=======================")
name = "Nguyen huu viet dung"
print("Original: " + name)
print(f"name.title:", name.title())
print(f"name.upper:", name.upper())
print(f"name.lower:", name.lower())

print("===========Single and double quote==========")
print("\t\tAlbert Einstein once said, \"A person who never made a \n\t\tmistake never tried anything new\".")
# Combining or Concatenating Strings
print("==============Combining or COncatenating Strings===================")
first_name = "Nguyen Huu"
last_name = "Viet Dung"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
# tab and new line (\t & \n)
print("=================Tab & new line====================")
print("Python")
print("\tPython")
print("Python1\nPython2")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# Striping whitespace
# for compare 2 strings, ...
# rstrip() == right strip, lstrip() == left strip, strip() == strip both end
print("=================Strip====================")
extra_wp = " python "
print(extra_wp.rstrip())
print(extra_wp.lstrip())
print(extra_wp.strip())


print('===========Exercise=========')
# Print simple message with name is a variable "Hello Eric, would you like to learn something today?"
name = "Eric"
print(f"Hello {name}, would you like to learn something today?")
# Print famous quote
print("\t\tAlbert Einstein once said, \"A person who never made a \n\t\tmistake never tried anything new\".")
# print famous quote, with name is a variable, message is a variable
name3 = "Albert Einstein"
message = "\t\t" + name3 + \
    " once said, \"A person who never made a \n\t\tmistake never tried anything new\"."
print(message)
# Strip name
name4 = "\tViet Dung\t\t\nNguyen Huu\t\t"
print(name4.strip())
