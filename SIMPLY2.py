# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:50:42 2021

@author: k
"""
A='''James C. Maxwell Biography
(1831–1879)

James C. Maxwell was a 19th-century pioneer in chemistry and physics who articulated the idea of electromagnetism.
Who Was James C. Maxwell?
James C. Maxwell studied at the University of Cambridge before holding a variety of professorship posts. Already known for his innovations in optics and gas velocity research, his groundbreaking theories around electromagnetism, articulated in the famed Maxwell's Equations, greatly influenced modern physics as we know it.
Academic Background
James Clerk Maxwell was born on June 13, 1831, in Edinburgh, Scotland. Having a keen intellect from childhood, he had one of his geometry papers presented at the Royal Society of Edinburgh during his adolescence. By 16 he'd enrolled at the University of Edinburgh, pursuing a fervent interest in optics and color research. He studied there for three years and eventually attended Cambridge University's Trinity College, graduating in 1854.
After teaching at Trinity for a time, Maxwell moved on to Marischal College as part of the physics faculty. He wed Katherine Mary Dewar in 1858.
Saturn's Rings
While at Marischal, Maxwell pondered a major astronomical question, looking at the case of Saturn and coming up with the idea that the planet's rings are comprised of particles, a theory later confirmed via 20th-century space probes. For this, Maxwell received the Adam Prize.
Upon Marischal becoming part of the University of Aberdeen, Maxwell took on a professor position at King's College in London. He taught there until 1865 when he resigned from his post to do research from his home in Glenlair. Having continued to do work with Cambridge University as well, Maxwell was instrumental in helping to establish the institution's Cavendish Laboratory, and he took on roles there as lab director and professor of experimental physics at the start of the 1870s.
Pioneer in Electromagnetism
Maxwell had continued his research on color and made ground breaking discoveries around gas velocity. It was during Maxwell's time at King's College that he began to share revolutionary ideas around electromagnetism and light.
Fellow physicist Michael Faraday had already championed the notion that electricity and magnetics were connected; Maxwell, via experimentation with vortexes, expanded on Faraday's work and came up with the theory of electromagnetic movement being conceptualized in the form of waves, with said energy traveling at light speed.
Maxwell's Equations
Supporting his theorems, Maxwell's Equations—speaking to the scholar's aptitude in using math to articulate scientific occurrences—were found in the paper "Dynamical theory of the electromagnetic field," presented to the Royal Society of London in 1864 and published the following year. In 1873 he published the book A Treatise on Electricity and Magnetism, which further expounded on his research.
Maxwell's other scientific contributions included producing the first color photograph, taken in 1861, and creating structural engineering calculations for bridge maintenance. He earned an array of awards over the course of his career, including the Rumford Medal, Keith Prize and Hopkins Prize, in addition to receiving membership in groups like the Royal Academy of Sciences of Amsterdam. Other publications included Theory of Heat (1871) and Matter and Motion (1877).
Death and Legacy
Maxwell died in Cambridge, England, on November 5, 1879, from abdominal cancer. His discoveries paved the way for much of the modern world's technological innovations and continued to influence physics well into the next century, with thinkers like Albert Einstein praising him for his indispensable contributions. Maxwell's original house, now a museum, is the site of the James Clerk Maxwell Foundation.'''
B=list(set(A))
thedict={}
for i in B:
    thedict[i]=A.count(i)
k=list(thedict.keys())
v=list(thedict.values())
print(k,v)
    