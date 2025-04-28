class Base:
    def __getattr__(self, name):
        print(f"Base.__getattr__({name})")
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

class Derived(Base):
    @property
    def foo(self):
        print("Derived.foo property")
        return self.bar  # This will raise AttributeError

d = Derived()
try:
    print(d.foo)
except AttributeError as e:
    print(f"AttributeError: {e}")
