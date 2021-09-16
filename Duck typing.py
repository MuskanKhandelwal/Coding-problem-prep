class jiocaller:
    def call(self):
        print("Calling")
class truecaller:
    def call(self):
        print("Ringing")
        print("Caller data")
class phone:
    def callFunc(self,PhoneApp):
        PhoneApp.call()

#PhoneApp=truecaller()
PhoneApp=jiocaller()
p1=phone()
p1.callFunc(PhoneApp)

## So it doesn't matter which app we are using since both of them have the call method(behaviour same)
# This is called as Duck typing. We care about behaviour and not the type 