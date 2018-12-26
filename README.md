# Fermat's Last Python Script

![Fermat portrait](fermat.jpg)

## Theorem Description
Fermat's last theorem states that for any positive integer *c* to a power greater
than 2, there are no two positive integer's to the same power that add up to
the value of *c*<sup>n</sup>. In other words, *a*<sup>n</sup> + *b*<sup>n</sup> = *c*<sup>n</sup>
has no solutions for positive values of *a*, *b*, and *c* and values greater than 2 for *n*.
## Script Description
For simplicity's sake, the script asks for a value of *c*, since you can't
test for all values of both *c* and *n* if both approach infinity in my
implementation. Then it loops through all possible values of *a* and *b*
that don't total to a value greater than *c*<sup>n</sup>. Once all possible values are
proven to not equal *c*<sup>n</sup>, *n* is incremented and the loop repeats. According
to Fermat's theorem, this loop should never terminate, which it does not.
