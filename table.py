import conversion

# Conversion table that is dependent on wildcard characters
# Format: (String to replace, function used to replace)
patternSwapTable = [
(r"double integral of [^\$]+ from [^\$]+ to [^\$]+ and [^\$]+ to [^\$]+",conversion.toDoubleIntegral),
(r"triple integral of [^\$]+ from [^\$]+ to [^\$]+ and [^\$]+ to [^\$]+ and [^\$]+ to [^\$]+",conversion.toTripleIntegral),
(r"integral of [^\$]+ from [^\$]+ to [^\$]+",conversion.toIntegral),
(r"summation of [^\$]+ from [^\$]+ to [^\$]+",conversion.toSummation)
]

# Conversion table that is not dependent on wildcard characters 
# Format: (String to replace, what to replace with)
swapTable = [
# Lower Greek
("infinity","\\infty"),
("alpha","\\alpha"),
("beta","\\beta"),
("epsilon","\\epsilon"),
("theta","\\theta"),
("lambda","\\lambda"),
("pi","\\pi"),
("sigma","\\sigma"),
("phi","\\phi"),
("omega","\\omega"),
("gamma","\gamma"),
("zeta","\\zeta"),
("eta","\\eta"),
("iota","\\iota"),
("nu","\\nu"),
("rho","\\rho"),
("tau","\\tau"),
("chi","\\chi"),
("delta","\\delta"),
("kappa","\\kappa"),
("xi","\\xi"),
("upsilon","\\upsilon"),
("psi","\\psi"),
("mu","\\mu"),

# Upper Greek
("Gamma","\Gamma"),
("Delta","\\Delta"),
("Theta","\\Theta"),
("Lambda","\\Lambda"),
("Xi","\\Xi"),
("Pi","\\Pi"),
("Sigma","\\Sigma"),
("Upsilon","\\Upsilon"),
("Phi","\\Phi"),
("Psi","\\Psi"),
("Omega","\\Omega")
]