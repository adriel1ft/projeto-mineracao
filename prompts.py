RQ1_prompt_1 = """ Which are the features of the Dimensional Fact Model (DFM)? """

RQ1_prompt_2 = """How would you design a multidimensional schema using the DFM?"""

RQ1_prompt_3 = """How would you refine a draft DFM schema obtained by supply-driven design from a source database?"""

RQ2_prompt_1 = """ Make names more intuitive for end-users """

RQ2_prompt_2 = """ Label measure as either additive, semi-additive, ornon
additive. """

RQ2_prompt_3 = """ Either find descriptive attributes or discretize them. """

RQ2_prompt_4 = """ Not all regions have a state. """

RQ2_prompt_5 = """  Complete time hierarchies. """

RQ2_prompt_6 = """  StoreId is not interesting to me """

RQ3_prompt_1 = """ (6) Remove uninteresting attributes. The rule to safely remove
 an attribute “b”, whose father is attribute “a”, is to make all the children
 attributes of “b” children of “a”. Make sure to add the arcs from “a” to all
 the children of “b” underthe“dependencies”tag(evenif “a” is the fact). If
 among the children of the attribute “b” you remove there are descriptive
 attributes, these should be removed as well both under the “descriptive”
 and the “dependencies” tags (do not remove ALL descriptive attributes,
 only the children of “b”). I may ask for removing an attribute by saying
 that I’m not interested in it. """

RQ3_prompt_2 = """ Merge “drop-off date” and “pick-up date” into a single “date”
 node."""

RQ3_prompt_3 = """ Some arcs are missing, please try again. """