from sys import stdout as console
class COM2:
    
    def __init__(self,driver):
        self.driver=driver

    def Element(self,Locatr):
        
        def findElement(findAll=False,returnItem=False):
            try:
                if findAll:
                    elems=self.driver.find_elements(*Locatr)
                else:
                    elem=self.driver.find_element(*Locatr)
                
                
                if findAll and returnItem ==False and elems:
                    return elems
                elif findAll and returnItem!=False and elems:
                    return elems[returnItem-1]
                else:
                    return elem

            except Exception as ex:
                console.write(str(ex))
                console.write("Element not found")
                raise Exception("Element Not found")
                return None
        return findElement

