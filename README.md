The purpose of this tool is to be able to generate a list of controller tags that you would like to be able to easily cross-reference. Then, the program will generate a parallel branch consisting of an XIC(Touch Tag) on each rung that references any of the tags in the list (This includes nth degree aliases). Now if you import the original L5K file in Studio 5000 and cross-reference the Touch Tag, you can see every instance where the list of tags you generated is mentioned.

An example use case:
    You have two mixers, Mixer A and Mixer B. You currently have all the code set up for Mixer A and you want to duplicate it because Mixer B is almost an exact copy of Mixer A. You take all the unique controller tags associated with Mixer A and add it to your "Tags of Interest". Now since you can easily cross-reference to see anywhere these unique controller tags are used, you can add in the appropriate logic for Mixer B using the appropriate tags. Furthermore, you can then change the name of the tag to reflect that you have reviewed and made the change.
   
Prompted Parameters:

	"Tags of Interest" - TXT file with format:
	    Controller Tag 1
	    Controller Tag 2
	    Controller Tag ...
	    Controller Tag N

	"Touch Tag" - Name of tag you will be cross-referencing:
	    String consisting of Alpha-Numeric Characters and Underscore Characters

	L5K file:
	    Exported state program of Studio 5000 L5K program

This script was written using PEP 8 standards - https://peps.python.org/pep-0008/