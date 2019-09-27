# Class to declare the response of interactions between peers
class response:
    data = ''
    message_type = ''  # 1. Register 2. Leave 3. PQuery 4. KeepAlive 5. RFCQuery 6. GetRFC
    status_code = ''  # 1. OK 2. Error
    final_data = ''  # the data that need to be returned
    hostname = ''  # hostname or IP address of the destination peer
    header_tag = ''
    header_value = ''

    def message_attributes(self, value):  # function to define individual attributes from the data received
        self.data = value
        actual_message = value.split("###")
        self.message_type = actual_message.pop(0)
        self.status_code = actual_message.pop(0)
        self.hostname = actual_message.pop(0)
        self.header_tag += actual_message.pop(0)
        self.header_value += actual_message.pop(0)
        value.remove('')
        self.final_data = actual_message.pop(0)

    def return_message(self):  # function to put all the attributes in one string
        self.data = self.message_type + ': ' + self.status_code + ': ' + self.hostname + ': ' + self.header_value + ': ' + self.header_tag + ': ' + self.final_data
