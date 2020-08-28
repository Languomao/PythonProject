class SecretTest:
    publicCount = 1
    __secretCount = 2

    def count(self):
        self.publicCount += 1
        self.__secretCount += 5

    def __prifun(self):
        self.__secretCount = 100


st = SecretTest()
st.count()
st.count()
print(st.publicCount)

st._SecretTest__prifun()

print(st._SecretTest__secretCount)
