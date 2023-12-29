# return unformatted string instead of raising error
# when key is missing within dictionary
# https://stackoverflow.com/a/17215533/3127170
class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}' 

def send(recipient, message):

    print(f"Sending mail to {recipient['email']}")
    text = message["content"]
    
    message = text.format_map(SafeDict(recipient))
    print(message)
