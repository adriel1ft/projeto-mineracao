format_prompt_q2 = r"""The input I give you and the output I expect
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
attributes, if any, are listed under an “optional” tag


----
INPUT YAML FILE: {content}
MSG : {msg}

"""

format_prompt_q3 = r"""The input I give you and the output I expect
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
attributes, if any, are listed under an “optional” tag


----
INPUT YAML FILE: {content}
MSG : {msg}

"""

task_prompt_q2 = """ You receive in input a draft DFM
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

procedure_prompt_q3 = """(2) Classify measures into additive, semi-additive, or non-additive. If you find a measure is non-additive, i.e., it can never be summed (e.g., the unit price of a product, a currency exchange, or a discount percentage), you should add “(AVG)” to its name.
If you find it is semi-additive, i.e., that it can be summed along all hierarchies except temporal ones (e.g., inventory level), you should add “(SUM-AVG)” to its name.
If you find it is additive, i.e., it can be summed along all hierarchies (e.g., the number of products sold in a day and the monthly revenue), just leave its name as it is.
Make sure you rename measures also under the “dependencies” tag.
"""