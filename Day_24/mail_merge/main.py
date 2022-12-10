class Mail_Merge:
    def __init__(self):
        with open("Python/100-Days-of-Code/Day_24/mail_merge/Input/Letters/starting_letter.txt", mode="r") as content:
            self.content = content.read()
            
    def create_new_doc(self, name):
        with open(f"Python/100-Days-of-Code/Day_24/mail_merge/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as doc:
            new_content = self.content.replace("[name]", name)
            doc.write(new_content)
            
    def next_name(self):
        with open("Python/100-Days-of-Code/Day_24/mail_merge/Input/Names/invited_names.txt", mode="r") as names:
            for name in names.readlines():
                self.create_new_doc(name.replace("\n", ""))
            
main = Mail_Merge()
main.next_name()
