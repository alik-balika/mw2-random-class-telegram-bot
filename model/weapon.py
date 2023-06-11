class Weapon:
    def __init__(self, name):
        self.name = name
        self.attachments = {}

    def add_attachment_to_slot(self, attachment, slot):
        if slot not in self.attachments:
            self.attachments[slot] = []
        self.attachments[slot].append(attachment)

    def get_attachments_copy(self):
        return self.attachments.copy()
