import re

class program:

   
    def __init__(self):
        self.TAGS_IN_PROGRAM = []
        self.TAGS_OF_INTEREST = []
    def calculate_tags_in_program(self,aliases:list,ofs:list):
        
        while len(ofs) > 0:
            base = {aliases.pop(0),ofs.pop(0)}
            i = 0
            while i < len(ofs):
                if ofs[i] in base:
                    base.add(ofs.pop(i))
                    base.add(aliases.pop(i))
                else:
                    i+=1
            self.TAGS_IN_PROGRAM.append(base)

    def calculate_tags_of_interest(self,TARGET_TAGS):
        for x in self.TAGS_IN_PROGRAM:
            for y in x:
                if y in TARGET_TAGS:
                    self.TAGS_OF_INTEREST.extend(x)
                    break
        self.TAGS_OF_INTEREST.extend(TARGET_TAGS)
        self.TAGS_OF_INTEREST = list(set(self.TAGS_OF_INTEREST))
                    
    def update_line(self,inline,addtouchtag):
        refs = re.findall(r"\(\S+?\)",inline)
        for x in refs:
            tmp = x[1:len(x)-1]
            items = tmp.split(",")
            for y in items:
                sub_items = y.split(".")
                for z in sub_items:
                    if z in self.TAGS_OF_INTEREST:
                        edit_index = inline.index(":")
                        return inline[0:edit_index+1] + " [XIC("+addtouchtag+",]" + inline[edit_index+1:]
def test_main():
    test_program = program()
    test_aliases = ['1','2','3','4','6']
    test_ofs = ['c','1','d','f','3']

    test_program.calculate_tags_in_program(test_aliases,test_ofs)
    test_program.calculate_tags_of_interest(['c'])
    
if __name__ == "__main__":
    test_main()
