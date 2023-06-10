class Weapon:
    def __init__(self, name):
        self.name = name
        self.slots_to_attachments = {}

    def add_attachment_to_slot(self, attachment, slot):
        if slot not in self.slots_to_attachments:
            self.slots_to_attachments[slot] = []
        self.slots_to_attachments[slot].append(attachment)
