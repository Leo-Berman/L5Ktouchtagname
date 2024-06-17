import re

class L5KProgram:

    def __init__(self, target_tags:list, input_aliases:list, input_ofs:list):

        # Create lists to store tags in the program and tags of interest
        self.program_tags = []
        self.tags_of_interest = []

        # Calculate tags_of_interest
        self.calculate_tags_of_interest(target_tags, input_aliases, input_ofs)
        
    def calculate_tags_in_program(self, input_aliases:list, input_ofs:list):

        # Repeat until list is empty
        while len(input_ofs) > 0:

            # Store both the alias and tag literal in A SET
            tag_group = {input_aliases.pop(0),input_ofs.pop(0)}

            # Iterate though the whole list
            i = 0
            while i < len(input_ofs):

                # If either the tag literal and alias matches the
                # tag_group
                if input_ofs[i] in tag_group or input_aliases[i] in tag_group:

                    # Add them to the tag_group
                    tag_group.add(input_ofs.pop(i))
                    tag_group.add(input_aliases.pop(i))
                    
                else:
                    i+=1
                    
            # Add the grouped tags to the program tags
            self.program_tags.append(tag_group)

    def calculate_tags_of_interest(self, target_tags:list, input_aliases:list,
                                   input_ofs:list):

        self.calculate_tags_in_program(input_aliases,input_ofs)

        # Iterate through program tag groups
        for x in self.program_tags:

            # Iterate through each tag groups tags
            for y in x:

                # If any of the tags in the group are in the target_tags
                if y in target_tags:

                    # Add the whole group to the tags of interest
                    self.tags_of_interest.extend(x)
                    break

        # Add target controller tags to tags of interest
        self.tags_of_interest.extend(target_tags)

        # Remove duplicates
        self.tags_of_interest = list(set(self.tags_of_interest))
                    
    def add_touch_tag(self,input_line,touch_tag):

        # Find all of the logical components
        logic_list = re.findall(r"\(\S+?\)",input_line)

        # Iterate through all the logical components
        for logic in logic_list:

            # Remove the parenthesis and split into parameters
            logic_parameters = logic[1:len(logic)-1].split(",")

            
            for parameter in logic_parameters:

                # Split parameter into components
                sub_parameters = parameter.split(".")

                # Iterate through the components
                for component in sub_parameters:

                    # If the component is a tag of interest and the
                    # touch tag isn't already there, add one
                    if (component in self.tags_of_interest and not
                        input_line.__contains__( " [XIC(" + touch_tag+"),]")):

                        # Find the beginning of the logical rung
                        edit_index = input_line.index(":")

                        # return the line with the added tag
                        return (input_line[0:edit_index + 1]
                                + " [XIC("+touch_tag+"),]"
                                + input_line[edit_index + 1 :])
                    
        # return the original line if nothing changed
        return input_line

