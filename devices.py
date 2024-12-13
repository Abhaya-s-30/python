class laptop:
    def specs(self):
        return "laptop:16gb ram,512gb std"
    def __str__(self):
        pass
class mobile:
    def specs(self):
        return "mobile:6gb ram,128gb storage"
    def __str__(self):
        pass
def describe(device):
    print(device.specs())
devices=[laptop(),mobile()]
for device in devices:
    describe(device)