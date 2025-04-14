prompt_artigo = """The input I give you and the output I expect
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