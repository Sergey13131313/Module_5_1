def testFunction():
    def innerFunction():
        print('Я в области видимости функции testFunction')

    innerFunction()


testFunction()

innerFunction()