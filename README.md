BLAS/LAPACK Operation Counts
============================

This repository holds the FLOP counts for BLAS and LAPACK operations found in 

LAPACK Working Note 41 Version 3.0
by Susan Blackford and Jack Dongarra
June 30, 1999

[Appendix C - Operation Counts for the BLAS and LAPACK](www.netlib.org/lapack/lawnspdf/lawn41.pdf)

This appendix lists the FLOPs required to compute routines in BLAS and LAPACK
as a function of the size of the input matrices. 

This file doesn't OCR well so I wrote the formulae in by hand. 

Verification
------------

The document contains formulae for the number of adds, the numbers of multiplies, and the number of total flops. The first two expressions should add to the third. The file test.py reads in this data and checks this assertion on all functions. This method was used to check the accuracy of my transcription.

After removing syntax errors (such as forgetting -,+ signs) I detected less than five errors of substance (such as replacing n with m) out of the roughly 50 lines. There may be other errors not caught by this procedure. However any uncaught error would need to be accompanied by a second uncaught error on the same line which exactly countered the effect in the flops = adds + muls assertion. This is unlikely given the estimated 5/50 error rate (although this is admittedly biased).

This process also uncovered some mistakes in the original document, in particular I believe that the expressions for SGEQRF, SGERQF, and SSYTRD are in error.

test.py depends on Python and the symbolic algebra library SymPy.

Authors
-------
Matthew Rocklin
