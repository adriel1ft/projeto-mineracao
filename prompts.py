instruction_prompt = """You are a data warehouse designer. I’m the
 end-user."""

format_prompt = """The input I give you and the output I expect
are DFM schemata in YAML formatted as follows: (1)
the fact is a “fact” tag including a “name” tag; (2) all
measures are listed inside a “measures” tag, each is an
empty item containing a “name” tag; (3) all many-to-
one associations between attributes in a hierarchy are
listed inside a “dependencies” tag: each is an empty
item containing a “from” tag, listing the finer attribute,
a “to” tag, listing the coarser attribute, and optionally
a “role” tag; (4) the “dependencies” list also includes an
item from the fact to each dimension, and one from the
fact to each measure; (5) all descriptive attributes, if
any, are listed under a “descriptive” tag; (6) all optional
attributes, if any, are listed under an “optional” tag.

"""

task_prompt = """ You receive in input a draft DFM
schema obtained by supply-driven design. A DFM 
schema is a connected graph where the fact is a node
in which no arcs enter. [...] Your task is to refine the
DFM schema given as input in different ways: (1) Make
names more intuitive for end-users. (2) Label measures
as either additive, semi-additive, or non-additive. If
you find a measure is non-additive, you should add
“(AVG)” to its name. If you find it is semi-additive, you
should add “(SUM-AVG)” to its name. If you find it
is semi-additive, just leave its name as it is. (3) Find
descriptive attributes. (3bis) Discretize attributes. (4)
Find optional attributes. (5) Complete time hierarchies. 
(6) Remove uninteresting attributes.
"""

procedure_prompt = """(2) Classify measures into additive, semi-additive, or non-additive. If you find a measure is non-additive, i.e., it can never be summed (e.g., the unit price of a product, a currency exchange, or a discount percentage), you should add “(AVG)” to its name.
If you find it is semi-additive, i.e., that it can be summed along all hierarchies except temporal ones (e.g., inventory level), you should add “(SUM-AVG)” to its name.
If you find it is additive, i.e., it can be summed along all hierarchies (e.g., the number of products sold in a day and the monthly revenue), just leave its name as it is.
Make sure you rename measures also under the “dependencies” tag.
"""

instance_prompt = """Here is a draft DFM schema: ⟨YAML code for draft
DFM schema⟩. First of all, make names more intuitive for
end-users. Return only the YAML without any further
information/explanation.
"""

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