class NewAutoSegRep:
    def __init__(self, inputString):
        self.inputString = inputString
        self.modString = []
        self.positions = set()
        self.orderEdges = set()
        self.assocEdges = set()
        self.toneLine = ""
        self.assocLine = ""
        self.syllableLine = ""
        self.labels = {}
        
        lastTone = ""
        
        stringLength = len(inputString)
                
        
        i = 0 # position in original string
        p = 0 # position in position set
        
        while i < stringLength:         # Syllable line: Positions, labels, and order edges
            #self.syllableLine = self.syllableLine + "σ"
            if ((inputString[i] == "!") or (inputString[i] == "+") or (inputString[i] == "-")):
                i+= 1
                continue
            
            self.positions.add(p)
            self.labels[p] = "σ"
            
            if i != 0:
                self.orderEdges.add((p-1, p))
                
            i+=1
            p+=1
    
        i = 0
        h = 0 #h will hold the position of the last unique tone so future syllables can map back to it.
        
        while i < stringLength:         # Tone line: Positions, labels, order edges. Also association edges

            if ((inputString[i] == "!") or (inputString[i] == "+") or (inputString[i] == "0") or (inputString[i] == "-")):
                if ((inputString[i] == "+") or (inputString[i] == "0") or (inputString[i] == "-")):
                    if  (inputString[i] == "0"):
                        self.syllableLine = self.syllableLine + "σ"
                    else:
                        self.syllableLine = self.syllableLine + inputString[i]

                    self.toneLine = self.toneLine + " "
                    self.assocLine = self.assocLine + " "
                    if inputString[i] != ("-"):
                        lastTone = ""
                    i += 1
                    continue
                else:
                    lastTone = ""
                i += 1
                continue
            
            if inputString[i] == "R":
                tone1 = "L"
                tone2 = "H"             
            elif inputString[i] == "F":
                tone1 = "H"
                tone2 = "L"
            else:
                tone1 = ""


            if (inputString[i] == lastTone) or ((tone1 == lastTone) and (tone1 != "")): #If tone is same as last
                self.assocEdges.add((h, i))
                #self.labels[p] = "σ "
                #self.orderEdges.add((p-1,p))
                self.assocLine = self.assocLine + "\\" 
                
                if ((tone1 == lastTone) and (tone1 != "")): #(Rising and falling tones), need extra space in lines
                    self.positions.add(p)
                    self.assocEdges.add((p,i))
                    self.labels[p] = tone2
                    self.orderEdges.add((p-1,p))
                    self.toneLine = self.toneLine + " " + tone2
                    self.assocLine = self.assocLine + "|"
                    self.syllableLine = self.syllableLine + " "
                    lastTone = tone2
                    h = p
                    p += 1
                    
                else:
                    self.toneLine = self.toneLine + " "
                
                self.syllableLine = self.syllableLine + "σ"
            else: # If tone is not same as last
                self.positions.add(p)
                self.assocEdges.add((p, i))
                
                self.assocLine = self.assocLine + "|"
                self.syllableLine = self.syllableLine + "σ"
                
                if i != 0: #Connecting to previous tones
                    self.orderEdges.add((h,p))
                    
                if (tone1 != ""): #For rising and falling tones
                    self.positions.add(p+1)
                    self.assocEdges.add((p+1, i))
                    self.labels[p] = tone1
                    self.labels[p+1] = tone2
                    self.orderEdges.add((p,p+1))
                    
                    self.toneLine = self.toneLine + tone1 + tone2
                    self.assocLine = self.assocLine + "/"
                    self.syllableLine = self.syllableLine + " "
                    lastTone = tone2
                    h = p+1
                    p += 1
                else:
                    self.labels[p] = inputString[i]
                    self.toneLine = self.toneLine + inputString[i]
                    lastTone = self.inputString[i]
                    h = p
                p += 1
            i += 1
            
        
    def __str__(self):
        return self.inputString
                                        
    def printDiag(self):
        print(self.toneLine +"\n" + self.assocLine + "\n" + self.syllableLine)

def concat(a1, a2):
        return  NewAutoSegRep(a1.inputString + a2.inputString)
