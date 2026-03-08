# FINITE: 677 -> 255
## Equational channel — 631 messages

**Terence Tao:**

Creating a thread here for the last remaining unknown implication for the finite graph, whether [677](https://teorth.github.io/equational_theories/implications/?677&finite) `x = y ◇ (x ◇ ((y ◇ x) ◇ y))` implies [255](https://teorth.github.io/equational_theories/implications/?255&finite) `x = ((x ◇ x) ◇ x) ◇ x`.

We know remarkably little about this equation.  @Pace Nielsen worked out that the solutions over a generic field to a linear model $$x \diamond y = \alpha x + \beta y$$ come in two flavors. Type 1: $$\beta$$ is negative a primitive 5th root of unity (i.e. a root of $$x^4+x^3+x^2+x^1$$ and $$\alpha = 1-\beta$$ (so it is a translation-invariant model). Type 2: $$\beta$$ is a root of $$x^4+x^3+2x^2+2x+1$$ and $$\alpha=−\beta^3−\beta−1$$, which (as observed by @Ben Gunby-Mann) also implies $$\alpha^2+\alpha+1=0$$ (i.e., $$\alpha$$ is a primitive root of unity).  Unfortunately, for such models 255 factors as $$(\alpha^2+\alpha+1)(\alpha+\beta−1)=0.$$

The smallest non-trivial model [model-is of order 5]; this particular example is $$x \diamond y = 2x - y$$ on $${\mathbb Z}/5{\mathbb Z}$$. 

Empirically, the magma cohomology approach seems to fail for this equation, but we do not have a satisfactory explanation as to why.

**Douglas McNeil:**

I only know of four nontrivial examples in total for 677 and would love some more if anyone has any!

The minimal [model-5], [model-7a] and [model-7b], and [model-11] .

All Latin squares, and some quick checks made it seem like the only diagonals which will satisfy 614 but violate 255 are also permutations of [0..n-1], but that was a little rushed the other day.

**Ibrahim Tencer:**

What do you mean by nontrivial? It's easy to generate linear models, so are these all known to be non-linear? It seems difficult to characterize the linear models only using the magma operation.

**Ibrahim Tencer:**

So at least in the Type 1 models we'll have $$x^2 = x$$. So if I understand correctly that means that the implication is immune to linear models.

**Ibrahim Tencer:**

Here are all the linear models up to order 500 in ℤ/pℤ, p prime:

[*Linear models (ℤ/pℤ, p prime, up to order 500) — omitted*]

I'm searching with Vampire for an order 17 model but it hasn't found one yet.

**Douglas McNeil:**

Ha, no, I was crossing streams in my mind.  I was associating the linear models, which even include small ones like the ones I hit, with the enormous ones in the other thread!  :upside_down:  Neither vampire nor mace4 seems to like finding these guys for me for very much.. thanks for the list!

**Bruno Le Floch:**

This 677->255 implication is immune to all linear models based on a (not necessarily commutative) ring where left-invertible ⇔ right-invertible (this includes finite rings and finite matrices over a field for instance).

The required equations to obey 677 are $$\beta(\alpha+\beta\alpha\beta)=1$$ and $$0=\alpha+\beta^3+\beta^2\alpha^2$$.  We want to show the condition for 255, which is $$(1+\alpha+\alpha^2)(\beta+\alpha-1)=0$$.  To proceed, we work with $$\beta$$ and $$\gamma=\alpha+\beta-1$$.  Note that the first assumption makes $$\beta$$ invertible.    The two assumptions are
```math
\gamma\beta + \beta^{-1}\gamma = \beta^2 - \beta + 1 - \beta^{-1} - \beta^{-2} , \qquad
\gamma^2 = (\beta-2-\beta^{-1}-\beta^{-2})\gamma .
```
The first equation tells us how $$\beta$$ commutes through $$\gamma$$: intuitively it is mapped as $$\beta\to-\beta^{-1}$$.  This is an involution, so we can get useful mileage from commuting through $$\gamma^2$$.  Namely, we write $$\beta^{-1}\gamma^2\beta-\gamma^2 = [\beta^{-1}\gamma, \gamma\beta+\beta^{-1}\gamma]$$ and compute the LHS using the formula for $$\gamma^2$$ and the RHS using the formula for $$\gamma\beta+\beta^{-1}\gamma$$.  After reordering $$\beta,\gamma$$ using the first identity, we get a formula of the form $$f(\beta)\gamma=g(\beta)$$.  Right-multiplying by $$\gamma$$ and reducing $$\gamma^2$$ we get $$h(\beta)\gamma=0$$.  If I didn't mess up my calculations, we have enough to deduce $$(3-3\beta+\beta^2+3\gamma-\beta\gamma-\gamma\beta+\gamma^2)\gamma=0$$, which is 255.

**Matthew Bolan:**

I think I have also used Magma to rule out all non-commutative linear models modelled on a vector space with scalar field of characteristic 0 or positive characteristic less than 10000. In this [online calculator](https://magma.maths.usyd.edu.au/calc/) one can run 
```
for p in PrimesUpTo(10000) do
    F<a, b, c> := FreeAlgebra(FiniteField(p),3);
    B := [(-1)+(b*a)+(b*b*a*b),(a)+(b*b*a*a)+(b*b*b),(b*b*a*c)+(b*b*c)+(b*c)+(c)];
    I := ideal<F | B>;
    if not ((-1)+(a*a*a)+(a*a*b)+(a*b)+(b) in I and (a*a*c)+(a*c)+(c) in I) then
        print(p);
    end if;
end for;
print("Done");
``` 
to test small characteristics. (And testing the rationals is similar).

**Pace Nielsen:**

Sorry I didn't make this clearer on the previous thread.  When I worked out the two solutions over a generic field, I actually worked out the full reduction system over (potentially noncommutative) rings.  For a map of the form $$x\diamond y=ax+by+c$$, a reduction system is given by
```math
ba\mapsto ab,\qquad b^3\mapsto a^2b+b^2+a^2-a,\qquad a^2b\mapsto -a^3-ab-b+1,
```
```math
a^4\mapsto ab^2+2a^3+ab-a^2+b+a-2,\qquad b^2ac\mapsto -b^2c-bc-c,
```
```math
a^2c\mapsto -ac-c,\qquad b^2c\mapsto abc+ac
```
(255 does indeed follow for such linear maps over rings.)

**Matthew Bolan:**

Did you do that by hand or do you have software which can do that automatically? I'd like to compute the graph for linear implications.

**Terence Tao:**

I can't believe it took 70 days into the project before we finally were able to make use of Magma...

**Matthew Bolan:**

And it still isn't very useful (I was able to rediscover something close to your 1117 -> 2441 example with it though).

**Matthew Bolan:**

(with this code in case you are curious. The ideal is the needed equations to be a linear model of 1117, the final two inclusions come from 2441)
```
F<a, b, c> := FreeAlgebra(Rationals(),3);
B := [(-1)+(b*a*b*a),(a)+(b*a*a),(b*a*b*b)+(b*b),(b*a*b*c)+(b*a*c)+(b*c)+(c)];
I := ideal<F | B>;
GroebnerBasis(I);

(-1)+(a*a)+(a*b*a*a)+(a*b*a*b)+(a*b*b)+(b) in I;
(a*b*a*c)+(a*b*c)+(a*c)+(c) in I;
```

**Pace Nielsen:**

I used code I wrote (and have updated over the years) in Mathematica.  I'm happy to share it if you are interested---just shoot me an email.

**Matthew Bolan:**

That's some useful stuff, I really could not find a standard package to do it for me and was dreading writing it myself.

**Ibrahim Tencer:**

So do we really not have a single model that is known not to be linear?

**Bruno Le Floch:**

A diagnosis of linear models is that all (finite) linear models are Latin squares (the condition $$b(a+bab)=1$$ makes $$b$$ invertible, then the condition $$(1+b^2a)a=-b^3$$ makes $$a$$ invertible).  It's clear that 677 implies that left multiplication is invertible, since $$\text{im}(L_y)$$ is the whole magma and surjective implies injective.  Both prover9 and mace4 are inconclusive on whether right multiplication has to be invertible in a general 677 magma (I am not very good with these tools though).  This could influence the type of counterexamples we seek.

Terry used $$x\diamond y=y$$ as a fall-back rule for his gigantic 1518 example because this was an easy way to fulfill the equation for most of the table.  Here one option is to use a linear fallback, but the linear models are somewhat complicated.  Another option is to use as a fallback a magma satisfying equation 14 ($$x = y \diamond (x \diamond y)$$), but modifying the squares (or the products involving squares).  Then for most $$x,y$$ the equation would reduce to $$x=y\diamond x^2$$.  I didn't push this yet, in part because I wasn't sure if I had to make the magma right-cancellative.

**Terence Tao:**

Hmm, the latter option looks problematic because it's going to be hard to have $$x = y \diamond x^2$$ and $$x = y \diamond (x \diamond y)$$ both hold for most $$x,y$$ (if one replaces $$y$$ by $$S^2 y$$ then the first equation suggests that $$S^2 y \diamond (x \diamond S^2 y)$$ should equal $$y$$, not $$x$$).    One could perhaps ask an ATP whether the constant-squaring case $$x \diamond x = 0$$ is at all permissible, if so that might be a possible model to pursue.

**Douglas McNeil:**

FWIW, there are definitely x*x=0 cases which satisfy 14/614, e.g. [model-5] or [model-13].

Ah, but you want eq 13 too, at least mostly, hmm.

**Bruno Le Floch:**

Sorry, you're right, imposing equations 14 and 13 at the same time makes no sense.  I had started an attempt by partitioning the magma in two subsets, but I don't have anything concrete at this stage.

The question of right-cancellation remains.  In some sense, we need multiplication to preserve all the information in the right operand (due to left-cancellation) and at least "half" of the information in the left operand: indeed, the equation can be written as $$x = L_{x'}(L_{x''}(y))$$ where $$x' = y\diamond x$$ and $$x''=y\diamond x'$$, and we want the pair of $$L_{x'}$$ and $$L_{x''}$$ to uniquely determine $$x$$ (for a given $$y$$).  So maybe a better starting point would be to try a carrier $$M=P\times P$$ and  $$(x_1,x_2)\diamond(y_1,y_2) = f(x_2,y_1,y_2)$$ to find an example of 677 magma that is not right-cancellative.  Then *hopefully* it helps with making a 255 counterexample.

**Jose Brox:**

If we impose bijectivity of left and right multiplications, then 677 implies 255. Here is a Prover9 proof (it only uses left injectivity and right surjectivity):
[attached: PROVER9 677 plus left and right mult bijective implies 255 PROOF.txt]

**Jose Brox:**

677 plus left multiplication bijective plus x^2 = y^2 implies 255.

I'm running a search of 677+left mult bijective + equation against 255, where equation ranges in [2,4694]. For now there are only 225 candidates left; I'll update soon.

**Bruno Le Floch:**

The specific idea of dropping uniformly the "same half" of the left operand fails.  In the equation written (in the finite case) as `x = (y ◇ x) ◇ ((y ◇ (y ◇ x)) ◇ y)`, that would mean that the only dependence on y1 is from the last variable, and this dependence never disappears because this `y` is acted on by bijective `L_{y ◇ x}` and `L_{y ◇ (y ◇ x)}`.  So we need more mixing.

**Douglas McNeil:**

So, that was a complete failure: mutation didn't work at all here, despite a fresh run.

I had one last faint hope that I simply had too few samples, but even after I had the dozens of linear models to play with thanks to Ibrahim, no luck.  They're too tightly coupled together to use as good seeds.  If you remove too few cells you wind up completing back to the original, and if you don't, you get an enormous number of linked failures which don't seem repairable.  Reducing to a partial solution using fewer elements and trying to grow that, which helped before, also didn't work.  Frankly, both vampire and mace4 have trouble finding the *known* solutions for me without a lot of prompting at larger N, although that might not apply to less coupled solutions, to be fair.

Efforts to use 614 as a base and then migrate back towards 677 didn't work either, and I can't even use the trick of driving toward a solution gradually by imposing some of an equation's implications because 677 doesn't have any in our set.

For evolutionary approaches to work, you need at least to be able to jump from one useful state (target or not) to another efficiently.  This fails when useful states are too rare or it takes too long to get a new state, both of which seem to be true here.

**Terence Tao:**

This feels like an important clue to me.  For finite magmas we get left injectivity for free. If we can get a human proof of why right surjectivity implies 255 that should make it clearer what a counterexample might look like (or what a proof might look like - this implication could well be true for finite magmas!).

**Terence Tao:**

One possible thought is to try to adapt a technique that worked for weak central groupoids (see [blueprint](https://teorth.github.io/equational_theories/blueprint/weak-central-groupoids-chapter.html)), which is to find a small (e.g., order 2) "relaxed" solution to 677 (where the magma operation is slightly multivalued), and try to build an extension of that by some pseudo-greedy algorithm.  This amounts to imposing a coloring on the magma and imposing some rules about how the color of $$x \diamond y$$ relates to the color of $$x$$ and $$y$$ (e.g., if $$x$$ is red and $$y$$ is blue, then $$x \diamond y$$ must be blue, but if $$x$$ and $$y$$ are both red, then $$x \diamond y$$ could be either red or blue, etc.).  It may be possible to "decouple" the magma structure this way, for instance one could try to make the equation 13 hold for red elements and 14 hold for blue elements, thus dodging the issue that 13 and 14 are not compatible with each other.  However I don't know if there is a practical relaxed magma that can be used as a base (of course one can always use the trivial relaxation in which every color output is permitted, but this doesn't gain anything).

**Jose Brox:**

Ok! I will have a look at it later and translate it from "telegraphic superposition calculus" to something more human-readable.

**Jose Brox:**

24 candidates have survived a 10min Prover9 search. So, together with 677 (and left multiplication bijective) it is probably also safely to assume any of
[411, 513, 623, 642, 817, 1020, 1035, 1048, 1223, 1238, 1251, 1426, 3659, 4065, 4073, 4131, 4276, 4293, 4321, 4343, 4380, 4591, 4599, 4695]
against 255.

Later I will look at combinations of these additional equations.

**Ibrahim Tencer:**

There are no 677 models of size 2, 3, 4, and 6. I've been running a Vampire search for a model of order 8 for 26 hours but it still hasn't found one.

**Terence Tao:**

It's relatively rare for a two-variable equation such as 677 to have so few models, and so much restriction on the order.  Weak central groupoids (1485) also had a lot of restrictions on the order, but that's a three-variable equation, so less surprising (it imposes $$n^3$$ constraints rather than $$n^2$$ constraints).

On the other hand, in contrast to say 854, 677 does  not seem to be implying a lot of other laws (Equation Explorer only lists the trivial consequence 614, even if one assumes finiteness).  So this equation is imposing some "rigidity", but the rigidity is coming from an unknown source.

**Matthew Bolan:**

The key point of the prover9 proof seems to be that 677 says that $$x = y \diamond (x \diamond ((y \diamond x) \diamond y),$$ so $$R_x^{-1}(x) \diamond x = x = R_x^{-1}(x) \diamond (x \diamond (x \diamond R_x^{-1}(x)))$$ and thus $$x = x \diamond (x \diamond R_x^{-1}(x))$$ by left injectivity.

From here, the point is that 677 + left injectivity tell us $$y = (x\diamond y) \diamond ((x \diamond (x \diamond y)) \diamond x)$$, so $$x \diamond R_x^{-1}(x) = x \diamond ((x \diamond x) \diamond x)$$, and so $$R_x^{-1}(x) = (x \diamond x) \diamond x.$$ Right multiplying this by $$x$$ gives 255.

**Terence Tao:**

To rephrase the argument: if we have $$y \diamond x = x$$, then by 677 $$x = y \diamond (x \diamond ((y \diamond x) \diamond y)) = y \diamond (x \diamond (x \diamond y))$$, hence by left-cancellativity $$x = x \diamond (x \diamond y)$$.  Meanwhile from 677 with $$y$$ replaced by $$x$$ we also have $$x = x \diamond (x \diamond (Sx \diamond x))$$, so by left-cancellativity again $$y = Sx \diamond x$$ and hence $$(Sx \diamond x) \diamond x = x$$ which is 255 for $$x$$.

So we don't even need full right surjectivity; just being able to solve $$y \diamond x = x$$ for each $$x$$ would give 255.  Conversely, 255 clearly implies that $$y \diamond x = x$$ is solvable, so this is an equivalent form of 255.

**Terence Tao:**

This now reminds me of the ruleset of the (automatically generated) [greedy algorithm refuting 677->255 for infinite magmas](https://github.com/teorth/equational_theories/blob/main/equational_theories/Generated/Greedy/Eq677.lean#L714) (which is conveniently accessible from the 677 Equation Explorer page).  The 677 ruleset (ignoring Rule 0, which says that $$\diamond$$ is a partial function) is
1.  If $$y \diamond x = z$$, $$z \diamond y = w$$, $$x \diamond w = u$$, then $$x = y \diamond w$$ (this is just 677)
2. If $$x \diamond y = y \diamond x = x$$ then $$x \diamond x = y$$
3. If $$x \diamond x = y$$, $$x \diamond y = z$$, and $$z \diamond x = x$$ then $$z = x$$
4. If $$x \diamond y = z$$, $$y \diamond w = x$$, and $$z \diamond y = w$$, then $$z \diamond w = y$$. 

Rule 2 can be strengthened with the above analysis: if $$y \diamond x = x$$ then $$x = x \diamond (x \diamond y)$$ so if we also have $$x \diamond y=x$$ then $$x$$ is idempotent, and by left-cancellativity we have $$x=y$$.  Not sure yet where Rule 3 and Rule 4 are coming from though.

**Terence Tao:**

A proof of Rule 3 (for finite magmas at least): by hypothesis, $$z = Sx \diamond x$$.  From 677 we have $$Sx = x \diamond (Sx \diamond ((Sx \diamond x) \diamond x)) = x \diamond (Sx \diamond x) = x \diamond z$$ hence by left-cancellability $$x = z$$ as required.

**Matthew Bolan:**

Rule 4 holds since $$w = y \diamond (w \diamond ((y \diamond w) \diamond y)) = y \diamond (w \diamond z)$$, so $$y =  z \diamond (y \diamond ((z \diamond y) \diamond z)) = z \diamond w. $$

**Terence Tao:**

Given that one needs to avoid solving the equation $$y \diamond x = x$$ to obtain a counterexample, a possible relaxed base magma to choose is the carrier $$\{0,1\}$$ with $$0 \diamond 1 = 1 \diamond 1 = 0$$ and $$1 \diamond 0, 1 \diamond 1$$ permitted to be either $$0$$ or $$1$$, thus $$y \diamond x$$ cannot equal $$x$$ when $$x=1$$.  An extension of this relaxed base would thus be a magma colored in two colors, 0 and 1, such that the product of anything with a 1-colored object must be 0-colored.  As far as I can tell, this is compatible with 677 (but perhaps having an ATP confirm this would be great).  So if we can create such a 2-colored finite 677 magma with at least one element 1-colored, we have refuted 677 -> 255 for finite magmas!

One natural place to start is to see if it is possible to start with some base 677 magma, such as a linear model, declare it to be 0-colored, and see if one can add a single 1-colored element to it and preserve 677.   Given how rigid the 677 magmas seem to be, this seems unlikely, but perhaps discovering the obstruction to this working would be instructive.

**Terence Tao:**

OK, adjoining 1-colored objects to an existing 0-colored magma would not work, as it would violate left-surjectivity (the product of a 0-colored object with anything would not be 1-colored).

**Jose Brox:**

I'm now running 10min searches for models with 677+one of the 24 candidates+left multiplication bijective + (exists x such that doesn't exist y such that yx = x). Already without adding any candidate, size 8 is exhausted in seconds.

**Terence Tao:**

One possible stronger axiom than (exists x such that doesn't exist y such that yx = x) is (exists distinct 1,0 such that y1=0 for all y).  If we can find a finite 677 magma that obeys this axiom then we are done, but perhaps there is a simple reason why such axioms are incompatible with 677.

**Terence Tao:**

OK, the strong axiom $$y \diamond 1 = 0$$ is not compatible.  677 implies $$0 = y \diamond (0 \diamond ((y \diamond 0) \diamond y))$$, so by left invertibility $$(y \diamond 0) \diamond y = L_0^{-1} 1$$ is independent of $$y$$.  In particular $$(y \diamond 0) \diamond y = (1 \diamond 0) \diamond 1 = (y \diamond 0) \diamond 1$$, hence by left cancellability $$y = 1$$ for all $$y$$, which is absurd.

**Terence Tao:**

This still allows for the possibility that one has $$y \diamond 1 = 0$$ for all $$y \neq 1$$ (and $$1 \diamond 1 = 2$$ for some $$2 \neq 0,1$$), though.

**Ibrahim Tencer:**

One observation: 255 says $$x = x^4$$ where we define powers with right-multiplication. The model is finite so two powers of x must coincide, giving $$yx = x^n$$ with $$y = x^m$$. If right-cancellation holds then we can repeatedly take x's off of both sides to get it in the form $$x = x^k$$, but otherwise we can repeat @Terence Tao 's argument to instead get $$x(x^2 x) = x^n y = x^n x^m$$. So for a counterexample we should think about what m and n can be.

**Terence Tao:**

Sorry, could you clarify how you get that final equation $$x(x^2 x) = x^n y$$?  I can see that $$x = y(x(x^n y))$$ and we also have $$x = x(x(x^2 x))$$, but then I get stuck.

**Ibrahim Tencer:**

Ah never mind, I was getting x^n and x mixed up there.

**Terence Tao:**

I assume that a law such as $$x^2 = x^3$$ (equation 359) would already have been ruled out by @Jose Brox 's sweep, though perhaps it is worth figuring out why such a law would immediately give 255.

**Jose Brox:**

Making trials with sizes 6 and 7, it seems that the best Mace4 configuration for 677 is selection_order 2, selection_measure 3, skolems_last set. With it, Mace4 has been able to check in 41min that 677 has NO models of size 8. 

Size 9 has been running for almost 4h already, no models yet.

Btw, in sizes 5 and 7 there is only one model (up to isomorphism).

**Douglas McNeil:**

@Jose Brox : you mean only one model under the additional props of your search, right?  There are definitely two non-iso order 7 677s (with and without constant squares).

**Jose Brox:**

Oh, this seems like another bug in Windows' isofilter :melting_face: 

I meant without any other properties, because that is what isofilter says! It only returns the model with non-constant squares (see the pictures below), but it does find the constant squares one, so it seems to be isofilter and not Mace4 what fails.

Thank you for this observation!

[attached: Isofilter serious bug 1.JPG]
[attached: Isofilter serious bug 2.JPG]

EDITED: This bug only appears in the Windows GUI, isofilter in the Ubuntu command line gives the right answer, with two isoclasses.

**Jose Brox:**

And if I have everything right, indeed it is!

677 + left multiplication injective + (right multiplication injective iff right multiplication surjective) implies 255:

```
**Prover9 assumptions**
x = y * (x * ((y * x) * y)) #label(677).
x*y = x*z -> y = z.
(y*x = z*x -> y = z) <-> (all u all v exists w (w*u = v)).
**Prover9 goal**
x = ((x * x) * x) * x #label(255).
```
[attached: PROVER9 677 implies 255 in finite setting PROOF2.txt]
The proof is simpler if we also impose that $$yx = x$$ is not always solvable, as we know we can do:
[attached: PROVER9 677 implies 255 in finite setting PROOF.txt]

Is everything right?

**Matthew Bolan:**

I think the "for all" quantifiers have the wrong scope in the third assumption, they should be inside the parentheses. I'd expect 
```
(all y all z (y*x = z*x -> y = z)) <-> (all v exists w (w*x = v)).
```
or
```
(all x all y all z (y*x = z*x -> y = z)) <-> (all u all v exists w (w*u = v)).
```

**Bruno Le Floch:**

EDIT: I had previous claimed here that prover9 finds a proof with the corrected version given by Matthew, but actually I missed parentheses.  Now it doesn't work.

**Terence Tao:**

No problem, we all make mistakes here (I've certainly made my own fair share)!

**Bruno Le Floch:**

(incorrect) [model-25-element refutation of 677->255]

**Douglas McNeil:**

Uh, doesn't that refute 255->677 instead?  :upside_down:

**Bruno Le Floch:**

Ouch. Yes! Perfect smiley, by the way.

**Jose Brox:**

Thank you, this is indeed the case! This one is subtle: according to its manual, when parsing free variables in clauses and formulas Prover9 assumes they are universally quantified *at the outermost level*. I had understood this fact to be relative, i.e., to mean "at the outermost level of each subformula given by parentheses", but it is in fact absolute, meaning "at the outermost level of the global formula". Hence
```x*y = x*z -> y = z``` works as intended, but
```(x*y = x*z -> y = z)<->(all u all v exists w (w*u = v))``` actually means
```all x all y all z ((y*x = z*x -> y = z) <-> (all u all v exists w (w*u = v)))``` instead of
```(all x all y all z (y*x = z*x -> y = z)) <-> (all u all v exists w (w*u = v))```. The variant 
```all x all y all z (y*x = z*x -> y = z) <-> all u all v exists w (w*u = v)``` also works as intended.

I've made quite a few! Mine tend to be misunderstanding errors (worse in weekends :upside_down:) ...

**Zoltan A. Kocsis (Z.A.K.):**

@Jose Brox :

> meaning "at the outermost level of the global formula"

In first-order model theory, writing down the simplest possible definition of the satisfaction relation naturally leads to interpreting "free variables as universally quantified", in the sense that a formula $$P(x,y,\dots)$$ with free variables counts as satisfied in a model precisely if its [universal closure](https://proofwiki.org/wiki/Definition:Universal_Closure_of_Well-Formed_Formula) $$\forall x. \forall y. \dots . P(x,y,\dots)$$ is satisfied in that model.

The treatment of free variables in Prover9/Mace4 attempts to follow the same convention. This explains why the manual's explanation is so unnuanced. The authors failed to anticipate that the users would not necessarily be logicians familiar with this convention.

**Bruno Le Floch:**

Consider 677-cohomology.  We consider an abelian coefficient group $$M$$ with a linear operation $$s*t=as+bt$$ with $$a,b\in\mathrm{End}(M)$$.  The extension is $$G\times M$$ equipped with $$(x,s)\diamond(y,t)=(x\diamond y,as+bt+f(x,y))$$.  The cocycle equation (stating that the extension obeys 677) is
```math
0 = b^2 a f(y,x) + b^2 f(y\diamond x,y) + b f(x,(y\diamond x)\diamond y) + f(y,x\diamond((y\diamond x)\diamond y))
```
On the other hand, $$M$$ has to obey 677, so $$1=b(a+bab)$$ and $$a+b^2a^2+b^3=0$$, which reduce in the abelian case to $$P_8(b)=(1-b+b^2-b^3+b^4) (1+2b+2b^2+b^3+b^4) = 0$$ and $$a=(b+b^3)^{-1}$$.

**Claim:** if a 677 model $$(G,\diamond)$$ has $$x\diamond x=x$$ (which holds for type 1 linear models over fields), then for any 677-coefficients the 677-cohomology is a subgroup of the 255-cohomology.  In other words, any of its extensions by linear models obeys 255.
For $$y=x$$ the cocyle equation reduces to $$0 = (b^2 a + b^2 + b + 1) f(x,x)$$.  To establish 255 we want to show $$(a^2+a+1)f(x,x)=0$$.  The bookkeeping, working modulo $$P_8(b)$$, works out.

This suggests looking at type 2 linear models over fields, such as the two 7-element magmas.  Unfortunately both of them have trivial cohomology over $$\mathbb{C}$$ (hence with arbitrary coefficients?).  It would be good to understand why.
Another option for the base is a magma that has already been linearly extended once.

**Matthew Bolan:**

I've already checked all extensions with $$G$$, $$M$$ linear (including a constant term) and order <= 25 with no luck. I can try taking the base to be magmas which have been extended once though.

**Terence Tao:**

It's good to get some theoretical explanation as to why the cohomological approach wasn't being successful here!  We already knew that to disprove a one-variable equation like 255 one can assume without loss of generality that the base model $$G$$ is generated by a single element, which explains why it isn't productive to use base magmas in which every element is idempotent.

My cohomological algebra is extremely rusty (definitely not my favorite class in grad school) but I guess these magma cohomology groups should obey some sort of "universal coefficient theorem" that relates the complex coefficient groups to the others [EDIT: but then I guess we also have to define some "magma homology" that is dual to "magma cohomology"?].  I had some vague hope that even if the characteristic zero cohomology is trivial, there is some "ramification" at some prime caused by some determinant in the linear algebra having a prime or prime power factor which could then lead to a finite counterexample.  I think it would also be interesting to find infinite counterexamples to 677->255 defined over the complex numbers; currently our only construction of this counterexample proceeds by the greedy method and does not give a very tractable description of the resulting magma.

**Matthew Bolan:**

I think we actually already have an example of some kind of "ramification" for the linear models. Bruno's degree 307 counterexample in the HN law project is very interesting, over $$\mathbb Z[a,b]$$ the polynomial $$307b + 307$$ is in the relevant ideal, and if $$307$$ is invertible, then $$b=-1$$ and no linear counterexample can exist, but modulo 307 we have a linear counterexample.

**Matthew Bolan:**

the degree 103 example has a similar property, though I think it also has counterexamples in characteristic 5.

**Matthew Bolan:**

There are examples of similar phenomena in the main project by the way, for example law 895 (Which is a law for abelian groups of exponent 2) only has linear models in characteristic 2.

**Terence Tao:**

I have a vague intuition that such exceptional primes may be the best bet for finding counterexamples from the cohomological approach, because often the relevant matrices in the linear algebra calculations are going to have full rank (after quotienting out the coboundaries) and so in general characteristic will not have an interesting kernel that we can use to produce non-trivial extensions.  But if there is ramification then we can hope to sneak in an interesting counterexample at specific primes.  Except that for this particular equation, we only get magmas at relatively large primes like 5, 7, or 11, so the probability of getting ramification is sadly somewhat low.  Though your examples at 307 and 103 do indicate that maybe all hope is not lost...

**Terence Tao:**

Actually, at every prime $$p$$ it should be possible to construct a linear magma in characteristic $$p$$ by using an appropriate finite field $$F_{p^j}$$ that holds all the relevant coefficients $$\alpha,\beta$$, so maybe one will be fine as soon as there is ramification at any prime...

**Terence Tao:**

Would it be possible to make your cohomology code give the Smith normal form of the cocycle equation for a given base magma (presumably a Type 2 base model, given that Type 1 models are useless)?  The prime factors of the elementary divisors of that form would be the natural choices for the characteristic for the coefficient magma $$M$$ as the cohomology groups should be unusually large over those characteristics. (One may have to work first in some abstract coefficient ring over $${\mathbb Z}$$ generated by the defining equations for the coefficients $$\alpha,\beta$$  before specializing to a finite characteristic $$p$$.)

**Matthew Bolan:**

I think that should be possible provided sage supports the Smith Normal Form computation over the relevant ring, which it hopefully does.

**Matthew Bolan:**

Hmm, I'm running into some trouble. The needed abstract coefficient ring is not a PID, and so I don't think Smith Normal Form makes sense for it (at least, not in a way sage supports or I can easily implement).

**Terence Tao:**

OK so apparently there is something called the Hermite normal form that can work for Dedekind domains that aren't PIDs and may be sufficient here as a substitute for the Smith normal form.  It's implemented in SAGE at https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_integer_dense.html#sage.matrix.matrix_integer_dense.Matrix_integer_dense.hermite_form

**Terence Tao:**

Hmm but the sage implementation is only over the integers

**Terence Tao:**

Following links from ChatGPT, I find that this specific functionality was listed as "Extreme difficulty" to implement in SAGE in https://wiki.sagemath.org/GSoC/2015?utm_source=chatgpt.com#Hermite_Normal_Forms_for_modules_over_the_ring_of_integers_of_number_fields.  , and presumably never implemented. :sad:

**Terence Tao:**

Though it suggests that Magma or PARI can do it.

**Terence Tao:**

Apparently the relevant documentation page for the Magma implementation is https://magma.maths.usyd.edu.au/magma/handbook/text/276 , but I've never actually used Magma so I don't know how easy it would be to use these methods for our specific application.

**Matthew Bolan:**

I think it is definitely worth pursuing, it didn't occur to me to check Magma but if is has this functionality then it should have enough to just let me compute $$H^2(G, \mathbb Z[a,b] / I)$$ directly.

**Matthew Bolan:**

In the meantime I'm going to go back to trying base models which are already extensions, so that I can do an overnight run of that check.

**Terence Tao:**

Do you know by the way if any of the extensions were non-trivial (i.e., not by coboundaries)?  That is to say that $$H^2(G,M)$$ was actually non-trivial for some choices of $$G,M$$?

**Matthew Bolan:**

Yes, that seems to occur. In fact for some choices of $$G, M$$ I was surprised by how large $$H^2$$ was - makes me worry I've done something wrong in my computation of $$B^2$$ I've just written.

**Terence Tao:**

It might be worth sharing some examples of such non-trivial extensions here for others to play with.  As I understand it right now the only explicit finite models we have for this equation are the linear ones (and direct products thereof).

**Matthew Bolan:**

I was planning to, just trying to make sure I don't share any nonsense (Is there any easy way to prove a model is non-linear?).

**Terence Tao:**

Hmm.  In a linear model all the left and right multiplication operators lie in the affine group, which is solvable (and even metabelian), so for instance $$[[L_y,L_{y'}], [R_z, R_{z'}]]=1$$.  Most likely any nonlinear model would fail this identity.

**Matthew Bolan:**

Alright, implementing that test currently seems like more trouble than it is worth. I'm just going to print out for each the magmas corresponding to some basis of $$H^2$$ and send a giant text file.

**Matthew Bolan:**

They should work out anyway

**Matthew Bolan:**

[attached: 677_probably_nonlinear.txt]

**Matthew Bolan:**

Using $$M, G$$ linear models of size <= 15

**Jose Brox:**

A model of 677 of size 9, found in 32.5h by Mace4 (it also satisfies 255):

        [[ 0, 2, 3, 5, 1, 7, 4, 8, 6],
          [ 1, 3, 4, 6, 7, 0, 2, 5, 8],
          [ 2, 8, 5, 1, 3, 4, 6, 0, 7],
          [ 3, 5, 6, 7, 4, 2, 8, 1, 0],
          [ 4, 6, 8, 0, 2, 3, 5, 7, 1],
          [ 5, 1, 7, 4, 6, 8, 0, 3, 2],
          [ 6, 7, 0, 2, 8, 5, 1, 4, 3],
          [ 7, 4, 2, 8, 0, 1, 3, 6, 5],
          [ 8, 0, 1, 3, 5, 6, 7, 2, 4]]

**Zoltan A. Kocsis (Z.A.K.):**

@Jose Brox : The structure $$J$$ your long search found appears to be a "twisted copy" of the elementary Abelian group $$ (\mathbb{Z}/3\mathbb{Z})^2$$.

*edit*: There was a miscalculation here - the model is linear however, see below.

We can find functions $$f : (\mathbb{Z}/3\mathbb{Z})^2  \rightarrow J$$ and $$g,h : (\mathbb{Z}/3\mathbb{Z})^2 \rightarrow (\mathbb{Z}/3\mathbb{Z})^2 $$ so that $$x \diamond y = f(g(F(x)) + h(F(y)))$$. Or, more legibly, if you change the base set of your magma to coincide with that of $$(\mathbb{Z}/3\mathbb{Z})^2$$, then you in fact have $$x \diamond y = g(x) + h(y)$$, where $$+$$ is the group operation.

Let's use a compact notation for elements of $$ (\mathbb{Z}/3\mathbb{Z})^2$$, with e.g. $$02$$ denoting the pair $$(0+3\mathbb{Z},2+3\mathbb{Z})$$.

Then the permutation $$g$$ is given by the cycles $$g=(02,10,11,12,21)(20,22)$$, while  $$h$$ is given by $$h=(01,10,21,20,12,02,11)$$. And $$f$$ is just the obvious map $$(x,y) \mapsto 3x+y$$ sending $$(\mathbb{Z}/3\mathbb{Z})^2$$ into $$\{0,\dots,8\}$$, and $$F$$ its inverse.

NB I found $$g,h$$ by fixing $$f$$ first, so mayhap for some other $$f$$ the two permutations admit a more readable form. But in the end $$\diamond$$ is a $$g,h$$-twisted version of a group operation.

**Zoltan A. Kocsis (Z.A.K.):**

(Please note that I'm still mostly out-of-the-loop after my long hiatus, maybe it's already obvious from the study of the linear case that these examples will always have this form. If so, apologies. Just thought it was a fact that should be documented.)

**Terence Tao:**

Interesting!  It's not obvious to me why an operation of the form $$x \diamond y = g(x) + h(y)$$ should have any particular likelihood to solve 677 if $$g,h$$ are nonlinear.  Perhaps if we figure this out, we would have a new ansatz for searching for finite models (right now we basically only have three viable ansatzes: the linear model, the translation-invariant model, and cohomological models.  Of the three, we haven't really explored translation-invariant models much, but the functional equation for 677 is rather unappetizing there...)

**Terence Tao:**

@Zoltan A. Kocsis (Z.A.K.)  I'm having trouble matching your model with @Jose Brox 's model.  For instance, Jose's model is right-unital, $$x \diamond 0 = x$$, but the model $$x \diamond y = g(x) + h(y)$$ is not going to be right-unital unless $$g$$ is a shift of the identity map.  Perhaps there is a typo somewhere?

**Matthew Bolan:**

Just to make sure, we know that Jose's model is not one of the two linear ones over $$F_{3^2}$$? Those are both right unital

**Terence Tao:**

According to my calculations, the magma is instead equivalent to a linear model with carrier $$({\mathbb Z}/3{\mathbb Z})^2$$ and operation $$x \diamond y = x + \beta y$$ where $$\beta(a,b) := (b,a+b)$$.  I think this is also a linear model over $${\mathbb F}_9$$.

**Matthew Bolan:**

The linear models over $$F_9$$ are $$x \diamond y = x + \beta y$$ and $$x \diamond y = x + (2\beta + 1) y$$ , where $$\beta^2 - \beta - 1 = 0$$.

**Terence Tao:**

Yeah that matches.  So unfortunately this isn't a new model

**Jose Brox:**

I should have made a search for more than one model, as Mace4 tends to find them in batches, with small perturbations of the first one encountered. I'm running two new searches, one of them forcing the model not to have a right unit.

**Douglas McNeil:**

@Jose Brox : is it just me or are 677 magmas noticeably slower to find than others?  It was easier for me to find models in the ~15 range for some three-variable equations than it is to find models with only a third as many cells here.  I don't know if it's the fact every substep has a new element so there's lots of coupling or what.

**Terence Tao:**

There's something very "mixing" about 677.  It doesn't have easy models like left-absorptive or right-absorptive models that one can hope to modify, nor does it involve the squaring map which seems to simplify the structure (in that a law involving three magma operations and a square seems easier to satisfy than four magma operations and no square).  Also it can't be easily expressed purely in terms of left multiplication or purely in terms of right multiplication, but instead mixes together both.  So, other than using a linear ansatz, there don't seem to be cheap ways to try to make it more likely to create a 677 magma.  Also the fact that half of the linear models are idempotent is also weakening the power of the cohomological method to construct interesting magmas.

**Jose Brox:**

There are no countermodels of 255 satisfying 677 in size 9, computation done in 29.6h by Mace4 (order 2, measure 3, skolems_last) with the formulas
```
**ASSUMPTIONS**
x = y * (x * ((y * x) * y)) #label(677).
x*y = x*z -> y = z.
all x all y exists z (x*z = y).
exists x -(exists y (y*x = x)).
(all x all y all z (y*x = z*x -> y = z)) <-> (all u all v exists w (w*u = v)).
**GOAL**
x = ((x * x) * x) * x #label(255).
```

**Zoltan A. Kocsis (Z.A.K.):**

Yes, I revisited my notes and found the miscalculation :/ Apologies for sending you on a wild goose chase. Further reviewing the notes, I think I do show that one can at least write $$x \diamond y = j(g(x) + h(y))$$ for a nontrivial $$j$$ over $\mathbb{Z}/3\mathbb{Z}^2$$ but since this happens to be a linear model anyway, I won't pursue it any further.

**Jose Brox:**

Two negative results:
1) There are no other size 9 models of 677 satisfying $$0*0=0$$, $$0*1 =2$$, $$0*2=3$$ besides the linear one (1.2h in Mace4).
2) There are no size 9 models of 677 that are not right unital (5.8h in Mace4).

There seem to be few models of size 9...

**Bruno Le Floch:**

The cohomological approach cannot yield counterexamples to 255.  The set of (right-)cancellative 677 models is stable under cohomological extensions (see proof below), so for each $$x$$ we have a solution $$y=R_x^{-1}(x)$$ of $$y\diamond x=x$$, which [we know implies 255](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486686097).  Copying Terry Tao's version of the argument here: $$y\diamond x=x\overset{677}{=}y\diamond(x\diamond((y\diamond x)\diamond y))=y\diamond(x\diamond(x\diamond y))$$ so by left-cancellativity $$x\diamond(x\diamond y)=x\overset{677}{=}x\diamond(x\diamond(Sx\diamond x))$$ so by left-cancellativity $$y=Sx\diamond x$$ hence $$(Sx\diamond x)\diamond x=x$$, equation 255.

Why is right-cancellativity stable?  Consider $$(x,s)\diamond(y,t)=(x\diamond y,as+bt+c+f(x,y))$$ with $$s*t=as+bt+c$$ a linear model.  We know (finite) linear models are right-cancellative (in other words $$a$$ is invertible).  If $$(x,s)\diamond(y,t)=(x',s')\diamond(y,t)$$ then $$x\diamond y=x'\diamond y$$ and $$as'+bt+c+f(x',y)=as+bt+c+f(x,y)$$.  The first equation gives $$x=x'$$ by right-cancellativity of the base.  The second equation then gives $$s'=s$$ by invertibility of $$a$$.

That said, the cohomological approach could still possibly provide nonlinear examples of 677, which may be of independent interest.

**Bernhard Reinke:**

Were finite non-commutative translation invariant models already considered?

**Bernhard Reinke:**

I think in that setting, one could try to consider something like $$ x \diamond y = x f(x^{-1} y) $$ so that $$ f(x) = 1 \diamond x$$, left cancellative implies that $$f$$ is a injective (so a bijection for finite models), and what we want to avoid is $$f(x) = x$$, so $$f$$ should be fixed-point free (hence a derangement).

**Bernhard Reinke:**

if I am not mistaken, then 677 translates to $$ h = f(h f( h^{-1} f (h) f( f(h)^{-1}))) $$.

**Bernhard Reinke:**

Or in straight-line notation: if we denote the graph of $$f$$ by $$E$$, then we have
```math
(a,b) \in E \wedge (b^{-1},c) \in E \wedge (a^{-1}bc, d) \in E \Rightarrow (ad, a) \in E
```

**Bruno Le Floch:**

Is it clear that we need non-commutativity to get interesting 677 models?  It seems easier to explore if the carrier is simply a finite abelian group.

**Bernhard Reinke:**

For me it is not clear, but maybe it can help. Here is a naive exploration idea that doesn't really see the commutativity: we fix a finite group `G` (represented by its multiplication table and inverse function). We can try to construct a SAT problem with $$O(|G|^2)$$ variables and $$O(|G|^3)$$ clauses: basically, for each subterm of the equation that we consider, we have a |G|^2 many variables corresponding to the graph of the subterm (so for each subterm $$s$$ and $$g, h \in G$$, we have a variable $$s_{g,h}$$ corresponding to $$s(g) = h$$. For each multiplication in the equation, we have |G|^3 3-term clauses that correspond to $$ s_1(g) = h_1 \wedge s_2(g) = h_2 \Rightarrow s_1 s_2(g) = h_1 h_2$$. Similar, for function application we have |G|^3 3-term clauses corresponding to $$ s(g) = h_1 \wedge f(h_1) = h_2 \rightarrow (f \circ s)(g) = h_2 $$ (for inversion we only need |G|^2 2-term clauses). The equation itself gives us also 2|G|^2 clauses. Then we add that each subterm should be a function and $$f$$ should be a derangement, and then we ask a SAT solver whether this has a solution.

**Pace Nielsen:**

Unless I made a mistake, Vampire says that 677 does imply 255 subject to (1) left cancellativity and (2) right cancellativity => surjectivity of right multiplication.  I believe both conditions hold for finite models.  Here is the code I ran:
```
fof(eq677, axiom, X = mul(Y, mul(X, mul(mul(Y, X), Y)))).
fof(leftcanc, axiom, mul(X, Y) = mul(X, Z) => Y = Z).
fof(rtcanctosurj, axiom, (! [U, V, W] : mul(V, U) = mul(W, U) => V = W) => (! [Y, Z] : ? [X] : mul(X, Y) = Z)).
fof(eq255, conjecture, X = mul(mul(mul(X, X), X), X)).
```

Edited to add: Jose found the error below.

**Matthew Bolan:**

Why does right surjectivity hold for finite models?

**Pace Nielsen:**

I'm not assuming surjectivity of right multiplication.  I'm assuming that such surjectivity follows from injecitivty of right multiplication (which is true for finite models).

**Matthew Bolan:**

Ah, understood.

**Pace Nielsen:**

Just ran a sanity check, by simply assuming that right multiplication is not cancellative, and Vampire couldn't prove 255 in that case.  So, I'm thinking that something is wrong with that 3rd line (but I'm not sure what, since I've looked it over a few times now).

**Jose Brox:**

I think here there is the same mistake that I made with Prover9: in TPTP language, [quantification has higher precedence than binary connectives](https://tptp.org/UserDocs/TPTPLanguage/TPTPLanguage.shtml), so you need to move the parentheses to the inside of the formula.

**Jose Brox:**

`fof(rtcanctosurj, axiom, ! [U, V, W] : (mul(V, U) = mul(W, U) => V = W) => ! [Y, Z] : ? [X] : (mul(X, Y) = Z)).`

**Pace Nielsen:**

That fixed it.  Thanks Jose!

**Pace Nielsen:**

By the way (after that fix) Vampire is finding no problems with a (commutative or noncommutative) translation-invariant approach.

**Pace Nielsen:**

This might be a silly question, but what was the method used to disprove the implication 677 => 255 for infinite magmas?

**Matthew Bolan:**

It was among those resolved by the automated greedy algorithm.

**Matthew Bolan:**

There's some discussion about the nature of its greedy algorithm here: [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486686097)

**Jose Brox:**

Sorry, this message went under my radar until now! Yes, 677 with 359 implies 255 in the finite case. I attach the shortest proof I've been able to extract from Prover9 (it has 39 steps):

[attached: PROVER9 677 with 359 finite implies 255 PROOF.txt]

**Terence Tao:**

@Bruno Le Floch Thanks for explaining why the implication is immune to the cohomological method!  Disappointing of course - this looked like our best shot to finishing off the last implication - but at least we now have a satisfactory explanation for why the numerical implementation of the cohomological method was not working.

So now we need a new method.  Bernard is already proposing the translation invariant model, which seems to be the best option we currently have.  Regarding other constructions, I only have some largely negative results to report here.

1. One variant of the cohomological construction is a piecewise linear model $$(x,s) \diamond (y,t) = (x \diamond y, \alpha_{x,y} s + \beta_{x,y} t)$$.  Let's say the base is the order 5 model, then we have 50 unknowns here $$\alpha_{x,y}, \beta_{x,y}$$.  For idempotent $$x$$, $$\alpha_{x,x}, \beta_{x,x}$$ have to be coefficients of a linear model (and in particular will exhibit right cancellativity) but a priori there is no such requirement for off-diagonal coefficients $$\alpha_{x,y}, \beta_{x,y}$$.  On the other hand, 677 will force 50 separate quartic equations on these 50 unknowns, which is quite unappealing (with a translation invariant ansatz one can cut this down to 10 equations in 10 unknowns, which is still bad) but also would suggest there are only finitely many solutions in any given field, with no particular reason for any one of the $$\alpha_{x,y}$$ to vanish.  So the chance of getting a non-right-cancellative example here is slim. [EDIT: one can combine this model with the cohomological model to consider the more complex operation $$(x,s) \diamond (y,t) = (x \diamond y, \alpha_{x,y} s + \beta_{x,y} t + f(x,y))$$, but this doesn't add any capabilities - if we had such a model that was not right-cancellative, then we could set $$f=0$$ and already get a model that was not right-cancellative.]

2. Another option is the extension method: start with an existing model, e.g., a linear model $$M$$, and add a few elements to it with the hope of making a new model.  One cannot just add one element: if one adds a new element $$0$$ to an existing 677 magma $$M$$, then by left-invertibility we must have $$x \diamond 0 = 0$$ for all $$x \in M$$, which is not actually possible since by previous analysis for each $$x$$ the only possible solution to $$y \diamond x = x$$ is $$y = Sx \diamond x$$.  So the first available option is to add two elements $$0,1$$ to $$M$$ and impose the laws $$x \diamond 0 = 1$$, $$x \diamond 1 = 0$$ for $$x \neq 1,0$$.  If one can also assure that $$0 \diamond 0, 1 \diamond 0 \neq 0$$, say, then one is done, as now there is no solution to $$x \diamond 0 = 0$$.  So perhaps one could explore if an ATP thinks this is a viable approach?

**Jose Brox:**

Recall that together with 677 plus finiteness conditions it seems safe to assume one of the following list of
[*Spoiler: Additional properties — omitted*]
At first glance,
`513: x = y * (y * (y * (y * x)))`, `4591: (x * x) * x = (y * y) * y`, and `4599: (x * x) * y = (x * y) * y` seem particularly interesting to me. With the last two there are no countermodels up to size 13 (I'm running size 14 now). Also 4276, 4293, 4321, 4343 look similarly promising.

With 513, note that we can write the inverse of any left multiplication $$L^{-1}_x = L^3_x$$, and from $$y(x((yx)y)) = y(y(y(yx)))$$ we get $$x((yx)y) = y(y(yx))$$ and other interesting identities like
$$R_y x = L^3_{L^3_y x} L_y^2 x$$,
$$L_y x = L^2_y x(R_y L^3_y x)$$, and
$$x = L_yx(R_yL^2_y x)$$,
which may suggest an approach focused on the functions
$$A(x,y):=L_y x, B(x,y):=L^2_y x, C(x,y):=L^3_y x.$$

**Bernhard Reinke:**

Oh well, that is too bad. Do you mind sharing the final tptp file you used for this?

**Pace Nielsen:**

Oh, I realized I made an error.  After the fix, Vampire is finding no problem with a carrier group for a translation-invariant model to be commutative of exponent 3.

**Terence Tao:**

More negative progress: my proposal to have two elements $$0,1$$ with $$x \diamond 0 = 1, x \diamond 1 = 0$$ for $$x \neq 0,1$$ won't work.  If a 677 magma has more than 5 elements we can find $$x \neq 0, 1, 0 \diamond 0$$ such that $$0 \diamond x \neq 0,1$$.  On the other hand, 677 gives $$x = 0 \diamond (x \diamond ((0 \diamond x) \diamond 0))$$ which simplifies using the given hypotheses to $$x = 0 \diamond 0$$, contradiction.

More generally this suggests that taking an existing 677 magma and adding a small number of elements to it is unlikely to be possible once the base magma is moderately large.

**Terence Tao:**

Recording another failed approach as a negative result.  If one defines $$f(x,y) := (y \diamond x) \diamond y$$, then 677 can be written as $$x = y \diamond (x \diamond f(x,y))$$.  So, using left cancellativity, one can describe the relation between $$\diamond$$ and $$f$$ by two axioms:

1.  If $$y \diamond x = z$$, then $$z \diamond y = f(x,y)$$.
2. If $$y \diamond z = x$$, then $$x \diamond f(x,y) = z$$.

So I tried first choosing the function $$f: M \times M \to M$$, and seeing if one could build a magma operation $$\diamond$$ that obeyed Axiom 1 and Axiom 2 for that choice of $$f$$.  The point is that the axioms are rather simple: both axioms assert that one entry in the multiplication table propagates to another.  The problem is that these axioms don't commute, and in principle after N applications of these axioms, a single entry $$y \diamond x = z$$ on the table can propagate into 2^N other entries, leading almost certainly to collisions.  One somehow wants to choose an $$f$$ with a special property that the propagation rules of Axiom 1 and Axiom 2 (i.e., the functions $$(y,x,z) \mapsto (z,y,f(x,y))$$ and $$(y,z,x) \mapsto (x,f(x,y),z)$$) obey a lot of algebraic relations that cuts down on this complexity, but setting $$f$$ to be too simple (e.g., constant) quickly leads one to violate the requirement that each entry of the multiplication table has a unique answer.  Of course, because we have linear models, we know that it is possible to satisfy both of these axioms with a linear choice of $$f$$; I tried a little bit with the scenario in which $$f$$ stays linear but we allow for nonlinear $$\diamond$$, but didn't make much headway there. (Also, if $$f$$ is right-cancellative then $$\diamond$$ will be also, since we already have left-invertibility, so even if I did make a non-linear model out of this, it still wouldn't refute 255.)

**Ben Gunby-Mann:**

Possibly interesting to note (not hard to show but on my phone now) is that 677+513 has no nontrivial commutative linear models. So *any* nontrivial model of both of these simultaneously will be something new!

EDIT: Not true; this has the solution $$x*y=2x-y$$ in any commutative ring of characteristic 5; however, these are the only linear solutions in commutative integral domains; see correction below.

**Jose Brox:**

EDITED: Already running in sizes 13 and 14 :fingers_crossed:

**Giovanni Paolini:**

I used Gurobi to look for translation-invariant 677 models of the form $$x \diamond y = x + f(y-x)$$ on $$\mathbb{Z}_n$$ for $$n \leq 16$$ (not sure if these are ruled out by previous considerations).

For an arbitrary (bijective) $$f \colon \mathbb{Z}_n \to \mathbb{Z}_n$$, such models exist only for $$n=5$$ and $$n=11$$; and the known linear models have this form, with $$f(x) = -x$$ on $$\mathbb{Z}_5$$ and $$f(x) = 6x$$ on $$\mathbb{Z}_{11}$$.

By additionally imposing that $$f$$ has no fixed point, there is no such model at all for $$n \leq 16$$.

**Zoltan A. Kocsis (Z.A.K.):**

The [model-unique 5x5 model] of 677 already satisfy 513, Said model is also linear over $$\mathbb{Z}/5\mathbb{Z}$$, with $$x \diamond y = 2x + 4y$$. So the "nontrivial" clause says that this is the only linear model of 677+513, right?

**Ben Gunby-Mann:**

Ack, you’re right of course. I accidentally did it as if beta is a primitive 5th root of unity in case 1, instead of the negative of that.

I think the correct statement you get from taking linear combinations of the polynomials is that the only nontrivial commutative linear models are Type 1 models in characteristic 5 (which must be of the form 2x-y, as you said).

**Terence Tao:**

More negative results: the implication is immune not only to the cohomological extensions $$(x,s) \diamond (y,t) = (x \diamond y, \alpha s + \beta t + f(x,y))$$, but even to the more general piecewise affine extensions $$(x,s) \diamond (y,t) = (x \diamond y, \alpha_{x,y} s + \beta_{x,y} t + f(x,y))$$, at least when extending by a field.   Given $$(y,t)$$,  we know that to solve 255, we need to find $$(x,s)$$ such that $$(x,s) \diamond (y,t) = (y,t)$$.  Assuming the base already obeys 255, we can find $$x$$ such that $$x \diamond y = y$$, and then we are done unless $$\alpha_{x,y}$$ vanishes, so that $$(x,s) \diamond (y,t')$$ is independent of $$s$$.  But in that case, we apply 677 to see that for any $$s$$ one has
$$ (y,0) = (x,s) \diamond ((y,0) \diamond (((x,s) \diamond (y,0)) \diamond (x,s)))$$
and use the aforementioned invariance (and the fact that $$y \diamond ((x \diamond y) \diamond x)) = y$$ when $$x \diamond y = y$$,  by left cancelling $$x \diamond y = y = x \diamond (y \diamond ((x \diamond y) \diamond x)))$$) to conclude that
$$ (y,0) = (x,0) \diamond ((y,0) \diamond (((x,0) \diamond (y,0)) \diamond (x,s)))$$
but this contradicts left-invertibility.

**Ben Gunby-Mann:**

To be explicit about this, 513 implies that for commutative linear models $$a(b^3+b^2+b+1)=0$$ and $$b^4=1$$, so as long as we're in an integral domain, either we have the model $$y*x=x$$ (which doesn't satisfy 677) or $$b^3+b^2+b+1=0$$. In case 2, b is both a root of $$x^3+x^2+x+1$$ and $$x^4+x^3+2x^2+2x+1$$, and since $$(x^2+1)(x^3+x^2+x+1)-x(x^4+x^3+2x^2+2x+1)=1$$ the model must be trivial. However, in case 1 we have $$x^3+x^2+x+1=0$$ and $$x^4-x^3+x^2-x+1=0$$, which has solutions only over characteristic 5 (similarly, $$(2x^3-4x^2+x+2)(x^3+x^2+x+1)-(2x^2-3)(x^4-x^3+x^2-x+1)=5$$). In characteristic 5, $$x^4-x^3+x^2-x+1=(x+1)^4$$, so again if we are in an integral domain the only root is $$x=-1$$, and we are left with the solution $$x\diamond y=2x-y$$, as mentioned. So this is the only linear solution in a commutative integral domain. Not sure what happens if we drop either the commutativity or the integral domain condition, though.

Possibly also interesting here is 4599, which @Jose Brox mentioned. It has no nontrivial models which are both left- and right-cancellative (as then $$L_xR_yx=L_xR_yy$$ would imply $$x=y$$), so this actually *does* have the property that any nontrivial model of both 677 and 4599 together would be something notably new.

**Jose Brox:**

Reporting some "fieldwork":
1) The only other equations (up to 4694) that can be added to 677+513 without provably implying 255 are:
- 411 `x = x * (x * (x * (x * x)))`, which is just 513 with $$y=x$$.
- 4380  `(x * x) * x = x * (x * x)`, which is implied by 677+513 (put $$y=x$$ and cancel on the left twice).
- 3659 `x * x = (x * x) * (x * x)`, which doesn't seem to be implied by 677+513 (plus left bijectivity and $$yx=x$$ not always solvable), survives 30min in Prover9.

I have checked 677+513+3659 (plus left bijectivity) against 255 with Prover9, Vampire, and Vampire in CASC mode, for 30min each without getting a proof, so it seems a safe combination to take.

2) We also know that a model of 677+513 against 255 must have size at least 14 [UPDATED].

3) Other idea I have tried: I have looked at models of 513 against 255, and it turns out that they allow "complete failure" of right injectivity, i.e., there are models satisfying $$xy = zy$$. As we already know this doesn't work with 677, and neither does it if all rows of the multiplication table are equal but one; but if it is all rows but two, 
```all x all y all z ((x!=0 & x!=1 & z!=0) -> x*y = z*y),```
then the problem 677+513+3659+most rows equal (with left bijectivity) survives 30min in Prover9 (I'm looking for models of size 13 now).

(Deleted, silly comment)

4) On the other hand, 577+4599 against 255 (plus the extra clauses) progresses faster: any model must have size at least 17. This is somewhat suspicious, as problems that exhaust sizes quick tend to don't actually  have models (i.e., the implication can be proven in those cases), but the progress is not *that* fast. In any case, I have tried to prove the implication without success for 30min with Vampire and Vampire-CASC (but Vampire in normal mode exits quickly, only saying "killed" :melting_face: ), and for 3h in Prover9 (still running, just in case).

**Terence Tao:**

I managed to convert the greedy construction of a 677 magma into a Kisielewicz type model (which I believe to in fact be a free 677 magma (or at least contain such a free magma as a submagma), though I have not proved this).  Unfortunately, it is infinite and I see no way to convert it to a finite model, but I report it here in case it somehow is helpful.

The carrier $$M$$ is the positive integers $$\{1,2,3,\dots\}$$.  We will build the multiplication table recursively, one row at a time: thus to define $$x \diamond y$$ for a given $$y$$ we assume that $$x' \diamond y'$$ has already been defined for all $$y' < y$$.  The multiplication rule is then

**Rule**.   If $$x < y = 2^z 3^{(x\diamond z) \diamond x}$$ for some $$z \in M$$, then $$x \diamond y = z$$.  Otherwise, $$x \diamond y = 2^x 3^y$$.

Note that there is only one possible choice of $$z$$ that can be assigned to $$x \diamond y$$ in the former case (namely, the number of times $$2$$ divides $$y$$).  Also, by construction in that case $$z$$ and $$x$$ are both less than $$y$$, so to evaluate the rule one only needs to compute products $$x' \diamond y'$$ with $$y' < y$$.  So the rule is recursively well defined. Intuitively, for "most" $$x,y$$, $$x \diamond y = 2^x 3^y$$ will be larger than $$x,y$$ and "remember" all the information about $$x$$ and $$y$$ (this is a capability that only seems possible in infinite models), but for some exceptional $$x,y$$, $$x \diamond y$$ will be smaller than $$y$$, and return the number of times $$2$$ divides $$y$$ instead.  Because of this, $$y \diamond (x \diamond w)$$ can become $$x$$ for certain $$x,y,w$$ (and specifically $$w$$ of the form $$(y \diamond x) \diamond y$$, which is where 677 will come from.

From definition we have the following property:

**Lemma 1**:  For any $$x, y \in M$$, we either have $$x, y < x \diamond y = 2^x 3^y$$, or $$x, x \diamond y < y = 2^z 3^{(x \diamond z) \diamond x}$$ with $$z := x \diamond y$$.  In particular, in both cases we have $$x < \max( y, x \diamond y )$$.

From this and a somewhat involved case analysis we have

**Lemma 2**: For any $$x,  y \in M$$, we have $$x \diamond ((y \diamond x) \diamond y)) = 2^x 3^{(y \diamond x) \diamond y}$$.

**Proof**: Write $$ z := y \diamond x$$, $$w := z \diamond y$$, and $$u := x \diamond w$$, then we wish to show $$u = 2^x 3^w$$.  Suppose for contradiction this were not the case, then by Lemma 1 we have $$x < w = 2^u 3^{(x \diamond u) \diamond x}$$.  From Lemma 1 again we have $$y < \max(x, y \diamond x) = \max(x,z) \leq \max(x,w )$$ and $$z < \max(y, z \diamond y) = \max( y, w )$$, hence $$y < w$$.  Since $$w=z \diamond y$$, we conclude from Lemma 1 that $$w = 2^z 3^y$$; comparing with our previous formula for $$w$$, we conclude $$u=z$$ and $$y = (x \diamond z) \diamond x$$.  From Lemma 1 we have $$x < \max(z,x \diamond z)$$, $$x \diamond z < \max(x,(x \diamond z) \diamond x)=\max(x,y)$$, and $$y < \max(x,y \diamond x)=\max(x,z)$$.  Thus only $$z$$ can be the largest of $$x, y, z, x \diamond z$$, so $$y < y \diamond x = z$$ and hence $$z = 2^y 3^x$$ by Lemma 1.  Since $$x \diamond z < z = 2^y 3^x$$ we then have $$x \diamond z = y$$ by Lemma 1, hence $$y = (x \diamond z) \diamond x = y \diamond x$$, contradicting Lemma 1. $$\Box$$

**Remark**: the ability to prove this lemma roughly corresponds to the ability to close the greedy argument when constructing 677 magmas, where in both cases the point is that no "unexpected collisions" show up to derail things.

Now we can verify 677:

**Lemma 3**:   For any $$x,y$$ we have $$y \diamond (x \diamond ((y \diamond x) \diamond y)) = x$$.

**Proof**: By Lemma 2 and the multiplication rule, it suffices to show that $$y < 2^x 3^{(y \diamond x) \diamond y}$$.  From Lemma 1 we have $$y<\max(x,y \diamond x)$$ and $$\max(y \diamond x) < \max(y, (y \diamond x) \diamond y)$$, hence $$y < \max(x, (y \diamond x) \diamond y)) < 2^x 3^{(y \diamond x) \diamond y}$$, as required. $$\Box$$

From Lemma 1 we have $$x \diamond y \neq y$$ for all $$y$$, so in particular 255 fails in this model.

**Giovanni Paolini:**

I continued the search for translation-invariant 677 models of the form $$x \diamond y = x f(x^{-1} y)$$, as suggested by @Bernhard Reinke, across all groups of order up to 17. Aside from the previously identified cases, namely $$\mathbb{Z}_5$$ and $$\mathbb{Z}_{11}$$, only $$\Z_2 ^4$$ supports such models. In addition, for all such models, $$f$$ has a fixed point (so 255 holds).

This is an example of a translation-invariant 677 model over $$\Z_2^4$$:
[0, 4, 14, 10, 2, 6, 12, 8, 5, 1, 11, 15, 7, 3, 9, 13]                             
[5, 1, 11, 15, 7, 3, 9, 13, 0, 4, 14, 10, 2, 6, 12, 8]
[12, 8, 2, 6, 14, 10, 0, 4, 9, 13, 7, 3, 11, 15, 5, 1]                                                                                                                 
[9, 13, 7, 3, 11, 15, 5, 1, 12, 8, 2, 6, 14, 10, 0, 4]                             
[6, 2, 8, 12, 4, 0, 10, 14, 3, 7, 13, 9, 1, 5, 15, 11]                  
[3, 7, 13, 9, 1, 5, 15, 11, 6, 2, 8, 12, 4, 0, 10, 14]                             
[10, 14, 4, 0, 8, 12, 6, 2, 15, 11, 1, 5, 13, 9, 3, 7]             
[15, 11, 1, 5, 13, 9, 3, 7, 10, 14, 4, 0, 8, 12, 6, 2]                             
[13, 9, 3, 7, 15, 11, 1, 5, 8, 12, 6, 2, 10, 14, 4, 0]                             
[8, 12, 6, 2, 10, 14, 4, 0, 13, 9, 3, 7, 15, 11, 1, 5]                                                                                                                 
[1, 5, 15, 11, 3, 7, 13, 9, 4, 0, 10, 14, 6, 2, 8, 12]                             
[4, 0, 10, 14, 6, 2, 8, 12, 1, 5, 15, 11, 3, 7, 13, 9]                             
[11, 15, 5, 1, 9, 13, 7, 3, 14, 10, 0, 4, 12, 8, 2, 6]                             
[14, 10, 0, 4, 12, 8, 2, 6, 11, 15, 5, 1, 9, 13, 7, 3]                             
[7, 3, 9, 13, 5, 1, 11, 15, 2, 6, 12, 8, 0, 4, 14, 10]                             
[2, 6, 12, 8, 0, 4, 14, 10, 7, 3, 9, 13, 5, 1, 11, 15]

In this example, the permutation $$f$$ is a product of three 5-cycles:
$$f$$ = (0)(1 4 2 14 9)(3 10 11 15 13)(5 6 12 7 8).
The elements of $$\Z_2 ^4$$ are indexed in such a way that the group operation is the bit-wise sum mod 2. In particular, the five elements in each cycle have sum 0. All of this strongly suggests that we are in fact looking at a linear model over $$\mathbb{F}_{16}$$, with $$f$$ acting as multiplication by a 5-th root of unity, though I have not checked it.

Interestingly, the time taken by Gurobi to prove non-existence of models differs significantly across the remaining groups of order 16: 7 groups are "hard" (~1 hour), 5 are "easy" (< 2 minutes), and 1 is "intermediate" (~10 minutes).

**Jose Brox:**

This doesn't work: already with 2 rows equal, there seems to be no finite models (we can go up to size 100 quickly). The fact that a proof is not found probably means that there are infinite models satisfying the property.

5) A similar, interesting thing happens with 4343 `x(yy) = y(xx)`:
There are no models of 4343, left bijectivity and $$yx=x$$ not always solvable up to size at least 237 :scream: ... (this is true even without 677!) ...

...but Vampire-CASC says that the problem is satisfiable (even when a bunch of finiteness conditions are thrown in), what points to the existence of infinite models.

Is there some clear reason why this is the case, why imposing $$xy^2 = yx^2$$ together with left bijectivity forces a solution $$y$$ to $$yx = x$$ for all $$x$$ in the finite case? 

(NOTE: The model search is so fast thanks to choosing selection_measure 1 in Mace4, so it could be interesting to replicate the Mace4 process in this case and see why the multiplication table is so easily seen to be impossible to fill with these conditions. Vampire's finite model builder is also fast, but slower than Mace4 with this configuration).

**Jose Brox:**

Not sure if this is interesting, but I've looked for $$f$$ in the form of another magma expression. The only one in 2 variables up to degree 4 that doesn't seem to get the implication to 255 is $$f(x,y) := ((xx)y)y$$. I have checked that there are no models of 677+$$(yx)y = ((xx)y)y)$$ against 255 up to size 13 (included).

In degree 5 we have 64 candidates that stand against 255 for 1min in Prover9:
[*Spoiler: candidates — omitted*]
I haven't run the search for degree 6 or higher, but if we impose 513, since then $$L^{-1}_x = L^3 x$$, from equating 513 to 677 through $$x$$ we get
$$(yx)y = x(x(x(y(y(yx))) = L^3_xL^3_y x$$.

**Douglas McNeil:**

Given the size of counterexamples lately it's hard to put too much weight on the resistance this one's putting up, but am I the only one wondering if this one's actually true?

Are there properties of finite magmas we haven't invoked yet, or consequences of them that ATPs would have trouble detecting?

**Zoltan A. Kocsis (Z.A.K.):**

Okay, I have some questions at this point.
The possibility that 677 has very few models in general seems like a major obstacle to me, especially when trying search based approaches. If 677 has only, say, 6 models of order $$\leq 13$$, then the fact that our searches fail to find models of certain combinations if equations really doesn't tell us much.

I wish I could confirm my hunches myself, but the thread has grown too long to search efficiently given my current time constraints, and I suspect that many of you have tacit knowledge not written up here, so I think I'll ask a series of questions instead.  Hopefully, the answers will help refine the main axis of effort instead of just satisfying my personal curiosity.

1. Do we know *any* finite models of 677 that are not outright cancellative? If not, do we have proof (or at least some heuristic) telling us not to expect such models? NB if we cannot expect such models, then imposing 4599 and similar equations whose models tend to be very  noncancellative is perhaps not that promising.
2. Do we know *any* finite models of 677 that have even order? If not, do we have reason not to expect such models?
3. Do we know two non-isomorphic finite models of 677 that have the same order? If not...
4. How many different models do we know? How many models of order less than 15?

**Matthew Bolan:**

For question 2, there are linear models of even order, for example over $$F_{16}$$. The answer to question 3 is yes, for example there are two non-isomorphic linear models of order 7. For question 4, AFAIK we only know linear models and cohomological extensions of linear models, and I think there are only linear models known below order 15. I'd have to check which linear models are isomorphic in order to give an exact count.

**Zoltan A. Kocsis (Z.A.K.):**

Technically, proofs that some implication always holds in a finite magma can be arbitrarily difficult (which doesn't mean that we should expect *this particular problem* to be difficult; indeed, I don't think this one's true). One could look up famous such proofs ([starting with Artin-Zorn perhaps?](https://en.wikipedia.org/wiki/Artin%E2%80%93Zorn_theorem)) to see what sorts of properties they invoke, and whether we're missing any of them.

**Bruno Le Floch:**

**Summary of what we know.**
- All known finite models are linear or [cohomological extensions thereof](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486840636), [typically nonlinear](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488751388).
- [List of linear models on Z/pZ for primes p up to 500.](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486395178)  More general (e.g., non-commutative) [linear models are mostly understood](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486431381).
- 677 implies left-cancellative.  Finite linear 677 [implies right-cancellative](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486592632) too.  Cohomological extensions [keep cancellativity](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488063585). 677 and cancellativity implies 255.
- Assuming 677, [equation 255 is equivalent to `∀x ∃y y*x=x`](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486686097).  Piecewise affine extensions $$(x,s)\diamond(y,t)=(x\diamond y,\alpha_{x,y}s+\beta_{x,y}t+f(x,y))$$ **by a field** preserve that property so [cannot produce counterexamples](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488539534).
- [677 is incompatible with `0!=1∧∀y,y*1=0`](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486697932) —also incompatible with `0!=1∧∀y,(y=1 or y*1=0)` by a quick prover9 run I just did and [also with `∀x(x=0 or x=1 or (x*0=1 and x*1=0))`](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488154964).
- [677 together with any of {411,513,623,...} does not imply 255.](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488137777) —particular interest for 513 combined with translation-invariance ([no new model for n≤16](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488518385)) or with 3659.
- [Some hope to use translation-invariant models.](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488106580)
- Some inconclusive usage of [rule sets](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486687134) and a concrete Kisielewicz type [infinite counterexample](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488718563).
- [An idea of using a relaxed base magma.](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486690215).

**Bruno Le Floch:**

Some other equations with very few finite models seem to have a good reason for that.  The cardinal of finite central groupoids must be a square because the square of the adjacency matrix is an all-1 matrix.  For weak central groupoids we have a conjecture that the cardinal is a square or twice a square.  Is there anything special about the cardinal of 677 models, or the size of cosets, etc?

For $$y\in R_v^{-1}(u)$$, namely $$y*v=u$$, we have $$y*v = u = y*(u*((y*u)*y))$$ hence $$(y*u)*y = L_u^{-1} v$$, which is $$y$$-independent.  For any $$y\neq z\in R_v^{-1}(u)$$, we get $$(y*u)*y = (z*u)*z \neq (z*u)*y$$ by left-cancellativity, so the map $$R_y\circ R_u\colon R_v^{-1}(u)\to\mathrm{im}(R_y)$$ is injective.  In particular, $$\mathrm{im}(R_y)$$ has at least as many elements as $$R_v^{-1}(y*v)$$ for any $$y,v$$.  This generalizes the incompatibility with `0!=1∧∀y,y*1=0` because $$R_1^{-1}(y*1)=M$$ so all $$R_y$$ have to be surjective, which is wrong for $$y=1$$.  But it does not capture the other related incompatibilities listed in my previous post.  There is probably something more conceptual tracking the whole set of $$\mathrm{im}(R_y)$$ and $$R_v^{-1}(w)$$.

**Matthew Bolan:**

It is very likely that the cohomological extensions are not linear I think. If they are it's probably good to know, as it means that something about 677 really is forcing linearity. I'd be very surprised if even the first example in my file, [model-this order 25 magma] , were linear.

**Matthew Bolan:**

I'll also comment that 1076 has very few finite models, but I am not aware of a good reason for this.

**Terence Tao:**

One consequence of linearity is that the operators $$L_y L_{y'}^{-1}$$, being translations, commute with each other and with the $$R_x R_{x'}^{-1}$$ (assuming right invertibility in the latter case).  So this may be one test to verify if a given magma is linear or not.

**Matthew Bolan:**

Hmm, the order 25 one can't be proven non-linear by that test, so perhaps it is some linear model over $$F_{5^2},$$ after all $$H^2$$ is only one dimensional in that case. Other models in the file are able to be proven non-linear via that method though.

**Matthew Bolan:**

[model-This model is not linear], $$L_0 L_7^{-1} L_0 L_{14}^{-1}(14) \not = L_0 L_{14}^{-1} L_0 L_{7}^{-1}(14)$$

**Bruno Le Floch:**

I was a bit quick concerning the piecewise affine models: Terry Tao's argument only proves immunity to piecewise affine extensions by a field.  I don't see how to rule out a case where $$\alpha_{x,y}$$ would be non-invertible but non-zero.  I've edited my summary above to reflect that information.  This is one of our best hopes.  In particular the proof that finite linear 677 [implies cancellative](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486592632) clearly does not go through when you have multiple $$\alpha$$ and $$\beta$$.

**Terence Tao:**

I guess I should share some inconclusive attempts to study these sorts of extension models then.  We know that the base should contain non-idempotents, so the order 5 magma isn't a useful base; it's the two order 7 models that offer the first shot at some non-trivial constructions.  I'll arbitrarily choose the model $$x \diamond y = 4x + 3y$$ on $${\mathbb Z}/7{\mathbb Z}$$ (the other model $$x \diamond y = 4x + y$$ has broadly similar behavior).  One could consider general extension models $$(x,s) \diamond (y,t) = (4x+3y, s \diamond_{x,y} t)$$ on carrier $${\mathbb Z}/7{\mathbb Z} \times M$$ for some binary operations $$\diamond_{x,y}: M \times M \to M$$ to be chosen later.  The rule 677 then becomes
$$  s = t \diamond_{y,5x+y} ( s \diamond_{x, 5y+5x} ( (t \diamond_{y,x} s ) \diamond_{4y+3x,y} t )$$
for all $$x,y \in {\mathbb Z}/7{\mathbb Z}$$ and $$s,t \in M$$.  This is 49 equations involving 49 different binary operations - not appetizing!  However, the $$x=y=0$$ case doesn't interact with any other case, and is just saying that $$0 \times M$$ is a submagma of $${\mathbb Z}/7{\mathbb Z} \times M$$.  As for the other 48 cases, one can impose a projective symmetry $$\diamond_{x,y} = \diamond_{y/x}$$ where $$y/x$$ takes place in the projective line $${\mathbb Z}/7{\mathbb Z} \cup \{\infty\}$$ with the convention that $$y/0=\infty$$ for any non-zero $$y$$.  Then we get to divide by six, and end up with eight equations in eight unknowns $$\diamond_0,\dots,\diamond_6, \diamond_\infty$$, of the form
$$  s = t \diamond_{5x+1} ( s \diamond_{(5/x)+5} ( (t \diamond_{x} s ) \diamond_{1/(3x+4)} t )$$
for $$x = 0,\dots,6,\infty$$.  More explicitly, one has
$$  s = t \diamond_{1} ( s \diamond_{\infty} ( (t \diamond_{0} s ) \diamond_{2} t )$$
$$  s = t \diamond_{6} ( s \diamond_{3} ( (t \diamond_{1} s ) \diamond_{\infty} t )$$
$$  s = t \diamond_{4} ( s \diamond_{4} ( (t \diamond_{2} s ) \diamond_{5} t )$$
$$  s = t \diamond_{2} ( s \diamond_{2} ( (t \diamond_{3} s ) \diamond_{6} t )$$
$$  s = t \diamond_{0} ( s \diamond_{1} ( (t \diamond_{4} s ) \diamond_{4} t )$$
$$  s = t \diamond_{5} ( s \diamond_{6} ( (t \diamond_{5} s ) \diamond_{3} t )$$
$$  s = t \diamond_{3} ( s \diamond_{0} ( (t \diamond_{6} s ) \diamond_{1} t )$$
$$  s = t \diamond_{\infty} ( s \diamond_{5} ( (t \diamond_{\infty} s ) \diamond_{0} t )$$
(if I did not make any mistakes).  Note that the most important case here for the purposes of testing 255 is when $$x \diamond y = y$$, so that $$y/x = 5$$ and so one is interested in seeing whether the equation $$t \diamond_5 s = s$$ admits solutions for every $$s$$.  The equation
$$  s = t \diamond_{5} ( s \diamond_{6} ( (t \diamond_{5} s ) \diamond_{3} t )$$
together with the left-cancellability of $$\diamond_6$$ and $$\diamond_3$$ will tell us that one cannot have $$t \diamond_5 s$$ depend only on $$s$$; there has to be some $$t$$-dependence, which in the case of piecewise linear models over a field implies solvability and hence 255.  (This is what led me to my previous result about how the implication is immune to piecewise linear models extending by a field.)  In fact this argument tells us for linear models $$s \diamond_5 t = \alpha_5 s + \beta_5 t + f(5)$$ that the kernel of $$\alpha_5$$ can at most be the cardinality of the square root of the cardinality of $$M$$.

One could just write down the linear ansatz $$s \diamond_x t = \alpha_x s + \beta_x t$$ (ignoring for now any lower order term $$f(x)$$) and try to solve the resulting system of sixteen quartic equations in sixteen non-commutative unknowns, but I don't know if this is even computationally feasible.  We do have the known solutions where $$\alpha_x = \alpha$$, $$\beta_x = \beta$$ is independent of $$x$$ and solves the original system of equations, but this is presumably only a small subset of all possible solutions here.

One amusing thing about the above system is that $$\diamond_4$$ only appears in two equations:
$$  s = t \diamond_{4} ( s \diamond_{4} ( (t \diamond_{2} s ) \diamond_{5} t )$$
$$  s = t \diamond_{0} ( s \diamond_{1} ( (t \diamond_{4} s ) \diamond_{4} t ).$$
This raises the possibility that this particular operation is more "mutable" than the others, and one could create models in which all the other $$\diamond_x$$, $$x \neq 4$$ are standard operations (e.g., a standard linear model $$s \diamond_x t = \alpha s + \beta t$$) and $$\diamond_4$$ is modified from the linear model.  On the other hand, since 255 concerns $$\diamond_5$$ rather than $$\diamond_4$$, such modifications don't actually bring us any closer to refuting 255.

I wish we had a simpler model to play with than the above system of eight equations.  If the base magma was translation-invariant then we could play with a translation-invariant model instead of a projection-invariant one, but the translation-invariant models that I know of are all idempotent and therefore not useful to us.

**Bruno Le Floch:**

A curious ramification.  Linear models $$x\diamond y=ax+by+c$$ over Z/pZ (p prime) are nicely classified between type 1 with $$a=1-b$$ and $$b$$ a primitive 10th root of unity and $$c=0$$, and type 2 with $$b^4+b^3+2b^2+2b+1=0$$ and $$a=-b^3-b-1$$ and $$a^2+a+1=0$$ and arbitrary $$c$$.  The parameter $$c$$ can be set to zero by shifting magma elements $$x\to x+(a+b-1)^{-1}c$$ in all models except one which is both of type 1 and 2, namely $$x\diamond y=5x-4y+c\mod 31$$.  This number comes from $$\gcd(b^4-b^3+b^2-b+1, \  b^4+b^3+2b^2+2b+1)=31$$.  That might be a hint to this case being slightly more flexible than usual linear models.  In particular it is a **non-idempotent translation-invariant model.**  That said, it is big, so I'm not sure it is an improvement over the 7-element magmas as a base.

**Terence Tao:**

Thanks for this.  Taking for instance $$x \diamond y = 5x - 4y + 1 \hbox{ mod } 31$$ (I think all other non-constant choices of $$c$$ can be rescaled to this one and taking the translation-invariant ansatz $$\diamond_{x,y} = \diamond_{y-x}$$, I get a system of 31 equations in 31 unknown operations $$\diamond_h, h \in {\mathbb Z}/31{\mathbb Z}$$:

$$ t = s \diamond_{23h-23} (t \diamond_{10h+6} ((s \diamond_h t) \diamond_{4h-1} s)$$

for $$h \in {\mathbb Z}/31{\mathbb Z}$$.  To solve $$x \diamond y = y$$ requires $$y = x + 25$$ on the base, so one is interested in seeing whether $$s \diamond_{25} t = t$$ is solvable for each $$t$$.  For this choice of $$h$$ we have $$23h-23 = h = 25$$ so the previous argument blocking $$s \diamond_{25} t$$ from being independent of $$s$$ still applies.

I don't see an obvious further structure here to reduce the complexity of a system of 31 equations in 31 unknowns while still having a decent chance at solvability.  One could maybe consider an ansatz $$s \diamond_h t = \alpha_h s + \beta_h t$$ where the $$\alpha_h, \beta_h$$ vary linearly in $$h$$ (in some field of characteristic 31), but I think this creates 8 equations in 4 unknowns, so very unlikely to be solvable.

**Bruno Le Floch:**

Your projective model is more promising than the 31 equation one.  I've checked that your set of 8 equations for the projective model is correct.  A commutative linear version of that ($$s\diamond_x t=\alpha_x s+\beta_x t$$) is not ruled out I think?

It might be barely tractable.  The equations are of the form $$(\alpha+\alpha\beta\beta)\beta=1$$ and $$\alpha+(\alpha\alpha+\beta)\beta\beta=0$$ with various indices.  The first type of equations give invertibility of $$\beta$$ and can be solved for $$\alpha$$ assuming that $$\beta_0\beta_1\beta_2\beta_3\beta_4\beta_5\beta_6\beta_\infty$$ differs from $$\beta_3/\beta_4$$ and from $$\beta_4/\beta_3$$. (If we decide to violate that, then we get two free $$\alpha$$ but two constraints on $$\beta$$ from this set of equations.)  The second set of eight equations becomes 25th-degree polynomials in $$\beta$$ with a total of 210 terms, but at least we only have $$8$$ variables left.

Surprisingly, the equations are invariant under scaling $$\beta_0,\alpha_\infty$$ by some factor and $$\beta_1,\alpha_1$$ by the inverse factor, so we can normalize $$\beta_0=1$$.  There are also some discrete scalings of other $$\alpha,\beta$$ by fourth roots of unity.

**Bruno Le Floch:**

**Ah, nooo!! :sad: ** Yet another immunity, this time to **all (finite) piecewise affine extensions** of the kind we consider here, so $$(x,s)\diamond(y,t)=(x\diamond y, \alpha_{x,y} s + \beta_{x,y} t + \gamma_{x,y})$$.  Namely, if the base magma obeys 255 the extension also does.

Pick some $$(y,t)$$.  By 255 on the base we have some $$x$$ with $$x\diamond y=y$$, so $$x\diamond(y\diamond((x\diamond y)\diamond x))=x\diamond y$$ hence $$y\diamond((x\diamond y)\diamond x)=y$$ as we already observed.  Then equation 677 implies
```math
t = s\diamond_{x,y} \bigl(t\diamond_{\dots}((s\diamond_{x,y} t)\diamond_{\dots} s)\bigr)
```
where dots denote unimportant indices.  Crucially, the same left-multiplication map $$s\diamond_{x,y} (\dots) = \alpha_{x,y}s + \dots$$ appears twice.  If $$\alpha_{x,y}\in\mathrm{End}(M)$$ is not injective, then two different $$s$$ (say, $$s_1,s_2$$) will have equal left-multiplications, but then we can cancel all these by left cancellativity so eventually $$s_1=s_2$$.  Thus $$\alpha_{x,y}$$ is injective.  By finiteness, it is surjective, so there exists $$s$$ such that $$(x,s)\diamond(y,t)=(y,t)$$.  Namely 255 holds.

I think this kills any hope based on anything linear.  Are there some extra twists that I forgot to account for?

I'm starting to think that the implication might hold.  Maybe we should try to track how much information $$w\mapsto L_w$$ has.  It must not be too invertible nor too forgetful.

**Terence Tao:**

Wow, that's a pretty strong immunity.  Well, I'm glad you found it before we decided to set up a massive calculation that was doomed to fail...

For the more general extension models $$(x,s) \diamond (y,t) = (x \diamond y, s \diamond_{x,y} t)$$, what this shows is that whenever $$x \diamond y = y$$, the left multiplication maps $$L^{x,y}_s: t \mapsto s \diamond_{x,y} t$$ have to depend injectively on $$s$$:  $$L^{x,y}_s = L^{x,y}_{s'} \iff s =s'$$.  In piecewise affine models, these left multiplication maps are translations (composed with a fixed invertible map), so injectivity and finiteness forces all translations to be attained, and then we can solve $$s \diamond_{x,y} t = t$$.    So if we want to keep an extension model, these left multiplication maps have to be genuinely more complicated than translations, but then it's much less likely that the required equations are going to hold.

Another way of thinking about it: one feature of linear models $$\diamond_{x,y}$$ is that if $$L^{x,y}_s, L^{x,y}_{s'}$$ agree at one location, they in fact agree at all locations: $$s \diamond_{x,y} t = s' \diamond_{x,y} t \implies s \diamond_{x,y} t' = s' \diamond_{x,y} t'$$.  [Geometrically: two lines of the same slope are either parallel or identical.] So injectivity of $$s \mapsto L^{x,y}_s$$ implies injectivity of $$s \mapsto L^{x,y}_s t$$ for any fixed $$t$$, i.e., the $$R^{x,y}_t$$ are injective, hence invertible by finiteness, and we get 255.  So we need operations $$\diamond_{x,y}$$ for which left-multiplication  by different elements $$s,s'$$ can agree in some locations but not in others.

Forgetting about extensions for the moment, maybe this suggests semilinear models such as $$x \diamond y = \alpha_x + \beta_x y$$ that are linear in the second variable but not the first.  Ugh, but this particular model just leads to a total mess when one computes 677.  

There's something very special about linear (or affine) binary operations - the composition of linear operations is again linear, and this is essential in keeping the number of equations and the number of unknowns matching when considering an equation like 677.  If one starts looking at quadratic maps, for instance, suddenly one gets way more equations than unknowns when one matches coefficients.   If there was some other class of binary operations $$x, y \mapsto x \diamond y$$ than linear or affine for which operations such as $$x,y \mapsto (y \diamond x) \diamond y$$ had the "same" complexity as the original map (in that they are described by exactly the same number of parameters), then we might have a shot, but I can't think of any other candidates... [EDIT: Okay, translation invariant models are one other candidate of this type.  And I guess, trivially, the entire class of arbitrary binary operations are also of this type.]

**Terence Tao:**

Reporting a very silly thing I tried, just to take it off the table: instead of trying to extend or enlarge a base magma, I tried for an embarrassingly long amount of time to experiment with the reverse operations of quotienting a magma by an equivalence relation, or restricting to a submagma.  For instance I was poking around to see if the linear magma model had any quotients that were not linear.  But then I realized that any law such as 255 would be automatically preserved by passing to quotients or submagmas, so there is probably no point in trying to use such constructions (unless perhaps as a base magma for some construction for which we don't currently have an immunity result).  [EDIT: there is perhaps a possibility that one could start with a magma that doesn't obey either 677 or 255, then perform a quotienting to enable 677 but not 255, which might work if we had some useful way of constructing a magma that "nearly" obeys 677, but I have no proposal in this direction.]

**Bernhard Reinke:**

Maybe I am confused, but shouldn't left cancellativity give you that $$\beta_{x,y}$$ is always injective, not $$\alpha_{x,y}$$?

**Bruno Le Floch:**

What you say is correct, but the argument I meant is that if $$t = s_j \diamond_{x,y} (t\diamond_{\dots} ((s_j\diamond_{x,y} t) \diamond_{\dots} s_j))$$ for $$j=1,2$$, and if the two $$s_j \diamond_{x,y}$$ coincide, then we have that $$s_1 \diamond_{x,y} (t\diamond_{\dots} ((s_1\diamond_{x,y} t) \diamond_{\dots} s_j))$$ are equal for $$j=1,2$$.  This takes the form
```math
L^{x,y}_{s_1} \circ L^{\dots}_t \circ L^{\dots}_{s_1\diamond_{x,y} t} s_j
```
and we can cancel any $$L^{\dots}_{\dots}$$ from this equation to get that the two $$s_j$$ agree.  We *deduce* from that that $$\alpha_{x,y}=0$$.

**Bernhard Reinke:**

Oh I see, thanks for the explanation!

**Zoltan A. Kocsis (Z.A.K.):**

Random thought: we know at least one infinite model where 677 holds but 255 fails. IIRC it's obtained by a greedy construction, so I guess it'd be hard to tell whether it admits finite factors of the relevant kind.

**Terence Tao:**

That's a good point.  It's possible that if we understand the infinite model better then we could figure out how to place a cofinite equivalence relation on it that one can quotient by to create a useful finite 677 model.  Though this hasn't been super successful in group theory - we completely understand what the free group on a fixed set of generators looks like, but this doesn't exactly make it easy to generate finite groups.

In group theory we have this extremely useful family of groups coming from permutations on an arbitrary set, with Cayley's theorem guaranteeing that all the other groups are basically subgroups of this model.  (Similarly for monoids and functions on an arbitrary set.)  There's also the group of general linear transformations of vector spaces, leading to the extremely rich and useful field of representation theory. I guess there's no reason to expect a similarly useful family for 677 though.  For some other laws, we had the left-absorptive or right-absorptive models which were also useful (though more as base models to modify than models to take submagmas of), but again these are not available here.  Instead we just have a twp strange families of linear models,some extensions of them, and a handful of infinite models...

**Pace Nielsen:**

I've been playing with the translation-invariant models, but no real progress.  Setting $$x\diamond y = xf(x^{-1}y)$$ in some group, we have injectivity of left multiplication
```math
x\diamond y = x\diamond z \Rightarrow y=z.
```
Setting $$x=1$$, this translates to
```math
f(y)=f(z) \Rightarrow y=z.
```
Thus, $$f$$ is injective, and so bijective.  Hence, the functional equation for $$f$$ can be rewritten as
```math
h^{-1}f^{-1}(h) = f(h^{-1}f(h)f(f(h)^{-1})).
```

Eq513 is equivalent to $$f^4=1$$, which would mean that under eq513 $$f$$  takes the carrier set and decomposes it into cycles of lengths 1, 2, 4.  Vampire says that no cycle of length 1 is allowed if 255 fails.  So the carrier set must have even cardinality, and it seems reasonable to just suppose that $$f$$ is a bunch of 4-cycles.  I'm not sure if this would speed up searches using Mace4.

**Terence Tao:**

I have a tentative approach based on my previous suggestion to split up 677 into two equations 

$$f(x,y) = (y \diamond x) \diamond y \quad (1)$$

and

$$x = y \diamond (x \diamond f(x,y)). \quad (2)$$  

The vague idea I had is to somehow propose a candidate for $$f$$ first, and then use (1) and (2) to solve for $$\diamond$$.  So we would like to understand the properties we want $$f$$ to have.

We can rewrite (1) in the form
$$ y \diamond x = z \implies z \diamond y = f(x,y) \quad (1')$$
and by left cancellativity we can similarly write (2) in the form
$$ x = y \diamond z \implies x \diamond f(x,y) = z \quad (2').$$
Thus both equations relate one entry of the multiplication table to another.  But there is a difference in behavior between the two equations, as we shall now see.

Observe that the transformation in (1') is injective: given $$z,y$$, one can recover $$x$$ by left cancellativity. 
 By finiteness, the transformation (1') must therefore be a bijection on the multiplication table.  Among other things this means that $$f(x,y)$$ is "equidistributed" in the sense that each element of $$M$$ is attained exactly $$|M|$$ times by $$f$$.

If 255 fails at some $$x$$, then $$R_x$$ is not surjective, hence not injective, thus $$y \diamond x = y' \diamond x = z$$ for some $$y \neq y'$$.  From (2') we then have $$z \diamond f(z,y) = x = z \diamond f(z,y')$$, so $$f(z,y) = f(z,y')$$, thus $$f$$ is not injective on columns.  Intuitively, $$f(z,y)$$ is "forgetting" some information about $$y$$.

Furthermore, if 255 fails at $$x$$, then $$w \diamond x \neq x$$ for all $$w$$, so from (1) we see that $$f(u,x) \neq  x$$ for all $$u$$.  Thus $$f(x,y)$$ is not surjective on rows either, and must "forget" some information about $$x$$ as well as $$y$$.

Now that $$f(x,y)$$ is forgetting information about both $$x$$ and $$y$$, we see that the transformation in (2') is non-injective: there are $$|M|^2$$ entries $$x \diamond y = z$$ of the multiplication table, but this needs to somehow transform to fewer than $$|M|^2$$ entries $$x \diamond f(x,y) = z$$.

So I started searching for candidate functions $$f: M \times M \to M$$ that were equidistributed, but which forgot some information on both inputs.  My first candidate was the natural central groupoid law, where $$M = S \times S$$ for some finite set $$S$$ and $$f( (x_1,x_2), (y_1,y_2) ) = (x_2,y_1)$$; note that this is equidistributed while still forgetting information from both inputs.  The equation (1) can be solved in this case as follows.  Suppose one has located some subset $$\Gamma$$ of $$S^5$$ which is invariant under shifts $$(a_0,a_1,a_2,a_3,a_4) \mapsto (a_1,a_2,a_3,a_4,a_0)$$, and is a bijection when projected to any four of the five components.  (For instance, if $$S$$ was an abelian group, one could take $$\Gamma$$ to be the hyperplane obeying $$a_0+a_1+a_2+a_3+a_4=0$$, but many other choices were possible).  If one then defines $$\diamond$$ by the law
$$ (a_1, a_4) \diamond (a_0, a_3) = (a_2,a_0)$$
for all $$(a_0,a_1,a_2,a_3,a_4) \in \Gamma$$, one can check that this operation is well-defined and obeys (1') and hence (1).  [Conversely, one can show that all solutions to (1') for this choice of $$f$$ are of this form; this is a fun little exercise, coming from iterating (1') five times.] Unfortunately, one cannot make it obey (2').  Inserting the above law into (2') one obtains
$$ (a_2,a_0) \diamond (a_0,a_4) = (a_0,a_3).$$
This law is not directly consistent with the previous one since $$a_3 \neq a_0$$ in general, but I don't see this as a fatal obstacle because one could perhaps modify the law (and $$f$$) on a small set to get around this.  The more serious problem is that the left-hand side only constrains three coordinates $$a_0,a_2,a_4$$ out of the tuple $$(a_0,a_1,a_2,a_3,a_4)$$, leaving $$a_3$$ unconstrained, so this equation is necessarily inconsistent, in a way that I don't see easy to fix with small modifications.

One can try more complicated constructions of this type, but so far I have run into similar obstructions.  Suppose for instance that now $$M = S \times S \times S$$ and one has a subset $$\Gamma$$ of $$S^7$$ which is shift-invariant and a bijection when projected to any six coordinates.  We can similarly define
$$ (a_1, a_3, a_5) \diamond (a_0, a_2, a_4) = (a_2,a_4,a_6)$$
for $$(a_0,\dots,a_6) \in \Gamma$$, and this will obey (1') with
$$ f( (a_0, a_2, a_4), (a_1, a_3, a_5) ) = (a_3, a_5, a_0).$$
If we insert the above law into (2'), we obtain
$$ (a_2, a_4, a_6) \diamond (a_4, a_6, a_1) = (a_0, a_2, a_4).$$
Again, this is not directly consistent with the previous law, but only covers a small minority of the multiplication table ($$|S|^4$$ of the $$|S|^6$$ entries) so I don't see this as fatal.  Again, we have the more serious issue that upon fixing $$a_2,a_4,a_6,a_1$$, $$a_0$$ remains unconstrained.

I'm still experimenting with this paradigm, so I don't know yet whether these difficulties can be overcome, or conversely whether they are hinting at a way to establish the positive implication, but I thought I would report this work in progress.

**Giovanni Paolini:**

If I am not mistaken, then a translation-invariant model satisfying 677 + 513 would not satisfy 255? (Because we know that 677 + 255 require $$f$$ to have a fixed point.)

The size-5 model $$x \diamond y = 2x - y$$ over $$\mathbb{Z}_5$$ is translation-invariant (with $$f(x) = -x$$) and satisfies 677, 513, and 255, though.

**Bruno Le Floch:**

What you write is correct.  What Pace Nielsen meant is that if $$f$$ has a fixed point then 255 is satisfied.  A putative translation-invariant counterexample to 677+513⇒255 must thus be such that cycles are of lengths 2 and 4, only.

**Terence Tao:**

Not much positive progress on my previous approach, but I at least have a model problem to propose:

* Can one build a finite left-cancellative magma that obeys 677 at least 99% of the time (thus, the 677 equation holds for at least 99% of pairs $$x,y$$) but for which right surjectivity only holds 1% of the time (i.e., the equation $$x \diamond a = b$$ is solvable for at most 1% of pairs $$a,b$$)?

(The reason why I ask for failure of right surjectivity rather than failure of 255 is that it is easy to make the one-variable equation 255 fail 100% of the time just by modifying the multiplication table on the diagonal, so I need a two-variable condition instead.)

The hope is that if such a counterexample can be found, then one can modify the example on a small portion fo the multiplication table to exactly solve 677 but fail to solve 255.  (This may be related to a discussion @Zoltan A. Kocsis (Z.A.K.) and I [had back in October](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/Future.20directions/near/474934527) on magmas that nearly obey a given law.)

Anyway, to construct such a counterexample, it suffices to find a left-cancellative operation $$\diamond$$ on a finite carrier $$M$$ that does two things:
1.  The expression $$f(x,y) := (y \diamond x) \diamond y$$ "forgets" information about $$y$$, in the sense that at most 1% of pairs in $$M \times M$$ can be of the form $$(x, f(x,y))$$.
2. The expression $$L_y^{-1} x$$ forgets the *same* information about $$y$$, that is to say for a given $$x,y,y'$$, one has $$f(x,y) = f(x,y')$$ if and only if $$L_{y}^{-1} x = L_{y'}^{-1} x$$.  (One could maybe tolerate a a failure of this if-and-only-if 1% of the time for the purposes of this model problem.)

Then if one modifies the operation on the small number of pairs $$(x,f(x,y))$$ so that $$x \diamond f(x,y) = L_y^{-1} x$$ (maybe doing a few more modifications to preserve left cancellativity), one obtains 677 basically 99% (or maybe 98%) of the time while (probably) violating right surjectivity quite a bit (because of all the collisions $$L_{y}^{-1} x = L_{y'}^{-1} x$$.

So far I can get constructions where $$f(x,y)$$ and $$L_y^{-1} x$$ both lose a comparable amount of information about $$y$$, but I can't get them to lose the *same* information, which is the main remaining obstacle.  Consider for instance a linear model $$x \diamond y = \alpha x + \beta y$$ where $$\alpha,\beta$$ are not commutative and possibly non-invertible linear transformations on $$M$$.  We already have ruled this model out for the original problem, but it also runs into problems here.  In this model, $$\beta$$ has to be invertible for left-cancellability, and we have $$f(x,y) = \beta \alpha x + (\alpha^2 + \beta) y$$.  If $$\alpha^2 + \beta$$ is non-invertible then there will be some loss of information about $$y$$, coming from the kernel of $$\alpha^2 + \beta$$.  We also have $$L_y^{-1} x = \beta^{-1} x - \beta^{-1} \alpha y$$, so information is lost here if $$\alpha$$ is non-invertible, coming from the kernel of $$\alpha$$.  But, unfortunately, the two kernels cannot coincide: if $$v$$ lies in the kernel of both $$\alpha$$ and $$\alpha^2+\beta$$ then it lies in the kernel of $$\beta$$, contradicting the invertibility of $$\beta$$.

Another model I played with was a model where $$M$$ was a non-abelian group and the operation $$\diamond$$ was conjugation, $$x \diamond y = x y x^{-1}$$, which is left-cancellative but not right-cancellative when $$M$$ is non-abelian.  Here $$f(x,y) = y x y x^{-1} y^{-1}$$ can lose some information in $$y$$ but it is hard to discern exactly what information is lost; meanwhile $$L_y^{-1} x = y^{-1} x y$$ loses information in $$y$$ relating to the centralizer of $$x$$.  It doesn't look like one can create a group where the information lost is the same.  One can play with other words here than the conjugation word $$xyx^{-1}$$ but there doesn't seem to be an obvious way to make the two information losses resemble each other.

I'm not throwing in the towel yet, but I think there is a possibility that we may eventually have to "declare victory" on the ETP without necessarily closing off this final implication, and pose it in the paper as an open problem.  Still, a success rate of 100.00% on the original graph and 99.99999% on the finite graph isn't exactly a terrible record...

**Terence Tao:**

By the way, here is a linear model that I found somewhat instructive.  Let $$F = F_p$$ be a field of large prime order $$p$$, let $$E$$ be a finite subset of $$F$$ with $$E$$ and its translate $$E+1$$ by one disjoint, but $$E$$ and $$E+2$$, $$E+3$$ having non-trivial intersection, e.g., one can take $$E = \{0,3,5\}$$.  Take the carrier to be $$F^E$$, i.e. the space of tuples $$(x_e)_{e \in E}$$ taking values in $$F$$.  Then take the following (linear) magma operation: given any polynomial $$P: F \to F$$ of degree at most $$2|E|-1$$, set
$$ ( P(e+1) )_{e \in E} \diamond (P(e))_{e \in E} := (P(e+2))_{e \in E}.$$
This is a well-defined map due to the disjointness of $$E$$ and $$E+1$$ and the Lagrange interpolation formula; it is left-cancellative but will not be right-cancellative since $$E$$ and $$E+2$$ overlap, so $$L_y^{-1} x$$ loses information about $$y$$.  It is easy to see that the function $$f$$ defined previously can be given by
$$ f( ( P(e) )_{e \in E}, (P(e+1))_{e \in E} ) = (P(e+3))_{e \in E}.$$
Because $$E+3$$ overlaps with $$E$$, $$f(x,y)$$ will lose information about $$y$$: knowing $$x$$ and $$f(x,y)$$ only specified $$P$$ on the set $$E \cup (E+3)$$ which has cardinality strictly smaller than the $$2|E|$$ degrees of freedom of $$P$$, whereas knowing $$x$$ and $$y$$ specifies all $$2|E|$$ degrees of freedom.   I tried for a while to make the information losses in $$f(x,y)$$ and $$L_y^{-1} x$$ line up until finally realizing that all linear models are obstructed by the argument given previously.

**Terence Tao:**

Here is an amusing reformulation of 677.  Given a left-cancellative magma $$(M,\diamond)$$, define a *good sequence* to be a sequence $$(x_n)_{n \in {\mathbb Z}}$$ obeying the recursion $$x_{n+1} \diamond x_n = x_{n+2}$$.  By left-cancellativity, every pair $$(x_0, x_1) \in M \times M$$ extends uniquely to a good sequence, which looks like
$$ \dots, L_{x_0}^{-1} x_1, | x_0, x_1, x_1 \diamond x_0, (x_1 \diamond x_0) \diamond x_1, \dots$$
(with the bar being notation for indicating the element of this sequence indexed by zero). We call this the good sequence generated by $$x_0,x_1$$.

Let $$G$$ be the set of good sequences.  Given any integers $$j,k$$, let $$A_{j,k}: G \to G$$ be the function that takes a good sequence $$(x_n)_{n \in {\mathbb Z}}$$ to the good sequence generated by $$x_j, x_k$$.  Thus for instance $$A_{j,j+1}$$ is just the shifted sequence
$$ \dots, x_{j-1}, |x_j, x_{j+1}, \dots $$
and is an invertible transformation on $$G$$.  The maps $$A_{j+1,j}$$ can also be seen to be invertible. 
 However, the other $$A_{j,k}$$ can be non-invertible.  (For instance, the invertibility of $$A_{1,-1}$$ is equivalent to right cancellability.)

The law 677 can now be rewritten as $$A_{1,2} A_{3,0} A_{1,0} = A_{1,-1}$$.  Indeed, if one starts with the good sequence $$g$$ generated by $$y,x$$, i.e.,
$$ \dots, L_y^{-1} x, |y, x, \dots$$
then $$A_{1,0} g$$ is the sequence
$$ \dots, |x, y, y\diamond x, (y \diamond x) \diamond y, \dots,$$
so $$A_{3,0} A_{1,0} g$$ is the sequence
$$ \dots, |(y \diamond x) \diamond y, x, x \diamond ((y \diamond x) \diamond y), \dots$$
and hence $$A_{1,2} A_{3,0} A_{1,0} g$$ is the sequence
$$ \dots, (y \diamond x) \diamond y, |x, x \diamond ((y \diamond x) \diamond y), \dots$$
which matches $$A_{1,-1} g$$ precisely when $$L_y^{-1} x = x \diamond ((y \diamond x) \diamond y)$$, i.e., when 677 holds for $$x,y$$.

In the equation $$A_{1,2} A_{3,0} A_{1,0} = A_{1,-1}$$, the maps $$A_{1,0}$$ and $$A_{1,2}$$ are invertible, so the equation implies that $$A_{3,0}$$ and $$A_{1,-1}$$ are "equally non-invertible" in some sense.  This is another way of stating the previous assertion that $$f(x,y)$$ and $$L_y^{-1} x$$ "lose the same information in $$y$$).  

Specifying a left-cancellative operation is equivalent to specifying a class of good sequences that is shift-invariant, and such that any pair $$x_0,x_1$$ uniquely generates a good sequence.  Such a class then generate the $$A_{j,k}$$ operators.  But I don't see a good candidate for a class for which we have a hope of matching $$A_{1,2} A_{3,0} A_{1,0}$$ with $$A_{1,-1}$$ (other than ones coming from 677 magmas that we already know how to construct, of course).

**Bruno Le Floch:**

I want to focus on some other parts of the project for a bit (especially Higman-Neumann), but am hoping to return here in two weeks or so, near the very end of the project.  There is still a bit of time as the formalization work is not done yet.

I like your model problem, but so far did not have any success.  On the other hand I think your reformulation in terms of $$A_{j,k}$$ complicates things.

Central groupoids, which are subject to a three-variable equation (hence expected to be more restrictive), can often be modified by a "switching" operation that acts very simply on the graph.  In an n-element magma it affects sqrt(n) entries in the multiplication table if I remember correctly.  So it wouldn't be crazy to hope that for our two-variable equation 677 we could also modify a large linear magma "by hand" in a reasonable number of places to get a new magma that violates 255.  I don't think we've explored this enough.  The problem is that 677 is very mixing somehow.

Maybe we could learn something about sizes of cosets, and the flow of information, from having a model that is not right-cancellative.  However, the only current hope to produce them is piecewise affine models which involve solving huge systems of nonlinear equations.

I don't think we've ruled out models of the form $$x\diamond y = a_x y + c_x$$ that are linear in one of the two arguments only.  We could even try something like $$x\diamond y = a_{\pi(x)} y + c_x$$ with $$\pi\colon M\to\{0,1\}$$ or a similar tiny set.

**Amir Livne Bar-on:**

I ran some searches with mace4. Assuming I got the syntax right, there are likely no translation-invariant models with $$f^2=1$$. Mace4 searches up to order 120 in under 30 seconds, then it reaches its memory limit and gives up. I don't know an argument why it's impossible to have such models with a non-trivial group.
Searching with $$f^4 = 1$$ does do some work, I'll let it run for a few hours.

Attaching here my file: [attached: eq677.in]

**Amir Livne Bar-on:**

Mace4 is magical, with the right selection order it also eliminated $$f^4=1$$ up to order 120

**Jose Brox:**

I've extended the computation (allocating more memory with
```assign(max_megs, 2000).```
) to confirm that there are no models up to size 216 (in 300s).

Do you mean selection *measure*, or did you actually find a selection order which is better than 2 for this problem? (I've never encountered such a problem before!). Can you share the input file for this one too? Thank you!

**Amir Livne Bar-on:**

Selection measure 3, and using selection order 2 (which might be the default).

I edited the file and I didn't save a version to reproduce, but it's the same as the $$f^2=1$$ file except for these changes. The run took 6 or 7 minutes.

**Jose Brox:**

In fact, from the premises Prover9 derives FALSE (it arrives at `f(inv(f(0)) = inv(f(0))`), so we have proof that there are no translation-invariant models with $$f^2 = 1$$ and $$f(x)\neq x$$ for all $$x$$.

**Bruno Le Floch:**

If I understand correctly, $$f^2=1$$ means $$x\diamond(x\diamond y) = xf(f(x^{-1}y))=xx^{-1}y=y$$.  We know that this assumption (or even the weaker $$x\diamond(x\diamond x)=x$$) together with 677 and finiteness implies 255, even without assuming translation invariance.

Indeed, (attempting to translate a prover9 proof) 677 with `x,y` replaced by `xx,x` and applying `x(xx)=x` gives `xx=x((xx)(xx))` hence `(xx)(xx)=x`, then 677 with `x,y` replaced by `x,x` gives `x(x((xx)x))=x=x(xx)` then left-cancellativity gives `(xx)x=x`.  This equals `(xx)(xx)` so left-cancellativity gives `x=xx` and we are done showing 255.

**Bruno Le Floch:**

On the other hand Jose Brox didn't find a contradiction with 513 which in the present context is $$f^4=1$$.  So that's a worthwhile class of models to study.

**Amir Livne Bar-on:**

My run with $$f^2 = 1$$ showed that it implies not only 255 but 2, i.e. no models (up to order 120, which Jose extended up to order 216)

**Zoltan A. Kocsis (Z.A.K.):**

I think at this stage it's worth considering the possibility that the implication might hold in the finite case (e.g. something like right-cancellativity holds over all finite models).

Perhaps the tools of classical universal algebra could help in such investigations? I mean things like subdirect representation, congruence lattices, characterizations of direct irreducibility.

Here's a concrete idea: If finite directly irreducible 677-magmas satisfy 255, then of course all finite 677-magmas do. Over certain algebraic structures, one can determine direct reducibility by counting solutions to equations. For example, a finite Heyting algebra is directly reducible precisely if the equation $$x \vee \neg x = \top$$ has more than 2 solutions (btw this is why all finite Boolean algebras have $$2^n$$ elements).

I wonder if 677-magmas admit any similar solution-counting characterization for direct reducibility. If so, these could be added as assumptions to Prover9 to see if they allow us to conclude e.g. right-cancellativity or 255.

**Terence Tao:**

@Bruno Le Floch Yeah, the $$A_{j,k}$$ formulation was less useful than I had hoped.  It does show that the maps $$(x,y) \mapsto (x, y \diamond x)$$ and $$(x,y) \mapsto (x, (y \diamond x) \diamond y)$$ are "equally non-invertible" for 677 magmas in the sense that one can transform one to the other by separate invertible transformations of the domain and range.  Indeed, using left cancellativity one can transform $$(x,y) \mapsto (x, (y \diamond x) \diamond y)$$ to $$(x,y) \mapsto (x, x \diamond ((y \diamond x) \diamond y))$$, which by 677 is $$(x,y) \mapsto (x, L_y^{-1} x)$$.  Substituting $$x = L_y z$$ we get the map $$(z,y) \mapsto (y \diamond z, z)$$, which after some rearranging gives $$(x,y) \mapsto (x, y \diamond x)$$.

In the specific case of $$x \diamond y = 2x-y$$ on $$F_5$$, the good sequences are the linear ones $$n \mapsto an+b$$, and $$A_{j,k}$$ maps a linear sequence $$n \mapsto an+b$$ to the linear sequence $$n \mapsto (k-j)an + aj + b$$.  One can manually verify the identity $$A_{1,2} A_{3,0} A_{1,0} = A_{1,-1}$$ in this case.

Somehow the problem is that this equation 677 is only barely solvable with finite non-trivial models; it seems very hard to find a construction in which there are more variables than unknowns (the cohomological approach comes the closest), but unfortunately all known constructions preserve 255.  In particular, imposing more conditions on the magma seems to make it almost impossible to find any non-trivial model at all.

**Terence Tao:**

By the way, not that it helps directly, but I was able to modify the previous Kisielewicz construction to describe the free 677 magma; details are [in the blueprint](https://teorth.github.io/equational_theories/blueprint/677-chapter.html#a0000000040).

**Terence Tao:**

The final formalization of the outstanding implications for the infinite graph seems like a natural milestone to assess whether to "declare victory" on the project, regardless of whether 677->255 is resolved by then, but I suppose we can debate that (and/or hold a vote) when that day comes.

**Bruno Le Floch:**

It sounds reasonable indeed to declare victory at that point, since all the finite implications (except that one of course) have been formalized.

**Bruno Le Floch:**

Equation 677 `x = y ◇ (x ◇ ((y ◇ x) ◇ y))` is equivalent (in the finite setting) to equation 19855 `x = (y ◇ x) ◇ ((y ◇ (y ◇ x)) ◇ y)`.  There is a reformulation of 677 in terms of $$x\odot y = L_x^{-1} y$$ which looks somewhat similar, Equation 9321: `x = y ⊙ ((x ⊙ y) ⊙ (x ⊙ (x ⊙ y)))`.  However, I don't have much hope that it would be useful: linearity is preserved by passing from `◇` to `⊙`, right-invertibility as well (`(∀y,z,∃x,x⊙y=z) ⇔ (∀y,z,∃x,y=x◇z)`), and the condition for 255 too (`(∀y,∃x,x⊙y=y) ⇔ (∀y,∃x,y=x◇y)`).  But maybe it inspires someone something.

**Terence Tao:**

I can solve the model problem: given any $$\varepsilon>0$$, one can find a left-cancellative finite magma $$M$$ which obeys 677 for $$1-O(\varepsilon)$$ of pairs $$x,y$$, but is highly non-right-invertible in the sense that $$(x, y \diamond x)$$ only occupies $$O(\varepsilon |M|^2)$$ of pairs.

We take a translation-invariant model $$x \diamond y = x + f(y-x)$$ for some invertible $$f: M \to M$$, with $$M$$ an abelian group.  As previously computed, 677 becomes the equation
$$ h = f( h + f( -h + f(h) + f(-f(h)) ))$$
which we can rearrange as
$$ f^{-1}(h) - h = f(-h + f(h) + f(-f(h)) )$$
or equivalently
$$ h - f(h) = f( -f(h) + f^2(h) - f(-f^2(h))).$$
To simplify the algebra we assume that $$M$$ is of exponent 2, to eliminate all the minus signs:
$$ h + f(h) = f( f(h) + f^2(h) + f^3(h))). \quad (1)$$
One should think of this as saying (among other things) that the functions $$h \mapsto h + f(h)$$ and $$h \mapsto f(h) + f^2(h) + f^3(h)$$ are "equally non-invertible".

We would like this equation (1) to hold $$1-O(\varepsilon)$$ of the time, while $$h+f(h)$$ only takes $$O(\varepsilon |M|)$$ values.

Note that (1) and the invertibility of $$f$$ implies that collisions in $$h+f(h)$$ are equivalent to collisions in $$f(h)+f^2(h)+f^3(h)$$:
$$ h+f(h) = h'+f(h') \iff f(h)+f^2(h)+f^3(h) = f(h')+f^2(h') + f^3(h') \quad (2).$$
Conversely, suppose that (2) holds for all $$h,h'$$ outside of an exceptional set of cardinality $$O(\varepsilon |M|)$$, and that $$h+f(h)$$ only takes on $$O(\varepsilon |M|)$$ values.  This implies that $$f(h)+f^2(h)+f^3(h)$$ also takes on only  $$O(\varepsilon |M|)$$ values.  Then one can upgrade (2) to (1) (outside of an exceptional set of size $$O(\varepsilon |M|)$$) by modifying $$f$$ on $$O(\varepsilon |M|)$$ values (mostly on the values of $$f(h)+f^2(h)+f^3(h)$$, making some additional swaps as needed to maintain the invertibility of $$f$$).  So we just need to construct a function $$f$$ that obeys (2) most of the time, while $$h+f(h)$$ takes few values.

There are lots of ways to proceed here, I will take a piecewise linear model.  Let $$F$$ be a large finite field of characteristic 2 (of size much larger than $$1/\varepsilon$$) and let $$\alpha$$ be a generator of the multiplicative group, thus the non-zero elements of $$F$$ are $$1, \alpha, \alpha^2, \dots, \alpha^{|F|-1}$$.  I will take the carrier $$M$$ to be $$F \times F^3$$ and the function $$f$$ to take the form
$$ f( \alpha^i, s ) = (\alpha^{i+1}, T_i(s) )$$
for all $$i=0,1,\dots,|F|-1$$ and some invertible linear transformations $$T_i: F^3 \to F^3$$ to be defined later.  I don't bother defining $$f$$ on $$0 \times F^3$$ as this is only $$O(\varepsilon)$$ of the elements.  The relation (2) then reduces the following: for $$1-O(\varepsilon)$$ of the $$i$$, and all $$s \in F^3$$, we have
$$ s + T_i s = 0 \iff T_i s + T_{i+1} T_i s + T_{i+2} T_{i+1} T_i s = 0 $$
or equivalently
$$ T_i s = s \iff T_{i+2} (T_{i+1} s ) = T_{i+1} s + s. \quad (3)$$
If we require each of the $$T_i$$ have exactly one eigenvector $$e_i$$ (up to scaling) with eigenvalue one, then $$h+f(h)$$ will only take on about $$|F|^3$$ of the $$|F|^4$$ possible values, which is $$O(\varepsilon |M|)$$ as desired, and the constraint (3) simplifies to asking that
$$ T_{i+2} (T_{i+1} e_i ) = T_{i+1} e_i + e_i \quad (3')$$
and that there is no other solution to $$T_{i+2} (T_{i+1} s ) = T_{i+1} s + s$$ up to scalar multiples.  So, one just needs to construct a sequence $$T_0, T_1, \dots, T_{|F|-1}$$ of invertible linear transformations on $$F^3$$, with each $$T_i$$ having an eigenvector $$e_i$$ of eigenvalue one, that obeys the recursive condition (3'). But this can be done recursively.  Choose $$T_0, T_1$$ to be invertible transformations with linearly independent eigenvectors $$e_0, e_1$$ of eigenvalue one.  One can then select a vector $$e_2$$ independent of both $$e_0$$ and $$T_1 e_0$$ (which are themselves independent of each other) and it is not difficult to then locate an invertible linear transformation $$T_2$$ that maps $$e_2$$ to itself, maps $$T_1 e_0$$ to $$T_1 e_0 + e_0$$, and has no other solution to (3') other than scalar multiples.  We keep iterating this procedure to construct $$T_3, T_4, \dots$$.  One may have some failure near the final step $$i=|F|-1$$ but that's OK since we are allowing things to break down $$O(\varepsilon)$$ of the time anyway.

**Pace Nielsen:**

I had thought that a carrier group with exponent 2 was disallowed, but checking again I see that's only when we assume 513 in conjunction with 677.

**Pace Nielsen:**

Actually, exponent 2 forces 255 when assuming 677 + injectivity of $$f$$.  I'm guessing that the issue is being shoved into into the $$O(\varepsilon|M|)$$ failure set, somehow.

**Terence Tao:**

Hmm, interesting.  Are you able to extract a human readable proof of 255 in this case?

**Pace Nielsen:**

I'll see what I can do.  It doesn't look too bad.

**Pace Nielsen:**

Throughout, assume translation-invariance in an exponent 2 group (which is thus commutative, so we write the operation additivitely).  Also throughout, assume 677+injectivity of $$f$$.

Write $$p:=f(0)$$ and $$q:=f(p)$$.    Equation 677 at $$h=0$$ yields
```math
f^2(p+q)=0.
```
Next, equation 677 at $$h=p$$ yields
```math
p=f(p+f(p+q+f(q))).
```
Since $$p=f(0)$$, using injectivity we get $$0=p+f(p+q+f(q))$$.  Moving $$p$$ to the other side and using injectivity again, $$0=p+q+f(q)$$.  In other words $$f(q)=p+q$$.

Next, equation 677 at $$h=p+q$$ yields
```math
p+q=f(p+q+f(p+q+f(p+q)+f^2(p+q))).
```
Recalling that $$f^2(p+q)=0$$ and $$p+q=f(q)$$, then using injectivity of $$f$$ we have $$q=p+q+f(p+q+f(p+q))$$.  Simplifying and using injectivity again, $$0=p+q+f(p+q)$$, or in other words $$f(p+q)=p+q$$.

We now have that $$f$$ takes $$p+q\mapsto p+q\mapsto 0$$.  This means $$f(0)=0$$, and hence 255 holds.

**Terence Tao:**

Thanks for this!  I don't think the exponent 2 hypothesis is extremely essential to the sort of construction in my post to be possible, but it certainly makes things a little cleaner and simpler.  But your argument shows that while it may end up leading to constructing a non-right-injective 677 finite magma (which I think we haven't yet been able to accomplish), it won't quite refute 677->255 on its own, unless we move away from exponent 2.

I might keep playing with the exponent 2 model a bit more as a toy problem.  In particular if there is some way to take a model that solves 677 $$1-\varepsilon$$ of the time and make some modification to it so that it now solves 677 say $$1-\varepsilon/2$$ of the time then one could iterate all the way to an exact 677 model, which would give a new way of constructing these models that might hopefully adapt beyond the exponent 2 case and refute 677->255.  Still more of a hope than a strategy, though.

**Jose Brox:**

The results are slightly different: @Bruno Le Floch only imposes $$f^2=1$$ and this implies equation 16, which together with 677 already implies 255. On the other hand, if we also impose $$f(x)\neq x$$ for all $$x$$, then we know that the axioms are inconsistent, i.e., even the trivial model is invalid.

**Amir Livne Bar-on:**

The proof is rather simple too. It even suffices to have $$f^2(0)=0$$. If $$h=f(0)$$ and $$0=f(h)$$, then we get from the functional equation $$h=f(h+f(-h+f(h)+f(-f(h)))) = f(h+h)$$ and hence $$2h=0$$. Then by putting $$0$$ in the equation, we get $$0=f(0+f^2(0))=h$$.

**Terence Tao:**

I'm beginning to understand now that the task of establishing 677 on $$1-\varepsilon$$ of pairs $$x,y$$ (or $$1-\varepsilon$$ of shifts $$h$$, in the translation-invariant model) is rather different than that of establishing 677 everywhere.  The problem with the latter is that it is exactly determined: $$|M|^2$$ equations on $$|M|^2$$ unknowns, or $$|M|$$ equations on $$|M|$$ unknowns in the translation-invariant case.  But once one allows a failure rate, one now has an underdetermined problem, basically $$(1-\varepsilon) |M|$$ equations on $$|M|$$ unknowns in the translation-invariant case, so it is much easier to build examples.  On the other hand, obstructions such as the exponent 2 construction only require a small number of equations and unknowns and so are invisible to the $$1-\varepsilon$$ variant of the problem.

For three-variable equations such as the associative law, there can be ways to relate a specific operation on the multiplication table with quite "generic" entries of the multiplication table, with the upshot being that if such a table obeys the law 99% of the time then it is possible to modify it on a small number of entries to be obeyed 100% of the time.  A classic example of this is the Blum-Luby-Rubinfeld linearity testing result: if a function $$f: F_2^n \to F_2^n$$ obeys the linearity property $$f(x) + f(y) = f(x+y)$$ 99% of the time, then one can modify $$f$$ a ilttle bit to be perfectly linear.  The point, roughly speaking, is that one can work out what $$f$$ should be at $$x$$ by looking at $$f(x+y)-f(y)$$ for a "typical" $$y$$ and use this to perform "error correction".  Here it is essential that the functional equation has at least two variables, in contrast to the one-variable situation we have with translation-invariant 677.  This is also related to the fact that three-variable equational laws are highly overdetermined, in contrast to two-variable laws that are perfectly determined.

In the construction I gave with carrier $$M = F \times F^3$$, each of the vertical slices $$\{x\} \times F^3$$ are self-contained submagmas which are completely arbitrary.  It could be that an improved version of the construction leads to a method where one can place an arbitrary 677 structure on each such slice and then fill in the multiplication table for off-diagonal products $$(x,s) \diamond (y,t)$$ with $$x \neq y$$ so that there is significant failure of right cancellativity "off the diagonal", but this wouldn't affect 255 which can be verified entirely within a single slice at a time.  (This is related to the previous observation that we can assume without loss of generality that the magma is generated by a single element, so there is no point playing with models in which the magma splits into disjoint submagmas.)  

Anyway, I think I'm already to abandon my tentative "99% construction" method here, as the hoped for "rigidity", "stability", or "error-correcting" phenomenon (in which a 99%-perfect 677 magma could be corrected into a 100%-perfect 677 magma) looks unlikely to be the case.  (A model situation is when 677 fails for a single pair $$x,y$$.  As far as I know we have no way of ruling out this scenario, but also there is no obvious way to "repair" such a near-miss magma to obey 677 without exception.)

**Zoltan A. Kocsis (Z.A.K.):**

In my experience, similar "reconstruction" tends to be quite difficult in the absence of rigid structure. For example, if you start with the axioms `x*x=0`, `x*(y*z)=(x*y)*z`, `x*0=0*x = x`, then you get only $$\mathbb{Z}/2\mathbb{Z}^n$$ as your finite models.

But if you allow for these axioms to hold only up to epsilon, you immediately get many models where you have to change a *fixed proportion* of the operation table on $$\{0,..,2^n\}$$ before you get a group, much less $$\mathbb{Z}/2\mathbb{Z}^n$$. IIRC the operation given below, defined on a large $$\{0,..,n=2^k\}$$, constitutes such an example:
```
0 * y = y
x * 0 = x
x * x = 0
x * y = min{x,y}   if x,y both in {1..n} and x /= y
```

If you do have some rigid structure, e.g. cancellativity/injectivity, such examples do not arise (like in the theorem of Gowers and Long), but cancellativity/injectivity is precisely what we do not want in this case.

Here's a question: what if we could construct an operation table on which not just 677, but *all* algebraic consequences of 677 are also satisfied with high probability. Is the operation table epsilon-close to an actual model then? The analogous question for the consequences of the $$\mathbb{Z}/2\mathbb{Z}^n$$ axioms above has a positive answer.

**Jose Brox:**

Before abandoning this line of thought, let me comment that I've been trying to automatically find specific models where your conditions:
 are satisfied. The problem is that if we use first-order logic, imposing a condition like the 1% is tricky (we can do it if we impose a specific model size and throw in a bunch of variables, one for each element, etc.). So before resorting to higher-order logic I thought that perhaps I could compute all models satisfying condition 2 for many sizes, then choose the optimal models and try to approach condition 1 as the size grew, or else see if the limit was bounded from below for some reason. If things went well, one could perhaps study the optimal models and try to find some iterative construction. Hence I've used this Mace4 code:
```
x*y = x*z -> y=z.
all x all y exists z (x*z = y).
f(x,y) = (y*x)*y.
g(x,y) = z <-> y*z = x.
f(x,y) = f(x,z) <-> g(x,y) = g(x,z).
```
Up to size 6, things went well, I got a fast computation. But then Mace4 completely stalled at size 7: it has been there for more than 20h, finding only 306 models in the meantime.

Anyway, the smallest proportion of elements of the form (x,f(x,y)) (i.e., the sum of the cardinals of the sets given by the rows of the table of f(x,y) if I understood correctly) to the size of the model is 100% for size 3, 81.2% for size 4, 60% for size 5, and 58.3% for size 6. Since the naive lower bound for this proportion is 1/size, this results struck me as perhaps too high, and I thought that maybe there were some combinatorial reason (related to injectivity etc.) for this, hence to get 1% by this method we might need a size quite higher than 100.

In case they may result interesting, the optimal models for each size in [3,6] have the following $$f$$ functions:
[*Spoiler: OPTIMAL MODELS — omitted*]
If someone thinks of some smart sentence to automatically approach condition 1 (maybe with higher-order logic), we could speed up the search significantly.

A simple thing I've tried (but with no expectations at all) is just try to get $$f(x,y)=f(x,z)$$ unless $$x\in\{0,1,2\}$$. The search is in size 76 after 35h, so not many hopes there.

**Pace Nielsen:**

How hard would it be to find (or rule out) a translation-invariant model of 677on $$(\mathbb{Z}/4\mathbb{Z})^4$$, where $$f^4=1$$, but 255 fails?  Is size 256 just too big to effectively look for examples, even if we have constrained things a lot by fixing the carrier group?

**Jose Brox:**

@Terence Tao It is late for me in the night, but I think here we have an sketch showing that we can't go below 50%:

Suppose $$f(x,y)=f(x,z)$$ for $$y\neq z$$; then $$L_y^{-1}x = L_z^{-1}x$$. Therefore
$$x = zL_z^{-1}x = zL_y^{-1}x$$, thus if $$f(L_y^{-1}x, y) = f(L_y^{-1}x, z)$$ then $$xy = xz$$, a contradiction with the injectivity of $$L_x$$. Hence for each pair $$(y,z)$$ such that
$$f(x,y)=f(x,z)$$ in the $$x$$-th row, we get the same pair $$(y,z)$$ such that $$f(w,y)\neq f(w,z)$$ in the $$w$$-th row for $$w:=L_y^{-1}(x)$$ (this extends to an arbitrary finite number of elements), and since $$L_y$$ is injective, if $$x,x'$$ give different rows having repeated element $$y$$ with some $$z$$, then $$L_y^{-1} x$$ and $$L_y^{-1} x'$$ produce different rows having different elements $$y,z$$.

Based on the examples, I'd bet that in addition we cannot have more than $$\lfloor n/2\rfloor+1$$ repeated elements per row, where $$n$$ is the size of the model, but no time to think about that now.

**Terence Tao:**

Hmm, I think this shows something like that the number of possible values of $$f(x,y)$$ for a given $$x$$ has to be at least $$2$$, rather than at least $$n/2$$.  (It's not quite this, but if $$f(x,y)$$ takes $$k$$ values, then the proportion of times one expects to have $$f(x,y) = f(x,z)$$ should be heuristically $$1/k$$, which is the quantity that I think you've shown cannot exceed 50%.)

**Terence Tao:**

The following argument can show that at least one of the right multiplication operators $$R_y$$ must have a range of size at least $$n^{1/2}$$: If all $$R_y$$ take on less than $$n^{1/2}$$ values, then for fixed $$y$$ there are less than $$n^{1/2}$$ values for $$R_y L_y x$$,and hence less than $$n$$ values for $$R_{R_y L_y x} x = L_y^{-1} x$$ thanks to 677, but this contradicts left-invertibility.

**Bruno Le Floch:**

Three disorganized thoughts, sorry.

- Earlier, @Terence Tao considered M₇×S with M₇ one of the two 7-element 677-magmas, took an operation $$(x,s)\diamond(y,t) = (x\diamond y, s\diamond_{x,y} t)$$, noted that $$\diamond_{0,0}$$ decouples, and used a projective Ansatz to reduce from 48 operations to only 8.  We could take small S in an ATP.  EDIT: I've ruled out $$|S|\leq 3$$.
[*Spoiler: The equations, for reference. — omitted*]

- We could combine magma extensions with twisting, so take a carrier $$G\times M$$ with both $$G$$ and $$M$$ being 677-magmas (and typically $$M$$ being itself a power a 677-magma), and set $$(x,s)\diamond(y,t) = (x\diamond y, S_{x,y}(s)\diamond T_{x,y}(t))$$ where every $$S_{x,y}$$ and $$T_{x,y}$$ is a magma morphism of $$M\to M$$ (with $$T_{x,y}$$ bijective to get left-cancellability).  If we did not have dependence on x,y then we know there is no non-trivial twisting, but using the dependence could help make the relations more redundant, hence have a solution. *EDIT: for the 8-operation projective model the twists are given by $$T_0=S_\infty=(T_1)^{-1}=(S_1)^{-1}$$ and all other $$S_p,T_p$$ are the identity; in particular $$S_5=T_5=1$$ so the model obeys 255.  This may hint to a general immunity.*

- Maybe the following graph is an interesting bookkeeping device: `y→z` if and only if `∃x,z = (y ◇ x) ◇ y` if and only if `∃x,x = y ◇ (x ◇ z)`.  The direct implication `z = (y ◇ x) ◇ y ⇒ x = y ◇ (x ◇ z)` is 677.  The reverse `z = (y ◇ x) ◇ y ⇐ x = y ◇ (x ◇ z)` is 677 together with left-invertibility in `y ◇ (x ◇ ((y ◇ x) ◇ y)) = x = y ◇ (x ◇ z)`.

**Terence Tao:**

The twisting extension construction is interesting!  $$M$$ (or $$S_{x,y}, T_{x,y}$$) will have to be nonlinear for it to have a chance at evading 255 since otherwise it will be a linear extension model which we already know 677->255 is immune to.  That is slightly worrying because the twisting semi-group doesn't seem to be aware of whether the magma one is working with is linear or not, though perhaps the nonlinearity will become important when trying to refute 255 rather than when trying to establish 677.

**Bruno Le Floch:**

Sadly, twisting-extension doesn't work for finite 677->255.  Left-invertibility (in the finite setting) requires all $$T_{x,y}$$ to be invertible.  One of the equation (which states that the first and last variables receive the same action of the morphisms) has the schematic form $$S = T T T$$, so $$S$$ is invertible.  This implies right-invertibility, which implies 255.

**Bruno Le Floch:**

Ah, I was too quick.  If M is not right-invertible to begin with (which we might achieve with other constructions?),  then the result is not right-invertible.  And maybe `∀x,∃y,yx=x` is **not** preserved by this construction: even invertible twists might "move" the failures of right-invertibility from some $$\mathrm{im}(R_x)$$ that contains $$x$$ to one that does not.

**Jose Brox:**

I'm not sure, I don't have the experience to tell: on the one hand, size 256 is quite big (tends to really slow things down), but on the other the product and inverse functions are completely specified, and $$f^4=1$$ (with $$f(x)\neq x$$) is quite specific, so some search parameters combination may make the "magic" as Amir put it the other day.

In any case, I have started the experiment with two different selection measures in parallel (here I cannot tune the search parameters looking at lower sizes as easily, I'd have to generate other problems with $$(Z/4Z)^2, (Z/2Z)^2$$, etc. and time the experiments to decide) and Mace4 has been holding up for a while (for comparison I have run another experiment, same carrier but arbitrary $$f$$, and it has exited saying "killed" in seconds).

Apart from the lines with the multiplication (addition) table and the inverse (opposite) map, the code for this is
```
MACE4 ASSUMPTIONS
all x  x = f(x * f((inv(x) * f(x)) * f(inv(f(x))))).
all x x != f(x).
all x x = f(f(f(f(x)))).
all x all y x@y = x*f(inv(x)*y).
all x all y all z x@y = x@z -> y = z.

MACE4 GOAL
all x x = ((x @ x) @ x) @ x.
```
(Please, check that I got everything right!).

I attach the complete file (close to 1MB):
[attached: MACE4 677 anti 255 linear over product of 4 copies of Z4 f order 4 measure 4.in]

The Sage code I've used to generate the multiplication and inverse maps is
```python
rings=[Zmod(4) for i in range(4)]
R=cartesian_product(rings)

#Multiplication table of R, in Mace4 format with sum written as *
s=""
for i,x in enumerate(R):
    for j,y in enumerate(R):
        s=s+f"""{i}*{j}={R.list().index(x+y)}.
"""
print(s)

#Inverse function of R, in Mace4 format with inverse as inv(x)
ss=""
for i,x in enumerate(R):
    ss=ss+f"""inv({i}) = {R.list().index(-x)}.
"""
print(ss)
```
I attach a Jupyter notebook with the maps already computed and printed out:
[attached: MAGMAS PROJECT - Cartesian product of Z4, translation to Mace4.ipynb]

**Jose Brox:**

A brief summary of the experiments I'm conducting right now with Mace4, the running sizes (no models for smaller sizes) and the time they have already spent in the current size:

1. 677+513+3659 anti 255: In size 14 for 109.5h
2. 677+4073 anti 255: In size 14 for 107.5h
3. 677+4131 anti 255: In size 14 for 107.5h
4. 677+4276 anti 255: In size 13 for 116h
5. 677+4293 anti 255: In size 16 for 43h
6. 677+4321 anti 255: In size 15 for 107.5h
7. 677+4591 anti 255: In size 14 for 106.5h
8. 677+4599 anti 255: In size 18 for 96h
9. 677 with translation-invariant model over noncommutative ring, any f: In size 15 for a few hours
10. 677 with linear product in semirring without annihilation nor distributivity anti 255: In size 10 for 105h
11. 677 with linear product in semirring without distributivity anti 255: In size 19 for 93h

The rationale for the last two is the following: over noncommutative rings the linear models cannot work. But we can keep removing axioms from the base ring until perhaps the two varieties (for 677 and 255) start differing. Even if we don't ask for distributivity or opposite elements for addition, the mere presence of $$0$$ and $$1$$ produces the same sets of polynomials (when written as sums of monomials) as the ring case, but this doesn't necessarily mean that their solutions are still the same. I have checked with Vampire that if we ask for annihilation ($$0*x = 0 = x*0$$) and left distributivity, then (with 677 anti 255) there must be opposite elements even if there is no right distributivity; and Mace4 is interestingly faster without any distributivity law, so I'm conduncting two experiments: one with annihilation, one without, both without distributivity nor opposite elements.

**Giovanni Paolini:**

In the meantime, I've kept searching for 677 translation-invariant models over groups of order >17 where $$f$$ has no fixed points. No model was found of order 18 and 19. I am currently checking $$\mathbb{Z}_{20}$$ (Gurobi has been running for 27h, with no sign of being close to finish).

To answer @Pace Nielsen, I don't think my current approach with Gurobi has any hope to handle $$(\mathbb{Z}_4)^4$$, even if we add $$f^4 = 1$$ and no fixed points.

**Jose Brox:**

Apologies for being stubbornly fixated with a problem that is probably unproductive for the project, but I'm captivated by its beauty :big_smile: My "toothbrushing" sketch proof wasn't directed to find the bound for each row of $$f$$ (fixed $$x$$), but for the sum of the rows (that I believe is what you were asking with your condition 1 upstream). The combinatorial problem would be as follows, denoting $$[n]:=\{1,\ldots,n\}$$:

Let $$f,g:[n]\times [n]\to[n]$$ be two functions with $$g(\cdot,y)$$ bijective for all (fixed) $$y$$ and such that
1) $$f(x,y) = f(x,z)$$ iff $$g(x,y) = g(x,z)$$.
2) $$f(x,y) = f(x,z)$$ implies $$f(g(x,y),y)\neq f(g(x,y),z)$$.
For each $$x$$, let $$m_x$$ denote the cardinal of the range of $$f(x,\cdot)$$. Then 
$$\sum_{x\in [n]} m_x \geq F(n),$$
where $$F(n)$$ is to be determined and sharp.

My idea wasn't having into account some kind of collisions, but there is some subtlety in the iterative process: Let $$R_x$$ denote the $$x$$-th row of the table of $$f(x,y)$$, and write $$\sim_x$$ for the equivalence relation in $$[n]$$ given by $$y \sim_x z$$ iff $$f(x,y)=f(x,z)$$. Let $$R^i_x$$ for $$1\leq i\leq m_x$$ be the equivalence classes of $$[n]/\sim_x$$ and $$c^i_x$$ be their respective cardinals. Then the partition structure of $$R_x$$ affects $$m_x$$ other rows, saying that if $$a\in R^i_x$$ then the $$g(x,a)$$-th row has at least $$c^i_x$$ elements (partitions). In particular, if $$R_x$$ has exactly two elements, then it has $$R^1_x, R^2_x$$ with cardinals $$n/2+k, n/2-k$$, and hence there are two other rows with at least $$n/2+k$$ and $$n/2-k$$ elements respectively (so having at least $$2$$ elements per row is not the end of the story when accounting for the sum).

Also of potential interest is that $$R^i_x$$ forces $$g(x,\cdot)$$ to have at least $$c^i_x$$ different elements in its range (which may be quite more than $$n^{1/2}$$).

At the moment I don't see how to integrate the global conditions arising from the partitions of all rows in order to find the minimal sum (because a "descendant" row can have its "parent" as "descendant"). Do you have any ideas? :star_struck:

But we can show that $$F(n)$$ cannot be $$n^2/2$$: the following optimal model for size $$n=6$$ shows $$F(6) = 15 < 18 = 36/2$$.

[*Spoiler: MODEL — omitted*]
Nevertheless, this combinatorial problem doesn't fully capture all the restrictions of your original 677-inspired problem, for which I still believe $$F(n)$$ may be bounded from below by $$n^2/2$$, and for which a check of all isoclasses for sizes $$4-6$$ suggest more: that even for each fixed row, the cardinal of the range cannot be smaller than $$n/2$$ (may be a small-numbers mirage). Here the fact that $$f,g$$ are related through the product is relevant, and not fully captured by condition 2) in my problem above (e.g. we have $$g(y*x,f(x,y)) = y$$).

**Ibrahim Tencer:**

Some assorted observations:

- Notice that the argument translated by @Terence Tao  [above](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486686097) shows that there is a unique $$y$$ such that $$L_y$$ fixes $$x$$. In a linear model $$1 - b$$ is invertible iff every $$L_y$$ fixes some $$x$$, in which case there is a bijection between fixers and fixpoints. (Notice that in Type 1 models $$1 - b = a$$, so we know it's invertible. Not sure about Type 2 -- is $$1 - b$$ always invertible if nonzero?) We might try to find a counterexample where all of the $$L_x$$ have no fixpoints, or show that it can't exist.
- In a linear model $$L_k = 1$$ implies $$k = 0, (a, b) = (4, 1)$$ and that the characteristic is 7. And in fact these models all work.
- In all cyclic linear models other than the characteristic 7 ones above (and the order 9 and 16 models), all of the $$L_x$$'s appear to be conjugate as permutations, and always have orbits of equal size other than the unique fixpoint - not sure why this is. But it is not true in the order 25 model, and this is also a model where some $$L_x$$ is neither the identity nor has <= 1 fixpoints: $$L_{7k}$$ fixes $$7k$$ through $$7k + 6$$.

I also tried to manually prove that there is no model (or countermodel) of various orders in order to gain some insight, here are a couple small results:

- $$L_a$$ cannot have a 2-cycle containing $$a$$.
- If $$ab = b$$ and $$ba = a$$ then $$a = b$$, i.e. there are no mutual fixpoints.

It wasn't too hard to show that there's no model of order 2 or 3, but even at order 4 the cases start to become unmanageable, there seems to be no clear pattern. So then I wrote a finite model builder in Ruby specialized to finding a counterexample for 677 => 255, it's much slower than Vampire (got up to size 7 in runs, and non-exhaustively -- it assumes the model consists only of left powers of the counterexample) but also easier to change and can give intermediate output. Code is [here](https://github.com/ibrahimtencer/magma_rb) along with some general code about linear models and 1518 and 677 in particular.

Note that all models found so far, including the extension models, are cancellative. If a magma is linear then

$$L_0(x) = a0 + bx = bx$$

$$R_0(x) = ax + b0 = ax$$

So if it's cancellative and finite, $$a$$ and $$b$$ must be invertible, and

$$L_0^{-1}(x) = b^{-1}x$$

$$R_0^{-1}(x) = a^{-1}x$$

so we can recover the addition operation via

$$x + y = (R_0^{-1}x)\diamond (L_0^{-1}y)$$

So more generally, if a magma $$(M, \diamond)$$ is cancellative and has an idempotent $$z$$ then this construction will work and give an auxiliary cancellative magma $$(A(M), +)$$ with the same carrier in which we have $$x \diamond y = f(x) + g(y)$$ for some invertible functions $$f, g$$ that fix $$z$$. Then $$z$$ is a 2-sided identity for $$+$$, but $$+$$ need not be either associative or commutative, nor do $$f$$ and $$g$$ need to be homomorphisms (distributive). This is similar to the twisting construction.

I tested this on the extension models found by @Matthew Bolan  [here](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486848334). All of them have idempotents (and sometimes every element is an idempotent). Some of them don't give a commutative auxiliary magma for any choice of idempotent, some give a commutative one for only a single choice of idempotent. But only three give an associative auxiliary magma: the first (index 0) magma (of order 25), and two magmas of order 121 (at indices 98 and 240). All three are idempotent, and any element works as the 0. 

Note that a finite cancellative unital magma will have both left and right inverses because $$L_x$$ and $$R_x$$ are surjective. If the magma is commutative then they are equal by cancellativity, and if the magma is associative these inverses will be equal by the usual argument. So in fact all of the commutative auxiliary magmas have inverses including the three associative ones, so they are in fact abelian groups. And according to my calculations the functions are also homomorphisms, so these could be linear. I am not sure how to determine whether they admit a ring structure that makes the homomorphisms into left-multiplication operations.

All code is [here](https://github.com/ibrahimtencer/magma_rb), along with the three pseudolinear magmas and their associated abelian groups (in magma_tables.rb) for anyone who wants to see or check for themselves.

**Bernhard Reinke:**

Here is a question that hopefully can give a new line of attack: Is there a finite group $$G$$ with subgroup $$H$$, such that there is a word $$w(x,y) \in G \sqcup  \{ x^{\pm 1}, y^{\pm 1}\} $$, such that $$w(x,y) \in H $$ for $$x,y \in H$$, so that $$w$$ defines a magma structure on H that satisfies 677 (but not 255)? I tried to do this with words of the form $$w(x,y) = x * a * y^{-1} * x * b $$ or $$ w(x,y) = x * a * x^{-1} * y * b $$. Note both words actually define something translation invariant. I can recover the ["flexible" translation invariant affine model](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488926120) on $$Z / 31 Z$$. Unfortunately it seems that they always satisfy 255.

For left cancellation, I think it is a good idea if $$y$$ appears exactly once (as $$y$$ or $$y^{-1}$$) in w. I think in order to avoid the issues of right cancellation as in [here](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488957686), we should consider words where x appears to the left and the right of y.

**Bruno Le Floch:**

Nice, so it's a nonabelian generalization of linear models.  If we only use a single $$y$$ then the expression can maybe be abstracted as $$x\diamond y = f(x) y g(x)$$.  Given a group's multiplication table we could use ATPs to seek solutions f,g to the resulting equation
```math
x = f(y) f(x) f(f(y)xg(y)) y g(f(y)xg(y)) g(x) g(y) .
```

It looks complicated in general, so I considered the case $$x\diamond y = x y x$$, so that the equation is $$x = (yx)^2 y^3 (xy)^2$$ and thought about groups with an exponent $$n$$ (large enough, for now).  Then multiplying the equation with $$x(yx)^{n-3}$$ on the left and right gives $$(xy)^{n-3} x^3 (yx)^{n-3} = y$$, which after swapping $$x,y$$ becomes $$x = (yx)^{n-3} y^3 (xy)^{n-3}$$.  Applying the original equation to simplify the middle $$y^3$$ gives $$x = (yx)^{n-5} x (xy)^{n-5}$$, which has a $$x^3$$ in the middle hence simplifies further to $$x = (yx)^{n-8}y^3(xy)^{n-8}$$ etc:
```math
x = (yx)^{n-5k} x (xy)^{n-5k} , \quad
x = (yx)^{n-3-5k} y^3 (xy)^{n-3-5k} .
```
If $$n=1\mod 5$$ then $$x=yx^3y$$, and inserting this (twice) in the original equation gives $$x=y^3$$ for all $$x,y$$ so the magma has a single element.  If $$n=2\mod 5$$ then $$x=yxyx^3yxy$$ and the same happens.  If $$n=3\mod 5$$ then we directly get $$x=y^3$$.  If $$n=4\mod 5$$ then $$x=yxy^3xy$$, which inserted in the equation gives $$x=yx^3y$$ and we conclude as in the first case.  On the other hand, if the exponent is a multiple of $$5$$ there is no inconsistency, the equation with $$k$$ eventually gives $$x=x$$ or gives back the original equation.

So I would say that working in a non-abelian group of exponent 5 is promising.

**EDIT: I forgot that for a 255 counterexample we can restrict to a magma with a single generator.  If the operation is $$x\diamond y = xyx$$ then our magma will be a subset of $$\{x^n,n\in\mathbb{Z}\}$$, so it's equivalent to working in an abelian group, and hence with a linear model $$x\diamond y = 2x+y$$, which is why I got an exponent/period of $$5$$.  We really need the more complicated Ansatz of Bernhard.**

**Bruno Le Floch:**

@Ibrahim Tencer  I think it is good to try to see if by any chance all of the linear and cohomological models share some properties that can be abstracted and perhaps proven for general models.

- Terry's argument tells us that $$y\diamond x=x$$ implies $$y = (x\diamond x)\diamond x$$ actually, so indeed we have uniqueness.  It's interesting that the map $$x\mapsto (x\diamond x)\diamond x$$ from fixpoint to fixer is bijective in all linear models (except one).  Is it also the case in cohomological extensions?  The one exception that you mentioned is the unique characteristic $$7$$ model with $$a=4,b=1$$ (the constant terms is irrelevant so there is a unique such model up to isomorphism); otherwise $$1-b$$ is always invertible.

- An explanation for why $$L_x$$ of linear models are conjugate by a bijection $$f(y)=y+k$$: we have $$f(L_x(f^{-1}(y)))=ax+b(y-k)+k = a(x + a^{-1}(1-b)k) + by = L_{x+a^{-1}(1-b)}$$, which can typically reach all $$L_x$$, unless $$1-b$$ is non-invertible.  I didn't track down why there are two other exceptions of order 9 and 16, it might be interesting.  It's really interesting that the cohomological models are richer in this respect.  It might be possible to get some intuition about the "flow of information" by looking at these models.

- One thing to investigate by hand/script maybe would be whether we can make a model of size $$n$$ with some undetermined entries (that will be later set to values larger than $$n$$) that obeys the magma rule whenever all the relevant entries are determined, then slowly add more elements (increase $$n$$) as needed, and try to make multiplication tables that are as full as possible.  One has to impose left-cancellability properly to avoid creating permanent obstructions that will never disappear as we increase $$n$$.

You don't need anything to get a ring: the homomorphisms of an abelian group $$G$$ are such a ring if I understand correctly.

**Ibrahim Tencer:**

Yeah I had a similar thought. I ran a few of the auxiliary magmas through the Finite Model Explorer but the results aren't too promising. The (first) auxiliary magmas for #2, #3, #10 satisfy no nontrivial laws. #47 only satisfies commutativity and its implications.

So, not much of a pattern just looking at equational laws at least. I can try to run all of them through it with a script later (hopefully it won't hit the site too hard - is there a local version?). Looking at how the two functions act might give more of an explanation.

"Is it also the case in cohomological extensions?"

I checked the first few magmas in the file and no they didn't have that property. Probably just a cyclic linear phenomenon.

Can you spell that out more? The endomorphisms of an abelian group do form a ring but I don't think there's a natural way to embed the group inside the ring (which is how we've basically been thinking of linear models, as defined using only ring operations). Anyways it's probably not too important to know whether it's a "real" linear magma, it's more of a side question.

**Vlad Tsyrklevich:**

`scripts/explore_magma.py`

**Bruno Le Floch:**

The point is that we don't actually have to embed the group inside the ring to define a linear model: you only need the ring to act on the abelian group to define $$x\diamond y = a\cdot x + b\cdot y$$ (with the dot denoting the action of ring elements $$a,b$$ on group elements $$x,y$$) and compute expressions such as $$(x\diamond y)\diamond z = a\cdot (a\cdot x+b\cdot y)+b\cdot z=a^2\cdot x+(ab)\cdot y+b\cdot z$$ with all the usual distributive rules because by definition of an action we have $$a\cdot(b\cdot y) = (ab)\cdot y$$.

So if you have a magma on $$G$$ with an idempotent $$0$$ such that $$L_0$$ and $$R_0$$ are invertible, and if $$x+y=R_0^{-1}(x)\diamond L_0^{-1}(x)$$ defines an abelian group structure on $$G$$, and if $$L_0$$ and $$R_0$$ are homomorphisms of $$(G,+)$$, then the magma is linear in the sense that $$x\diamond y = R_0(x) + L_0(x)$$ with $$L_0,R_0\in\mathrm{End}(G)$$.  It's a lot of conditions, and unfortunately they are not fulfilled as you found in your investigations of the auxiliary magma.

**Zoltan A. Kocsis (Z.A.K.):**

Interesting. I [tried a group-words approach](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/Confluence.20question.2Fidea/near/477671396) to refute `1112->8` with infinite groups back in October. Nothing came of it, but perhaps I should revisit the code I wrote back then to see if it contains anything that'd be useful for this question (though unlikely).

**Zoltan A. Kocsis (Z.A.K.):**

The Finite Magma Explorer runs its magma computations locally on your computer. The only load it places on the server is serving up the website, but the website is hosted on Github, so it won't really matter. Having long `?magma=` query strings does place a bit of a unnecessary load on Microsoft's servers, but not anything they can't cope with.

If you have [Elm](https://guide.elm-lang.org/install/elm.html), you can do everything locally by saving `https://teorth.github.io/equational_theories/fme/unknowns.json` in `equational_theories/tools/fme/dist/`, then running `elm reactor` in `equational_theories/tools/fme/` and calling `http://localhost:8000/dist/index.html?magma=...`.

**Zoltan A. Kocsis (Z.A.K.):**

Okay, I repurposed some of the old Python and GAP code I had, and can now make the following partial observations:

There is no group `G` of order less than 256 and word `w(x,y)` of length less than 5 for which $$x \diamond y = w(x,y)$$ satisfies Equation677 but not Equation255.

I am now running a search for words `w(x,y)` of length less than 7 with two parameters `z,w` each occurring once from the group `G`. So far up to order 18, no hits (needless to say, I won't run this up to 256 😃, will probably stop once I hit a few nonabelian grouos of odd order).

**Zoltan A. Kocsis (Z.A.K.):**

Okay, using  GAP I have managed to exhaustively check that:
- For all groups $$G$$ of order less than 256 and all words $$w(x,y)$$ of length less than 7, the operation $$x\diamonds y= w(x,y)$$ defined on all of $$G$$ is not a counterexample to `Equation667 => Equation255`.
- For all groups $$G$$ of order less than 48, all elements $$g_1,g_2 \in G$$ and all words $$w(x,y,c_1,c_2)$$ of length less than 8 in which the letters $$c_1,c_2$$ occur exactly once, the operation $$x \diamond y = w(x,y,g_1,g_2)$$ defined on $$G$$ is not a counterexample to `Equation677 => Equation255`.

(*edit*: rewritten using fewer double negatives)

**Zoltan A. Kocsis (Z.A.K.):**

The smallest word operation on a non-Abelian group that satisfies 677 at all seems to be
```
Group ID: [ 125, 3 ]
Structure: (C5 x C5) : C5
Word: xxY
```

You can present `[125,3]` as follows:
```
polycyclic group with 3 pc-generators and relations:
g1^5 = id
g2^5 = id
g3^5 = id
g2^g1 = g2*g3
all other pairs of generators commute
```

**Zoltan A. Kocsis (Z.A.K.):**

The URL is too long for Zulip, but you can copy-paste the file below into FME to see the resulting 125-element magma. 
Judging by the large number of equations it satisfies, I'd not be surprised if one could show it isomorphic to a linear model.
[attached: magma125.in]

**Ibrahim Tencer:**

Wait a sec, I was answering a different question (about the cycle types being all the same). In the extensions L_x always has a unique fixpoint in 287 out of 346 cases. Here are the cases where it does or doesn't and their orders:

[*Spoiler: unique fixpoints? — omitted*]

**Ibrahim Tencer:**

and 65 of those cases are idempotent (in which case L_x must have a unique fixpoint)

[*Spoiler: idempotent? — omitted*]

**Zoltan A. Kocsis (Z.A.K.):**

One more cheap exhaustive check, just to make sure we're not missing any low-hanging fruit. Call a magma operation $$x \diamond y$$ boring if it has the form $$x \diamond y = x^n y^m$$ for some $$n,m \in \mathbb{Z}$$ over a finite group $$G$$.  The only non-Abelian group of order < 256 which admits a boring operation satisfying 677 is `[125,3]` given above.

**Bruno Le Floch:**

Part of your search space @Zoltan A. Kocsis (Z.A.K.)  is already ruled out by some immunities.  Consider a finite counterexample of 677->255 that is a subset $$M\subset G$$ of some group (possibly infinite), equipped with $$x\diamond y = w(x,y)$$ with $$w$$ a word in the letters $$x,y$$ and some constants in $$G$$.

- $$w$$ cannot consist only of $$x$$ and $$y$$; otherwise the submagma of $$M$$ generated by a counterexample $$x$$ of 255 is simply contained in the subgroup $$\{x^n,n\in\mathbb{Z}\}\subset G$$ which is abelian, so the magma is linear, but we already ruled out such counterexamples.

- $$w$$ cannot take the form $$w_1(x)w_2(y)$$ nor $$w_2(y)w_1(x)$$.  First we show that $$w_1$$ is injective: if $$w_1(y_1)=w_1(y_2)$$ then $$L_{y_1}=L_{y_2}$$ then for any (irrelevant) $$x$$ we have $$x=L_{y_i}(L_x(L_{L_{y_i}(x)}(y_i)))$$, and the only difference between $$i=1,2$$ is the last $$y_i$$, so left-cancellativity implies $$y_1=y_2$$.  Then injectivity of $$w_1$$ implies that the operation is right-cancellative and it cannot be a counterexample.

- We need $$y\mapsto w(x,y)$$ to be injective on from $$M$$ to $$M$$.  If we take $$M=G$$ (which I think you are doing) then the easiest way to satisfy that is to take $$w(x,y)=f(x)y^b g(x)$$ with $$b$$ an integer coprime with $$|G|$$ (or equivalently with the group's exponent, or the order of every group element).

- If $$M=G$$ and the word $$w$$ only involves a single constant $$g$$ (in addition to $$x,y$$) then the equation has to hold for $$x=g^k$$ and $$y=g^l$$, so that the overall powers of $$x,y,g$$ in $$w$$ have to be the coefficients $$a,b,c$$ in a linear model on $$\mathbb{Z}/q\mathbb{Z}$$ with $$q$$ the order of $$g$$ in $$G$$.  This restricts the words quite a lot, especially if we think the form should be $$w(x,y)=u(x)y^bv(x)$$.  Then we could go through the low-order linear models, for instance the 5-element one with $$a=2,b=-1,c=0$$ so for instance $$w(x,y)=gxy^{-1}g^{-1}x$$ or $$w(x,y)=xgy^{-1}g^{-1}x$$ with $$g^5=1$$.  The first example here is ruled out by noting that idempotent models are solutions of 255, but the second is not.

**Zoltan A. Kocsis (Z.A.K.):**

@Bruno Le Floch Thanks, a nice collection of observations. I was aware that this hits some known immunities, calling the models above boring was no accident. My goal with the search was not finding potential counterexamples, I just wanted to see whether it's cheap-and-cheerful to construct yet-unseen 677-models by considering words over *small* non-Abelian groups, and after trying some templates, I'm satisfied that it isn't.

**Ibrahim Tencer:**

Here's something interesting. I noticed that there were never any distinct elements a, b in a finite 677 model such that $$ax = bx$$ for all x. And in fact there can't be: if there is, then $$x = a(x((ax)a) = b(x((bx)a)$$ and $$x = b(x((bx)b)$$ so then $$a = b$$ by canceling three times. But notice that all we need here is for $$L_a$$ and $$L_b$$ to agree on two points: $$ax = bx$$ and $$b(x((ax)b)) = a(x((ax)b))$$ (or $$a(x((ax)a)) = b(x((ax)a))$$, or put another way $$L_a^{-1}x = L_b^{-1}x$$). So a finite 677 model is "almost" right-cancellative. If we could say that $$ax = bx$$ implies $$a(ax) = b(bx)$$ then it would show right cancellation because $$L_a^{-1}$$ is a positive power of $$L_a$$ due to finiteness.

**Bruno Le Floch:**

How far was an exhaustive search of 677->255 counterexamples pushed?  With the following code I ruled out sizes up to 9 in ten seconds, but I killed the size 10 run after half an hour.  Maybe @Jose Brox already pushed this farther (without assumptions beyond 677)?
`[*Spoiler: mace4 code — omitted*]
assign(selection_order, 2).
assign(selection_measure, 1).
formulas(sos).
x=y*(x*((y*x)*y)).     % eq 677
x=(y*x)*((y*(y*x))*y). % consequence of 677
x*y = x*z -> y = z.
end_of_list.
formulas(goals).
x=((x*x)*x)*x.
end_of_list.
```
````

**Jose Brox:**

That's a good question that I posed to myself two days ago. I *believe* that I exhausted size 12, but couldn't find the proof for it (and I've lost some files due to a blackout), so I simply restarted the search again. Size 10 is ruled out, I have 11-13 in parallel now. With your script you have remembered me that the consequence of 677 in fact speeds up the search, so I have changed the script. Thanks!

**Jose Brox:**

I think this is a particular case of [my small exploration](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/489597701) of @Terence Tao's [two conditions idea](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/489094438): Since we have $$x = a(x((ax)a))$$ , $$L_a^{-1}x = x((ax)a)$$ and by left cancellation $$L_a^{-1}x = L_b^{-1}x$$ if and only if $$(ax)a = (bx)b$$, i.e., iff $$f(x,a) = f(x,b)$$ in Tao's terminology. I showed that by injectivity of $$L_y$$, if $$a\neq b$$ and $$L_a^{-1}x=L_b^{-1}x$$ then $$f(L_a^{-1}x,a)\neq f(L_a^{-1}x,b)$$, what implies that $$L_a^{-1}L_a^{-1} x \neq L_b^{-1}L_a^{-1}x$$. In other words, if $$L_a^{-1}L_a^{-1} x = L_b^{-1}L_a^{-1}x$$ (as would happen when $$ax = bx \Rightarrow a(ax) = b(bx)$$ in the finite case) then we must have $$a=b$$.

**Jose Brox:**

I'm leaving on vacation in a few hours! I will try to reappear around January 5th. Here I report about another idea I've worked with last week, I hope you can get some juice from it.

One clear problem we have is the rigidity of 677: it doesn't imply many other identities, so it is satisfied by fewer models, hence the finite search against 255 is costly. Given an equation $$p$$, call a *relaxation* to any equation $$q$$ such that $$p\Rightarrow q$$ (call $$p$$ a *constriction* of $$q$$). Obvious facts: A relaxation $$q$$ of $$p$$ has more models than $$p$$ has, and $$q$$ is a necessary condition for a model to satisfy $$p$$. If $$q\Rightarrow r$$ then necessarily $$p\Rightarrow r$$. To show that $$p\not\Rightarrow r$$, it may be easier to start with a model of $$q\not\Rightarrow r$$ and then modify such model to get the desired one.

Most relaxations may be trivial, at least to the human eye (i.e., substitutions), but perhaps we can find some interesting ones, or some easier for the ATPs to establish proofs with. With this in mind, I have tried to determine the relaxations of 677 up to 13*10^6. The (mostly raw) results follow:
[*Spoiler: IMPLIED BY 677 — omitted*]
Of these, equivalent to 677 when left multiplication is bijective (some obviously so):
[*Spoiler: EQUIVALENT TO 677 WITH LEFT BIJECTIVITY — omitted*]
While not equivalent to 677 with left multiplication bijective are:
[*Spoiler: NOT EQUIVALENT TO 677 WITH LEFT BIJECTIVITY — omitted*]
Interestingly, of these some don't imply 255 even with left multiplication bijective, so **are good candidates to try to find countermodels by modification**:
[*Spoiler: DON'T IMPLY 255 WITH LEFT BIJECTIVITY — omitted*]
The most promising seem to be 
```
1466035: x = y * (y * ((x * ((y * x) * y)) * (x * y))).
3919117: x = (y * y) * (x * (((y * y) * x) * (y * y))).
10383419: x * x = y * ((x * x) * ((y * (x * x)) * y)).
```
On the other hand, there are identities with inconclusive computation for being relaxations of 677 (some obviously so), when given 30s each in Prover9/Mace4:
[*Spoiler: INCONCLUSIVE RELAXATIONS — omitted*]
Of these, some are relaxations when bijectivity of left multiplication is added (the rest are all still inconclusive, with 130s for Prover9/Mace4):
[*Spoiler: INCONCLUSIVE WITH LEFT BIJECTIVITY — omitted*]
Interestingly, of the inconclusive ones there are some that imply 255 when left multiplication is bijective, so **if we can show that 677 indeed implies any of these, then 677 implies 255 in the finite case**:
[*Spoiler: INCONCLUSIVE IMPLYING 255 — omitted*]
And that's all, folks! I also did some work with constrictions of 677, but I don't have the time to upload the results. See you soon, Merry Christmas, and have fun!

**Ibrahim Tencer:**

FYI, only a few of the extension models have f or g as a homomorphism:

`[0, 3, 98, 240, 281, 283, 284, 292, 294, 295]`

The pseudolinear ones 0, 98, 240 have f and g as a homomorphism for any choice of idempotent.

For #3, only f is a homomorphism in one case (#3)

And for the rest, only g is a homomorphism and only in case 0.

**Terence Tao:**

Recording a negative result that I found somewhat instructive.  I considered the general extension method of trying to build a finite 677 magma $$(x,s) \diamond (y,t) = (x \diamond y,s \diamond_{x,y} t)$$ on a carrier $$G \times M$$ where $$G$$ already obeys 677.  Ostensibly, this gives us $$|G|^2$$ equations on $$|G|^2$$ operations $$ \diamond_{x,y}: M \times M \to M$$, namely
$$ t = s \diamond_{y, x((yx)y)} ( t \diamond_{x, (yx)y} ( (s \diamond_{y,x} t ) \diamond_{yx,y} s ).$$
So one could naively hope to just randomly assign the $$\diamond_{x,y}$$, so that there are $$(|M|^{|M|^2})^{|G|^2}$$ possibilities, and hope from random heuristics that each choice has a $$1 / (|M|^{|M|^2})^{|G|^2}$$ of working, so we might get a solution out of this.

Besides being computationally prohibitive, this approach ignores the fact that the $$\diamond_{x,y}$$ have to be left-invertible for this method to have a chance of working.  So one could try to modify the approach so that the $$|M|^{|M|^2}$$ arbitrary magma operations are replaced with left-cancellative ones, of which there are some number $$L_M \leq |M|^{|M|^2}$$.  But this cuts down the number of possibilities without a necessarily matching increase in the success probability.  This can be seen by solving for $$\diamond_{yx,y}$$ in the above equation: setting $$u = s \diamond_{y,x} t$$, we can rearrange it using left-invertibility as
$$ u \diamond_{yx,y} s =  (L^{x,(yx)y}_{(L^{y,x}_s)^{-1} u})^{-1} (L^{y,x((yx)y)}_{s})^{-1}(L^{y,x}_s)^{-1} u. \quad(1)$$
The right-hand side defines some magma operation $$ u \diamond_{*} s$$, and so one can view this equation as definining $$\diamond_{yx,y}$$ in terms of $$\diamond_{y,x((yx)y)}$$, $$\diamond_{x,(yx)y}$$, $$\diamond_{y,x}$$.  If $$\diamond_{*}$$ was left-cancellative and $$\diamond_{yx,y}$$ was chosen randomly, this equation would then have a $$1/L_M$$ chance of being obeyed.  But there is no obvious reason why $$\diamond_*$$ should be left-cancellative, hence the probability that this equation is satisfied should be less than $$1/L_M$$ and now this probabilistic approach is unlikely to produce solutions.

One can hope to get around this by restricting $$\diamond_{x,y}$$ to some subclass of operations in which the right-hand side of (1) stays in the same subclass.  For instance, we have affine models $$s \diamond_{x,y} t = \alpha_{x,y} s + \beta_{x,y} t + f(x,y)$$ which basically have this property (if $$M$$ is large then most models will be left-cancellative), and are a promising approach for building 677 solutions (but unfortunately not 255 counterexamples, due to affine extension immunity).  Linear models and cohomological models are subclasses of the affine model that also enjoy basically this property (and cohomological models obey it completely, as left-cancellativity is enforced).  Partially translation invariant models $$s \diamond_{x,y} t = s + f_{x,y}(t-s)$$, with $$f_{x,y}$$ required to be injective, unfortunately do not: the right-hand side of (1) will still have the translation-invariant form, which is good, but has no reason to be injective.

So, the only extension approaches I know of that still have a good chance of randomly generating finite models are the affine ones, but we know that 677->255 is immune to all such approaches (the problem being that $$L^{x,y}_s t = L^{x,y}_{s'} t$$ implies $$L^{x,y}_s = L^{x,y}_{s'}$$ in all such models) .  If we had a separate class of extensions that was basically "closed" under (1) and did not have this immunity, then we would be back in business...

**Bruno Le Floch:**

Sorry, what are f and g here? I lost track.

**Ibrahim Tencer:**

I mean when we define the 677 magma operation in the generalized-linear way as $$x \diamond y = f(x) \cdot g(y)$$ where $$\cdot$$ is recovered using an idempotent.

**Ibrahim Tencer:**

ok I will have to think more about this. The reason it came up, by the way, is that I was trying to do the generalized linear construction on an existing 677 magma. But this can't work because f has to be non-injective, but then we will have such a pair of distinct x, x' such that $$xy = x'y$$ for all y. So the construction will preserve right-cancellativity.

**Terence Tao:**

Here is a way to construct some more finite 677 magmas, including theoretically some non-right-cancellative ones (but unfortunately doesn't get us closer to disproving 255).  One can write this law as $$L_y^{-1} x = x \diamond R_y L_y x$$, which by left cancellativity is equivalent to $$x = L_y x \diamond R_y L_y^2 x$$.  Now suppose we have a finite magma $$M$$ with a 677 operation $$\diamond$$, as well as a left-cancellative operation $$\diamond'$$ obeying the relaxed version
$$U x = U L'_y x \diamond' U R'_y (L'_y)^2 x \quad (1)$$
of this equation, for some permutation $$U: M\to M$$.  Clearly this is a more general law (677 being the special case $$U=1$$) and so one should be able to find more operations obeying this relaxed law,  in particular it should be possible to find $$\diamond'$$ here that are not right cancellative.

Since $$U$$ is a permutation, it must have some finite order, $$U^n = 1$$.  Now, locate a finite field $$F = F_p$$ with $$p-1$$ divisible by $$10n$$, so that there is a fifth root of unity $$\omega$$, with the property that the $$\omega+1$$ is a primitive element of $$F^\times$$.  Such a field should exist by a version of Artin's primitive root conjecture, and should be locatable by brute force numerical search.

Now construct an operation $$\diamond$$ on $$F \times M$$ as follows: we have
$$ (x,s) \diamond (x, t) = (x, s \diamond t)$$
and for any integer $$m$$ we have
$$ (x,s) \diamond (x+(\omega+1)^m,t) = (x - \omega (\omega+1)^m, U^{-m} (U^m s \diamond' U^m t)).$$
We claim that this obeys 677 for any $$(x,s), (y,t)$$.  For $$x=y$$ this follows from the first law.  Now suppose that $$y=x+h$$ for some $$h \in F^\times$$.  From the second law, we write
$$ s \diamond_h t := U^{-m} (U^m s \diamond' U^m t)$$
for $$h = (\omega+1)^m$$; and observe that this is periodic in $$m$$ of period $$n$$; in particular, multiplying $$h$$ by any tenth root of unity will not affect this law.  Equation 677 can then be written after some calculation as
$$ s = t \diamond_{-\omega h} (s \diamond_{(\omega+1)h} ((t \diamond_h s) \diamond_{\omega h} t)$$
which by the above invariances simplifies to
$$ s = t \diamond_{h} (s \diamond_{(\omega+1)h} ((t \diamond_h s) \diamond_{h} t)$$
and by left-invertibility and writing $$s = t \diamond_h u$$ this can rearrange to
$$ u = L^h_t u \diamond_{(\omega+1) h} R^h_t (L^h_t)^2 u$$
which one can obtain from (1).

Unfortunately, this construction uses a Type I linear base model $$x \diamond y = x - \omega(y-x)$$ in which every element is idempotent, and so for the purpose of testing 255 we never get to use the second law for $$\diamond$$ and only the first law.  So this doesn't directly get us any closer to refuting 677=>255, but it may give some broader intuition as to what 677 finite magmas can look like.

**Ibrahim Tencer:**

Consider generalized-linear models of the form $$x \cdot y = f(x) * g(y)$$, with $$*$$ being the source operation (what was called auxiliary above).

If $$*$$ is left-cancellative and $$g$$ is invertible then $$\cdot$$ is also left-cancellative because $$ x \cdot y = x \cdot y'$$ implies $$f(x) * g(y) = f(x) * g(y')$$, so $$g(y) = g(y')$$ by left-cancellativity of $$*$$ and then $$y = y'$$ by injectivity of $$g$$.

But also, if $$\cdot$$ is left-cancellative, then $$g$$ is injective: if $$g(y) = g(y')$$ then $$f(x) * g(y) = f(x) * g(y')$$ for any arbitrary x so $$x \cdot y = x \cdot y'$$ so $$y = y'$$.

And if $$f$$ and $$g$$ are surjective then $$\cdot$$ being left-cancellative implies that $$*$$ is left-cancellative too: if $$x * y = x * y'$$, let $$x = f(w)$$, $$y = g(z)$$, and $$y' = g(z')$$. Then $$f(w) * g(z) = f(w) * g(z')$$ i.e. $$w \cdot z = w \cdot z'$$, so $$z = z'$$ by left-cancellativity of $$\cdot$$, so $$y = y'$$.

We showed [above](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/490422166) that f has to be a bijection in a finite generalized-linear 677 model, so $$*$$ must also be left-cancellative, and in a countermodel it can't be right-cancellative because $$f$$ is a bijection so then $$\cdot$$ would be right-cancellative too. (This also implies that $$*$$ can't be commutative or have two-sided inverses, which immediately rules out anything like linear countermodels.)

So to summarize: in a generalized-linear countermodel $$f$$ and $$g$$ are both bijections and the source magma is left-cancellative but not right-cancellative (and therefore neither commutative nor having right inverses).

This may help! Maybe I'm missing something but without right-cancellativity I don't see any reason why this won't work as a source magma for a generalized-linear countermodel (even if $$x^2 = x$$ which as I understand it does in this construction). We know 255 is equivalent to every x having some $$y$$ with $$y \cdot x = x$$, so $$g$$ can't be the identity, but it may still be possible in general.

**Matthew Bolan:**

I'm having trouble finding any solutions to $$Ux = UL'_y x \diamond' UR'_y(L'_y)^2 x$$ which are not right cancellative. Currently searching order 9. 

I am on vacation and so have not been following so closely lately, however I am intrigued by Zoltan's order 125 example. It is not linear as $$L_0 L_1^{-1} L_0 L_{2}^{-1}(0) \not = L_0 L_{2}^{-1} L_0 L_{1}^{-1}(0)$$, so it might be something new.

**Bruno Le Floch:**

I had missed Zoltan's example.  Is it $$x\diamond y=x^2 y^{-1}$$ in a group of exponent 5?  Could it simply be a cohomological extension of the 5-element 677-magma?  If so, it should partition into submagmas of order 25.

**Pace Nielsen:**

The following re-expresses some obvious consequences of finiteness, which might have some potential.  Given any finite set $$S$$ and any self-map $$f\colon S\to S$$, there must exist some nonnegative integer $$n$$ and positive integers $$k$$ such that $$f^{n+k}=f^n$$.  In particular, we could take taking $$S$$ to be a finite magma satisfying 677, and take $$f$$ to be left multiplication by some $$y\in S$$.  Since $$f$$ is invertible, we may as well take $$n=0$$, and so $$k$$ is just (a multiple of) the order of the left multiplication by $$y$$ map.  We can make $$k$$ independent of $$y$$, by replacing it with the lcm of all such $$k$$'s (as $$y$$ varies).  Thus, we should expect an equation like 513 [which corresponds to taking $$k=4$$] to hold in such a magma.

We can repeat this argument, but now with $$f$$ taken to be right multiplication by $$y$$.  Here, we don't want $$n=0$$, on pain of getting 255.  Taking $$n=1$$, then Vampire tells us that small values of $$k$$ are not allowed.  I wonder if this might help search for examples.  For example, we could assume 677+513+(n=5 and k=1 for right mult.), and look for examples in size 20.  Or instead take n=6, and look for examples in size 24.  Or perhaps modify 513 a bit to allow other possibilities.

Another thought I had was to consider taking $$f$$ above to be $$R_y\circ L_y$$, and doing a similar analysis.

**Bruno Le Floch:**

Throughout this discussion, we've had quite a few constructions, and ruled them out in different senses: some of them preserve right-cancellativity, some of them preserve `∀x∃y,y*x=x`, and some preserve idempotence or some other properties when restricted to the submagma generated by any given element.  I don't have time now but we should be very careful about which construction preserves what: maybe we can put together several constructions that would successively break right-cancellativity and then `∀x∃y,y*x=x` (or vice-versa).

**Bruno Le Floch:**

Just like twisting can be done with two different automorphisms, I suspect Terry's last construction could involve a pair of permutations instead of powers of a single one.

Terry's last construction is a magma extension $$(x,s)\diamond(y,t) = (x\diamond y, s\diamond_{x,y} t)$$ of a type 1 linear model $$G$$, with a useful Ansatz for the $$|G|^2$$ operations $$\diamond_{x,y}$$ that expresses all of them in terms of a single one (actually special-casing $$\diamond_{x,x}$$ to all be equal to another operation) in such a consistent way that the $$|G|^2$$ equations reduce to a single equation.  Maybe the general Ansatz could be
```math
s\diamond_{x,y} t = h_{x,y}( f_{x,y}(s) \diamond g_{x,y}(t) )
```
where `f_{x,y},g_{x,y},h_{x,y}` are chosen such that the resulting $$|G|^2$$ equations on $$\diamond$$ coincide.

I suspect the order-31 model $$x\diamond y=5x-4y+1\mod 31$$ that is in some sense the only one of type 1 and 2 could serve as a useful basis for a similar construction, but one has to find a variant of the idea of keeping all $$\diamond_{x,x}$$ the same, and treating the other $$\diamond_{x,y}$$ separately.

**Zoltan A. Kocsis (Z.A.K.):**

Thanks for checking this! Alas, I think @Bruno Le Floch 's suspicion about it being cryptomorphic to a cohomological construction is probably correct; indeed, one can partition the magma into disjoint submagmas of order 25 as follows:

```
Part 1: [1, 2, 6, 8, 15, 18, 29, 33, 48, 52, 53, 56, 60, 73, 77, 81, 92, 96, 99, 107, 110, 112, 117, 119, 120]
Part 2: [4, 5, 7, 12, 14, 17, 25, 28, 32, 43, 47, 51, 64, 68, 71, 72, 76, 91, 95, 106, 109, 116, 118, 122, 123]
Part 3: [10, 11, 13, 16, 22, 24, 27, 31, 39, 42, 46, 50, 59, 63, 67, 70, 80, 84, 87, 89, 90, 105, 115, 121, 124]
Part 4: [20, 21, 23, 26, 30, 36, 38, 41, 45, 49, 55, 58, 62, 66, 69, 75, 79, 83, 86, 88, 94, 98, 101, 103, 104]
Part 5: [0, 3, 9, 19, 34, 35, 37, 40, 44, 54, 57, 61, 65, 74, 78, 82, 85, 93, 97, 100, 102, 108, 111, 113, 114]
```

In the meantime, I checked that similar examples can be obtained in orders `7^3=343` and `5^4=625`; but we don't have them in orders `3^3 = 27`, `4^4=64`, `3^4=81`, and `6^3=216`. I think this leads further credence to the hypothesis that these non-Abelian group models arise from smaller linear models (Abelian group models) which exist in orders 5 and 7, but not 3,4,6. Of course, it still might be worth analyzing what actually happens in the other orders, but to me it didn't look that promising for constructing counterexamples.

**Ibrahim Tencer:**

The order-125 model is idempotent, and oddly enough for any choice of idempotent produces an *associative* source model (for the generalized-linear construction) which is however *not* commutative. This is the only example of that we have so far, all the other extensions have sources that are both associative and commutative, only commutative, or neither.

But, none of the f's and g's used in the generalized-linear construction are homomorphisms, and associativity (with its consequences) is the only equation it satisfies up to order 4.

**Ibrahim Tencer:**

I guess that is not so odd given how it was constructed :) but at least it is unique compared to the other models known.

**Terence Tao:**

I managed to construct a translation-invariant finite 677 model which is not right-cancellative, though unfortunately it still obeys 255.  The carrier is $$G = {\mathbb Z}/31{\mathbb Z} \times F$$, where $$F$$ is a finite field that supports both a cube root of unity $$\omega$$ and a fifth root of unity $$\zeta$$.   To solve 677 with a translation-invariant model $$x \diamond y = x + f(y-x)$$, $$f$$ has to be invertible and one has to solve the equation
$$ f(-h + f(h) + f(-f(h)) = f^{-1}(h) - h.$$
We use the ansatz $$f(a,h) = (-2a, f_a(h))$$ for various functions $$f_a: F \to F$$, and now we need to solve the system
$$ f_{-7a}(-h + f_a(h) + f_{2a}(-f_a(h)) = f^{-1}_{-a/2}(h) - h$$
for all $$a \in {\mathbb Z}/31{\mathbb Z}$$.  To handle the $$a=0$$ case we set $$f_0(h) = -\zeta h$$, and one can verify the equation here (this is just the standard linear Type I solution $$x \diamond y = x - \zeta(y-x)$$ on $$F$$).  For the non-zero $$a$$, we use the ansatz $$f_a(h) = f^+(h)$$ when $$a$$ is a quadratic residue and $$f_a(h) = f^-(h)$$ otherwise.  Since $$2$$ is a quadratic residue mod $$31$$, but $$-7$$ and $$-1/2$$ are not, we have the system
$$ f^-(-h + f^+(h) + f^+(-f^+(h)) = (f^-)^{-1}(h) - h$$
and
$$ f^+(-h + f^-(h) + f^-(-f^-(h)) = (f^+)^{-1}(h) - h.$$
Pen and paper revealed that the choice $$f^+(h) = h$$, $$f^-(h) = -\omega h$$ solves this system.  The function $$f(h)-h$$ is not injective because of the choice of $$f^+$$, so we get a loss of right cancellativity.  On the other hand we have idempotence $$f(0)=0$$, so 255 holds.

In less translation-invariant terms, if one defines the operations $$x \diamond^+ y := y$$ and $$x \diamond^- y := x - \omega(y-x)$$ on $$F$$, one can compute that
$$ (y \diamond^- x) \diamond^- y = y \diamond^- (x \diamond^- y) = x$$
and hence one has the 677-pair
$$ x = y \diamond^+ (x \diamond^+ ((y \diamond^- x) \diamond^- y))$$
and
$$ x = y \diamond^- (x \diamond^- ((y \diamond^+ x) \diamond^+ y)).$$
The above constructions are basically a way to convert such a 677-pair to an actual 677 magma.

**Matthew Bolan:**

[attached: 677_non_right_cancellative.txt]
Here is an order $$31 *16$$ example of Terry's construction. Right cancellativity fails quite often, for example $$48 \diamond 0 = 49 \diamond 0.$$

**Matthew Bolan:**

The argument for immunity to cohomological constructions used that such constructions preserved right cancelativity - perhaps extensions of this have a shot? Unfortunately the relevant linear algebra will be in $$(31 * 16)^2 = 246016$$ dimensions, but at least it's pretty sparse...

**Bruno Le Floch:**

Cohomological extensions are a special case ($$\alpha_{x,y}$$ and $$\beta_{x,y}$$ constant) of piecewise affine extensions $$(x,s)\diamond(y,t)=(x\diamond y, \alpha_{x,y} s + \beta_{x,y} t + \gamma_{x,y})$$.  The implication 677->255 is [immune to those](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488946270) in the sense that if the base magma obeys 677 and 255 and the resulting magma obeys 677 then it obeys 255.

I proposed "twisting-extension" earlier, namely $$(x,s)\diamond(y,t) = (x\diamond y, S_{x,y}(s)\diamond T_{x,y}(t))$$.  If the base 677 magma is right-cancellative then the resulting magma is right-cancellative, but there was no direct immunity to 677->255, so there is still a bit of hope there.

**Terence Tao:**

Unfortunately my model is idempotent and so useless as a base (for the purpose of testing 255 one can restrict attention to magmas generated by a single element, hence we can restrict to base magmas that are generated by a single element.  But in the idempotent case that only leaves the trivial magma).  In the notation of my construction, all the 255 action is taking place in the $$a = 0$$ portion of the construction, while the right-cancellativity is living in the $$a \neq 0$$ portion.  

Another way of thinking about it is as follows.  We know that in order for an extension model $$(x,s) \diamond (y,t) = (x \diamond y, s \diamond_{x,y} t)$$ on $$G \times M$$ to obey 677, the base model $$G$$ must already obey 677, and we also need the system of equations
$$ s = t \diamond_{y, x((yx)y)} (s \diamond_{x, (yx)y} ((t \diamond_{y,x} s) \diamond_{yx,y} t) \quad (1).$$
Suppose we have some collection $${\mathcal O}$$ of left-cancellative magma operations $$\diamond$$ on $$M$$, and call a four-tuple $$\diamond_1,\diamond_2,\diamond_3,\diamond_4$$ of such operations "compatible" if one has the identity
$$ s = t \diamond_1 (s \diamond_2 ((t \diamond_3 s) \diamond_4 t).$$
Solving (1) then amounts to coloring the table $$G \times G$$ by elements of $${\mathcal O}$$ such that, for any $$x,y$$, the colors of $$(y, x((yx)y))$$, $$(x,(yx),y)$$, $$(y,x)$$, $$(yx, y)$$ are compatible.  We now know that $${\mathcal O}$$ can admit some non-right-cancellative operations, though they are not in the right "places" to contradict 255 unfortunately.

In my construction, I have three colors $$\diamond^0$$, $$\diamond^+$$, $$\diamond^-$$ on $$M$$, with $$s \diamond^0 t = s - \zeta(t-s)$$, $$s \diamond^+ t = t$$, $$s \diamond^- t = s - \omega(t-s)$$.  There are three compatible tuples: $$(\diamond^0, \diamond^0, \diamond^0, \diamond^0)$$,  $$(\diamond^+, \diamond^+, \diamond^-, \diamond^-)$$, $$(\diamond^-, \diamond^-, \diamond^+, \diamond^+)$$.  So I can get a valid coloring by selecting $${\mathbb Z}/31{\mathbb Z}$$ as a base with $$x \diamond y = x - 2(y-x)$$ and coloring $$(x,x+h)$$ by $$\diamond^0$$ if $$h=0$$, $$\diamond^+$$ if $$h$$ is a non-zero quadratic residue, and $$\diamond^-$$ if $$h$$ is a non-zero quadratic non-residue.  Because $$\diamond^+$$ is not right-cancellative and this color is used at least once, the entire magma is not right-cancellative.

On the other hand, if the base $$G$$ obeys 255, then for any $$x$$ we can solve $$y \diamond x = x$$, and then $$(y,x), (x, xy), (y,x), (x, y)$$ must be a colored by a compatible tuple.  So the compatible tuples we care about the most are the ones in which the first and third colors are the same, and these cases we unfortunately know that linear (or affine) operations will necessarily be right-cancellative.  So the tuples $$(\diamond^+, \diamond^+, \diamond^-, \diamond^-)$$, $$(\diamond^-, \diamond^-, \diamond^+, \diamond^+)$$ I used are not directly useful for attacking 255.  However, the broader strategy of locating pairs (or maybe larger numbers) of magma operations that generate several compatible tuples, combined with a suitable coloring of a base magma, may be potentially promising.  Unfortunately, even if such magma operations can be located, the coloring problem could be difficult: for the Type I models $$x \diamond y = x - \zeta (y-x)$$ with $$\zeta$$ a fifth root of unity, there is an affine structure to the tuples $$(y, x((yx)y))$$, $$(x,(yx),y)$$, $$(y,x)$$, $$(yx, y)$$ that makes them relatively easy to color, but these models are idempotent and so not useful.  For the other models I know of, the tuples are much more "mixing" or "expanding" and thus unlikely to be colored with a small number of colors and compatible tuples (except with the degenerate case of constant colorings).

**Terence Tao:**

Reporting a negative attempt.  I was playing around with the extension model, where the task is to solve the system of equations
$$ s = t \diamond_{y,L_y^{-1} x} ( s \diamond_{x, (y \diamond x) \diamond y} ((t \diamond_{y,x} s) \diamond_{y \diamond x, y} t). \quad (1)$$
In order to break 255, i.e., to not be able to solve $$(y,t) \diamond (x,s) = (x,s)$$ for all $$(x,s)$$ we need $$\diamond_{y,x}$$ to be non-right-cancellative for at least one $$x,y$$ with $$y \diamond x = x$$.  With my previous construction, we have non-right-cancellative behavior for some $$\diamond_{y,x}$$, but unfortunately not with $$y \diamond x = x$$.  And we know that in order to break non-right-cancellativity in this case, we need to use a nonlinear operation; linear or affine operations will allow one to solve $$(y,t) \diamond (x,s) = (x,s)$$.

I was trying a mostly linear model, where $$\diamond_{y,x}$$ is linear if $$y \diamond x \neq x$$ and non-linear if $$y \diamond x = x$$, with the hope of simplifying the large system (1) to a much more manageable system involving only one nonlinear operation.  When we have $$y \diamond x = x$$ in (1), then things look reasonably good for (1), as we will have two nonlinear operations $$\diamond_{y,L_y^{-1} x}, \diamond_{y,x}$$ while the other two operations can be checked to be linear (unless we are in the idempotent case $$x = y = Sx$$, which we want to avoid).  However, problems arise because $$\diamond_{y \diamond x, y}$$, $$\diamond_{x, (y \diamond x) \diamond y}$$ could also be non-linear.  If only one of them is non-linear then it is very unlikely that (1) is solvable (for instance, as observed earlier, one can solve for $$\diamond_{y \diamond x,y}$$ in terms of the other three operations, so if the latter three are linear, this one is linear too).  So what one would like is that these operations are nonlinear at the same time, i.e., $$(y \diamond x) \diamond y = y$$ if and only if $$x \diamond ((y \diamond x) \diamond y) = (y \diamond x) \diamond y$$.  But if both equations are true then $$x \diamond y = y$$ (hence $$x = Sy \diamond y$$, while from 677 $$Sy = y \diamond (x \diamond ((y \diamond x) \diamond y)) = x$$.  Hence $$y = x \diamond y = Sy \diamond y = x$$, and so we are back in the idempotent case $$x=y=Sx$$ which is no good for extensions.

In general, any attempt to use an extension involving a mixture of linear and nonlinear operations, with $$\diamond_{y,x}$$ non-linear for at least one $$y,x$$ with $$y \diamond x = x$$, seems to either lead to (a) a single nonlinear operation obeying 677 (which brings us back to the original problem), (b) at least one equation involving three linear and one nonlinear operation, or (c) at least one equation involving multiple nonlinear operations (so no essential simplification to the system (1)).

**Terence Tao:**

This is perhaps my last-ditch attempt to resolve this implication before throwing in the towel.  Here are two conjectures which, if both true, would refute 677 -> 255 for finite magmas:

**Conjecture 1**.  There exists a finite set $$M$$ with two operations $$\diamond_0, \diamond_1: M \times M \to M$$ obeying the three 677-like laws
$$ s = t \diamond_0 (s \diamond_0 ((t \diamond_0 s) \diamond_0 t)) \quad (1)$$
$$ s = t \diamond_1 (s \diamond_0 ((t \diamond_1 s) \diamond_0 t)) \quad (2)$$
$$ s = t \diamond_0 (s \diamond_1 ((t \diamond_0 s) \diamond_1 t)) \quad (3)$$
for all $$s,t \in M$$, and such that the equation $$t \diamond_1 s = s$$ is not solvable for at least one choice of $$s$$.

Note: if 677->255 is false for a finite magma $$(M,\diamond)$$, then Conjecture 1 is true, since we can set $$\diamond_0 = \diamond_1 = \diamond$$ in this case.  So this is a weaker conjecture than the original problem, and thus hopefully easier to establish. The point here is that only two of the four magma operations need to come from the non-right-cancellative operation $$\diamond_1$$, the others can come from the "base" operation $$\diamond_0$$, which can be a standard choice such as a Type 1 or Type 2 operation.

**Conjecture 2**: There exists a finite 677 magma $$(G,\diamond)$$ and a set $$E$$ of pairs in $$G \times G$$ obeying the following axioms:

1.  $$E$$ contains at least one pair $$(y,x)$$ with $$y \diamond x = x$$.
2. For any $$y,x \in G$$, we have $$(y,x) \in E$$ iff $$(y,L_y x) \in E$$.
3. For any $$y,x \in G$$, we have $$(y \diamond x, y) \in E$$ iff $$(x, (y \diamond x) \diamond y) \in E$$.
4. For any $$y,x \in G$$ we do not have $$(y,x)$$ and $$(y \diamond x, y)$$ both in $$E$$.

If we join two pairs in $$G \times G$$ by a blue edge if they arise in axiom 2 or axiom 3, and a red edge if they arise in axiom 4, Conjecture 2 asserts that one of the components of the blue graph has no red edges, and also contains a vertex $$(y,x)$$ with $$y \diamond x = x$$ (or equivalently $$y = Sx \diamond x$$).  So basically it's a hope that Axioms 2 and 3 do not propagate to cover so much of the pairs in $$G \times G$$ that they start violating Axiom 4.

If Conjecture 1 and Conjecture 2 are both true, we can build a 677 magma on $$G \times M$$ by declaring $$(x,s) \diamond (y,t)$$ to equal $$(x \diamond y, s \diamond_1 t)$$ if $$(x,y) \in E$$ and $$(x \diamond y, s \diamond_0 t)$$ otherwise.  The various conclusions of the two conjectures imply that this is indeed a 677 magma, and that the equation $$(y,t) \diamond (x,s) = (x,s)$$ is not solvable for at least one choice of $$(x,s)$$, giving the desired refutation.  So this factors the original problem into two independent sub-problems that are hopefully simpler to establish.

I have some hope that we can resolve Conjecture 2 with one of our existing magmas that is not completely idempotent, e.g., the Type 2 linear magmas, or the special translation-invariant magma on $$F_{31}$$ (or maybe $$F_{31^2}$$).  For Conjecture 1, my plan was to take $$\diamond_0$$ to be a translation-invariant linear magma $$x \diamond_0 y = x - \zeta(y-x)$$ with $$M$$ a finite field and $$\zeta$$ a primitive fifth root of unity, and $$\diamond_1$$ to be a non-linear translation-invariant operation $$x \diamond_1 y = x + f(y-x)$$.  Then (1) is obeyed, and axioms (2) and (3) become
$$ h - \zeta (f(h) + \zeta f(h) - h) = f^{-1}(h)$$
and
$$ h + f(-\zeta h + f(-\zeta h) - h) = -h/\zeta$$
if I computed correctly.  This can be written as
$$ f(h) = k \iff f( h - \zeta(k+\zeta k - h))  = h$$
and
$$ f(h) = k \iff f(h + k + h/\zeta) = h/\zeta^2 + h/\zeta$$
(I think).  There is already a standard solution $$f(h) = - \zeta h$$ to this system (arising from setting $$\diamond_1 = \diamond_0$$), and I am hoping that for some choices of field there is a non-standard solution for which $$f$$ has no fixed points (so basically one should modify the standard solution at $$h=0$$ and at some other points); this amounts to understanding the group generated by the linear transformations $$(h,k) \mapsto (h-\zeta(k+\zeta k-h), h)$$ and $$(h,k) \mapsto (h+k+h/\zeta, h/\zeta^2+h/\zeta)$$, and hoping that this group is relatively small for at least some choices of field.  It seems vaguely advantageous to work in a field $$M$$ that is large enough that it is not completely generated by $$\zeta$$, so that one can set $$f(0)$$ to equal something that is independent of $$\zeta$$, e.g., $$M = F_{25}$$ may be the first place to look.

It's sort of a long shot at present, but if we somehow manage to verify one of the two conjectures, then I think we have a viable strategy.

**Terence Tao:**

Grr, Conjecture 1 is immune to idempotent $$\diamond_0$$, which rules out my proposal to resolve it using the Type 1 linear models for $$\diamond_0$$.  Indeed, suppose that $$s \diamond_0 s = s$$, then by (3) $$s = s \diamond_0 (s \diamond_1 (s \diamond_1 s))$$, hence by left-cancellativity of $$\diamond_0$$ $$s \diamond_1 S_1 s = s$$ where $$S_1 s = s \diamond_1 s$$.  Now from (2) we have $$S_1 s = s \diamond_1 (S_1 s \diamond_0 ((s \diamond_1 S_1 s) \diamond_0 s)) = s \diamond_1 (S_1 s \diamond_0 s)$$, hence by left-cancellativity $$ s = S_1 s \diamond_0 s$$, hence by the 677 nature of $$\diamond_0$$, $$S_1 s = (s \diamond_0 s) \diamond_0 s = s$$, so $$\diamond_1$$ is idempotent whenever $$\diamond_0$$ is.  In particular the equation $$t \diamond_1 s = s$$ will be solvable for all $$s$$ if $$\diamond_0$$ is idempotent.

There is still a chance that one can attack Conjecture 1 using the Type 2 models for $$\diamond_0$$, butincluding the special models in characteristic 31, but this is beyond the abilities of my pen-and-paper calculations, and would likely require some computer search.

**Jihoon Hyun:**

I made a c++ program which outputs a DIMACS CNF format with $$O(n^3)$$ variables and $$O(n^4)$$ clauses. This CNF will be satisfied if there is a magma which satisfies 677 but not 255 (If I haven't messed up).

```c++
#include <iostream>
#include <vector>

int main(int argc, char *argv[]) {
    using ssize_t = long long;

    if(argc != 2) {
        std::cerr << "Usage: " << argv[0] << " [Number of elements]" << std::endl;
        return 1;
    }

    ssize_t n;
    try {
        n = std::stoll(argv[1]);
        if(n < 0) { throw std::invalid_argument("Number of elements must be non-negative."); }
        if(n > 1'000'000) { throw std::invalid_argument("Number of elements is too large."); }
    } catch(std::exception const &e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    std::vector<std::vector<ssize_t>> clauses;
    /** `var1(x, y, i)` is $X_{yx, i}$. */
    auto const var1 = [n](ssize_t const x, ssize_t const y, ssize_t const i) noexcept {
        return 1 + (x * n + y) * n + i;
    };
    /** `var2(x, y, i)` is $X_{(yx)y, i}$. */
    auto const var2 = [n](ssize_t const x, ssize_t const y, ssize_t const i) noexcept {
        return 1 + n * n * n + (x * n + y) * n + i;
    };
    /** `var3(x, y, i)` is $X_{x((yx)y), i}$. */
    auto const var3 = [n](ssize_t const x, ssize_t const y, ssize_t const i) noexcept {
        return 1 + 2 * n * n * n + (x * n + y) * n + i;
    };
    /** `var4(x, i)` is $X_{((xx)x)x, i}$. */
    auto const var4 = [n](ssize_t const x, ssize_t const i) noexcept {
        return 1 + 3 * n * n * n + x * n + i;
    };

    /** For every $x$ and $y$, exactly one of $X_{yx, i}$ for $0 \leq i < N$ is true. */
    for(ssize_t x = 0; x < n; x++) {
        for(ssize_t y = 0; y < n; y++) {
            /**
             * For each distinct pair $X_{yx, i}$ and $X_{yx, j}$ of variables,
             * there is at least one false variable. */
            for(ssize_t i = 0; i < n; i++) {
                for(ssize_t j = i + 1; j < n; j++) {
                    clauses.push_back({-var1(x, y, i), -var1(x, y, j)});
                }
            }

            /** There is at least one true $X_{yx, i}$. */
            std::vector<ssize_t> clause;
            clause.reserve(n);
            for(ssize_t i = 0; i < n; i++) { clause.push_back(var1(x, y, i)); }
            clauses.push_back(std::move(clause));
        }
    }

    /** For every $x$ and $y$, exactly one of $X_{(yx)y, i}$ for $0 \leq i < n$ is true. */
    for(ssize_t x = 0; x < n; x++) {
        for(ssize_t y = 0; y < n; y++) {
            /**
             * For each distinct pair $X_{(yx)y, i}$ and $X_{(yx)y, j}$ of variables,
             * there is at least one false variable. */
            for(ssize_t i = 0; i < n; i++) {
                for(ssize_t j = i + 1; j < n; j++) {
                    clauses.push_back({-var2(x, y, i), -var2(x, y, j)});
                }
            }

            /** There is at least one true $X_{(yx)y, i}$. */
            std::vector<ssize_t> clause;
            clause.reserve(n);
            for(ssize_t i = 0; i < n; i++) { clause.push_back(var2(x, y, i)); }
            clauses.push_back(std::move(clause));
        }
    }

    /**
     * For every $x$, $y$, and $i$, $X_{(yx)y, i}$ is true if and only if there is some $j$ which
     * $X_{yx, j}$ and $X_{jy, i}$ are true.
     *
     * As we assumed there exists a unique $i$ which makes $X_{yx, j}$ true, we may simplify the
     * proposition as follows.
     *
     * For every $x$, $y$, and $i$, $X_{(yx)y, i}$ is true if and only if for every $j$ which
     * $X_{yx, j}$ is true, $X_{jy, i}$ is also true. */
    for(ssize_t x = 0; x < n; x++) {
        for(ssize_t y = 0; y < n; y++) {
            for(ssize_t i = 0; i < n; i++) {
                for(ssize_t j = 0; j < n; j++) {
                    clauses.push_back({var1(y, j, i), -var1(x, y, j), -var2(x, y, i)});
                    clauses.push_back({var2(x, y, i), -var1(x, y, j), -var1(y, j, i)});
                }
            }
        }
    }

    /** For every $x$ and $y$, exactly one of $X_{x((yx)y), i}$ for $0 \leq i < n$ is true. */
    for(ssize_t x = 0; x < n; x++) {
        for(ssize_t y = 0; y < n; y++) {
            /**
             * For each distinct pair $X_{x((yx)y), i}$ and $X_{x((yx)y), j}$ of variables,
             * there is at least one false variable. */
            for(ssize_t i = 0; i < n; i++) {
                for(ssize_t j = i + 1; j < n; j++) {
                    clauses.push_back({-var3(x, y, i), -var3(x, y, j)});
                }
            }

            /** There is at least one true $X_{x((yx)y), i}$. */
            std::vector<ssize_t> clause;
            clause.reserve(n);
            for(ssize_t i = 0; i < n; i++) { clause.push_back(var3(x, y, i)); }
            clauses.push_back(std::move(clause));
        }
    }

    /**
     * For every $x$, $y$, and $i$, $X_{x((yx)y), i}$ is true if and only if there is some $j$ which
     * $X_{(yx)y, j}$ and $X_{xj, i}$ are true.
     *
     * As we assumed there exists a unique $i$ which makes $X_{(yx)y, i}$ true, we may simplify the
     * proposition as follows.
     *
     * For every $x$, $y$, and $i$, $X_{x((yx)y), i}$ is true if and only if for every $j$ which
     * $X_{(yx)y, j}$ is true, $X_{xj, i}$ is also true. */
    for(ssize_t x = 0; x < n; x++) {
        for(ssize_t y = 0; y < n; y++) {
            for(ssize_t i = 0; i < n; i++) {
                for(ssize_t j = 0; j < n; j++) {
                    clauses.push_back({var1(j, x, i), -var2(x, y, j), -var3(x, y, i)});
                    clauses.push_back({var3(x, y, i), -var2(x, y, j), -var1(j, x, i)});
                }
            }
        }
    }

    /** For every $x$, $y$, and $i$, if $X_{x((yx)y), i}$ is true, then $X_{yi, x}$ is also true. */
    for(ssize_t x = 0; x < n; x++) {
        for(ssize_t y = 0; y < n; y++) {
            for(ssize_t i = 0; i < n; i++) { clauses.push_back({var1(i, y, x), -var3(x, y, i)}); }
        }
    }

    /** For every $x$, exactly one of $X_{((xx)x)x, i}$ for $0 \leq i < n$ is true. */
    for(ssize_t x = 0; x < n; x++) {
        /**
         * For each distinct pair $X_{((xx)x)x, i}$ and $X_{((xx)x)x, j}$ of variables,
         * there is at least one false variable. */
        for(ssize_t i = 0; i < n; i++) {
            for(ssize_t j = i + 1; j < n; j++) { clauses.push_back({-var4(x, i), -var4(x, j)}); }
        }

        /** There is at least one true $X_{((xx)x)x, i}$. */
        std::vector<ssize_t> clause;
        clause.reserve(n);
        for(ssize_t i = 0; i < n; i++) { clause.push_back(var4(x, i)); }
        clauses.push_back(std::move(clause));
    }

    /**
     * For every $x$ and $i$, $X_{((xx)x)x, i}$ is true if and only if there is some $j$ which
     * $X_{(xx)x, j}$ and $X_{jx, i}$ are true.
     *
     * As we assumed there exists a unique $i$ which makes $X_{(xx)x, i}$ true, we may simplify the
     * proposition as follows.
     *
     * For every $x$ and $i$, $X_{((xx)x)x, i}$ is true if and only if for every $j$ which
     * $X_{(xx)x, j}$ is true, $X_{jx, i}$ is also true. */
    for(ssize_t x = 0; x < n; x++) {
        for(ssize_t i = 0; i < n; i++) {
            for(ssize_t j = 0; j < n; j++) {
                clauses.push_back({var1(x, j, i), -var2(x, x, j), -var4(x, i)});
                clauses.push_back({var4(x, i), -var2(x, x, j), -var1(x, j, i)});
            }
        }
    }

    /**
     * We want to find a case when the equation 677 (x = y(x((yx)y))) is satisfied but the equation
     * 255 (x = ((xx)x)x) is not.
     *
     * If there is some $x$ which $X_{((xx)x)x, x}$ is false, then we are done. */
    {
        std::vector<ssize_t> clause;
        clause.reserve(n);
        for(ssize_t x = 0; x < n; x++) { clause.push_back(-var4(x, x)); }
        clauses.push_back(std::move(clause));
    }

    // DIMACS CNF Generation start
    std::cout << "p cnf " << 3 * n * n * n + n * n << ' ' << clauses.size() << '\n';
    for(auto const &clause: clauses) {
        for(auto const lit: clause) { std::cout << lit << ' '; }
        std::cout << "0\n";
    }
}
```
You can get an executable with `g++ code.cpp -o generator` on any reasonable linux machine supporting c++11.

I'm not sure if this will help as there are more applicable tools in use already. However the sat attack for this problem was stuck in my head for quite a long time, and I couldn't help writing the generator.

**Pace Nielsen:**

@Jihoon Hyun Can you give a low-level explanation of how you translated this question into an SAT problem?  (And any report on runs with small values of n?)

**Jihoon Hyun:**

@Pace Nielsen [말함](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/492571347):

Let $$n$$ be the number of elements of the magma.
I declared four types of variables: $$X_{yx, i}$$, $$X_{(yx)y, i}$$, $$X_{x((yx)y), i}$$, and $$X_{((xx)x)x, i}$$. Each variables are true if and only if for given $$0\leq x<n$$ and $$0\leq y<n$$, the expression results in $$0\leq i<n$$. They are named as `var1` to `var4` in the program.

For each type of variables, the first thing to note is that given $$x$$ and $$y$$, there exists a unique $$i$$ which makes $$X_{expr,i}$$ true. This condition can be expressed by first denoting that no two distinct pair of variables are both true, and there is at least one variable which is true.

The second type of restriction comes from the expression. For example, $$X_{(expr)x, i}$$ is true if and only if there is some $$j$$ which $$X_{expr,j}$$ and $$X_{jx, i}$$ are both true. We can tweak the existing condition by using the uniqueness condition above. Also, by replacing $$i$$ with another value like $$x$$, we can restrict the CNF to satisfy the equation 677.

The last restriction lets us find the magma which satisfies the equation 677 but not 255. For this we simply check the clause of all $$\neg X_{((xx)x)x,x}$$, to see if there is any false variable.

With CaDiCaL, the cases when $$n=5,6,7$$ turned out to be unsatisfiable after a few seconds, meaning that there is no magma with 5, 6, or 7 elements which satisfies eqn 677 but not 255.

+ 10.1k seconds of CaDiCaL with $$n=8$$ showed that there is no magma satisfying 677 but not 255. However this was expected as there is no magma satisfying 677 with order 8.

**Matthew Bolan:**

I'm back from my holiday, so I decided to try tackling this conjecture. However, Prover9 suggests it is false, with input
`[*Spoiler: Input — omitted*]
x = y * (x * ((y * x) * y)).
f(1,0) & (1*0=0).
f(y,x) <-> f(y,y*x).
f(y*x,y) <-> f(x,(y*x)*y).
(-f(y,x))|(-f(y*x,y)).
```
````
and this output
`[*Spoiler: Output — omitted*]
1 f(1,0) & 1 * 0 = 0 # label(non_clause).  [assumption].
2 f(x,y) <-> f(x,x * y) # label(non_clause).  [assumption].
3 f(x * y,x) <-> f(y,(x * y) * x) # label(non_clause).  [assumption].
4 x = y * (x * ((y * x) * y)).  [assumption].
5 x * (y * ((x * y) * x)) = y.  [copy(4),flip(a)].
6 f(1,0).  [clausify(1)].
7 1 * 0 = 0.  [clausify(1)].
9 f(x,y) | -f(x,x * y).  [clausify(2)].
10 -f(x * y,x) | f(y,(x * y) * x).  [clausify(3)].
12 -f(x,y) | -f(x * y,x).  [assumption].
15 f(x,y * ((x * y) * x)) | -f(x,y).  [para(5(a,1),9(b,2))].
16 -f(x,y) | f(x * ((y * x) * y),x * y).  [para(5(a,1),10(a,1)),rewrite([5(8)])].
19 -f(x,y * ((x * y) * x)) | -f(y,x).  [para(5(a,1),12(b,1))].
43 f(1 * ((0 * 1) * 0),0).  [hyper(16,a,6,a),rewrite([7(10)])].
51 f((1 * ((0 * 1) * 0)) * 0,(1 * ((0 * 1) * 0)) * 0).  [hyper(16,a,43,a),rewrite([5(16),7(10)])].
103 f((1 * ((0 * 1) * 0)) * 0,((1 * ((0 * 1) * 0)) * 0) * ((((1 * ((0 * 1) * 0)) * 0) * ((1 * ((0 * 1) * 0)) * 0)) * ((1 * ((0 * 1) * 0)) * 0))).  [hyper(15,b,51,a)].
105 $F.  [ur(19,b,51,a),unit_del(a,103)].
```
````
The point seems to be that if $$(a,a) \in E$$, then $$(a,a \diamond((a \diamond a)  \diamond a)) \in E$$ by axiom 2, but this conflicts with axiom 4. Axioms 1 and 3 then provide such an $$a$$ pretty easily (this is in lines 16, 43, 51 of the Prover9 proof), namely $$(1 \diamond ((0 \diamond 1) \diamond 0)) \diamond 0$$, where $$1 \diamond 0 = 0$$ and $$(1, 0 ) \in E$$.

**Terence Tao:**

Ah, good to know. (I had also tested quite a few linear magmas and showed they could not be used to verify conjecture 1, so i think I’m ready to abandon this attack strategy.)

**Jose Brox:**

Hi again! Reporting on experiments and negative results after my holidays!

1. 6 experiments have been running in some size for 25 days now (e.g. 677 with 4073 anti 255 in size 14); I now know how to make them faster, but I hesitate to kill them and start again with some unknown speed up factor, since some of the others have finished in the last few days... I will eventually do it though.
2. 677 anti 255 is still in size 11 after 19 days, so there is no way I had exhausted up to size 12 before. We only know there are no models up to size 10 (included).
3. There is only one model of 677 in size 9 (the linear one). With speed ups, this was found in 6min. I'm searching for all models of sizes 10,11 now (more than 1 day of computation already).
3. There are no models of 677+513 in size 13, now looking in sizes 14-16. Size 13 needed 8h.
4. There are no models of 677+4131 in size 14 (size 15 for 5 days already).
5. There are no models of 677+4276 in size 12 (size 13 for 6 days already).
6. There are no models of 677+4591 in size 14 (size 15 for 6 days already).
7. There are no translation-invariant models (with any f) up to size 17 included (size 18 for 5 days already). Size 17 needed 25h.
8. I have several other experiments with variations of linear products (without distributivity, identity, annihilation, with weaker axioms than associativity of the product...). For the moment being, no new models of 677 have been found, although I have found some weaker underlying products giving rise to the same magma product; e.g. in size 16 there are both a nonassociative flexible product, and a nonflexible product satisfying $$x(xx) = (xx)x$$ but not $$(xx)(xx) = x(x(xx))$$, that give rise to the unique linear model. Some of those I think we may theoretically show to give no new magma models through an endomorphism ring argument.
9. The previous experiments show that size 16 may be qualitatively different, since there appear many more possibilities (for underlying products for example) and runs tend to take much more time in this size relatively speaking (also happens with other square numbers). Accordingly, I am also trying 677 anti 255 in size 16, just in case; apart from the Mace4 run, I also tried Vampire for 10h, without success; I will give it unlimited time next time.

**Jose Brox:**

11. Also, @Pace Nielsen's idea of trying a translation-invariant model of 677 anti 255 with $$f^4=1$$ over $$(Z/4Z)^4$$ is still running after 23 days.

**Daniel Weber:**

What techniques were attempted to resolve this positively? I mostly see discussion about constructing counterexamples

**Zoltan A. Kocsis (Z.A.K.):**

@Daniel Weber|690858 I don't know what others did, as we didn't discuss much, but I made attempts using both the usual injective/surjective arguments, and trying to use the fact that iterating a function $$x,f(x),f(f(x)),\dots$$ on a finite set eventually repeats a value, using various term functions $$f$$, both by hand and by ATP. Didn't get anything.

After @Terence Tao constructed his large non-right-cancellative model, I kinda gave up: it convinced me that one can probably build a large model where this implication fails too. But before I gave up, I was planning to try the following approaches:

1. Look up proofs of the most impressive implications I know about finite structures (e.g. [Artin-Zorn](https://en.wikipedia.org/wiki/Artin%E2%80%93Zorn_theorem)) to see if any general algebraic techniques used in them are missing from our ATP toolbox.
2. Try to find a first-order property $$\varphi$$ characterizing the directly irreducible models of 677, and see using ATP whether $$677+\varphi$$, along with the finiteness assumptions above, implies 255. If so, we're done, since every finite model is a product of directly irreducible finite models, and each product satisfies the equations that hold in all its factors.

Since I mostly converted to the "there is a counterexample" side, there is one more thing I would like to try in an attempt to construct one. Take the largest set of equations $$\Gamma$$ such that our ATPs fail to prove $$\Gamma, 677 \vdash 255$$. Try to brute-force the free $$\Gamma+677$$-algebra on one generator. If we get lucky (and our $$\Gamma$$ is big enough), this free algebra should be finite of manageable size, and thus a counterexample of the sort we're looking for.

**Matthew Bolan:**

I think @Vlad Tsyrklevich also ran a number of such experiments.

**Vlad Tsyrklevich:**

Mostly I just tested the injective<=>surjective hypotheses and coping the arguments of the eventually-periodic finite implications in as much as I was able to express them to the ATP--so nothing new.

**Terence Tao:**

This may be our best remaining hope.  One thought is to work both with the original operation $$\diamond$$ and its reflection $$y \tilde \diamond x = L_y^{-1} x$$, so one has the relation $$y \diamond x = z \iff y \tilde \diamond z = x$$.  The reflected operation obeys a nice law $$x \tilde \diamond ( \tilde L_y x \tilde \diamond \tilde L_y^2 x ) = y$$.  Perhaps if we use both $$\diamond$$ and $$\tilde \diamond$$ to fill out our additional system $$\Gamma$$, we may be able to get enough equations to constrain the magma.

**Jose Brox:**

More negative results in small sizes:
1. There are no models whatsoever of 677 in size 10 (39h in Mace4).
2. I have written a better Mace4 script for translation-invariant models of 677 anti 255. There are no such models with any $$f$$ up to size 19 included (73min for this last size), and no models with $$f^4=1$$ up to size 29 included (size 28 in 65min). I have also started a new @Pace Nielsen's size-256 experiment with a faster script.

**Jose Brox:**

About using SAT solvers: Vampire already implements SAT solvers inside its finite model builder (it uses Minisat and Z3).

As a matter of fact, my Vampire search for a 677 anti 255 model in size 16 with unlimited time was killed after 15h because Minisat needed more than the 2GB of RAM I had allocated for it (it's running again with 10GB of RAM).

**Henrik Böving:**

If you want to do some work with SAT solving and are concerned about speed I would still recommend giving more modern solvers like CaDiCal or Kissat a try though, I would expect both of them to always outperform minisat and Z3 when you just give them a query directly.

**Daniel Weber:**

Is there an infinite counterexample where $$L_x$$ is bijective? Maybe we can try to construct such an example with the greedy method

**Jose Brox:**

Yet more negative results:
1. 677+4599 anti 255 has finally ended in size 18 after 26.5 days (without models). I can make the script faster, so I will try with 19+ (EDITED: with the new script, size 18 was completed in 25min :sweat_smile: ).
2. No translation-invariant models with any $$f$$ in size 20 (4h).
3. No translation-invariant models with $$f^4=1$$ in size 30 (28h). Given the progression of time with size in this case (24: 3min, 26: 9min, 28: 1h, 30: 28h) I don't expect to be able to exhaust size 32, but it still is worth a shot, since it is a power of 2 (like 16).

**Bernhard Reinke:**

Has there already been a search for a 677 anti 255 model that is explicitly one-generated? If there is finite counterexample, then there must be a finite counterexample $$M$$ that is only generated by an element $$x$$. For this counterexample there must be a constant `n` such that every element of $$M$$ can be written via at most `n`multiplications of $$x$$.

If we are given such an `n`, we could try to do the following: we consider $$D_n$$, the [Dyck words](https://en.wikipedia.org/wiki/Dyck_language) with at most `n` pairs of brackets. We can search for a pair of an equivalence relation $$\sim$$ and $$R \subset D_n \times D_n \times D_n$$ such that

1. R descends to a magma on $$D_n / \sim $$ satisfiying 677
2. We have $$R(v,w,[v]w)$$ whenever $$v,w,[v]w \in D_n$$
3. 255 fails for x

I think up to n=4 we know it is not possible (as there are only 9 Dyck words with at most 4 pairs of brackets), n=5 might be feasible to check and is not yet covered by our computations.

**Jose Brox:**

I have tried more or less what you suggest using Prover9, but the search (at least with my code) is slower than just checking 677 against 255. For example, for $$n=3$$ my code is:
```
PROVER9 ASSUMPTIONS

x = 0 | x = (0*0) | x = (0*(0*0)) | x = ((0*0)*0) |
x = (0*(0*(0*0))) | x = (0*((0*0)*0)) | x = ((0*0)*(0*0)) | x = ((0*(0*0))*0) | x = (((0*0)*0)*0).

x=y*(x*((y*x)*y)) #label(677).
x=(y*x)*((y*(y*x))*y) #label(consequence677).
x*y = x*z -> y = z.
exists x -(exists y (y*x = x)).

PROVER9 GOAL
x=((x*x)*x)*x #label(255).
```
With usual 677 anti 255, size 9 is exhausted in 12s (with selection_measure 1 and without the last clause included in the code above), while with the one-generator code, times are 36s, 42s, 65s for $$n=4,5,6$$ (with selection_measure 4 and skolems_last checked).

**Terence Tao:**

This is an interesting idea!  I think abstractly one exists: one considers the theory with two operations $$\diamond, \tilde \diamond$$, with $$\diamond$$ obeying 677 and with the additional laws $$y \diamond (y \tilde \diamond x) = x$$ and $$y \tilde \diamond (y \diamond x) = x$$, so that the left multiplication operators $$L_y, \tilde L_y$$ invert each other.  I think the Type II linear models contain arbitrarily large submodels that are generated by a single generator, so the free magma for this theory from one generator is necessarily infinite.

With pen and paper it does not seem that the greedy algorithm converges for this system, but there were a lot of cases and I am not 100% sure about this.

**Terence Tao:**

By the way, one simple infinite example with one generator: take a Type II linear model over the complex numbers and restrict to the submagma generated by, say, the complex number 1.

**Jose Brox:**

No models of 677+4599 anti 255 in size 19 (7.5h).
No translation-invariant models with any $$f$$ in size 21 (10h).
Still some room to explore with these.

**Jose Brox:**

Something I'm starting to explore is **semantic guidance**: when we have a theory T that does not imply a fact F, but T together with some extra hypothesis H does, then a model of T anti F can be used to speed up a proof of T+H -> F, by evaluating the candidate clauses in the model to see if they are false or not for it.

Semantic guidance is implemented in Prover9, we just need to find some model(s) of T+neg(F) with Mace4 and include them as guidance. What I'm doing is using, from my [lists of relaxations](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/490348960), those equations that are implied by 677 but are not equivalent to it (even when left multiplication is bijective) and do not imply 255; I take such an equation T as a theory (weaker than H=677) and use its countermodels for F=255 as semantic guidance. For the moment I have only explored 
`1466035: x = y * (y * ((x * ((y * x) * y)) * (x * y)))` with Prover9 (different configurations with more or less max_weight and sos_limit, and more or less finiteness bijectivity conditions, for 10h each), without success.

Something I also tried was simply adding to the 677 anti 255 Prover9 search the (higher-order-logic) clause
`all f ( (all x all y f(x) = f(y) -> x = y) <-> (all x exists y f(y) = x) )`
but it didn't produce a proof.

**Jose Brox:**

I also thought that using typed higher-order logic, a priori it should be possible to write a Vampire script in which the finiteness of the model is imposed, and not just some weaker consequences, but I haven't deepened into this. With Prover9 perhaps it could be done with an order relation and a successor function.

**Jose Brox:**

What speed up factor do you guess we may get? Would it be worth the effort?

**Jose Brox:**

The dimacs format that @Jihoon Hyun's script gives as output is the standard one for CaDiCaL? (Btw, I checked that the program compiles and runs correctly giving some array of numbers).

**Jihoon Hyun:**

Yes, it is. The first line with `p cnf` is the header with the number of variables and clauses. The rest are clauses, each ending with 0.

**Douglas McNeil:**

I've done a fair bit of SAT work now, mostly using glucose which knocked off two implications early and after that kissat which helped springboard 854.  I don't think there are a lot of performance gains lurking there left for us, TBH.  mace4 and vampire in solver mode both seemed to work better for me at larger sizes.

**Jihoon Hyun:**

If you're using my generator, there are many places for improvement. I'll share a repo for updates within a couple of hours.

**Daniel Weber:**

@Jose Brox|761825 [said](https://leanprover.zulipchat.com/#narrow/stream/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/493459079):

Could you take `H = the magma is finite` here? The greedy ruleset lets us decide the free theory modulo 677 efficiently

**Jihoon Hyun:**

I got a result that if, for given $$x$$, there is some $$y$$ which $$x = y \diamond x$$, then such $$y$$ is unique and  $$y = (x \diamond x) \diamond x$$.
So proving the existence of such $$y$$ for all $$x$$, especially for all $$x \neq x \diamond x$$, is equivalent to proving 255.
Is there any known result for this?
I know there is a non-right cancellative model, but that won't imply there is some $$x$$ which for every $$y$$, $$x \neq y \diamond x$$ holds.

**Zoltan A. Kocsis (Z.A.K.):**

Iirc it's [been known](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486686097) that this condition is equivalent to 255 given 677, but the non-right-cancellative model is idempotent so not very useful for constructing 255-counterexamples.

Since many linear models were enumerated: On a related note, @Bruno Le Floch do you know if we have a nowhere-idempotent model with even cardinality?

**Henrik Böving:**

Dimacs is the standard for all serious SAT solvers basically since the dawn of time :tm:.

Well what is the effort? You should just need to swap the binary that you run? Also note that you can gear the heuristics of some solvers to optimize looking for a certain outcome. E.g. cadical has a --unsat flag to make trying to find UNSAT instances faster etc.

**Henrik Böving:**

And regarding the performance expectations, as j mentioned above I would expect them to be notably faster when you let e.g. minisat run straight at a problem, this is not to say that a tool like vampire that can do additional preprocessing etc isn't going to be faster vs a custom but not well optimized encoding

**Bernhard Reinke:**

Thanks for doing this! Just to make sure, for the list of times with the one-generator code, do you still impose the overall size bound of 9 or is it without any size bound?

**Jihoon Hyun:**

@Jihoon Hyun [말함](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/493473675):

I just made a [repository](https://github.com/qawbecrdtey/magma_dimacs_cnf) to update the code. I believe there are still more places for improvements, and will update when found.

Also, if you have any experiments in mind, I might craft a generator for it.

**Bruno Le Floch:**

I didn't track all the models.  I know of the order-31 linear model that is nowhere idempotent, and I *think* the type II linear model over $$\mathbb{F}_{16}=\mathbb{F}_2[X]/(X^4+X^3+1)$$ with $$\beta=X$$ and $$\alpha=-X^3-X-1$$ is almost nowhere idempotent, with the exception of $$0\diamond 0=0$$.
[*Spoiler: Operation table for the F16 model — omitted*]
[model-same In the finite magma explorer.]
It obeys 677, 255 of course and all $$x\diamond x^2$$ are equal, and $$R_y^3=\mathrm{id}$$ and $$x\diamond(x\diamond y)$$ and $$x\diamond(y\diamond x)$$ and $$y\diamond x^2$$ are each symmetric in $$x,y$$ for some reason.

**Matthew Bolan:**

The direct product of the order 31 nowhere idempotent model with a model of even order should work

**Giovanni Paolini:**

You are clearly faster than me at checking translation-invariant models! :smiley: I had size 20 running for several days and I have now stopped it. (My computer was longing for a restart, so this is for the best.)

**Zoltan A. Kocsis (Z.A.K.):**

Sorry, I assumed you had, based on how quickly you could answer my previous question! And this is not the first time this particular 16-element linear model almost-satisfies a query I have, so I've now saved it on my "things to try before asking a question" list :)

**Jose Brox:**

These times are for size 9 only. I didn't compare times in size 10 because for usual 677 anti 255 it needs 1h, but now I've started size 10 with n=6, just in case [EDITED: killed after 1h without exhausting]. We should also try Vampire, could do things differently and be faster with one generator.

**Jose Brox:**

:big_smile: I recently changed the script to make it faster (you now, I didn't care that much about speed at first because I started running small experiments thinking we wouldn't explore many sizes and the problem would be solved sooner, etc.).

In fact now size 22 has also been exhausted (in 27h) and size 23 is running. The running time progression with size in this case is 
17: 12min, 18: 44min, 19: 73min, 20: 234min, 21: 603min, 22: 1633min.
As you see, the time increases by a factor of around 3, so I expect to be able to exhaust size 23 in around 3 days, size 24 in around 9 days, and size 25 in around 1 month if things come to this. This is the horizon for this experiment (with Mace4).

In case you are interested, the Mace4 script for this is
```
%677 anti 255, translation-invariant product. Exists any f?
%with 2,3,no
%size 23
%size 14: 2,3,no: 44.7s; 2,3,yes: 45.2s; 2,4,no/yes: more than 120s; 2,1,no/yes: more than 45s. 0,3/,no,yes: more than 45s

if(Mace4).   % Options for Mace4
  assign(max_seconds, -1).
  assign(max_megs, 2000).
  assign(selection_measure, 3).
end_if.

formulas(assumptions).

all x all y all z (((x * y) * z) = (x * (y * z))).
all x (0 * x = x).
all x (x * 0 = x).
all x (x * inv(x) = 0).
all x (inv(x) * x = 0).

all x (x = f(x * f((inv(x) * f(x)) * f(inv(f(x)))))) #label(677).
all x (x = f(x)*f((inv(f(x))*f(f(x)))*f(inv(f(f(x)))))) #label(677consequence).

end_of_list.

formulas(goals).

0 = f(0)*(f(inv(f(0)))*f(inv(f(inv(f(0))))*inv(f(0)))) #label(255).

end_of_list.
```

**Zoltan A. Kocsis (Z.A.K.):**

@Jose Brox : There are as many groups of order 24 as there are groups between orders 18 and 23 altogether. I'm not sure how that will affect the computation time, but I wouldn't be surprised if it took longer than what one would expect by continuing the exponential.
Do you have data on the jump from order 15 to order 16? That's similar to the 23-24 jump: there's only one group of order 15, but 14 groups of order 16.

I tried what happens if I give a group operation table explicitly to Mace4, instead of constructing it. I.e. instead of having
```
  all x all y all z (((x * y) * z) = (x * (y * z))).
  all x (0 * x = x).
  all x (x * 0 = x).
  all x (x * inv(x) = 0).
  all x (inv(x) * x = 0).
```
in your assumptions list, you explicitly supply

```
formulas(operations).
  0 * 0 = 0.
  0 * 1 = 1.
  0 * 2 = 2.
% ...
  inv(0) = 0.
  inv(1) = 10.
  inv(2) = 9.
end_of_list.
```

When I force Mace4 to construct the group of order 11 by itself using the assumptions,`time mace4 -n 11 -f ...` gives the following:

```
real	0m3.677s
user	0m3.667s
sys	0m0.003s
```

However, when I supply the operation tables in advance explicitly and ask it only to produce a suitable `f`, I get

```
real	0m0.287s
user	0m0.276s
sys	0m0.012s
```

This looks like a significant potential speedup to me.

**Giovanni Paolini:**

I agree, fixing the group would probably make things faster! That's what I did in my script (https://github.com/giove91/equational/blob/main/translation_invariant.sage). I got each group's multiplication table from Gap's atlas of small groups (through Sage).

**Jose Brox:**

Sure! Size 14 in 45s, size 15 in 103s, size 16 in 324s, size 17 in 12min.

My code didn't seem particularly affected by the fact of having "many" more groups. I guess this is due to the fact that when computing groups, Mace4 has a redundancy factor (finds many isomorphic models) that can be orders of magnitude higher than the actual number of isoclasses.

Yes, this is a nice idea! I've written a Sage script to generate the code (I've seen @Giovanni Paolini's answer later :melting_face:) also using GAP's database.

 There is indeed a significant speedup, although at the cost of quite more RAM (if we want to check all groups of a given order in one batch), since Mace4 evaluates all possibilities of all given clauses at the start. This also needs a significant amount of time, although much less than exhausting the size with the other method, if there are few groups. For example, for order 25 where we have two nonisomorphic groups, Mace4 has needed 18min to start the actual computation.

Here we find a wall I've been hitting a few times with Prover9/Mace4: no matter what memory limit you set up (even unlimited), it seems that it allows an absolute maximum of 1GB, and ignores any quantity above that. Do you know any way of shortcircuiting this? (Perhaps we could look at the code and modify it). I know there is (at least) a non-official newer version of Prover9/Mace4, available in Github, do you know if it is trustworthy?
Otherwise to avoid this artificial limit, we'll need to check groups in small batches.

Times with the explicit-groups method:
size 14 (2 models) in 18s, size 15 (1 model) in 1s, size 16 too much RAM (14 models), size 17 (1 model) in 7s, size 18 too much RAM (5 models), size 19 (1 model) in 46s, size 20 too much RAM (5 models), size 21 (2 models) starting up for a good while, size 23 (1 model) running for 20min…

**Jose Brox:**

I attach my Sage code:

[attached: MAGMAS PROJECT - Translate group Cayley table into MACE4 format.ipynb]
[attached: MAGMAS PROJECT - Translate group Cayley table into MACE4 format.py]

At present it only generates the groups clauses, which I copy-paste to a pregenerated Mace4 script. Tomorrow I will update the code to run Mace4 directly from the file and partition the groups in smaller batches.

**Bruno Le Floch:**

To me it seems much better to do one mace4 run for each group, rather than messing with the RAM.  The calculations for different groups are completely independent anyway.  Besides, it would give you more comparable timings, as a function of the group size and perhaps other aspects of its structure.

**Notification Bot:**

2 messages were moved from this topic to #**Equational>Mace4 malloc issues** by @Zoltan A. Kocsis (Z.A.K.).

**Jose Brox:**

I agree (once I write the code), but the RAM problem is important anyway, because eventually it will also affect computations with single groups when they are big enough, so we need to get rid of this artificial bottleneck (also for Prover9 computations with bijectivity conditions).

**Terence Tao:**

 = I played around with this idea more and came to the conclusion that a greedy construction will be quite difficult once one has left invertibility.  677 plus left invertibility implies the laws
$$ L_y^{-1} x = x \diamond ((y \diamond x) \diamond y) = x \diamond R_y L_y x$$
and also (substituting $$x = L_y z$$ and cancelling a $$L_y$$)
$$ z = L_y z \diamond R_y L_y^2 z$$
and hence
$$ R_y L_y^2 z = L_{L_y z}^{-1} z = z \diamond ((L_y z \diamond z) \diamond L_y z)$$
so on substituting $$y=b$$, $$z = L_b^{-2} a$$
$$ a \diamond b = L_b^{-2} a \diamond ((L_b^{-1} a \diamond L_b^{-2} a) \diamond L_b^{-1} a).$$
The upshot of this is that if one is performing a greedy algorithm and wants to assign $$a \diamond b = c$$ for some novel $$c$$, then (if one wants to retain on left invertibility) one may also have to assign $$L_b^{-2} a \diamond ((L_b^{-2} a \diamond L_b^{-1} a) \diamond L_b^{-1} a) = c$$ if all the sub-expressions in the left-hand side are already defined by the partially defined operation.  The problem is that this rule may propagate indefinitely, and when combined with the other rules forced by 677 could eventually lead to collisions that seem quite hard to rule out.  It also suggests that the free magma generated by 677 and left invertibiilty may be rather complicated.

In comparison, the greedy rule for 677 without left-invertibility is simpler: when imposing $$a \diamond b = c$$ for a novel $$c$$, also impose $$y \diamond c = a$$ for any $$y$$ for which $$b = (y \diamond a) \diamond y$$.  But no further relations of the form $$a' \diamond b' = c$$ are generated.

**Jose Brox:**

The new Sage script for translation-invariant models for all f with explicit groups, checked group by group, is already running. The previous summary is that there are no models for groups of orders 2-23,25 (included). I'm currently running orders 24 and 26.
I attach the Sage Jupyter notebook:
[attached: MAGMAS PROJECT - 677 anti 255 translation-invariant all f explicit groups.ipynb]

@Bruno Le Floch with the script you can collect the running time for each group. In this doc file you can find the times for all groups in orders 16-20:
[attached: 677 anti 255 translation-invariant all f explicit groups timings.docx]

I've also modified the script to run the $$f^4=1$$ case, currently in size 32:
[attached: MAGMAS PROJECT - 677 anti 255 translation-invariant f^4=1 explicit groups.ipynb]

**Jose Brox:**

Quick update of negative results:
No models of 677+4293 anti 255 in size 16 (2.1 days).
No models of 677+4599 anti 255 in size 20 (7.5 days).
No translation-invariant models with any $$f$$ in sizes 24-26 (2.6d, 8h, 10.5h respectively).
No translation-invariant models with $$f^4=1$$ in size 34 (3.8h, size 32 still running).

Running time for each group in translation-invariant models with any $$f$$, in minutes:
[*Spoiler: TIME PER GROUP — omitted*]

**Jihoon Hyun:**

I was searching for magma of size 15, with 677 anti 255. After 526k seconds(6 days) I got a segfault for some reason, and the solver spiited out an unknown result. Magmas of size 13 and 14 with same condition are still running. Still, I wanted to state that it is unlikely to find magma of size 15 with 677 anti 255. I used cadical with [this code](https://github.com/qawbecrdtey/magma_dimacs_cnf/blob/61bbe3ba2b2ce59a10d64bfa8ccd2be58c46f92b/677/search_na255.cpp) as a generator.

**Terence Tao:**

I have decided to bow to reality and rewrite the portion of the draft paper that tentatively claimed that both the infinite and finite magma implication graph was completed by the ETP, and instead posing 677->255 as an open problem: equational#1071 . Of course, if there is a new breakthrough on this implication before the paper is finalized, we can update the paper accordingly, but at our current trajectory it appears that the three remaining known anti-implications for the infinite graph will be formalized first, which I think would be a natural time to "declare victory" and then focus on finishing the paper.

**Matthew Bolan:**

Do we have a single finite 677 magma which is not linear and generated by only 1 element?

**Terence Tao:**

Not that I know of, though in principle the cohomological construction might be able to provide one (of course the linear base magma would have to be of the "Type II" kind without idempotents).

**Matthew Bolan:**

Ah, I thought I had checked those, but further inspection revealed a bug. Here is a non-linear order 49 magma which is generated by a single element (Any element $$\ge 7$$ works as a generator, and it is non-linear as  $$L_0 L_7^{-1} L_0 L_{14}^{-1}(7) \not = L_0 L_{14}^{-1} L_0 L_{7}^{-1}(7)$$)
[attached: 677_nonlinear_1_generated.txt]

**Bruno Le Floch:**

Claim: in a 677 magma, for a given $$x$$, (iv) $$\exists y,x\diamond(y\diamond y)=y$$ implies (iii) $$\exists y,(x\diamond y)\diamond x=y$$ implies (ii) $$\exists z,x\diamond (z\diamond x)=z$$ implies (i) $$\exists w,w\diamond x=x$$ implies that $$x$$ obeys 255.  We already knew this last implication, which was quite useful in finding immunities.  I think these observations are useless, but who knows, maybe someone will get inspired.

[*Spoiler: Proof of the implications — omitted*]

It might be interesting to look for a magma such that equation 255 is obeyed by none of the elements.  This would mean that (i)-(iv) above are always violated, so $$L_x\circ S$$ and $$R_x\circ L_x$$ and $$L_x\circ R_x$$ and $$L_x$$ have no fixed point (where $$S$$ is the squaring map).

**Terence Tao:**

Nice observations!  I just added them to the 677 chapter in the blueprint, just in case they are useful in the future.  I suspect that many of these implications are in fact reversible, so that this leads to several new equivalent conditions for 255.

**Matthew Bolan:**

Prover 9 suggests that $$x$$ obeying 255 implies (iv) for $$x$$ in a 677 magma, so they should all be equivalent conditions to 255.
`[*Spoiler: Proof — omitted*]
1 (exists x 0 * (x * x) = x) # label(non_clause) # label(goal).  [goal].
2 x = y * (x * ((y * x) * y)).  [assumption].
3 x * (y * ((x * y) * x)) = y.  [copy(2),flip(a)].
4 0 = ((0 * 0) * 0) * 0.  [assumption].
5 ((0 * 0) * 0) * 0 = 0.  [copy(4),flip(a)].
6 0 * (x * x) != x.  [deny(1)].
7 x * ((y * ((x * y) * x)) * (y * x)) = y * ((x * y) * x).  [para(3(a,1),3(a,1,2,2,1))].
8 x * (((y * ((x * y) * x)) * (y * x)) * ((y * ((x * y) * x)) * x)) = (y * ((x * y) * x)) * (y * x).  [para(7(a,1),3(a,1,2,2,1))].
14 0 * (((((0 * 0) * 0) * ((0 * ((0 * 0) * 0)) * 0)) * 0) * ((((0 * 0) * 0) * ((0 * ((0 * 0) * 0)) * 0)) * 0)) = (((0 * 0) * 0) * ((0 * ((0 * 0) * 0)) * 0)) * 0.  [para(5(a,1),8(a,1,2,1,2)),rewrite([5(59)])].
15 $F.  [resolve(14,a,6,a)].
```
````

**Viliam Vadocz:**

Hello, I would like to try finding a counterexample (via automated search). I skimmed the paper (accessed from the dashboard) looking for what has been tried. I did not see much mentioned about this particular implication.
1. Am I looking at the most recent version of the paper? If not, where can I see the latest version?
2. Is there a better way to get caught up on this particular problem?
3. I would also like to know how the implication for the infinite magmas was shown to be false. Where could I see that?

**Terence Tao:**

Welcome!  This particular Zulip thread is probably the main location to record all the different things that have been tried for this specific implication, with some of what we have done also recorded on the blueprint at https://teorth.github.io/equational_theories/blueprint/677-chapter.html , which contains details of the infinite magma construction as well.

**Matthew Bolan:**

Somewhat unimportant, but I was thinking a bit about other ways to detect if a magma is linear, and I noticed that in commutative linear magmas, any linear map $$f$$ is a homomorphism as $$f(x) \diamond f(y) = af(x) + bf(y) = f(ax + by) = f(x \diamond y) $$. In particular, checking whether squaring (or more general maps like $$f(x) = (x \diamond x) \diamond x$$) is a homomorphism seems to be a fast test for linearity which works well for 677 magmas.

**Bruno Le Floch:**

A human-understandable proof that my implications above are equivalences, loosely based on Matthew's prover9 output above.  I'll follow his lead denoting by $$0$$ the element whose properties we are looking at.
- 255 obeyed by $$0$$ implies (i) by taking $$y=(0*0)*0$$ so $$y*0=0$$;
- (i) implies (ii) by taking $$z=y*((0*y)*0)$$ so $$0*z=y$$ so $$(0*z)*0=y*0=0$$ so $$z=0*(z*((0*z)*0))=0*(z*0)$$;
- (ii) implies (iii) by taking $$w=z*0$$ so $$w=(0*(z*0))*0=(0*w)*0$$;
- (iii) implies (iv) by writing $$w=0*(w*((0*w)*0))=0*(w*w)$$.

So all around quite trivial equivalences.

**Terence Tao:**

I've updated the blueprint to state these equivalences more explicitly.  

I was playing around with a graphical interpretation of (left-invertible) 677 and came up with the following, though I wasn't able to get further with it.  We replace the magma operation with a labeled directed graph by writing $$x \stackrel{y}{\to} z$$ if $$y \diamond x = z$$.  Then left cancellability means that the edges labeled by $$y$$ form a permutation.  The law 677 then concerns paths of the form

$$ a \stackrel{e}{\to} b \stackrel{d}{\to} c \stackrel{a}{\to} d \stackrel{a}{\to} e.$$

Namely, any incomplete path that contains all of the above four edges except for one of the first three, can be completed by adding in the missing edge.  For instance,
$$ a \stackrel{e}{\to} b \stackrel{d}{\to} c \quad ? \quad d \stackrel{a}{\to} e$$
can be completed to
$$ a \stackrel{e}{\to} b \stackrel{d}{\to} c \stackrel{a}{\to} d \stackrel{a}{\to} e.$$
Indeed, if one replaces $$a, d$$ by $$y,x$$ and performs all the obvious substitutions, then the incomplete path is
$$ y \stackrel{y \diamond x}{\to} (y \diamond x) \diamond y \stackrel{x}{\to} x \diamond ((y \diamond x) \diamond y) \quad ? \quad x \stackrel{y}{\to} y \diamond x$$
and completing the path precisely corresponds to 677 holding for this choice of $$x,y$$.  Completing the first or second edge corresponds to other equivalent forms of 677 (assuming left cancellativity) that we have worked out in the past (and are also recorded in the blueprint).  (Completing the final edge is more problematic, this seems to require right cancellativity which we know can fail.)

**Shreyas Srinivas:**

I noticed an issue in the blueprint and wasn't sure if it was worth creating a separate thread for. We speak about duals of equations in chapter 2 of the blueprint without defining duality first.

**Shreyas Srinivas:**

This could potentially be fixed in any PR that updates the blueprint

**Shreyas Srinivas:**

The first occurrence of duality appears to be Chapter 4

**Terence Tao:**

I've added a forward reference to Chapter 4 in Chapter 2 to reflect this.

The blueprint is something of an organic mess right now; the paper has supplanted it as the main "official" record of the general theory, so it's main remaining purpose is to guide the formalization of the last few outstanding implications, though we did not really follow the paradigm of other formalization projects in strictly following the blueprint to decompose large formalization tasks into modular small components.

**Shreyas Srinivas:**

I think we should try to keep the blueprint consistent with the paper since we need a way to cross check things we say in the paper

**Shreyas Srinivas:**

Not only now, but whenever the reviewers get back (presumably a few weeks or months) and we have forgotten stuff

**Shreyas Srinivas:**

It's our equivalent of a lab notebook (without all the bureaucratic requirements associated with one).

**Terence Tao:**

I agree that we should maintain notational consistency between the blueprint and the paper.  But I am much more relaxed about having inconsistent emphasis of material between the two.  For instance the set of equations singled out in Chapter 2 of the blueprint is now somewhat different from the set of equations listed in the appendix of the paper (or from the "selected equations" page of the Github wiki, or the "commentary" pages in Equation Explorer), for a number of reasons, and similarly some proofs in the paper are arranged a little differently from their counterparts in the blueprint.  But I think as long as everything is technically correct and the notation is consistent, this should not be a major issue.

**Matthew Bolan:**

To return to 677, an outside idea for why the implication might hold in the finite setting that I've been playing with is to try and find in any magma violating 255 a proper submagma violating 255, in which case we would be done by infinite descent. I have no real reason to believe this is possible, besides that I think it is true of the free 677 magma. ATP seems to find no issue with a magma having only a single 255 counterexample, so probably the idea would need to be tweaked to find infinitely many distinct elements some other way. Still, in my personal list of reasons why an implication could imaginably hold for finite magmas and not infinite ones, this is up there and has a slightly different flavor to the methods we've tried so far. I personally believe the implication to be false though.

**Bruno Le Floch:**

Relatedly, ATP seem to find no immediate problem with having a single counterexample `2*0=1*0` to right-cancellativity (but I have no idea if my Prover9 settings are useful values).
```
assign(sos_limit, 2000).
assign(max_weight, 1000).
assign(max_seconds, 200).
formulas(sos).
y*(x*((y*x)*y))=x. % eq 677
(y*x)*((y*(y*x))*y)=x. % consequence
(x*y = x*z) -> (y = z). % left-cancellativity
2*0 = 1*0. 1 != 0. 2 != 1. 2 != 0. % failure of right-cancellativity
(x*z = y*z) -> (x = y | (x = 1 & y = 2 & z = 0) | (x = 2 & y = 1 & z = 0)). % no other failure
end_of_list.
```

**Matthew Bolan:**

Hmm, for finite magmas we know that there must be more than one counterexample to right-cancellativity, as in a magma of order $$n$$ left cancellativity implies each element is a product of two elements in exactly $$n$$ ways, but then if $$2 \diamond 0 = 1 \diamond 0$$ is the unique failure of right cancellativity, $$1 \diamond 0$$ is a product of two elements in exactly $$n+1$$ ways, by right cancellativity away from $$0$$.

**Bruno Le Floch:**

Great! What you just pointed out hints to an effect of finiteness that is not yet captured in any of the ATP runs as far as I know.  Maybe there is a way to state it without involving the cardinal explicitly?

**Matthew Bolan:**

One consequence ~~that actually seems to be speeding up Mace4 quite a bit for me~~ (Edit: I misremembered the old timings, a new control run suggests it isn't such a great speed-up) is that given some element $$a$$, we can solve $$a = b \diamond d = c \diamond d$$, $$b \not= c$$ if and only if there is an element $$e$$ such that $$a \not= f \diamond e$$ for all $$f$$.

**Matthew Bolan:**

That's interesting for 255, since if $$0 \not = ((0 * 0) * 0) * 0$$, then $$0 \not = x * 0$$ for all $$x$$, so we must have b,c,d with $$0 = b * d = c * d$$ and $$b \not = c$$.

**Bruno Le Floch:**

@Jose Brox If you are still running prover9/vampire on 677 + other equations + left-cancellativity, it might be interesting to also include Matthew's observation.  I think it is `all a ((exists b exists c exists d (b!=c & b*d=a & c*d=a)) <-> (exists e all f a!=f*e)).`

**Kevin M:**

I think it is probably better to break symmetry here.
Instead of having a clause that is essentially "there exists an element for which eqn 255 does not hold",  just require some specific element (for example: element 0) violates eqn 255. Which if I'm understanding, could be done by forcing $$X_{((00)0)0, 1}$$ true.

**Kevin M:**

For what sizes has the SAT instance been run on?

I only have a little experimental experience with SAT solvers, but proving UNSAT seems to take exponentially longer than finding a SAT instance if it exists. So maybe it would be worth just running the SAT problem for different sizes, but just for 10 hours each size or something.

Does anyone have a fair amount of experimental experience with SAT such that they could give a (very rough) estimate of what sizes are even worth running here?

Maybe we could try this type of encoding on some other equation where the allowed sizes are known -- just to get a rough experimental idea of what sizes are feasible to explore with this SAT encoding.

**Jihoon Hyun:**

@Kevin M [말함](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/501947795):

Currently it's running with size 12 to 17. To generate the cnf I'm currently using please check [the git repository](https://github.com/qawbecrdtey/magma_dimacs_cnf). ~~I'll update the compilation part of the README in a few minutes.~~ I updated the compilation part of the README. Please tell me if there are any issues when compiling.

You suggested some symmetry breaking, and I did implement it. It doesn't seem to give significant impact on large instances, though. (I mean, these are currently running for 3*10^6 seconds or so, and I can't tell if this was better with larger magmas. Still, breaking symmetries did reduce time for smaller instances, like n <= 10.)

Finally, please contact me any time if you have any questions about the source code.

**zirconium.n:**

Hello, new here. Just read through the topic. I still have this naive problem, what's the rationale behind assuming 677 does not imply 255?

**Vlad Tsyrklevich:**

People have also tried exploring that it may be an implication, but didn't make headway there, and it doesn't happen to fit the pattern of the other implications we have proved in the project. If it is an implication, it requires a new idea to prove it. I think most people do believe it is a non-implication though, because of the failed attempts to find proof that it is an implication.

**Zoltan A. Kocsis (Z.A.K.):**

@zirconium.n 

As Vlad Tsyrklevich points out, one reason comes by an argument from ignorance: assuming something fails because we tried hard but failed to prove that it holds. Indeed, we tried all our tricks to prove the `677->255` implication but made no progress. If it holds, its proof has to be quite unlike any other proof we've done over the course of the project.

But that's not all. As things stand, it looks quite plausible to me that *most* non-right-cancellative models of 677 would refute `677->255`, and we're just not very good at constructing such models. Let me elaborate.

We know that a countermodel to `677 -> 255` cannot be right-cancellative. Constructing a non-right-cancellative model of 677 is therefore no harder than constructing a countermodel to `677->255`. But when we actually try to construct non-right-cancellative finite models of 677, the very same difficulties appear as when we try to prove the `677->255`  implication:

1. Typical finiteness assumptions, such as function periodicity, injections coinciding with bijections, do not help our ATP tools prove the statement.
2. Mace4 and similar tools fail to construct a countermodel, possibly because even the smallest ones exceed feasible size limits.
3. The methods that we devised to extend existing models to larger models while refuting some property provably break down (i.e. we can prove that they would only work if the existing model was already a counterexample, and then there'd be no reason to use them).

Yet non-right-cancellative models of 677 turn out to exist! No *small* examples are known, of course: computer searches found none, and the smallest known case (whose table was computed by Matthew Bolan) has order 496. Worse, the only method we currently know to construct such models (due to Tao) always yields idempotent magmas, and such magmas cannot serve as counterexamples to `677->255`.

The overall pattern, and the fact that we could eventually construct non-right-cancellative models of 677, strongly suggest to me that we will eventually be able to construct countermodels to `677->255` as well: all known difficulties appear quite similar. Indeed, it looks plausible to me that *most* non-right-cancellative models of 677 would  refute `677->255` as well, and we just got unlucky in that the first working attempt to produce non-right-cancellative models yielded idempotent ones.

**Matthew Bolan:**

Terry's construction yields infinitely many non-right-cancellative models, one for each field $$F$$ supporting a 15th root of unity. The model corresponding to $$F_q$$ will be of order $$31q$$. All I did was produce the table corresponding to $$q = 16$$ to confirm it worked.

**Zoltan A. Kocsis (Z.A.K.):**

@Matthew Bolan I know that this results in infinitely many models: the point is that even the smallest one among them (the one whose operation table you computed)  is large. And as I stated above, the models resulting from this construction are all idempotent, so satisfy 255.

**Matthew Bolan:**

Right, I don't doubt that you know this, and I agree with your message. I was mostly reacting to the phrase "and the only case we could work out" which could mislead someone new to the project into thinking it was unique, or that the other models in the family are hard to compute (actually before I remembered $$16 = 15 + 1$$ I computed an order $$31^2$$ model, which I can dig up or recompute if anyone wants it).

**Zoltan A. Kocsis (Z.A.K.):**

@Matthew Bolan Thanks, that makes sense! I've now edited the comment and changed that phrase to clarify this.

**zirconium.n:**

Thank you for the explanations! These are very insightful. I will read through the topic again to gain further understandings. I think I will try to prove the positive result anyway (after reading all failed attempts ofc), since I get the feeling we get way more exploration on the anti-implication side. But surely it seems requires some creative thinking...

**Jose Brox:**

Did your computations for 13 and 14 finished eventually? And have you been able to exhaust sizes 11 and 12 with cadical? If this is the case, how much time did the size 11 computation need?

**Jose Brox:**

How did you find this magma, was it in the course of some more general search?

**Jose Brox:**

In my experience this kind of formula, with existence quantifiers or inequalities of elements, often does not improve MACE4 computing time, and this is consistent with the inner workings of the program: at the start it generates all combinations of elements of each formula, then applies its "sudoku" algorithm.

Nevertheless I have tried it for small sizes, and the computation is quite slower. But perhaps we can give another formulation which is better suited to MACE4.

I have also tried adding it as a finiteness condition to PROVER9, but it hasn't provided a proof. I will try with Vampire later, as it seems to be better for finding proofs when formulas have implications.

**Jose Brox:**

While I was in bureaucratic hell (from which I'm starting to return!), some more negative results have been found by my MACE4 experiments farm. We have exhausted:

1. 677 anti 255: size 11 (57 days).
2. 677+513+3659 anti 255: size 14 (34d).
3. 677+4073 anti 255: size 14 (17h).
4. 677+4131 anti 255: size 15 (57d).
4. 677+4321 anti 255: size 15 (2d).

Moreover, since there seems neither PROVER9 nor Vampire find any problems with a 677 model having just one failure of 255, I have also experimented with adding that condition to the 677 anti 255 search, giving a speedup of 3 for size 9, 5 for size 10, and 13 for size 11 (for which it needed 4.5 days). It is currently running in size 12.

I have also played with the idea of the magma operation * being the product of a nonassociative "semirring" (R,+,*): we of course remove 0 and opposites for +, but even then, if both distributive laws are satisfied, then PROVER9 can show that 677 implies 255 (under left cancellativity and the equation consequence of 677). Neither PROVER9 nor Vampire have been able to show the same when one of the two distributive laws is removed, so I'm running these "one-legged 677 semirring" experiments.
Having left distributivity is much better for computations, so we may guess that in this case 677 actually implies 255; with left distributivity I have already exhausted size 24 (16h), while with right distributivity is still running in size 12.

Lastly, the translation-invariant experiments run group-by-group had a big crash and I have yet to resume them (I'm waiting for a SAGE update in my department's computer).

**Jihoon Hyun:**

I didn't run it for size 11 as I thought you were exploring that space. Also there was a blackout once, so currently all experiments from size 12 to 17 are running for 4*10^6 seconds.

**Matthew Bolan:**

It was among the cohomological extension models I had already computed. It is an extension of an order 7 example by another.

**Jihoon Hyun:**

I leave a small lemma before I forget: If $$a\diamond a = (a\diamond a)\diamond a$$, then $$a=a\diamond (a\diamond (a\diamond a))$$ holds, and $$a \diamond a$$ satisfies Equation 255.

**Jihoon Hyun:**

I asked gpt to generate a visualizer of a magma. The result was satisfying, so I share the script here. All you have to do is to prepare a text file which contains a single integer representing the size of the magma, and the next n lines containing n integers each which is the magma multiplication table.
[*Spoiler: Python script — omitted*]python3
import tkinter as tk
from tkinter import filedialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt

# Global variable to store the magma table
magma = []
n = 0

def load_file():
    global magma, n
    file_path = filedialog.askopenfilename(
        title="Select a magma file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
        # First line gives n
        n = int(lines[0].strip())
        magma = []
        # Next n lines, each with n integers
        for i in range(1, n+1):
            row = list(map(int, lines[i].split()))
            if len(row) != n:
                raise ValueError("Row length does not match n")
            magma.append(row)
        messagebox.showinfo("Success", f"Loaded magma of size {n}.")
        update_dropdown()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file: {e}")

def update_dropdown():
    # Update the dropdown list with numbers 0 to n-1.
    selector['menu'].delete(0, 'end')
    for i in range(n):
        selector['menu'].add_command(label=str(i), command=tk._setit(selected_number, str(i)))
    selected_number.set("0")

def draw_graph():
    if not magma:
        messagebox.showerror("Error", "No magma loaded!")
        return

    try:
        a = int(selected_number.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid number selected!")
        return

    G = nx.DiGraph()
    # Add nodes labeled from 0 to n-1
    G.add_nodes_from(range(n))

    # For each b in 0..n-1, determine c = a * b and add a red edge (left multiplication)
    for b in range(n):
        c_left = magma[a][b]
        G.add_edge(b, c_left, color='red', label='L')

    # For each b in 0..n-1, determine c = b * a and add a blue edge (right multiplication)
    for b in range(n):
        c_right = magma[b][a]
        G.add_edge(b, c_right, color='blue', label='R')

    # Draw the graph using different colors for the two kinds of arrows
    pos = nx.spring_layout(G)  # Compute layout
    # Extract edge colors based on edge attributes
    edge_colors = [G[u][v]['color'] for u,v in G.edges()]

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', arrows=True, edge_color=edge_colors,
            connectionstyle='arc3, rad=0.1', node_size=800)

    # Optionally, you can add labels to edges if desired.
    # edge_labels = {(u, v): G[u][v]['label'] for u,v in G.edges()}
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(f"Graph for chosen element {a}")
    plt.show()

# Create the main window
root = tk.Tk()
root.title("Magma Graphical Helper")

# Button to load the file
load_button = tk.Button(root, text="Load Magma File", command=load_file)
load_button.pack(pady=10)

# Dropdown to choose an element from 0 to n-1
selected_number = tk.StringVar(root)
selected_number.set("Select element")
selector = tk.OptionMenu(root, selected_number, ())
selector.pack(pady=10)

# Button to draw the graph for the chosen number
draw_button = tk.Button(root, text="Draw Graph", command=draw_graph)
draw_button.pack(pady=10)

root.mainloop()
```
```
[*Spoiler: Example input: — omitted*]text
5
0 4 3 2 1
2 1 0 4 3
4 3 2 1 0
1 0 4 3 2
3 2 1 0 4
```
```

After importing the file, you should choose a number from 0 to n - 1. Red and blue arrows will appear in the graph, which represents the left and right multiplication of the selected number, respectively.

**Jihoon Hyun:**

1. Is there a non-right-cancellative finite 677 magma which is not idempotent? The non-right-cancellative model with $$31\times 16$$ elements uploaded here is idempotent.
2. Do all finite magmas satisfying 677 have a unique idempotent element, unless all elements are idempotent?
3. Is there an explicit example of non-isomorphic finite 677 magmas with equal order?

**Terence Tao:**

I think one can answer these questions with the direct product construction.  For instance, by taking the direct product of the idempotent non-right-cancellative finite model and a non-idempotent finite model one should get a finite model that is both non-right-cancellative and non-idempotent.  Similarly for the second question.  For the third one should be able to take the product of two linear models on $$F_p$$ which could be distinguished from a linear model on $$F_{p^2}$$.

**Jose Brox:**

The first size in which this happens is 7, in which there are two isoclasses of 677 models. Here you have two representatives:

[*Spoiler: NON-ISOMORPHIC MODELS OF SIZE 7 — omitted*]

**Jihoon Hyun:**

After looking into several 677 magmas, I now have a conjecture that $$((b \diamond a) \diamond a) \diamond a = b$$ when $$a \diamond b = a$$. This will give at least two fixed points for a map $$x\mapsto ((x\diamond a) \diamond a) \diamond a$$ unless $$a\diamond a=a$$ or not 255.

**Jihoon Hyun:**

[attached: 17.zip]
I had to interrupt cadical running for magma (satisfying 677 but not 255) of size 17. Here are cnf and its corresponding log.

**Jose Brox:**

Perhaps you know that yesterday there was a national electrical blackout in Spain (where I'm located) for several hours. Luckily, the computer where my experiments farm is running is sited inside a tier 2 data center, what has allowed the computations to survive the blackout. So the 23 experiments I'm running for 677 are still going on (although they may not matter much now with the initial project being officially completed, modulo the paper).

**Bruno Le Floch:**

*EDIT: Actually, scratch that, I think there are some obstructions to violating 255 with a Lie 677-magma that has an idempotent, so the approach may be doomed.  I will try to report in 1-10 days on whether the following calculation is useful to perform.*

Can someone with more computing power check that ATPs fail to prove 255 from `((x*y)*z)*x=((x*z)*(y*z))*x` and 677 and left-cancellability and existence of an idempotent?  Same question for `((x*y)*z)*y=((x*z)*(y*z))*y` instead.  Among 3-variable equations obeyed by linear 677-magmas of type 1 (`a+b=1` and `b^4-b^3+b^2-b+1=0`) they are the simplest that might not imply 255.

Then, I would seek Lie magmas obeying 677 and that equation, constructed order by order around an idempotent element.  With a 3-variable equation, the lowest-order terms in the expansion typically fix the higher-order terms, just like a Lie algebra exponentiates to a Lie group by Lie's third theorem —with possible non-perturbative obstructions.

**Jose Brox:**

What is a Lie magma for you?

Regarding the other two identities in your message (which are 16018451 and 16020367, respectively), Vampire in CASC mode cannot show 255 from either set of hypotheses in 30min (neither if we also add surjectivity of left multiplication). Neither can Prover9 with max_weight=300 and sos_limit=200 (without surjectivity). On the other hand, Mace4 has shown that with your hypotheses (even without the idempotent condition) there are no models of size 12 or 13 for either identity (25min for 16018451, 75min for 16020367). Recall that there are no models of 677 anti 255 of order up to 11 included.

I include the files here in case you want to play with them:
[attached: MACE4 anti 255 Bruno 2]
[attached: MACE4 anti 255 Bruno]
[attached: TPTP677anti255Bruno2.p]
[attached: TPTP677anti255Bruno.p]

**Bruno Le Floch:**

Thanks for running that code!

There is a lot of theory to be developed around Lie magmas, I don't want to get carried away too much in this thread, so I'll try to keep it short.  For me, Lie magmas over R or C are real/complex manifolds equipped with a smooth (analytic?) binary operation, possibly obeying one of our equational laws.  For instance Lie groups are equipped with $$g\diamond h=gh^{-1}$$ obeying the Higman-Neumann axiom.

Let me assume there is an idempotent (e.g. the identity element in a Lie group), and Taylor expand the magma operation in some coordinate patch around that idempotent point.  Terms in the series are binary operations that are polynomial in a pair of tangent vectors.  Only some combinations of them are coordinate-invariant (details have to do with magma cohomology).  The first-order term in the Taylor series is a binary operation that is linear in its arguments and obeys whatever equational law we want to impose.  E.g., for Lie groups $$(1+x)\diamond(1+y)=1+(x-y)+\dots$$ thus this operation is subtraction, which is the only linear model obeying Higman-Neumann.

The Lie bracket can be found at quadratic order in two ways: as whatever remains after fixing coordinate invariance, or as a coordinate-invariant combination of the group operations.  Let's work in $$G=GL(n,\mathbb{R})$$ for concreteness, so $$x,y$$ are $$n\times n$$ matrices.  (1) We have $(1+x)\diamond(1+y)=1+(x-y)+(-xy+y^2)+\dots$$.  A coordinate redefinition changes $$x\to x+B(x)+\dots$$ and likewise for $$y$$ and $$x-y$$ with the same quadratic $$B$$, which changes the quadratic term to $$-xy+y^2+B(x)-B(y)-B(x-y) = -xy+y^2+2B(x,y)-2B(y)$$ with $$B(x,y)$$ being the corresponding symmetric bilinear form.  Picking $$B(y)=y^2/2$$ we obtain $$-xy+(xy+yx)/2$$, which features the Lie bracket.  (2) We have the usual way to get the Lie bracket from $$(1+x)\diamond((1+y)\diamond((1+y)\diamond(1+x))) = (1+x)(1+y)(1+x)^{-1}(1+y)^{-1} = 1+(yx-xy)+…$$.  This combination of operations can probably be seen from magma cohomology.

For two-variable equations, the quadratic terms are not enough to fix higher-order terms.  For three-variable equations I think they are often enough to fix all higher-order terms.  However, even if the series converges the chart does not necessarily cover the whole Lie magma (for Lie central groupoids, I found a case where the law is obeyed as long as we stay in some patch but it doesn't seem possible to extend to a whole magma).  For Lie groups, Lie's third theorem tells us it works, but its proofs are not very nice.

My hope is that some of that discussion also works over a finite field.

**Grant P:**

Greetings from Big Proof! @Terence Tao mentioned this problem in his wonderful talk on Tuesday, and I haven't been able to stop thinking about it :-). I've been trying to read the full history in here to see what you've already discovered, and have two small observations (apologies if this is already known and I missed it!): 

- 677 + Associativity -> 255, so all counterexamples must be non-associative
- If there is even a single "middle associative element," then 677 -> 255. I.e. Given 677 and
```math
\exists c \ \forall y, z \quad y \diamond (c \diamond z) = (y \diamond c) \diamond z
```
then 255 holds. 

So, counterexamples must be extremely non-associative!

**Grant P:**

Prover9 input and proofs for the above: 
[attached: Passmore 677=>255.txt]

**Fox Room:**

~~In fact, it can't be alternative on either side (that is, equations 4396 and 4473), or many combinations of these identities:~~
~~1. z * (x * (z * y)) = ((z * x) * z) * y~~
~~2. x * (z * (y * z)) = ((z * x) * z) * y~~
~~3. (z * x) * (y * z) = z * ((x * y) * z)~~
~~4. (z * x) * (y * z) = (z * (x * y)) * z~~
~~5. ((z * x) * y) * x = z * ((x * y) * x).~~

~~In particular the pairs 1 and 2, 2 and 5, or 3 and 5 suffice.  I believe 2 and 4 or 2 and 3 also suffice but Prover9 takes forever (over 30 minutes) to prove it if true, and the proof of 3 and 5 indeed took like 15 minutes.~~
~~The triples 1, 3, 4 or 2, 3, 4 also suffice.~~
~~Note that this means that any set of four, and indeed any set of three except (1, 4, 5), suffices, and the insufficient remaining pairs (aside from the conjectural two above) are only (1, 3), (1, 4), (1, 5), (3, 4), and (4, 5).~~

~~If we add the flexible identity (4435), 1 or 5 alone also suffice, as well as (4, 5) and the pairs (2, 3), (2, 4) above.  This means that any pair except (3, 4) and any triple, suffices alongside flexibility.~~

~~Moreover, if we add the Jordan identity ((x * x) * y) * x = (x * x) * (y * x), I believe 1 alone, and all pairs other than (3, 4), suffice, but (1, 3) and (1, 5) certainly do, as well as the conjectural pair (2, 3), and all triples.  Note that even all of flexible, Jordan, and (3, 4) does not suffice.~~

~~Finally (??), the extra identity ((x * y) * z) * x = x * (y * (z * x)) suffices alongside 2 alone, but not even (1, 4, 5, extra) or (3, 4, extra, flexible, Jordan) do.~~
~~(1, 4, extra, Jordan) *is* sufficient.~~

~~All of these should be easy to verify with Prover9, and all except for 3+5 should be trivial to verify.~~

**Fox Room:**

Oh, actually, these were all trying to prove the existence of a middle associative element; in my excitement I forgot entirely about 677 itself!

All of the results above were a spectacular waste of time, as out of all eight of the conditions I mentioned above, the only one I can't immediately establish as proving 255 alongside 677, is the Jordan property :sweat_smile:

**Fox Room:**

Well, I suppose this is interesting in and of itself; yes indeed a counterexample must be INCREDIBLY non-associative, as the only associative-like properties I know of that don't prove it are cube-associativity and the Jordan property!

**Matthew Bolan:**

If you've not seen it, many results on this implication are written up at https://teorth.github.io/equational_theories/blueprint/677-chapter.html . Bruno has also collected a number of known results here [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488745524) (though this is somewhat outdated, Terry's construction gives examples which don't come from linear models for example).

**Jihoon Hyun:**

Updates on SAT attack: It's been 244 days since I ran the experiment on +677 -255 magmas of size 12 to 16, but none of them terminated yet. The experiment will terminate when the planned outage begins in early November.

**Jihoon Hyun:**

This is probably the last update on the fairly 'simple' SAT attack. The power is going down this weekend, so I will abort the experiment before that. Of course there is no sign of termination even for size 12 magma. I'm planning on constructing a better CNF next time..

**Bruno Le Floch:**

It would be interesting for a future experiment to try and construct partial models, namely partially-filled multiplication tables such that if `y◇x` is defined then `x=y◇(x◇((y◇x)◇y))` is entirely defined and satisfied.  Depending on details of numbers of edges modulo 2 and 5 they can be completed by partial models of sizes 5 and 11 obtained from idempotent linear models by removing the `x◇x` entries.

**Matthew Bolan:**

That sounds pretty promising - could you say more about the completion process? Are the details just that the partial model needs to be large enough, contain a counterexample to 677, and meet some congruence constraints? The greedy algorithm already may be able to provide a plethora of such examples, or grow an example not meeting the congruence constraints into one meeting them, though your definition of partial model may be stricter than the one used by the algorithm.

**Matthew Bolan:**

To copy from an ancient message in this channel, the greedy algorithm we have for 677 shows that we can greedily extend partial magmas obeying:
1.  If $$y \diamond x = z$$, $$z \diamond y = w$$, $$x \diamond w = u$$, then $$x = y \diamond u$$ (this is just 677)
2. If $$x \diamond y = y \diamond x = x$$ then $$x \diamond x = y$$
3. If $$x \diamond x = y$$, $$x \diamond y = z$$, and $$z \diamond x = x$$ then $$z = x$$
4. If $$x \diamond y = z$$, $$y \diamond w = x$$, and $$z \diamond y = w$$, then $$z \diamond w = y$$. 

(2-4 are requirements following from 677 which should be forced by your definition automatically)
Already the partial magma with $$1 \diamond 1 = 0, 1 \diamond 0 = 0$$ and no other products defined is a partial magma under this definition witnessing anti-255.

Your definition for partial magma uses a much stronger definition for the first constraint since the moment $$y \diamond x = z$$ is defined you require $$z \diamond y = w$$ and $$x \diamond w = u$$ to be defined, but perhaps we can just write up an extra greedy algorithm to promote one of these partial magmas into a partial magma under your definition, by picking a product not yet defined but required by your definition and trying to set it equal to some element we've already used.

**Matthew Bolan:**

I threw something quick together to try that and it doesn't seem too promising - if I tell it to try and keep the table as small as possible for as long as possible it is able to make quite large partial multiplication tables with around 84% of the products completed , but many of the remaining undefined products cannot be made to satisfy Bruno's condition without additional symbols, so the size is a bit of a lie. Still, I'll leave it running for the afternoon, and maybe we'll get lucky or someone will think of how to be smarter than randomly picking a previously used element which works. Probably we need to find such things through ATP runs though.

**Matthew Bolan:**

The correct heuristic might be to pick some product which Bruno's partial magmas require us to define (no idea how to pick this intelligently), try and set this to some already used symbol (no idea how to pick which one intelligently), run the greedy algorithm to complete the table, and if the total number of violations of Bruno's condition went down, keep it. If no such modifications are available then we have to define this product to be some new element, or maybe some previous element which introduces the smallest number of new violations. There also could be finiteness considerations in running the greedy algorithm, if we know laws 677 implies for finite magmas but not infinite ones our greedy algorithm has to be careful to respect those.

**Bruno Le Floch:**

Indeed, my definition of partial model is pretty restrictive so my comment was only a tiny step towards building a E677⊨E255 counterexample.  Long story short: for each $$y$$, left multiplication $$L_y$$ is a bijection on the subset $$A_y$$ on which it is defined, and the congruence condition is that $$A_y\setminus\{y\}$$ has even cardinal for each $$y$$.

Consider the (partially defined) left multiplication map $$L_y$$ by some element $$y$$, which maps a subset $$A_y = \{x\mid y\diamond x \text{ defined}\}$$ to $$B_y = \{y \diamond x\}$$.  Since $$y\diamond x$$ defined implies $$x=y\diamond\dots$$, we have $$A_y\subset B_y$$.  But $$|B_y|\leq|A_y|$$, with equality if and only if $$L_y$$ is injective (hence bijective on its image).  So we have that $$L_y$$ is a permutation of $$A_y=B_y$$.

A second restriction is that the set of defined products is symmetric.  If $$y\diamond x$$ is defined then $$x=y\diamond z$$ (for $$z=x\diamond((y\diamond x)\diamond y)$$), so $$z=y\diamond(z\diamond((y\diamond z)\diamond y))$$ and in particular the product $$(y\diamond z)\diamond y = x\diamond y$$ is defined.

Now let's try to complete such a partial model.  Set any undefined $$x\diamond x$$ to be $$x$$.  Consider the undirected graph with edges $$x-y$$ for each undefined product $$x\diamond y$$ (or equivalently $$y\diamond x$$).  If this graph can be written as a union of graphs isomorphic to $$K_5$$ and $$K_{11}$$, then for each $$K_5$$ we can use the multiplication table $$a\diamond b=2a-b\pmod{5}$$ with its idempotents omitted, and for each $$K_{11}$$ we can use the multiplication table $$a\diamond b=-a+2b\pmod{11}$$ with idempotents omitted.  This immediately gives a complete model: to test equation 677 for some $$(x,y)$$, just check whether $$y\diamond x$$ was defined in the original partial model, or in one of the $$K_n$$, and note that the equation only involves other products in this same portion of the multiplication table.

Now the less obvious part perhaps is when we should expect a decomposition into $$K_5$$ and $$K_{11}$$.  When building spectra of some 2-variable laws we came across some references that proved that large-enough random-enough graphs could be covered by such graphs $$K_k$$ for some set of $$k$$ if and only if the total number of edges was divisible by the gcd of the numbers of edges of the $$K_k$$ and the vertex degrees were divisible by the gcd of vertex degrees of the $$K_k$$.  Here $$K_5$$ has $$10$$ edges and vertices of degree $$4$$, while $$K_{11}$$ has $$55$$ edges and vertices of degree $$10$$, so these gcds are $$5$$ and $$2$$, respectively.  (Larger linear idempotent models do not help because tenth roots of unity only exist in characteristic congruent to $$1,5$$ mod $$10$$ as far as I can tell.)

Given a partial model of size $$n$$, we can add a large number $$N$$ of vertices to reach the "large-enough" and "random-enough" thresholds.  The degrees of the new vertices is $$N+n-1$$, which we want to be even and the degrees of a vertex $$y$$ in the original partial model is $$N+n-1-|A_y\setminus\{y\}|$$, so the parity condition is that every $$|A_y\setminus\{y\}|$$ is even.  The mod-5 constraint works out to be that the total number of products $$x\diamond y$$ with $$x\neq y$$ that are defined has to be congruent to $$0,1,2$$ modulo $$5$$.  This is easily achieved by taking five disjoint copies of the partial model.

**Bruno Le Floch:**

The congruence condition can be weakened very slightly: for each $$y$$ with $$y\in A_y$$ we need $$|A_y|$$ odd.  (Namely we can drop the condition completely for $$y\not\in A_y$$.)

Indeed, let $$K=\{y\mid y\not\in A_y,\text{odd }|A_y|\}$$ (in particular $$y\diamond y$$ is not defined in the partial model) and consider the subset $$(K\times M)\cup (M\times K) \subset M\times M$$, equipped with the partial operation $$(u,x)\diamond(u,y) = (u, x\diamond y)$$ and $$(x,u)\diamond(y,u)=(x\diamond y,u)$$ for $$u\in K$$ and $$x,y\in M$$ when $$x\diamond y$$ is defined.  The two definitions do not collide: they could only overlap if the two operands were the same and belonged to $$K$$, in which case $$x\diamond x$$ would not be defined.  It is easy to check that the new model is a partial model.  One has $$A_{(u,v)}=(\{u\}\times A_v)\cup(A_u\times\{v\})$$ for $$u,v\in K$$, with the union being disjoint and both sets having odd cardinality.  For $$u\in K$$ and $$x\in M\setminus K$$ one gets $$A_{(u,x)}=\{u\}\times A_x$$, which is also such that $$A_{(u,x)}\setminus\{(u,x)\}=\{u\}\times(A_x\setminus\{x\})$$, obeying the parity condition.

**Matthew Bolan:**

I decided to try Jose's suggestion from #**Equational>Writing the paper@546304765** of playing around with proof assistants capable of higher order logic, though probably he has done more in this direction than I have. I couldn't get the versions of vampire which support this to work, so I wound up using an ATP called leo-III (https://github.com/leoprover/Leo-III ). A minor victory is that I was able to tell Leo3 that it can assume injectivity and surjectivity are equivalent, and with just that it seems to be able to prove the simpler finite only implications (though I've not checked its output for correctness, and only checked a few). 

 I couldn't get it to prove the implication from 3308 to 3511, which was proven using Terry's lemma that if we let $$X$$ be finite, and let $$f, g: X \to X$$ be such that $$f = f \circ f \circ g$$, then $$f = f \circ g \circ f$$. The proof of this lemma uses some pigeonhole type arguments which I don't know how to teach Leo3. (However I could tell Leo3 that this lemma is true, after which it can prove the implication).

 Obviously I also could not get it to prove 677 implies 255.

**Matthew Bolan:**

Oh, and I also gave up on trying to modify the old greedy algorithm to try and make partial magmas of Bruno's type - the greedy algorithm for 677 seems very far from being a greedy algorithm for 677 + left multiplication being bijective.

**Bruno Le Floch:**

How fast does Leo3 find proofs of finite(73⊨125) and other easy finite implications that only rely on injectivity = surjectivity?  E.g., on a single 4.8GHz processor (Intel i7-11850H) I can prove every positive infinite implication with Prover9 in less than 30min.

**Matthew Bolan:**

For that implication it reports it took `1316 ms resp. 1162 ms w/o parsing`. I've not tried very many of the easy finite implications as I currently am just manually making the input files, but around 1 second seems to be the norm. 

`[*Spoiler: Here's the proof it finds for 73 implying 125 — omitted*]
thf(f_type, type, f: ($i > ($i > $i))).
thf(is_injective_type, type, is_injective: (($i > $i) > $o)).
thf(is_surjective_type, type, is_surjective: (($i > $i) > $o)).
thf(sk1_type, type, sk1: $i).
thf(sk2_type, type, sk2: $i).
thf(sk3_type, type, sk3: (($i > $i) > $i)).
thf(sk4_type, type, sk4: (($i > $i) > $i)).
thf(sk5_type, type, sk5: ($i > (($i > $i) > $i))).
thf(is_injective_def, definition, (is_injective = (^ [A:($i > $i)]: ! [B:$i,C:$i]: (((A @ B) = (A @ C)) => (B = C))))).
thf(is_surjective_def, definition, (is_surjective = (^ [A:($i > $i)]: ! [B:$i]: ? [C:$i]: ((A @ C) = B)))).
thf(3,axiom,((! [A:($i > $i)]: ((is_injective @ A) => (is_surjective @ A)))),file('leo_finite_73_125.thf',finite_inj_surj)).
thf(10,plain,((! [A:($i > $i)]: ((! [B:$i,C:$i]: (((A @ B) = (A @ C)) => (B = C))) => (! [B:$i]: ? [C:$i]: ((A @ C) = B))))),inference(defexp_and_simp_and_etaexpand,[status(thm)],[3])).
thf(11,plain,(! [B:$i,A:($i > $i)] : (((A @ (sk3 @ (A))) = (A @ (sk4 @ (A)))) | ((A @ (sk5 @ B @ (A))) = B))),inference(cnf,[status(esa)],[10])).
thf(13,plain,(! [B:$i,A:($i > $i)] : (((A @ (sk4 @ (A))) = (A @ (sk3 @ (A)))) | ((A @ (sk5 @ B @ (A))) = B))),inference(lifteq,[status(thm)],[11])).
thf(6,axiom,((! [A:$i,B:$i]: (A = (f @ B @ (f @ B @ (f @ A @ B)))))),file('leo_finite_73_125.thf',magma_axiom)).
thf(23,plain,((! [A:$i,B:$i]: (A = (f @ B @ (f @ B @ (f @ A @ B)))))),inference(defexp_and_simp_and_etaexpand,[status(thm)],[6])).
thf(24,plain,(! [B:$i,A:$i] : ((A = (f @ B @ (f @ B @ (f @ A @ B)))))),inference(cnf,[status(esa)],[23])).
thf(25,plain,(! [B:$i,A:$i] : (((f @ B @ (f @ B @ (f @ A @ B))) = A))),inference(lifteq,[status(thm)],[24])).
thf(1,conjecture,((! [A:$i,B:$i]: (A = (f @ B @ (f @ (f @ B @ A) @ B))))),file('leo_finite_73_125.thf',magma_conjecture)).
thf(2,negated_conjecture,((~ (! [A:$i,B:$i]: (A = (f @ B @ (f @ (f @ B @ A) @ B)))))),inference(neg_conjecture,[status(cth)],[1])).
thf(7,plain,((~ (! [A:$i,B:$i]: (A = (f @ B @ (f @ (f @ B @ A) @ B)))))),inference(defexp_and_simp_and_etaexpand,[status(thm)],[2])).
thf(8,plain,((~ (sk1 = (f @ sk2 @ (f @ (f @ sk2 @ sk1) @ sk2))))),inference(cnf,[status(esa)],[7])).
thf(9,plain,(((f @ sk2 @ (f @ (f @ sk2 @ sk1) @ sk2)) != sk1)),inference(lifteq,[status(thm)],[8])).
thf(26,plain,(! [B:$i,A:$i] : (((f @ sk2 @ (f @ A @ sk2)) != sk1) | ((f @ B @ (f @ B @ (f @ A @ B))) != (f @ sk2 @ sk1)))),inference(paramod_ordered,[status(thm)],[25,9])).
thf(36,plain,(! [B:$i,A:$i] : (((f @ sk2 @ (f @ A @ sk2)) != sk1) | (B != sk2) | ((f @ B @ (f @ A @ B)) != sk1))),inference(simp,[status(thm)],[26])).
thf(41,plain,(! [A:$i] : (((f @ sk2 @ (f @ A @ sk2)) != sk1))),inference(simp,[status(thm)],[36])).
thf(43,plain,(! [C:$i,B:$i,A:$i] : ((A != sk1) | ((f @ B @ (f @ B @ (f @ A @ B))) != (f @ sk2 @ (f @ C @ sk2))))),inference(paramod_ordered,[status(thm)],[25,41])).
thf(46,plain,(! [B:$i,A:$i] : ((A != sk2) | ((f @ A @ (f @ sk1 @ A)) != (f @ B @ sk2)))),inference(simp,[status(thm)],[43])).
thf(49,plain,(! [A:$i] : (((f @ sk2 @ (f @ sk1 @ sk2)) != (f @ A @ sk2)))),inference(simp,[status(thm)],[46])).
thf(225,plain,(! [C:$i,B:$i,A:($i > $i)] : (((A @ (sk4 @ (A))) = (A @ (sk3 @ (A)))) | (B != (f @ sk2 @ (f @ sk1 @ sk2))) | ((A @ (sk5 @ B @ (A))) != (f @ C @ sk2)))),inference(paramod_ordered,[status(thm)],[13,49])).
thf(233,plain,(! [B:($i > $i),A:$i] : (((f @ (B @ (sk4 @ (^ [C:$i]: (f @ (B @ C) @ sk2)))) @ sk2) = (f @ (B @ (sk3 @ (^ [C:$i]: (f @ (B @ C) @ sk2)))) @ sk2)) | (A != (f @ sk2 @ (f @ sk1 @ sk2))))),inference(pre_uni,[status(thm)],[225:[bind(A, $thf(^ [E:$i]: (f @ (D @ E) @ sk2))),bind(B, $thf(B)),bind(C, $thf(D @ (sk5 @ B @ (^ [E:$i]: (f @ (D @ E) @ sk2)))))]])).
thf(234,plain,(! [A:($i > $i)] : (((f @ (A @ (sk4 @ (^ [B:$i]: (f @ (A @ B) @ sk2)))) @ sk2) = (f @ (A @ (sk3 @ (^ [B:$i]: (f @ (A @ B) @ sk2)))) @ sk2)))),inference(pattern_uni,[status(thm)],[233:[bind(A, $thf(f @ sk2 @ (f @ sk1 @ sk2))),bind(B, $thf(B))]])).
thf(250,plain,(! [A:($i > $i)] : (((f @ (A @ (sk4 @ (^ [B:$i]: (f @ (A @ B) @ sk2)))) @ sk2) = (f @ (A @ (sk3 @ (^ [B:$i]: (f @ (A @ B) @ sk2)))) @ sk2)))),inference(simp,[status(thm)],[234])).
thf(554,plain,(! [C:$i,B:$i,A:($i > $i)] : (((f @ C @ (f @ C @ (f @ (A @ (sk3 @ (^ [D:$i]: (f @ (A @ D) @ sk2)))) @ sk2))) = B) | ((f @ (A @ (sk4 @ (^ [D:$i]: (f @ (A @ D) @ sk2)))) @ sk2) != (f @ B @ C)))),inference(paramod_ordered,[status(thm)],[250,25])).
thf(596,plain,(! [A:($i > $i)] : (((f @ sk2 @ (f @ sk2 @ (f @ (A @ (sk3 @ (^ [B:$i]: (f @ (A @ B) @ sk2)))) @ sk2))) = (A @ (sk4 @ (^ [B:$i]: (f @ (A @ B) @ sk2))))))),inference(pre_uni,[status(thm)],[554:[bind(A, $thf(A)),bind(B, $thf(A @ (sk4 @ (^ [D:$i]: (f @ (A @ D) @ sk2))))),bind(C, $thf(sk2))]])).
thf(968,plain,(! [A:($i > $i)] : (((A @ (sk4 @ (^ [B:$i]: (f @ (A @ B) @ sk2)))) = (A @ (sk3 @ (^ [B:$i]: (f @ (A @ B) @ sk2))))))),inference(rewrite,[status(thm)],[596,25])).
thf(12,plain,(! [B:$i,A:($i > $i)] : ((~ ((sk3 @ (A)) = (sk4 @ (A)))) | ((A @ (sk5 @ B @ (A))) = B))),inference(cnf,[status(esa)],[10])).
thf(14,plain,(! [B:$i,A:($i > $i)] : (((sk4 @ (A)) != (sk3 @ (A))) | ((A @ (sk5 @ B @ (A))) = B))),inference(lifteq,[status(thm)],[12])).
thf(974,plain,(! [C:$i,B:($i > $i),A:($i > $i)] : (((A @ (sk3 @ (^ [D:$i]: (f @ (A @ D) @ sk2)))) != (sk3 @ (B))) | ((B @ (sk5 @ C @ (B))) = C) | ((A @ (sk4 @ (^ [D:$i]: (f @ (A @ D) @ sk2)))) != (sk4 @ (B))))),inference(paramod_ordered,[status(thm)],[968,14])).
thf(1100,plain,(! [A:$i] : (((sk3 @ (^ [B:$i]: (f @ B @ sk2))) != (sk3 @ (^ [B:$i]: (f @ B @ sk2)))) | ((f @ (sk5 @ A @ (^ [B:$i]: (f @ B @ sk2))) @ sk2) = A))),inference(pre_uni,[status(thm)],[974:[bind(A, $thf(^ [D:$i]: (D))),bind(B, $thf(^ [D:$i]: (f @ D @ sk2)))]])).
thf(1101,plain,(! [A:$i] : (((f @ (sk5 @ A @ (^ [B:$i]: (f @ B @ sk2))) @ sk2) = A))),inference(pattern_uni,[status(thm)],[1100:[]])).
thf(1193,plain,(! [A:$i] : (((f @ (sk5 @ A @ (^ [B:$i]: (f @ B @ sk2))) @ sk2) = A))),inference(simp,[status(thm)],[1101])).
thf(1778,plain,(! [B:$i,A:$i] : ((A != (f @ sk2 @ (f @ sk1 @ sk2))) | ((f @ (sk5 @ A @ (^ [C:$i]: (f @ C @ sk2))) @ sk2) != (f @ B @ sk2)))),inference(paramod_ordered,[status(thm)],[1193,49])).
thf(1779,plain,(! [A:$i] : ((A != (f @ sk2 @ (f @ sk1 @ sk2))))),inference(pattern_uni,[status(thm)],[1778:[bind(A, $thf(C)),bind(B, $thf(sk5 @ C @ (^ [D:$i]: (f @ D @ sk2))))]])).
thf(1947,plain,(($false)),inference(simp,[status(thm)],[1779])).
```
````

**Bernhard Reinke:**

I played around a bit with translation invariant model on $$ \mathbf{F}_{31} $$ given by $$x\diamond y = 5 x - 4y + 1$$. I wanted to see if there exists a nice extension $$ \mathbf{F}_{31} \times M $$ of the form $$ (x, s) \diamond (y, t) = (x \diamond y, s \diamond_{x-y} t) $$, so that the extension will still have a translation symmetry. I tried to encode it into a SAT problem for z3 similarly to the encoding of @Jihoon Hyun . I think I can exclude extensions where $$ M $$ has cardinality less than 4, 4 is still running. It would be interesting so see at least if there are cases where we have an extension of a similar form satisfying 677 where the cardinality of M does not belong to the spectrum of 677.

**Bernhard Reinke:**

Another idea that unfortunately hasn't gone very far yet is to look at models on $$\mathbf{F}_{31} \times \mathbf{F}_{31} $$  where $$ (x, s) \diamond (y, t) = (5x - 4y + 1, p(x,y,s,t)) $$ where `p` polynomial of low degree `d` in  $$\mathbf{F}_{31}[x,y,s,t] $$. I think we have an argument to exclude affine polynomials, I guess we can exclude quadratic polynomials as well, but I am not 100% sure. I hope it gets interesting once $$d^4$$ is bigger than the characteristic of the ground field.

**Bernhard Reinke:**

btw, I think there is a small typo in the blueprint at https://teorth.github.io/equational_theories/blueprint/677-chapter.html#ext-eq : it is $$\diamond^+$$ that is not right-cancellative, not $$\diamond^0$$.

**Matthew Bolan:**

I was able to use leo to prove 27/45 of the implications in #**Equational>✔ List of finite-specific implications@526299732**  by only giving it second order statements saying injectivity/surjectivity/invertibility are equivalent for maps $$M \to M$$. It seems that when it finds a proof it finds it in a few seconds. 

It certainly is still missing some proofs that seem to me to be pretty basic consequences of the equivalence of surjectivity / injectivity / invertibility , for example it failed to prove that 65 implies 1491 for finite magmas. This might just be an issue of me giving it too little time. My vague hope is that I can eventually give Leo a list of reasonable facts about finite sets which are enough to resolve most/all the other finite implications, and then when it fails to prove 677 implies 255 that can be more weak evidence for the idea that a counterexample exists.

**Rudi Schneider:**

one class of 677 models that I haven't seen being discussed yet are models of the form `f(x, y) = M1*x + M2*y`,
where `M1, M2` are matrices, and `x, y` are vectors of elements modulus p.

For example the smallest non-linear model with size 9 is from this class with `M1 = I`, `M2 = [[0, 1], [1, 1]]`, `p=3`.

**Terence Tao:**

This looks essentially like a linear model of the type ruled out in Lemma 13.3 of https://teorth.github.io/equational_theories/blueprint/677-chapter.html .

**Matthew Bolan:**

@Jose Brox I know you also experimented with trying to find some reasonable set of higher order axioms which capture some useful effects of finiteness. In my view there should be some ATP which can at least rediscover the equivalence of 65 and 1491 given only some higher order facts about surjectivity implying injectivity, but I've yet to get Leo3 to do this. Can whatever version of Vampire you tried find this implication?

**Matthew House:**

~~old info~~

**Matthew House:**

Sorry if it was mentioned somewhere, but how can we derive the finite implication 677 `x = y*(x*((y*x)*y))` → 19855 `x = (y*x)*((y*(y*x))*y)`?

**Matthew House:**

Never mind, I see it's just substituting `y*x = y*((y*x)*((y*(y*x))*y))` then applying invertiblity. For SAT solvers, 19855 appears to help since it yields the simple biimplication `x*((y*x)*y) = z` ↔ `y*z = x`.

**Rudi Schneider:**

Hey, I had a look at the automorphism groups of known 677 magmas and noticed that most of them contain the symmetry `(0) (1 2 3 ... n-1)`.

If I'm not mistaken, this induces a model class very similar to translation invariant models, using a special element "r" and the following rules:
```
f(r, r) = r
f(i, r) = a + i
f(r, j) = b + j
f(i, j) = i + h(j-i) for some bijection h : [0, k-1] -> ([0, k-1] ∪ {r}) \ {a}.
```

I write + and - to express addition and subtraction modulus k, which we extend by the absorbing element r. (so r+i = r generally holds), and i, j to denote natural numbers mod k (which r is not).

A small search found 21 677-magmas of this class, but so far all of them are right-cancellative.
[attached: semitinv_models.txt]

**Matthew Bolan:**

I suspect the models in the text file are all linear, though maybe the order 25 ones are not. They at least all pass this test [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/497337336), but given how they are constructed maybe that's to be expected. Interesting observation though.

**Matthew Bolan:**

The last 7 of the order 25 models are not linear, but I think they may all come from the magma cohomology construction.

**Matthew Bolan:**

Perhaps they are new!! The current $$25 \times 25$$ models coming from cohomology I have on hand pass the test where the translations $$L_x L_y^{-1}$$ all commute, but your models fail this test!

**Matthew Bolan:**

When I get home I'll check that for the other size 25 magmas coming from cohomology, but they all come from the same class as the one I tested, so my guess is that these are the first genuinely new 677 magmas in months.

**Matthew Bolan:**

Its confirmed! The last 7 of these are not isomorphic to any linear/cohomological model of order 25. They are also not isomorphic to the five order 25 submagmas of Zoltan's order 125 magma described here: [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/490657100) (Unsurprising since I think these were shown to be cohomological models as well).

**Rudi Schneider:**

hey, very cool to hear! Here's a list of all sufficiently interesting small models I've found at some point (https://github.com/memoryleak47/eq677/tree/main/db), I could imagine that the 21-sized or 41-sized models haven't been shared yet. They were found by a translation-invariant search.

**Matthew Bolan:**

There are linear models of order 41, but order 21 is even a new ORDER.

**Matthew Bolan:**

Are all the models you find this way idempotent?

**Rudi Schneider:**

It's a general DPLL-based search, so it should find all models -- not idempotent by construction

**Rudi Schneider:**

the 41-sized ones were constructed using a translation invariant-search with `h = h⁻¹`(which implies 255),
and the 21-sized ones were general translation-invariant models.
The "general model search" works til size 11 (which you can clear in 3h).

**Matthew Bolan:**

I'm wondering about your order 21 model, since it definitely works, but I was under the impression that translation invariant models of this size had already been checked for. What is the carrier?

**Rudi Schneider:**

[attached: out]
Here are all the different 'h' that construct that model.

I'm using modular arithmetic mod 21.
so `f(x, y) = (x + h(y-x))%21`.

I would assume that either people only checked prime modulus, or restricted the search to anti-255?

**Rudi Schneider:**

I just checked the server, and there's a new semitinv model: https://github.com/memoryleak47/eq677/commit/48af85a510e4512cce6d3098baea974d5412dfd5
might very well be linear though

edit: It is linear.

**Matthew Bolan:**

The tests I know for linearity (though they don't prove it) are this one [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/497337336) (checking the squaring and cubing maps seems to be a quick way to catch many non-linear magmas) and this one [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488748039)

**Matthew Bolan:**

For 255 we only care about magmas generated by a single element. It would be interesting if any of your magmas give a new 677 magma generated by a single element.

**Matthew House:**

Huh, what does this "general model search" look like? I've been playing with various encoding and symmetry-breaking schemes on top of CaDiCaL, and my latest iteration can clear size 8 in 6s and size 9 in 3m42s, but is still running at 7h36m for sizes 10 and 11 (having not yet reported any results for the latter).

**Jihoon Hyun:**

@Matthew House [말함](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/558568437):

Actually, that's the performance you should get. Using CaDiCaL I got a negative result for size 10 in about 6 hours, and never got a result for size 12 after running for a bit less than a year..

**Matthew House:**

I'm mainly wondering if there's anything more I can wring out of the encoding. I've been trying to get my model-finder as fast as possible for some other projects I've been working on (for which 677 is a handy benchmark), and even a simple encoding with CaDiCaL will easily beat Mace4/Vampire at small sizes. But I'm no expert SAT-whisperer, and finding optimizations is a very unintuitive process.

**Matthew House:**

(In particular, when designing symmetry-breaking clauses, there seems to be an extremely fine line between optimizing and pessimizing the search.)

**Rudi Schneider:**

I had some fun building a custom DPLL-based model searcher entirely for equation 677 ^^
It's implemented here: https://github.com/memoryleak47/eq677/tree/main/src/c_dpll

The biggest perf effects were:
- simple freshness: I toyed around with more complicated notions of symmetry-breaking eg. starting to guess the first row, but simple freshness worked the best so far. Simple freshness just means "If for both x and y, you know no equations (i.e. `f(x, _) = _`, or `f(_, x) = _`, or `f(_, _) = x`"), then x and y are indistinguishable, and it suffices to only consider x"
- note that cadical is SAT-based, which this tool isn't. It's using constraints based on term equations `x = f(y, f(x, f(f(y, x), y)))` added for each pair of x, y. These constraints then simplify over time when more elements in the magma-matrix are filled out (using a listener scheme inspired by typical SAT watchers). This should generate far less constraints than you'd need in SAT, but I might miss some tricks there.
- model splitting: initially branch on `forall x: x*x = x`, which if true, fills out the whole diagonal, and otherwise gives you some non-idempotent element `x`, which you can choose as element 0 (which allows you to assume 0*0 = 1). And simply assuming `0*0 = 1` makes the the tool quite a bit faster. You can observe the same with mace4.
- When a constraint simplifies to `x = f(a, f(b, c))` check whether we know some `d` with `f(a, d) = x`. if yes, we can prove `f(b, c) = d`.

**Jihoon Hyun:**

@Rudi Schneider [말함](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/558572098):

Some tricks about this: You can assume not only $$0\diamond 0=1$$, but also:
- $$1\diamond 0=2$$
- $$0\diamond 2=3$$
- $$0\diamond 3=0$$
- $$3\diamond 1=2$$
- $$1\diamond 1\neq 0$$
- $$2 \diamond 1\neq 0$$
and some more as you wish.

**Rudi Schneider:**

that's true! I tried some of them, but for some reason they didn't work so well. I think it's due to the fact that eg. 1*0 = 2 "de-freshes" three elements (i.e. hinders our symmetry breaking), but just gives a single equation. I didn't really grok it though.

or do you mean we get *all* of those facts in combination without any other case to consider?

**Jihoon Hyun:**

Yes. As long as 0 and 1 are different and satisfy the construction that 0 does not satisfy 255, $$0\diamond 0=1$$, $$1\diamond 0=2$$, and $$0\diamond 2=3$$, you get the above result with $$0$$, $$1$$, $$2$$, and $$3$$ being pairwise disjoint.
As a consequence, you may let $$0\diamond 1 = 2$$ or $$0\diamond 1=4$$, but I wasn't sure what to do next after that.

**Jihoon Hyun:**

Okay, I have made my repository public:
https://github.com/qawbecrdtey/magma
There should be some information you'd like.

For example, for an element $$a$$ in a finite magma $$M$$ which satisfies equation 677, the following are equivalent:
- $$a$$ is idempotent, or, $$a\diamond a=a$$.
- $$(a\diamond a)\diamond a = a$$
- $$a\diamond (a\diamond a) = a$$
- $$a\cdot a = a$$
- $$(a\cdot a)\diamond a = a$$
- $$(a\diamond a)\diamond (a\diamond a)=a$$
- $$((a\diamond a)\diamond a)\diamond (a\diamond a)=a$$
- $$((a \diamond a)\diamond a)\diamond a=((a\diamond a)\diamond a)\cdot a$$
- For some $$n$$ which is not divisible by $$3$$, $$((a\diamond a)\diamond \cdots)\diamond a=a$$ when lhs have $$n$$ diamonds.

where $$a\cdot b = a\diamond ((b\diamond a)\diamond b)$$ is the left inverse.

By the way, I got a strong impression due to above, that any finite magma satisfying 677 ~~will always have an element which is idempotent~~, as there are so many equivalent equations to it. (Maybe anti-255 happens when no elements are idempotent?)

**Rudi Schneider:**

It improved n=10 performance from 20s down to 10s which is pretty good!
It's a slightly unfair comparison though, as the previous search did not assume ¬255.

**Rudi Schneider:**

> By the way, I got a strong impression due to above, that any finite magma satisfying 677 will always have an element which is idempotent, as there are so many equivalent equations to it.

I conjectured the same, but `f(x,y) = (5x + 27y + 1)%31` is a counter-example.

**Bernhard Reinke:**

I had a shot at this approach with similar techniques as for the models projecting to the translation invariant non-idempotent magma on $$\mathbf{F}_{31}$$,  assuming $$\neg 255$$ I got a little bit further and excluded $$|S| \leq 4$$.

**Bernhard Reinke:**

I would be curious to see whether @Rudi Schneider method works for more general symmetries, as for example `(0) (1) (2 ... n - 1)` or cycles with "small" set of fixed points.

**Rudi Schneider:**

I tried `(0) (1) (2 ... n-1)` but didn't find anything there up until size 26.

If you want to try something out, you can change this function, it encodes a forced automorphism that you can choose yourself: https://github.com/memoryleak47/eq677/blob/8b54ac3ac1469fce7b3e28ada77abc2a0db911b9/src/c_dpll/run.rs#L256

**Rudi Schneider:**

Here's a quick dump of the automorphism groups & some equational facts for magmas from the db.
[attached: analysis.txt]
You can see that the automorphism group is spanned mostly by a combination of
- tinv `(0 1 ... n-1)`
- semitinv `(0) (1 ... n-1)`
- but also some quirky ones like this one `(0) (1 3) (2 24) (4 14) (5 18) (6 10) (7) (8) (9 23) (11 12) (13 17) (15 20) (16 21) (19) (22)`.

But interestingly, I have not yet found a rigid model, i.e. one with trivial automorphism group. And in particular, all models from the db are either tinv or semitinv.

**Bernhard Reinke:**

this is on the `symmetric_dpll` branch?

**Bernhard Reinke:**

But I think some of the logic in `submit_model` on that branch still assumes the semitinv symmetry

**Rudi Schneider:**

oh sorry, yes. You'd need to comment that out. That's just debugging prints/checks basically.
You only need the call to `present_model` the rest is irrelevant.

**Matthew House:**

Thanks for all the tricks, I'd thought of writing a DPLL searcher, but I'd been a bit suspicious with how poorly Mace4's generic implementation fares at small sizes. A lot of it seems to be "finding helpful simple consequences", which is definitely an art that depends on the particular theory (especially with model splitting).

**Bernhard Reinke:**

Ok, I think there is an easy reason why this didn't produce any examples: the set of fixed points will form a submagma, but there are not magmas satisfying 677 of size 2. I am running a search for magmas with a symmetry consisting of a cyclic with 5 fixed points, but for size <= 25 I haven't found anything yet (excluding of course size 5)

**Bernhard Reinke:**

On the other hand, could it be useful to try to search for models that contain a certain model as a submagma? In principle we only need to consider magmas that are generated by one element, would it be possible for a minimal counterexample that the submagma generated by $$x \diamond x$$ is a proper submagma of the one generated by $$x$$?

**Bruno Le Floch:**

There are E677-magmas whose set of squares is a proper submagma: since one of the two models of size 7 is unipotent (all squares equal) and the other has a bijective squaring map, their product is a E677-magma whose set of squares has 7 elements.  Of course it isn't a E255 counterexample.

**Bruno Le Floch:**

The order 21 magma seems like a gluing of several submagmas of size 5.  It may be interesting to analyse it precisely.

**Rudi Schneider:**

some interesting properties of it are that it's tinv with `h = h⁻¹`, and
- `X = (f Y (f Y X))`
- `X = (f (f (f Y X) Y) Y)`
- `(f X Y) = (f (f Y X) X)`
- `X = (f (f Y X) (f X Y))`
- `X = (f (f (f X Y) X) Y)`

**Matthew Bolan:**

Looks like any two distinct elements of the order 21 magma generate an order 5 submagma.

**Matthew Bolan:**

An interesting observation by ChatGPT https://chatgpt.com/share/69208a78-ae8c-8012-abcf-afdb8bb5e030 the start of which seems correct to me.

**Terence Tao:**

I like this gluing operation!  So if I understand correctly, one can glue together any number of idempotent 677 magmas to form a larger idempotent 677 magma so long as one can arrange the carriers of the small magmas into a Steiner system of the big magma, where every pair of distinct points in the big carrier lies in exactly one small carrier?  This doesn't directly bring us closer to a 255 counterexample, but it could still somehow be a building block (or an inspiration) for a construction that does...

**Bruno Le Floch:**

Yes, the model of size 21 is just the projective plane over the finite field $$\mathbb{F}_4$$, with each projective line carrying the idempotent magma of size $$5$$.  To check equation 677 for $$y=x$$ just use idempotence, and for $$y\neq x$$ note that $$x,y$$ belong to exactly one line and the submagma they generate is just that line.

The magma of size 5 (namely $$x\diamond y=2x-y\mod 5$$) has automorphism group of order 20 (invertible affine maps) so on a set with five elements there are 120/20=6 different isomorphic binary operations.  For each of the 21 lines in the aforementioned projective plane we can choose one of these 6 operations.  I wonder if that can give magmas with trivial automorphism group.

The page https://web.math.pmf.unizg.hr/~krcko/results/steiner.html lists various collections of Steiner designs S(2,5,n) and S(2,7,n) which give us many models of 677 of cardinals 41, 45, 65, 91, 175, 213 (I think this list of values is completely ad-hoc, dependent of what cases some authors got interested in).  We already had linear models of these sizes, but there are considerably more.  All of them (by construction) are idempotent.

EDIT: This is redundant with the ChatGPT log above.  That said, the gluing operation was already mentioned earlier in this thread, and when studying the spectrum of various 2-variable laws that allow idempotent models.  In that spectrum discussion it allowed us to conclude IIRC that the spectrum of E677 contains all integers above some (unknown) value.

**Terence Tao:**

It doesn't help for this specific implication, but this gluing construction would be a general way to show that a given 2-variable law E does not imply a 3+-variable law E': find an idempotent magma obeying E, glue many copies of it together e.g., by a projective plane construction, and almost certainly this construction would not imply E' if E' was "genuinely" 3+-variable in nature.

**Matthew Bolan:**

I think at least some of the new order 25 models are also instances of this gluing construction for an $$S(2,5,25)$$.

**Rudi Schneider:**

I just looked at magmas with symmetry `(0) (1 2 3 4) (5 ... n-1)`, which has produced another brutal amount of 25-sized magmas. We're now at 24.

**Bruno Le Floch:**

Do we have a list somewhere of all magmas of low sizes coming from linear, cohomological, gluing, and symmetric constructions?  EDIT: https://github.com/memoryleak47/eq677/tree/main/db seems to be such a list up to order 41, plus the model below with $$\mathbb{F}_{16}$$.

Do we have any non-right-cancellative model other than Terry's idempotent translation-invariant model over $$\mathbb{Z}/31\mathbb{Z} \times \mathbb{F}_q$$ (for $$\mathbb{F}_q$$ admitting a fifteenth root of unity) given in [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/490772441)?

**Rudi Schneider:**

The list is by no means complete, let me know if you find a missing magma!

**Bruno Le Floch:**

I don't know how far up you want to push your list.  Up to size 100, there are linear magmas of sizes 5, 7 (two), 9, 11 (four), 13, 16 (two), 19 (two), 25 (several), 31 (six), 35 (two), 37 (two), 41 (four), 43 (four), 45, 49 (several), 55 (four), 61 (four), 63 (two), 65, 67 (two), 71 (four), 73 (two), 77 (eight), 80 (two), 81 (several), 91 (two), 95 (two), 97 (two), 99 (four).  I suppose your list contains all of the linear models up to size 50, including matrix ones over $$(\mathbb{F}_p)^2$$ for $$p=5,7$$?

**Matthew Bolan:**

My current understanding is that Terry's constructions are the only non-right-cancellative model known. Somewhere in this channel I sent a text file containing representatives from each cohomology class up to a reasonably large size, but now that list might need to be extended to include cohomological extensions of these new magmas. The linear magmas should all just be products of commutative linear models over fields (but this includes fields of non-prime order)

**Rudi Schneider:**

yeah, so far I just went up to n=50, but I can extend it to n=100.

But yes, the list so far is built using:
- linear/affine models modulus n up to n=50
- matrix/affine models modulus sqrt(n) up to n=50
- a general search up to n=11
- a translation invariant search up to n=37
- a semi translation invariant search up to n=31
- some random things I tried

**Terence Tao:**

One cautionary note is that if one actually wants to disprove 677 -> 255 for a finite magma, then wlog one can assume that the magma cannot be covered by proper submagmas, since otherwise this would create a smaller counterexample.  So one cannot "glue" one's way to a counterexample.  However, this does leave open the possibility of starting with one of these glued constructions and then doing some clever modification of it to make it fail 255 while still preserving 677.  No idea how to do that though - 677 is one of the more "rigid" laws we have, we don't have too many ways (other than the cohomological construction, or generic operations like Cartesian products) of turning one 677  magma to another.

**Bruno Le Floch:**

I don't think we've ruled out non-commutative linear models.  And even within commutative linear models, the coefficients $$\alpha,\beta$$ do not have to be diagonalizable.  For instance $$\alpha=((2,1),(0,2))$$ and $$\beta=((-1,-1),(0,-1))$$ over $$(\mathbb{F}_5)^2$$ gives a model that is not a square of the size-5 model since it does not obey $$x\diamond(x\diamond y)=y$$ obeyed by the size-5 model.

**Matthew Bolan:**

@Bruno Le Floch ah, you're right about the diagonalizability, so there is a little more there, but my recollection is that doing the non-commutative groebner basis computation one finds ab=ba, so the only linear models are commutative. See [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486431381) for example.

**Bruno Le Floch:**

@Matthew Bolan How certain are the Groebner basis computations?  E.g., in #**Equational>Non-commutative linear implications** you mentioned some bugs.  But @Pace Nielsen used some custom Mathematica code, so presumably these are two independent verifications that all linear models of E677 are commutative?

**Matthew Bolan:**

@Bruno Le Floch I think the ones for 677 are quite certain, though anything in that thread, while probably correct, has a chance to be wrong due to a few apparently rare bugs in the old version of singular I did the initial calculation in. I actually did start the work on producing certificates for all those results, but I'm on vacation so I can't produce the certificate for 677 right now, though I think there should be one on my desktop back home (in the form of expressions of the new generators in terms of the old and vice versa). I remember checking my results against Pace's when debugging and finding agreement.

**Bruno Le Floch:**

Thanks.  It's conceivable that the certificates would suggest some syzygies for E677, which might suggest useful ways to manipulate the equation.  But this is rather remote hope.  Do enjoy your vacation!

**Bruno Le Floch:**

As Terry says, gluing is mostly useless to refute E255.  But it can complete a partial model that is *self-contained* (in the sense that $$y\diamond x$$ defined implies E677(x,y) is defined and holds) and has a desirable property.  For instance, Terry's non-right-cancellative model, a piecewise-linear extension $$(\mathbb{Z}/31\mathbb{Z})\times\mathbb{F}_q$$, gives a self-contained partial model when we delete the definitions of $$(a,h)\diamond(b,k)$$ for $$a=b$$, and that partial model only needs $$\mathbb{F}_q$$ to have a third root of unity instead of a fifteenth root like the full model.  The partial model for $$q=7$$ can be completed to a full magma by gluing arbitrary 7-element models $$(a,h)\diamond(a,k)=h\diamond_a k$$ for each $$a\in\mathbb{Z}/31\mathbb{Z}$$.  This reduces Terry/Matthew's 496-element piecewise linear model down to 217 elements, with right cosets of size 127 (see Python script [attached: size-217.py]).

Gluing also helps with the fine spectrum of E677: I expect {all except exponentially few} large E677 magmas to be built almost entirely from the size-5 idempotent model.  In my Nov 1 message upthread [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/548283248) I worried about parity issues when gluing, but using idempotent models of sizes 5, 11, 16 we can complete any self-contained partial model into a magma obeying E677.

**Matthew Bolan:**

I had my Groebner basis code on my github, so I ran it on 677 again, producing the certificate [attached: 677_commutativity_proof.txt] proving linear 677 magmas are commutative. The claimed relation can be checked by replacing r and s with the corresponding generators as listed in the file.

**Bruno Le Floch:**

These expressions are seriously intimidating!  There goes my hope to extract detailed information from them.

By the way, I got down to a non-right-cancellative model with 77 elements with 47-element right cosets by replacing $$\mathbb{Z}/31\mathbb{Z}$$ by $$\mathbb{Z}/11\mathbb{Z}$$.  See Python script [attached: non-right-cancellative-677.py].  We can even go down to 33 elements if we only want a self-contained partial model: keep the same $$\mathbb{Z}/11\mathbb{Z}$$ base but only extend it by $$\mathbb{Z}/3\mathbb{Z}$$.  **EDIT:** Down to a **55-element model**, and a **22-element self-contained partial model**, by using a linear model $$h\diamond k = -h-k$$ of E14 to replace Terry's choice of translation-invariant model $$h\diamond k = h-\omega(k-h)$$ with $$\omega$$ a primitive third root.  I suspect dropping translation-invariance we may be able to reduce the base $$\mathbb{Z}/11\mathbb{Z}$$.

**Bruno Le Floch:**

``[*Spoiler: Detailed construction of 55-element model and 22-element partial model. — omitted*]spoiler 22-element self-contained partial model
````
[['', '',  4,  5,  8,  9, 12, 13, 16, 17, 20, 21,  2,  3,  6,  7, 10, 11, 14, 15, 18, 19],
 ['', '',  5,  4,  8,  9, 13, 12, 17, 16, 21, 20,  2,  3,  6,  7, 10, 11, 15, 14, 18, 19],
 [20, 21, '', '',  6,  7, 10, 11, 14, 15, 18, 19,  0,  1,  4,  5,  8,  9, 12, 13, 16, 17],
 [20, 21, '', '',  7,  6, 10, 11, 15, 14, 19, 18,  1,  0,  4,  5,  8,  9, 12, 13, 17, 16],
 [18, 19,  0,  1, '', '',  8,  9, 12, 13, 16, 17, 20, 21,  2,  3,  6,  7, 10, 11, 14, 15],
 [19, 18,  0,  1, '', '',  9,  8, 12, 13, 17, 16, 21, 20,  3,  2,  6,  7, 10, 11, 14, 15],
 [16, 17, 20, 21,  2,  3, '', '', 10, 11, 14, 15, 18, 19,  0,  1,  4,  5,  8,  9, 12, 13],
 [16, 17, 21, 20,  2,  3, '', '', 11, 10, 14, 15, 19, 18,  1,  0,  5,  4,  8,  9, 12, 13],
 [14, 15, 18, 19,  0,  1,  4,  5, '', '', 12, 13, 16, 17, 20, 21,  2,  3,  6,  7, 10, 11],
 [14, 15, 18, 19,  1,  0,  4,  5, '', '', 13, 12, 16, 17, 21, 20,  3,  2,  7,  6, 10, 11],
 [12, 13, 16, 17, 20, 21,  2,  3,  6,  7, '', '', 14, 15, 18, 19,  0,  1,  4,  5,  8,  9],
 [12, 13, 16, 17, 20, 21,  3,  2,  6,  7, '', '', 15, 14, 18, 19,  1,  0,  5,  4,  9,  8],
 [10, 11, 14, 15, 18, 19,  0,  1,  4,  5,  8,  9, '', '', 16, 17, 20, 21,  2,  3,  6,  7],
 [11, 10, 14, 15, 18, 19,  0,  1,  5,  4,  8,  9, '', '', 17, 16, 20, 21,  3,  2,  7,  6],
 [ 8,  9, 12, 13, 16, 17, 20, 21,  2,  3,  6,  7, 10, 11, '', '', 18, 19,  0,  1,  4,  5],
 [ 9,  8, 13, 12, 16, 17, 20, 21,  2,  3,  7,  6, 10, 11, '', '', 19, 18,  0,  1,  5,  4],
 [ 6,  7, 10, 11, 14, 15, 18, 19,  0,  1,  4,  5,  8,  9, 12, 13, '', '', 20, 21,  2,  3],
 [ 7,  6, 11, 10, 15, 14, 18, 19,  0,  1,  4,  5,  9,  8, 12, 13, '', '', 21, 20,  2,  3],
 [ 4,  5,  8,  9, 12, 13, 16, 17, 20, 21,  2,  3,  6,  7, 10, 11, 14, 15, '', '',  0,  1],
 [ 4,  5,  9,  8, 13, 12, 17, 16, 20, 21,  2,  3,  6,  7, 11, 10, 14, 15, '', '',  1,  0],
 [ 2,  3,  6,  7, 10, 11, 14, 15, 18, 19,  0,  1,  4,  5,  8,  9, 12, 13, 16, 17, '', ''],
 [ 3,  2,  6,  7, 11, 10, 15, 14, 19, 18,  0,  1,  4,  5,  8,  9, 13, 12, 16, 17, '', '']]
````
```
`````

**Matthew Bolan:**

I notice that if one takes the $$7 \times 7$$ model with $$x \diamond x = 0$$, deleting the entry for $$0 \diamond 0$$ leaves one with a self contained partial model.

**Bruno Le Floch:**

That is correct!  It also works for the other size-7 model.  In fact, one can remove any number of idempotent entries `x◇x=x` from any model.  I tried a little bit without success to use this size-7 model together with the idempotent ones (sizes 5, 11, 16 etc.) in concrete gluing constructions, but it would require some code.  The main theoretical understanding of such mixed-block designs is Wilson's theorem stating that they exist for large enough sizes (nested exponentials?) consistent with some modular conditions.  For law 677 we deduce an asymptotically complete spectrum and asymptotics of the log of the number of magmas (I would guess $$\frac{1}{20}n^2\log n$$).  It would be interesting to find some sparse self-contained partial models, not of this form.

**Bruno Le Floch:**

Piecewise affine extensions of a base magma, used to construct non-right-cancellative magmas (such as my 55-element one above), cannot produce counterexamples to E677⊨(finite)E255.  However, there could be counterexamples among **piecewise linear models** $$x\diamond y = x\diamond_i y$$ where $$i=1,2$$ depend on $$x,y$$ and each one of the two operations $$x\diamond_i y = \alpha_i x + \beta_i y$$ is linear.  Motivated by Terry's translation-invariant construction it makes sense to hope that $$x\diamond_1(y\diamond_1((x\diamond_2 y)\diamond_2 x)=y$$ and the same with the two operations swapped.

It seems easier to work over $$\mathbb{C}$$ as a practice run.  There are a few solutions with $$\diamond_1\neq\diamond_2$$:

1. $$x\diamond_1 y=y$$ and $$x\diamond_2 y = -\omega x-\omega^2 y$$ with $$\omega^3=1$$ (primitive or not), which we used in the finite case;

2. $$x\diamond_{1,2} y=\frac{1}{2}(1\pm\sqrt{-7})x+y$$;

3. $$\alpha_{1,2} = \frac{1}{2} (-1 \pm \sqrt{-9 + 6 \sqrt{5}})$$ and $$\beta_{1,2} = \frac{1}{2} (-5 - 2 \sqrt{5} \pm \sqrt{39 + 18 \sqrt{5}})$$, or the same with $$\sqrt{5}\to -\sqrt{5}$$.

To make a piecewise linear model, the idea would be to color pairs $$(x,y)$$ in colors $$1,2$$ (stating whether to define $$\diamond$$ as $$\diamond_1$$ or $$\diamond_2$$ such that if $$(x,y)$$ has a color $$1$$ (say) then $$(x\diamond_1 y,x)$$ has the same color, and $$(y,(x\diamond_1 y)\diamond_1 x)$$ has the opposite color and $$(x,y\diamond_2((x\diamond_1 y)\diamond_1 x))$$ also has color $$2$$.

Some messy Mathematica code suggests that the cases 1. and 2. above cannot give piecewise linear models (at least not if we assume that the color of $$(x,y)$$ only depends on $$x/y$$), but 3. might.  Maybe that's enough to suggest a search: pick a field $$\mathbb{F}_q$$ where $$5$$ is a quadratic residue and $$-9+6\sqrt{5}$$ and $$39+18\sqrt{5}$$ also are, compute $$\alpha_1,\beta_1,\alpha_2,\beta_2$$ given above, and seek a partition $$(\mathbb{F}_q)^2\setminus\{(0,0)\} = A_1\sqcup A_2$$ to serve as a coloring.  I'm excluding $$(0,0)$$ because both formulas give the same answer in this case, and it doesn't participate in any other condition anyways.

**Bernhard Reinke:**

Here is a small sage snippet that produces (if I didn't mess up somewhere) $$\alpha_1, \alpha_2, \beta_1, \beta_2$$ of case 3 (using rather naive reduction of the primary component corresponding to that case) for small prime fields:
[*Spoiler: Sage snippet — omitted*]python
for q in primes(100):
    A.<a_1,a_2,b_1,b_2> = AffineSpace(4,GF(q))
    S = A.subscheme([a_1+a_2+1,4*b_2^2+8*a_2+b_1+37*b_2+15,4*b_1*b_2+b_1+b_2-1,8*a_2*b_2+4*a_2-b_1+11*b_2-7,4*b_1^2-8*a_2+37*b_1+b_2+7,8*a_2*b_1+4*a_2-3*b_1+b_2+11,4*a_2^2+4*a_2+3*b_1+3*b_2+25])
    print("q = {}:".format(q))
    print(S.rational_points())
```
```
[*Spoiler: Output — omitted*]text
q = 2:
[(0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 0, 1), (1, 0, 1, 0)]
q = 3:
[]
q = 5:
[(0, 4, 1, 4), (4, 0, 4, 1)]
q = 7:
[]
q = 11:
[(4, 6, 4, 5), (5, 5, 7, 7), (6, 4, 5, 4)]
q = 13:
[]
q = 17:
[]
q = 19:
[(5, 13, 11, 4), (13, 5, 4, 11)]
q = 23:
[]
q = 29:
[(8, 20, 10, 21), (20, 8, 21, 10)]
q = 31:
[]
q = 37:
[]
q = 41:
[(17, 23, 23, 39), (23, 17, 39, 23)]
q = 43:
[]
q = 47:
[]
q = 53:
[]
q = 59:
[]
q = 61:
[(2, 58, 11, 54), (58, 2, 54, 11)]
q = 67:
[]
q = 71:
[]
q = 73:
[]
q = 79:
[(21, 57, 16, 18), (57, 21, 18, 16)]
q = 83:
[]
q = 89:
[(38, 50, 74, 48), (42, 46, 70, 65), (46, 42, 65, 70), (50, 38, 48, 74)]
q = 97:
[]
```
```
Probably the result will not work for very small characteristics, but maybe `q = 19` or `q = 29` could be interesting

**Bernhard Reinke:**

It seems like at least for `q = 19` and `q = 29` there is no possible color assignment, if my sat encoding was correct. I think it an assignment can be translated to a 2SAT problem, so it should be very fast to check it systematically

**Bernhard Reinke:**

I have checked primes <500, and haven't found a color assignment using case 3. For q = 2 the solutions are an artifact of bad reduction, for the other primes, they passed the sanity check $$x\diamond_1(y\diamond_1((x\diamond_2 y)\diamond_2 x)=y$$ and same for the two operations swapped. In principle I could also check prime powers, but this will be slightly more tedious to glue the sage output to z3 input

**Bernhard Reinke:**

Can this even work over odd characteristics? I think will still get that $$L_{x,i}(y) = x \diamond_i y$$ must be surjective, hence a bijection, and we have that $$y\diamond_2((x\diamond_1 y)\diamond_1 x)$$ must be $$L_{x,2}^{-1}(y)$$. So I think we can get that if we fix $$x$$ and look at the number of pairs $$(x, y)$$ that have color 1, we get that we have at least as many in color 2, so actually we need the same number of pairs, so the characteristic must be 2.

**Bernhard Reinke:**

It doesn't seem to work for `q = 16` either

**Bernhard Reinke:**

Hm, maybe we can use the fact that sometimes $$x \diamond_1 y$$ and $$x \diamond_2 y $$ give the same result. So the pairs $$(x, y)$$ where this holds should be colored by both colors at once. This could fix the parity issue. But this will probably only work if we have stuff like $$x \diamond_1 y = x \diamond_2 y \Rightarrow (x \diamond_1 y) \diamond_1 x = (x \diamond_2 y) \diamond_2 x $$

**Bernhard Reinke:**

I think the only case for which we have a result like this is case 1 with $$\omega$$ a primitive third root of unity, but then $$ \diamond_1$$ and $$\diamond_2$$ are idempotent, so we cannot construct a counterexample to E677⊨(finite)E255.

**Terence Tao:**

I tried something similar at [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/490809620)  and gave up, but perhaps it's actually better to ignore the negative comments I wrote in case you come up with a different route that avoids what I did.

**Bernhard Reinke:**

I thought a bit about the magmas where the set of squares is a proper submagma. For a E255 counterexample, the set of squares cannot be just one element. I checked this with vampire and I think it should easily follow from [Lemma 13.2 vii](https://teorth.github.io/equational_theories/blueprint/677-chapter.html#255-equiv) of the blueprint.

So the next question would be whether the set of squares can be a submagma of size 5. Vampire does not immediately rule this out for a E255 counterexample. I am curious how many of your examples of 25-sized magmas (even though they satisfy E255) have this property, probably a lot of them?

Could you also search with your methods for magmas with this property for other cardinalities? Probably you want the set of squares to be just `0 .. 4`, and maybe you can even throw in a symmetry of the form `(0) (1 2 3 4) (5 ... n-1)` (or replace the last cycle by a bunch of 4 cycles).

I am actually not sure what kinds of symmetries to expect, I think the product of the magma of size 5 and the unipotent magma of size 7 should give you something where you have $$(\mathbf{Z}/\mathbf{5Z})^\times \times (\mathbf{Z}/\mathbf{7Z})^\times$$ as the symmetry group.

So one thing to try would be `sq(x) = x % 5`, another one `sq(x) = ((x-1) % 4) + 1` for $$ x > 0 $$.

**Bernhard Reinke:**

Actually, the model of size 5 is translation invariant, so maybe it makes also sense to look at `sq(x) = x % 5` with symmetry `(0 .. 4) (5 .. n-1)` ? The product of the magma of size 5 and the unipotent magma of size 7 should have this symmetry.

**Bruno Le Floch:**

Looking at the database https://github.com/memoryleak47/eq677/tree/main/db there are magmas with bijective squaring map for all sizes (1, 5, 7, 9, 11, 13, 16, 19, 21, 25, 29, 31, 35, 37, 41, 43, 45, 49); there is a magma of size 7 and one of size 49 with all squares being equal; there is a magma of size 35 whose squares forms a size 5 submagma; there are two magmas of size 49 whose squares form a size 7 submagma (specifically the two non-isomorphic magmas of size 7).

**Bruno Le Floch:**

Oh, the [magma of size 29](https://github.com/memoryleak47/eq677/blob/main/db/29/0) in that database is very intriguing.  It is nonlinear ($$L_x\circ L_y^{-1}$$ do not commute).  It is not obtained by gluing (all permutations $$L_x$$ have a pair of 14-cycles and a fixed point $$L_x(x)=x$$).  Of course it is very far from being a counterexample to 255 since it is idempotent and is a quasigroup, but maybe it holds a hint to a new construction.

**Bruno Le Floch:**

Sadly it's just a translation-invariant model over $$\mathbb{F}_{29}$$.  Its automorphism group has order $$29\times 14$$.  I think the group is a semi-direct product of $$\mathbb{F}_{29}$$ by an index-2 subgroup of $$\mathbb{F}_{29}^{\times}$$.  Maybe the model has a nice abstract description.

**Bruno Le Floch:**

It is (isomorphic to) a piecewise linear model with two pieces: $$x \diamond y = x + \delta_{y-x} (y-x)$$ modulo $$29$$, with $$\delta_k = 27$$ if $$k$$ is a quadratic residue and $$\delta_k = 3$$ if $$k$$ is not (for $$k=0$$ it doesn't matter which coefficient we pick).  If I call $$\diamond_1$$ the operation for the quadratic residue case and $$\diamond_2$$ the other, then $$x\diamond_1(y\diamond_1((x\diamond_2 y)\diamond_1 x))=y$$ and $$x\diamond_2(y\diamond_2((x\diamond_1 y)\diamond_2 x))=y$$, which is not the pattern we explored a bit.
*EDIT 2:* the two operations are $$x \diamond y = 27 x + 3 y$$ and $$x \diamond y = 3x + 27y$$.
*EDIT:* Note that the piecewise linear nature of this model is pretty different from what @Terence Tao had explored some months ago since the carrier is not a product group.

**Bernhard Reinke:**

The run with symmetries `(0 .. 4) (5 .. n -1) ` hasn't produced new examples so far, but apparently the models `25/9` and `25/11` have this symmetry

**Bernhard Reinke:**

A similar construction seems possible for `q = 101` with $$\delta_{y-x} \in \{35, 67\}$$. Probably there should be a nice congruence condition on `q`.

**Bernhard Reinke:**

I am curious whether one can generalize this construction in the following way: We look at piecewise linear models $$ x \diamond y = x + \psi(y - x) \cdot (y - x)$$ where $$\psi(0) = 0$$ and $$ \psi $$ factors on $$\mathbf{F}^\times_q $$ over a small quotient group. For the examples so far, $$\psi$$ factors over $$\mathbf{F}^\times_q / (\mathbf{F}^\times_q)^2 $$, but probably we can also try to come up with something that factors over cubic residues. All these constructions will be idempotent though.

**Bernhard Reinke:**

Ok, I think I found some for the factorization over $$\mathbf{F}^\times_q / (\mathbf{F}^\times_q)^3$$, for $$q$$ prime < 100 there are essentially only two such examples:
[attached: q=79, delta=[5,53,6]]
[attached: q=97,delta=[23,76,26]]

**Bernhard Reinke:**

Back to the factorization over $$\mathbf{F}^\times_q / (\mathbf{F}^\times_q)^2$$, there is an example of this construction that is not right-cancellative, with `q = 181`,  $$\delta_{y-x} \in \{48, 139\}$$.

**Bernhard Reinke:**

Oh well, actually the "cubic" examples are also not right-cancellative

**Bruno Le Floch:**

Size 79 is a new size.  Size 97 and 181 are not new sizes as there were already some linear models of those sizes.

**Bernhard Reinke:**

I had a look at prime powers, here is an example for $$\mathbf{F}_{25}$$ that is not right-cancellative:
[attached: q=25 not right-cancellative]

**Bruno Le Floch:**

I'd be curious to know if you find models over $$\mathbb{F}_{2^k}$$ for $$k\not\equiv 0\mod 4$$.  So far, the only way to get sizes with 2-adic valuation that is not a multiple of four is the gluing construction, only known to work for multiply-exponentially large sizes by some probabilistic arguments (Wilson theorem).

**Bruno Le Floch:**

Here are vague thoughts to go beyond translation-invariant models.  Let's return to $$x\diamond y=\alpha_i x+\beta_i y$$ with two pairs $$(\alpha_1,\beta_1)$$ and $$(\alpha_2,\beta_2)$$ for $$(x,y)\in A_i$$ with a partition $$M^2=A_1\cup A_2$$.  Inspired by the translation-invariant case I want to define $$A_1$$ as the pairs where $$\gamma x+\zeta y$$ is zero or a quadratic residue, and $$A_2$$ as the pairs where $$\gamma x+\zeta y$$ is zero or a non-residue.  For the zero case we want the operations to match, which suggests $$\gamma=\alpha_1-\alpha_2$$ and $$\zeta=\beta_1-\beta_2$$.  (In the translation-invariant case, this gives $$\gamma x+\zeta y = \gamma(x-y)$$, which is a quadratic residue/non-residue exactly when $$x-y$$ is or isn't.)

**Bernhard Reinke:**

Hmm, if we want to construct a minimal example of a magma satisfying 677 but not 255, then the automorphism group cannot be too large: if `x` is an element not satisfying 255, then submagma generated by `x` will still satisfy 677 but not 255. So for a minimal example, the only automorphism that can fix `x` is the identity.

**Bruno Le Floch:**

I don't understand the argument.  It seems perfectly fine to have an automorphism group that acts transitively, with every element `x` being a counterexample to 255, and with every element `x` generating the whole magma, no?

**Bernhard Reinke:**

The stabilizer of `x` must be trivial. Strictly 1-transitive is fine, but not more

**Bernhard Reinke:**

I think your approach beyond translation-invariant models has only a $$ (\mathbf{F}^\times_q)^2$$ symmetry, so it should be fine

**Bernhard Reinke:**

I thought a bit about the partially linear translation invariant models, they have a $$ \mathbf{F}_q \rtimes (\mathbf{F}^\times_q)^2 $$ symmetry, that is already too much

**Bernhard Reinke:**

Of course, we also can see this directly because they are idempotent. Basically a too large automorphism group can force your model to be idempotent

**Rudi Schneider:**

Sorry, not sure whether this is still relevant, but I missed this question earlier:

I think unfortunately they are all idempotent. (edit: only talking about the 25-sized ones, not all ones.)

> Could you also search with your methods for magmas with this property for other cardinalities? Probably you want the set of squares to be just `0 .. 4`

So, you want the diagonal entries of the matrix to induce the 5/0 submagma?
I think you can force it like this: https://github.com/memoryleak47/eq677/tree/fix5

The search space seems to be a bit too huge still though, maybe adding some symmetries helps?

**Bruno Le Floch:**

@Rudi Schneider See my message above, there are three models in the db whose set of squares are the three smallest models of E677.

@Bernhard Reinke That's a good point.

**Bernhard Reinke:**

@Rudi Schneider, I think there are two viable strategies, one for lifting the translation symmetry, the other for lifting the homogeneous symmetry. For translation symmetry you could force`sq(x) = x % 5` and you add the symmetry `(0 .. 4) (5 .. n -1)`. I also described the homogeneous one earlier, but I am less optimistic about it.

**Rudi Schneider:**

I blindly implemented this -- not unlikely that I misunderstood something. It's pushed on the branch, feel free to double check. It didn't yield any models yet up to size 29.

I assume by `sq(x)` you mean `x ⋄ x`;

**Bernhard Reinke:**

I think you can skip the sizes where n is not divisible by 5. Did something interesting come out for size 30 or 35?

**Bernhard Reinke:**

I am doing a brute force search for  $$(\alpha_1,\alpha_2,\beta_1,\beta_1)$$ with  $$\gamma=\alpha_1-\alpha_2$$ and $$\zeta=\beta_1-\beta_2$$, but so far I haven't found any examples where $$\alpha_1 \not= \alpha_2$$ and $$\alpha_1 + \beta_1 \not= 1$$.

I think an advantage of the the translation invariant method is that we can check it by some residue properties of some small polynomials in the $$\beta_i$$. Basically, we can predict the "branch" for the operation on the pair $$(x\diamond y, x)$$ just based on whether $$h = x - y$$ is a quadratic residue and whether $$\beta_1$$ or $$\beta_2$$ (and -1) are quadratic residues. This continues for the subexpressions of E677 (for certain polynomials in $$\beta_i$$, for example  $$ -\beta_1 \beta_2+\beta_1-1 $$). I don't think this would work directly for your generalization.

**Bruno Le Floch:**

Ah, thanks, my generalization does not work.  We want the case $$j$$ in $$(x\diamond_i y)\diamond_j x$$ to be determined by the case in $$x\diamond_i y$$.  This requires $$\gamma x + \zeta y$$ to divide $$\gamma (x\diamond_1 y)+\zeta y$$ and $$\gamma(x\diamond_2 y)+\zeta y$$.  For the next step, we also need $$\gamma x + \zeta y$$ to divide $$\gamma y+\zeta((x\diamond_i y)\diamond_j x)$$.  Surprisingly, regardless of whether $$i=j$$ or $$i\neq j$$ this gives that $$\omega\coloneqq\zeta/\gamma$$ is a fourth root of unity, and $$\beta_i = \omega\alpha_i+\omega^2$$.  Unfortunately, for the next step $$\gamma x+\zeta(y\diamond_k((x\diamond_i y)\diamond_j x))$$ to work out, I find $$\omega=-1$$ as the only solution (regardless of whether $$i,j,k$$ are distinct or not), which is the case we looked at.  I think this proves that all piecewise linear models in which the pieces are characterized by $$\gamma x+\zeta y$$ must be idempotent, but I am not quite sure.

**Rudi Schneider:**

It just produced this 35-sized model:
[*Spoiler: Magma — omitted*]

Btw, Does anyone have a list (or even better code) of all linear magmas up to some size + cohomological extensions + gluing?
Would be cool to integrate that into the db (to see what is actually new), but I don't seem to find the time to implement them

**Matthew Bolan:**

I have that sans the gluing. You can find a large list of cohomological extensions produced by my code in one of my earlier messages in this channel.

**Matthew Bolan:**

Linear models I also have, but the actual list hasn't been shared anywhere and I'm on vacation still so no access to that code.

**Matthew Bolan:**

I think gluing is unlikely to make many small models, perhaps they can just be listed manually

**Bruno Le Floch:**

@Rudi Schneider If we give a list of linear magmas and cohomological extensions, how do you track which models are isomorphic?  Do you have a preferred normalization for the order of entries? (Maybe we could get the multiplication table that is earliest in lexicographic order?)

For gluing, the only ones I am aware of are gluings of copies of a single idempotent model of a given size k (=5,11,16,...), which are obtained from Steiner S(2,k,n) systems.  I know two sources (of sources),
- https://web.math.pmf.unizg.hr/~krcko/results/steiner.html which points to a list of 15 S(2,5,41), 1072 S(2,5,45), 1777 S(2,5,65), from which we should be able to get many more non-isomorphic idempotent models of 677.
- https://www.theoremoftheday.org/MathsStudyGroup/ADFnotes-Wilsons-theorem-for-block-designs.pdf which mentions that S(2,5,n) exists exactly for n≡1,5 mod 20 (citing Hanini, 1961) and mentions general constructions which apply to various infinite families of sizes, using that $$5$$ is a prime number, or one plus a prime power.

I had the idea of trying to find mixed-block designs, for instance one of size 51 (which would be new in the spectrum of 677) by taking five blocks of size 11 intersecting at a point, then covering the resulting complete multipartite graph $$K_{10,10,10,10,10}$$ by 5-cliques, but this is equivalent to a long-standing open problem of constructing three pairwise-orthogonal Latin squares of size 10.  *EDIT: There is also Keevash's general result which states in particular that mixed-block designs of large enough sizes will always exist (under obvious divisibility conditions).*

**Rudi Schneider:**

I lower the magma to a colored graph and then use Traces (https://pallini.di.uniroma1.it/) to find a canonical version of it. So I'm happy to get non-canonicalized magmas.

It's implemented here:
https://github.com/memoryleak47/eq677/blob/main/src/matrix/canon2.rs

**Bernhard Reinke:**

Are the linear examples over fields or also over finite rings? I would assume that the finite rings one should also turn up as cohomological extensions over fields

**Bernhard Reinke:**

Here would be a sage snippet that produces linear models over fields. I can see whether I can make it also work for finite rings.
[*Spoiler: Sage snippet — omitted*]python
from itertools import product

def produce_linear_models(max_q):
    result = {}
    for q in prime_powers(max_q):
        cur = []
        K = GF(q)
        A.<a,b> = AffineSpace(2,GF(q))
        S = A.subscheme([a^2*b^2+b^3+a,a*b^3+a*b-1])
        lookup = dict((v,k) for k,v in enumerate(list(K)))
        for a,b in S.rational_points():
            def f(x,y):
                return a*x + b*y
            for x,y in product(K,repeat=2):
                for i in range(2):
                    if f(x, f(y, f(f(x,y), x))) != y:
                        print("Values {} do not actually produce a magma satisfying E677".format(q,a,b))
                        return None
            cur.append([[lookup[f(x,y)] for y in K] for x in K])
        result[q] = cur
    return result
```
```
[attached: Output for q < 100]

**Bernhard Reinke:**

Probably there are some redundancies in the output if you consider the action of the Galois group for `q` proper prime power

**Bernhard Reinke:**

Is this the most complete of cohomological examples then?

**Matthew Bolan:**

Yep, that looks like it (I guess it won't include direct products... )

**Bernhard Reinke:**

Is there a hope to make this work by passing to an extension over a base magma or do we run into the same problem again?

**Bernhard Reinke:**

So i want something like $$(x, s) \diamond (y, t) = (x \diamond y, s \diamond_{x,y} t)$$ where $$s \diamond_{x,y} t$$ is $$ f_{x,y}(s,t) =  \alpha_{x,y} s + \beta_{x,y} t $$ or $$ g_{x,y}(s,t) = \gamma_{x,y} s + \delta_{x,y} t$$ depending on whether $$ f_{x,y}(s,t) - g_{x,y}(s,t) $$ is a quadratic residue or not. Probably the first interesting case would be where the base magma is the unipotent model of size 7.

**Rudi Schneider:**

Hey, I assume that even extending it to finite rings wouldn't cover all linear magmas in the sense of Lemma 13.3 from [here](https://teorth.github.io/equational_theories/blueprint/677-chapter.html)?

Would it be an option to iterate through all abelian groups of some size n (via prime decomposition), or has someone already tried this? Could imagine that iterating through all those homomorphisms won't be fast enough.
Would be cool to be able to check "linearity" via hashset lookup for small sizes.

**Rudi Schneider:**

Unrelated: When trying to extend the DB to size 100, I noticed that there's a virtually endless stream of translation-invariant models of size 61 that have `h=h⁻¹`.

Here's a list of 258 of those:
[attached: tinv61.txt]

Not sure how it would help, but it looked odd.
It doesn't seem to be caused by linear models / cohomological extensions, but I didn't look into gluing yet.

**Bruno Le Floch:**

Finite linear models just need an abelian group $$\prod_i \mathbb{Z}/n_i\mathbb{Z}$$, which is a direct product of $$p$$-groups for each prime, so let me search for models over $$G=\mathbb{Z}/p^{k_1}\mathbb{Z}\times\dots\times\mathbb{Z}/p^{k_m}\mathbb{Z}$$.  (The finite field case $$\mathbb{F}_{p^m}$$ is when $$k_1=\dots=k_m=1$$.)  We want linear maps $$\beta:G\to G$$ such that $$P(\beta)\coloneqq(\beta^4-\beta^3+\beta^2-\beta+1)(\beta^4+\beta^3+2\beta^2+2\beta+1)=0$$.

When all $$k_i=1$$, the group is a vector space over $$\mathbb{F}_p$$ so linear algebra is straightforward (maybe some weirdness for $$p=2$$?), the characteristic polynomial of $$\beta$$ must divide $$P(\beta)$$.  If the irreducible factors of $$P(\beta)$$ factored over $$\mathbb{F}_p$$ have no multiplicity the only models are products of models over the splitting fields of these irreducible factors, so we're back to models over finite fields.  When $$P(\beta)$$ factors with multiplicity, there can be some models where $$\beta$$ is not diagonalizable; for instance I gave such an [example on $$(\mathbb{F}_5)^2$$](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/558767469), but a more interesting one would be over $$(\mathbb{F}_9)^2$$ (the group $$(\mathbb{Z}/3\mathbb{Z})^4$$), using that $$P(\beta) = (\beta^2 - \beta - 1)^2 (\beta^4 - \beta^3 + \beta^2 - \beta + 1)$$ modulo 3.

When some $$k_i>1$$ the linear algebra question looks more complicated.  These models can be understood as cohomological extensions of products of finite field models, but that's probably not a great point of view.  The easiest case is when there is only one factor ($$m=1$$), for which we solve the scalar equation P(β)=0 modulo some prime power.  There are models over $$\mathbb{Z}/p^k\mathbb{Z}$$ for all $$k\leq 10$$ and all $$p\leq 2027$$ such that $$\mathbb{Z}/p\mathbb{Z}$$ has a linear model, except $$p=5, 13$$ for which there are linear models of size $$p$$ but not $$p^2$$ and higher.  Likely relatedly, $$\mathrm{gcd}(P(\beta), P'(\beta)) = 3^2 5^3 31^2 13$$.

Finite field models, and $$\mathbb{Z}/n\mathbb{Z}$$ models do not cover everything.  For instance there is a model on the ring $$(\mathbb{Z}/49\mathbb{Z})[\sqrt{-1}]$$ with $$\beta=15+23\sqrt{-1}$$, namely $$k_1=k_2=2$$.  I think on $$(\mathbb{Z}/31^2\mathbb{Z}) \times (\mathbb{Z}/31\mathbb{Z})$$ there are non-diagonalizable solutions such as $$\beta=((27,31),(0,27))$$ and $$\beta=((27,0),(1,27))$$ but I am getting myself confused about when such solutions are equivalent.

**Bruno Le Floch:**

The huge list of magmas of size 61 is entirely due to gluing, specifically Steiner S(2,5,61) designs.  Here is some Python code that finds the blocks and complains if any of them is anything else than of size 5: [attached: db-61.py].

**Bernhard Reinke:**

I had a look how the operations glue together there, we have $$x \diamond_1 y = x + 4(y - x) $$ (so the classical linear model that is already defined over $$\mathbb{F}_5$$), and $$x \diamond_2 y = x + \alpha (y - x)$$ where $$\alpha^2 + 3\alpha + 4 = 0$$. We pick a variant depending on whether $$ x - y $$ is a quadratic residue.

We have $$x\diamond_1(y\diamond_1((x\diamond_1 y)\diamond_1 x))=y$$ (i.e., $$\diamond_1$$ satisfies E677 on its own) and $$ x\diamond_2(y\diamond_1((x\diamond_2 y)\diamond_2 x)) =y$$. Maybe these combinatorics can be also helpful in other settings as well.

**Bruno Le Floch:**

This makes me wonder if any of the glued size-61 models could be piecewise linear by happenstance.  They could teach us new piecewise linear constructions.  So far, all piecewise constructions are idempotent, have a finite field as the carrier, and depend on whether x-y is a quadratic residue.

**Jihoon Hyun:**

@Jose Brox [말함](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/488134567):

Actually, any element satisfying $$x^2 = x^3$$ of a finite magma 677 will also be idempotent, as $$x=x^4$$ ([proof](https://github.com/qawbecrdtey/magma/blob/90fc643548063d5a28a49d6110da314cebf0af69/Magma/NA255.lean#L29-L50)) and $$x = x^4 = x^3=x^2$$.

Aside from that, I'm looking for equations which implies 255 when applied to finite 677 magma *elementwise*/*globally*. For example, if $$x$$ satisfies 359 then it also satisfies 255 as noted above. Are there list of known facts about this?

**Bernhard Reinke:**

As a preparation, I started to have a look at linear extensions. For some reason I started with the base magma $$x \diamond y = 4x + y$$ on $$\mathbb{F}_7$$ instead, but I will have a look at the unipotent model next. Here is hopefully one of the first nontrivial extensions (or order 49):

[attached: Extension over (4x + y)]

@Rudi Schneider, is this example already in your database, or how would I check this easily myself?

**Rudi Schneider:**

It was not in the db, and it was the first magma, where the left-multiplication bijection of some element forms a 3-cycle! I had not seen that before

**Rudi Schneider:**

Also, your construction has produced these models so far, for size 35. Didn't terminate yet

[attached: magmas2.txt]

**Rudi Schneider:**

> or how would I check this easily myself?

I typically do
```
let m = MatrixMagma::parse("<magma written as matrix>");
let m = m.canonicalize2();
m.dump();
```
and add the resulting magma to the db.
Then the test `cargo t --release db_unique` will fail, if it's already there.

I'm in the process of changing this though, might get simpler

**Bernhard Reinke:**

Ok, I also had a look at extensions over the unipotent magma on degree 7, but I didn't manage to produce a similar small example. One trick that I have used was to first find solutions over $$\mathbb{C}$$ and use them to guess some linear relations of the coefficients. If we write our Ansatz as $$(x,s)\diamond(y,t) = (x\diamond y, s\diamond_{y/x} t)$$ with $$s\diamond_i t = \alpha_i s + \beta_i t$$, then for the base $$4x + y$$ I got $$\alpha_i + \beta_i = \alpha_j + \beta_j $$ for $$i,j \in S_{4,1}=\{1,2,4,5,6\}$$, for the base $$4x + 3y$$ a similar relation for the set $$S_{4,3} = \{2,3,4,5,6\}$$. These are exactly those products with base behavior $$x \not= 0, y \not= 0, x\diamond y \not= 0$$.

  I am curious to see whether there is a more direct argument showing these relations, I added them also for the finite characteristic computation to speed up the Gröbner basis computation. This of course means that I could overlook some solutions in small characteristics.  Another thing to consider is that there is still a degree of freedom by scaling the copy that projects down to 0, so we fix $$\alpha_\infty$$.

With this I get equations of degree 29 for the extension over $$4x + y$$ and degree 78 for $$4x + 3y$$.

**Bernhard Reinke:**

For the linear extension over the both magmas of size 7 with the Ansatz as written before, it seems that either the extension splits or we have $$\alpha_i + \beta_i = 1$$, which is means that $$\diamond_i$$ are idempotent. So this doesn't look too promising to admit an interesting quadratic residue splitting.

**Bernhard Reinke:**

I get similar results for the base magma of size 9 with full projective symmetries. Here is a hopefully nontrivial extension by 19 (so total size 171):
[attached: Extension 9 x 19].

Overall it seems that after appropriate rescaling of the zero component we have that $$\alpha_i + \beta_i$$ must be constant, and if we have a nontrivial extension, it must be equal to $$1$$. Maybe there is still a hope for the quadratic residues splitting approach, but it seems unlikely. Probably one can go a little bit further computationally with the methods I have used. One thing I still want to try is to consider linear models over base 7, but with only "half" of the projective symmetries.

**Bruno Le Floch:**

Linear extensions cannot provide counterexamples to 255, as [shown in the blueprint](https://teorth.github.io/equational_theories/blueprint/677-chapter.html#linear-2).  I think the piecewise linear approach shows promise, but I won't have time to make serious progress until next week.  The rough idea is to write your Ansatz as $$s\diamond_{x,y}t = a_{x,y} s + b_{x,y} t + (c_{x,y} s + d_{x,y} t)^+$$, where the «positive part» $$(u)^+$$ is $$u$$ if $$u$$ is a quadratic residue and is zero otherwise.  Then the «branch» to be taken throughout $$(y,t) = (x,s) \diamond ((y,t) \diamond (((x,s) \diamond (y,t)) \diamond (x,s))$$ ought to be determined by that taken by $$s\diamond_{x,y} t$$.  This requires $$c_{x,y} s + d_{x,y} t$$ to divide several linear combinations of $$s,t$$ with coefficients polynomial in $$a,b,c,d$$.  Assuming that none of the $$c$$ or $$d$$ vanish, one quickly finds $$s \diamond_{x,y} t \equiv - (d_{x\diamond y,x} / c_{x\diamond y,x}) s \mod c_{x,y} s + d_{x,y} t$$, and eventually, in terms of $$e=d/c$$, the conditions
```math
e_{y,(x\diamond y)\diamond x} e_{(x\diamond y)\diamond x,x\diamond y} e_{x\diamond y,x} e_{x,y} = 1 , \qquad
e_{x,x\diamond w} = - e_{x,w} e_{w,x\diamond w} .
```
An obvious solution is $$e_{\bullet,\bullet}=-1$$, which means that the case distinction is always on whether $$s-t$$ is a quadratic residue or not, and we quickly get down to translation-invariant models only.

When the base magma is the unipotent 7-element magma *and* we require $$e_{x,y}=e_{x/y}$$ to be projectively invariant as you did, we get that all $$e$$ have to be $$-1$$ except one of them.  It's not clear to me if having one non-trivial $$e$$ would be enough to have interesting piecewise linear extensions: we need to set up different cases depending on how the different branches (quadratic residue or not) get composed, leading to polynomial equations on all of the $$a,b,c$$ (with $$d=ce$$ being imposed).  I also didn't check what happens without projective invariance, or taking other base magmas in the database.

**Bernhard Reinke:**

I think your second equation always forces $$e_{x,x} = - 1$$. So I am less optimistic that this can produce can produce counterexamples to 255, as this means that in testing 255 both branches have to agree. This definitely rules out the Ansatz where one of the branches on its own satisfies 677 (and, since it is a linear extension, also 255). Probably it also rules out more complicated ways of mixing two operations.

**Bruno Le Floch:**

That's a good point.  And indeed E255 is automatically satisfied by two-piece linear extensions of the kind considered here (at least if all $$c,d$$ are invertible and the linear maps are commutative) if the base satisfies E255.  (EDIT: proof simplified a lot.)

`[*Spoiler: Proof — omitted*]math
s \diamond_{x,y} t = - e_{x\diamond y,x} s + b_{x,y} (s + t e_{x,y}) / e_{x,y} + (c_{x,y} (s + t e_{x,y}))^+ .
```
For a given $$(y,t)$$ we seek $$(x,s)$$ such that $$(x,s)\diamond(y,t) = (y,t)$$ (this is known to be equivalent to E255).  Pick $$x=(y\diamond y)\diamond y$$ so $$x\diamond y=y$$ (by E255 on the base) and set $$s=-te_{x,y}$$.  Then $$s \diamond_{x,y} t = e_{y,x} e_{x,y} t$$ and it suffices to show that this is equal to $$t$$.  The second identity above on $$e$$ (with this $$w=y$$) gives $$- e_{x,w} e_{w,x} = e_{x,x} = -1$$, exactly as needed.
````

**Bruno Le Floch:**

There are a bunch of possible directions to explore:
- Allowing some $$c_{x,y}$$ or $$d_{x,y}$$ to vanish and checking if by any chance this opens up more options.
- Dropping commutativity, but I expect the proof to still go through.
- Adding constant terms to the linear maps, but they will be very constrained if we want the branch in $$(x,s)\diamond (y,t)$$ to determine all other branches when checking E677.
- More than two linear pieces, with a case distinction based on cubic residues or higher. (EDIT: this doesn't help, we get the same $$e$$ equations and same obstruction)
- Changing the case distinction to use something else than residues.
- Going back to the drawing board, such as looking at probabilistic proofs for existence of mixed block designs (the paper to read is [Keevash's 2024 new proof](https://arxiv.org/abs/2411.18291)).  They seem to rely on some algebraic building blocks, so maybe some of our exploration here can be repurposed.

**Bernhard Reinke:**

I had a look at the equations in [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/490348960) , by now we have that one of the not-right-cancellative models of size 25 violates Eq25258: x = (y * (y * (y * x))) * (x * y). i haven't checked the other inconclusive relaxations, maybe this is something we can do systematically against the database that we are constructing?

**Bernhard Reinke:**

On the other hand, since all our current models satisfy 255, I don't think the other inconclusive relaxations will be too interesting, some of them are implied by 255. Also, the 3-variable equations should fail in our gluing constructions.

**Bernhard Reinke:**

I had a look here for linear extensions, in particular I was curious whether the cardinality of $$M$$ could be a power of two that we haven't observed yet. I am reasonable certain that linear models with cardinality of the fiber being 4 are not possible, but I had to use a SAT solver to encode this, so I am not sure whether I can deal with much bigger cardinalities.

**Jihoon Hyun:**

I was tinkering around with equations, and figured out that the only magma of size 5 (up to equiv) satisfies both 677 and 47 (dual of 255), but not 2910 (dual of 677). As 47 is somewhat weaker than 2910, I'm searching for magmas satisfying both 677 and 47, but no magmas other than that of size 5 showed up to size 9. Is there some 677 magma which satisfy 47 (or, 2910) in the database? Also, is there something we know about magmas satisfying both 677 and 2910, and in general, magmas satisfying both some equation and its dual? If it shows some sort of symmetry then it may be easier to somewhat construct or analyze the structure.

**Jihoon Hyun:**

Never mind, under 677 and 2910 we get both left and right inverse which directly implies 255. So we may conclude that any 677 anti 255 model should not satisfy 2910 or 47.

**Bruno Le Floch:**

(EDIT: I just rederived the following.) For any equation E of order ≤4 other than 1, 411, 513, 614, 623, 642, 677, 817, 1020, 1035, 1048, 1223, 1238, 1251, 1426, 3659, 4065, 4073, 4131, 4276, 4293, 4321, 4343, 4380, 4591, 4599, the equation E together with E677 and injective left multiplications (which holds in finite models of E677) implies E255.  Note that 1, 614, 677 do not appear in Jose's list because they are consequences of 677, hence useless.

**Jihoon Hyun:**

I guess you're right! (**Jose Brox** [said](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486683331): ...)
However I'm not sure if we can safely assume one of the equations in the list globally along with 677 anti 255. For example, 411 $$x = x(x(x(xx)))$$ introduces a 4-cycle (or 2- or 1-, but 2-cycle implies 1-cycle) on a permutation $$L_x$$, but I don't think I have seen an example of $$L_x$$ containing an even cycle containing $$x$$ for every $$x$$. Maybe we can assume those equations locally, but assuming globally may clash with 677 itself. Please correct me if I'm wrong, though.
So I'll try assuming that some elements do not satisfy the equation outside the list.

**Bruno Le Floch:**

FWIW, in our database the only elements $$x$$ with $$x=x(x(x(xx)))$$ are the idempotent elements.  Many (97/301) magmas in the database satisfy E513, all of them have some pairs satisfying E513.  Obtained using this Python script: [attached: db-testeq.py].  I could continue for other equations in Jose's list, but it would be useful to have some kind of plan.

**Bruno Le Floch:**

FWIW, the list of equations of order up to 6 that are satisfied by all magmas in the database is
[*Spoiler: List of equations that are de facto consequences of E677 in the database — omitted*]`
1 x = x
255 x = ((x ◇ x) ◇ x) ◇ x
614 x = x ◇ (x ◇ ((x ◇ x) ◇ x))
677 x = y ◇ (x ◇ ((y ◇ x) ◇ y))
19604 x = (x ◇ x) ◇ ((x ◇ (x ◇ x)) ◇ x)
19855 x = (y ◇ x) ◇ ((y ◇ (y ◇ x)) ◇ y)
45037 x ◇ x = x ◇ (((x ◇ x) ◇ x) ◇ x)
45291 x ◇ y = x ◇ (((y ◇ y) ◇ y) ◇ y)
52930 x ◇ x = (((x ◇ x) ◇ x) ◇ x) ◇ x
53134 x ◇ y = (((x ◇ x) ◇ x) ◇ x) ◇ y
331677 x = ((x ◇ x) ◇ x) ◇ (((x ◇ x) ◇ x) ◇ x)
402057 x = ((x ◇ x) ◇ ((x ◇ x) ◇ x)) ◇ (x ◇ x)
406197 x = ((x ◇ (x ◇ x)) ◇ (x ◇ x)) ◇ (x ◇ x)
509697 x = ((x ◇ x) ◇ (((x ◇ x) ◇ x) ◇ x)) ◇ x
534537 x = ((x ◇ ((x ◇ x) ◇ x)) ◇ (x ◇ x)) ◇ x
567657 x = ((x ◇ (((x ◇ x) ◇ x) ◇ x)) ◇ x) ◇ x
604917 x = (((((x ◇ x) ◇ x) ◇ x) ◇ x) ◇ x) ◇ x
613197 x ◇ x = x ◇ (x ◇ (x ◇ ((x ◇ x) ◇ x)))
613260 x ◇ x = x ◇ (y ◇ (x ◇ ((y ◇ x) ◇ y)))
614114 x ◇ y = x ◇ (x ◇ (y ◇ ((x ◇ y) ◇ x)))
614276 x ◇ y = x ◇ (y ◇ (y ◇ ((y ◇ y) ◇ y)))
614493 x ◇ y = x ◇ (z ◇ (y ◇ ((z ◇ y) ◇ z)))
729117 x ◇ x = (x ◇ (x ◇ ((x ◇ x) ◇ x))) ◇ x
729360 x ◇ x = (y ◇ (x ◇ ((y ◇ x) ◇ y))) ◇ x
729995 x ◇ y = (x ◇ (x ◇ ((x ◇ x) ◇ x))) ◇ y
730709 x ◇ y = (y ◇ (x ◇ ((y ◇ x) ◇ y))) ◇ y
731505 x ◇ y = (z ◇ (x ◇ ((z ◇ x) ◇ z))) ◇ y
````
```
Many of them are obvious consequences of E677 or its finite equivalent E19855 `x = (y ◇ x) ◇ ((y ◇ (y ◇ x)) ◇ y)`.  Some others are equivalent to E255 (assuming E677).  The remaining ones could be targets for questions `E677 fin⊨ E?` that might possibly be easier than `E677 fin ⊨ E255?` to prove or disprove:

- 406197 `x = ((x ◇ (x ◇ x)) ◇ (x ◇ x)) ◇ (x ◇ x)`, which seems interesting;

- E52930 `x ◇ x = (((x ◇ x) ◇ x) ◇ x) ◇ x` and E331677 `x = ((x ◇ x) ◇ x) ◇ (((x ◇ x) ◇ x) ◇ x)` are obvious consequences of E255, but appear (from a quick prover9 run) strictly weaker.

**Rudi Schneider:**

Interesting!

I had a look at magma 25/25, which is the only 25-sized magma from the db that does not contain 5/0 as a submagma. It doesn't match any of the affine magmas/cohomological extensions I have seen either.

It is almost entirely defined by its automorphism group:
It can be defined as the unique 25-sized magma with `f(0, 0) = 0`, `f(0, 1) = 4` and these symmetries:
- (0) (1 2 3) (4 5 6) (7 8 9) (10 11 12) (13 14 15) (16 17 18) (19 20 21) (22 23 24) 
- (0 1 8 21 2 23 14 10) (3 4 19 6 12 11 22 7) (5 24 15 9 18 16 13 17) (20)
as witnessed by this script: 
[attached: 25_25.py]

Not sure how it helps as it's idempotent, but maybe it's part of a yet unknown model class.

**Bruno Le Floch:**

The automorphism group has 600=25×24 elements, it acts 2-transitively, it has elements of orders 1,2,3,4,5,6,8,12.  I don't have GAP to figure out what that group is.

**Rudi Schneider:**

Should be SmallGroup(600, 148)

[*Spoiler: group definition — omitted*]

**Bernhard Reinke:**

How did 25/25 arise? Is it the non-right-cancellative quadratic residue over $$\mathbb{F}_{25}$$ construction or did it come out of another search?

**Rudi Schneider:**

I think I took the symmetries of a previous magma, and searched for other magmas with the same symmetries.
I could be wrong but I think it was 25/24 which is your non-right-cancellative magma.

**Bernhard Reinke:**

Ah yes, this makes sense, the non-right-cancellative magma I constructed does contain 5/0.

**Rudi Schneider:**

Correction: the automgroup seems to come from 25/3, which is the cartesian product of 5/0 and 5/0.
If one changes `f(0, 1) = 4` to `f(0, 1) = 13` in the script, it results in magma 25/3.

25/24 has an automgroup of size 300.

**Bruno Le Floch:**

As @Bernhard Reinke pointed out in [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/560447951), models with too much symmetry cannot be minimal counterexamples of E677⊨E255: any minimal counterexample is generated by one element, whose stabilizer must be trivial.

**Bruno Le Floch:**

We could learn something about gluing by looking at 45/2, 45/3, 45/4 in the db: they have several five-element subsets whose multiplication tables partially match with that of 5/0 in the sense that 11 of the 20 off-diagonal entries coincide.  For instance `[1, 13, 16, 26, 35]` in 45/2.

Relatedly, I considered which subsets of the 20 off-diagonal entries in 5/0 are possible in principle, and prover9 could not rule out some the 16-element subset consisting of all off-diagonal entries except `0◇1=4, 1◇0=3, 3◇4=0, 4◇3=1` (or more generally `a◇b, b◇a, (a◇b)◇(b◇a), (b◇a)◇(a◇b)`).  Maybe we can build a finite 677 magma with a five-element subset whose multiplication table shares these 16 elements with 5/0 and not the other 4, or maybe we can prove that it forces the remaining 4 elements, learning new consequences of finiteness.

**Bruno Le Floch:**

To be more explicit, my question (with slightly different ordering of 0,1,2,3,4, matching with the ℤ/5ℤ description) is: is there a finite model of E677 such that `0◇1=4. 0◇2=3. 0◇3=2. 0◇4=1. 1◇0=2. 1◇2=0. 1◇3=4. 2◇0=4. 2◇1=3. 2◇4=0. 3◇0=1. 3◇1=0. 3◇4=2. 4◇0=3. 4◇2=1. 4◇3=0.` but `1◇4!=3.`?

**Bernhard Reinke:**

Yes, 2-transitive examples have to be idempotent, so they cannot be minimal counterexamples of E677⊨E255. That said, it is not too difficult to enumerate them with `GAP`. Here is a a snippet:
[*Spoiler: GAP Snippet — omitted*]gap
TestE677 := function (m)
	local i,j;
	for i in [1..Length(m)] do
		for j in [1..Length(m)] do
			if (m[i][m[j][m[m[i][j]][i]]] <> j) then
				return false;
			fi;
		od;
	od;
	return true;
end;

FillMatrix := function (d,T,k)
	local m, i, g;
	m := NullMat(d,d);
	for i in [1..d] do
		m[i][i] := i;
	od;
	for g in T do
		m[1^g][2^g] := k^g;
	od;
	return m;
end;

ProduceExamples := function (n)
	local result, G, k, m, H, mp, T;
	Print(n, ":\n");
	result := [];
	for G in AllPrimitiveGroups(NrMovedPoints,[n],Transitivity,[2]) do
		Print(G, "\n");
		H := Stabiliser(Stabilizer(G,1),2);
		mp := MovedPoints(H);
		T := RightTransversal(G,H);
		for k in [1..n] do
			if (k in mp) then
				continue;
			fi;
			m := FillMatrix(n,T,k);
			if (TestE677(m)) then
				AddSet(result, m);
			fi;
		od;
	od;
	Print(result, "\n");
end;

```
```
For most `n` we recover the linear translation invariant models we know already, but `n = 25` or `n = 81` might have some interesting output. I tried to remove some redundancies, but probably there are still some left. I am curious whether all of these are in our data base (note that `GAP` is `1`-based):
[attached: Output n=25]

**Bernhard Reinke:**

Probably the results for `n = 121` or `n = 23*23` could also be interesting. If we only interested in 2-generated magmas, I think we can restrict our attention to sharply 2-transitive examples. So there might be a nice description of the resulting magmas in terms of [near fields](https://en.wikipedia.org/wiki/Near-field_(mathematics)).

**Rudi Schneider:**

The 2-transitive automgroup of 5/0 should be `{a*x + b | non-zero a}` in GF(5), which I think is called the affine group.
It looks like both 25/3 (aka 5/0 × 5/0) and 25/25 inherit this field (or then near-field) in some twisted way.

> I am curious whether all of these are in our data base (note that `GAP` is `1`-based):

Yes, they are.
But higher n could be interesting.

**Rudi Schneider:**

I ran it til n=100, and found one new model of size 81, namely 81/20
https://github.com/memoryleak47/eq677/commit/8a5eb2797d7516143c767acddaff53ce1daca5b3

It's not a 5/0-gluing model, and not found in the affine/cohomological extension lists I have so far, even though I'm not yet confident this list is complete.

**Rudi Schneider:**

Hey, new construction to combine models together:
Let ML be an idempotent magma whose computation of f(y, f(x, f(f(y, x), y))) never evaluates f(a, a) for any a, except if x=y held initially.

Let MR and MR' be two 677 models of the same size n.

Then you can build an extension of ML by
```
f((x, s), (y, t)) =
  if x=y: (ML(x, y), MR(s, t))
  else: (ML(x, y), MR'(s, t))
```

found 26 new models under size 100: https://github.com/memoryleak47/eq677/commit/883ca99e96ac2ba788bee48e3e48061d95b6b9da

Edit: And just like with gluing, by shuffling MR or MR', you can create many more non-isomorphic magmas from the same input magmas.

It won't directly help with 255 though, the magma generated by a single element will always be isomorphic to the magma generated by the corresponding element in MR.

Edit 2: An extended construction would choose MR depending on the value of x=y. So MR' would be for the case where x != y, and for each x=y one could provide a specialized MR_x.

Edit 3: This can be generalized further: We can group pairs of ML-elements (a, b) and (x, y) into equivalence classes, based on whether the evaluation of 677 (i.e. f(x, f(y, f(f(x, y), x)))) might depend on f(a, b). Any equivalence class of pairs {(a, b), (x, y) , ...} of elements in ML can get their corresponding MR_(a,b) magma.
Computationally, we start by having all pairs (x, y) as separate singleton equivalence classes, and then if while evaluating f(x, f(y, f(f(x, y), x))) we encounter f(a, b), we'd have to merge the classes of (a, b) and (x, y).

For this generalization ML doesn't need to be idempotent, but in order to be interesting it needs to have more than just one equivalence class.

Maybe there is a way to find a 677 -/> 255 counter example using this. If we find an element x in ML, s.t. during evaluation of 255  (i.e. in f(f(f(x, x), x), x)) it evaluates f(a, b) and f(c, d), where the pairs (a, b) and (c, d) are not in the same 677-equivalence-class, then we would be free to choose some MR_(a,b) and MR_(c,d) that makes 255 false. So far it looks however, as if the equivalence relation of 255 refines the equivalence relation of 677.

**Bernhard Reinke:**

I think we can still conceptualize your construction by gluing partial models, in your case partial models that are direct products $$ ML_i \times MR_i $$ where $$ ML_i $$ form a partition of an actual model into partial ones, and $$ MR_i $$ are models. With this in mind, we have the following restriction:   

I think this implies that we should be able to evaluate 255 in only one partial magma, so I don't think we can use this to find a 677 -/> 255 counter-example using this.

**Bruno Le Floch:**

Indeed, it's a gluing of partial models.  So far the only partial models we have are magmas in which some subset of entries `x◇x=x` have been removed, and their products (used in Rudi's latest construction).  Does the database feature any other partial model?

There could be such partial models that are subsets of linear magmas perhaps.  IIRC some exploration I did, submagmas of linear magmas are linear, but I didn't study partial models.

**Rudi Schneider:**

If my computations of these equivalence classes are correct, this would be a dump of them up to n=50.
It seems we have more than just the ones you mentioned.
[attached: partials]
I'm considering to build a db for partial models, this might deduplicate a lot of models that only distinguish themselves in how we glue together their fragments.

(But these could actually be due to gluing. Gotta go, but will check later)

**Bruno Le Floch:**

Is it clear that these should be equivalence classes?  Namely, if I take a subset A of pairs such that (x,y)∈A ⇒ (x◇y,x)∈A and (x,y)∈A ⇒ (y,(x◇y)◇x)∈A and (x,y)∈A ⇒ (x,y◇((x◇y)◇x))∈A, is it clear that the converses of these implications also hold?

By the way, I should have restricted my question to indecomposable partial models, only.  If you take the size 21 magma built by gluing several size 5 submagmas, and delete the Cayley table of one of these submagmas from the Cayley table of the big magma, you get a partial model that is not in the class described in my previous message.  But that is uninteresting because the resulting partial model is just a union of partial models of order 5 that we already know.

**Rudi Schneider:**

I think they need to be equivalence classes for the ML/MR construction above, but partial models might not generally form equivalence classes. I intended to check that out for the db later today.
Shouldn't be too hard to compute the minimal partial model spanned by some element (x, y) using the code I have from earlier.

> I should have restricted my question to indecomposable partial models

Agreed, the db I mentioned was also only intended for primitive partial models.

**Bernhard Reinke:**

I think in general they don't have to be equivalence classes. I checked the model 25/24, and constructed the directed graph on pairs that is given by the implications. We have 26 weak connected components but 41 strong ones, so some of the implications are not reversible.

**Bernhard Reinke:**

Not sure if this is the smallest example in the database, but it seems like an obvious candidate to me (the smallest known example that is not right cancellative)

**Bernhard Reinke:**

The weakly connected components are 25 singleton components of the form `{(x,x)}` and one component that is the complement of the diagonal.

**Rudi Schneider:**

I did a pass through the db and computed for each pair of elements (x, y) the smallest partial model defining `x ⋄ y`.
[attached: partials2]

Other than ones we knew there's the cases where models have a single idempotent element,
in this case the remaining magma turns out to be an partial model, like here with 7/0:

```
05 06 03 01 00 02 04 
03 00 06 04 02 01 05 
02 04 01 06 05 03 00 
04 03 05 02 06 00 01 
01 05 04 00 03 06 02 
06 02 00 05 01 04 03 
00 01 02 03 04 05 -
```

The list is deduplicated by throwing away isomorphic partial models per db-magma, and by removing single-element partial models.

**Rudi Schneider:**

But there's also these couple of cases like this one:
[attached: 45/4 minimal partial model with (0, 5)]
whichs looks like the original magma with some small submagmas cut out. Not sure about them

**Bruno Le Floch:**

Just from looking at holes, this last one looks like it could be 5/0 minus idempotents, times 9/0, can you easily check?

**Rudi Schneider:**

Good point, the number of holes does match. But assuming my canonicalization works correctly for partial magmas, it does not seem to be the same.
[attached: compare]

Uh the original magma 45/4 does come from a cohomological extension

**Rudi Schneider:**

probably from here

Edit: It's the model at line 533.

**Rudi Schneider:**

It seems by starting the general dpll-searcher with a mostly-complete partial model, we can find a couple more new completions for them:
https://github.com/memoryleak47/eq677/commit/fc8379803af8ed8c8da9a863765543ee1dad6edb

Probably some form of gluing, but not only steiner S(2,5,n) gluing as it also works for size 35 models.

**Bernhard Reinke:**

Have you tried completing this partial model [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/558842589) ?

**Bruno Le Floch:**

Note that this probably requires adding more elements than the original 22.  I don't know if dpll-searcher is set up to do that.

**Rudi Schneider:**

Yeah that's a good point, I can add elements in preprocessing however.

if I add just a few extra elements it doesn't find a completed magma, and when I give 3 (edit: 4) or more elements it takes too long as the search space gets too big.

**Bernhard Reinke:**

By the way, what is your current way to search for models with a given list of generators of a group of automorphisms? At some point you considered cyclic groups (where one generator is enough), do you have now methods in your search algorithm for more symmetries?

**Rudi Schneider:**

The c_run function (https://github.com/memoryleak47/eq677/blob/9528466b813e29de85fbfed3e89df3df60448411/src/c_dpll/run.rs#L12)
now gets a size and a list of automorphisms.
So you don't need a branch anymore

**Rudi Schneider:**

So you can freely put any automorphisms there.
I've seen automorphisms with phi(0) = 0, and otherwise m many k-cycles with m*k+1=n quite a bit.
But it doesn't seem to restrict the search space as well as having just one big cycle.

**Bruno Le Floch:**

I'd be interested in seeing the new size-35 magmas that come up by recompletion, I think the size-25 are mostly just gluings of size 5.

**Rudi Schneider:**

Sure!
[attached: new-35ers]

**Rudi Schneider:**

To me it seems we generate 5/0 without idempotents times a 7-sized model, generating something like [attached: this], so pretty much the construction you mentioned before.

And the 5 resulting gaps can be filled with any of the 7 sized magmas respectively, which are allowed to be permuted in any way (so 2*7! options per gap minus symmetries).

I think this can be seen as an instantiation of the ML x MR scheme.

**Bruno Le Floch:**

I think what I was missing is the cohomological extension version of that: if you have $$(x,s)\diamond(y,t) = (x\diamond y,s\diamond_{x,y}t)$$ and remove $$(x,s)\diamond(x,t)$$ whenever $$x\diamond x=x$$, then you get some partial model that has the same holes as a product I described, but a different magma operation.

Setting up a partial magma db seems necessary to avoid combinatorial explosion of the kind you noticed.  Maybe also a db of "ways to glue", where we only track which (weak?) (strong?) connected components there are.

**Rudi Schneider:**

Ah, cool observation. So ML x MR_i don't need to be direct products, but we can also allow them to be different extensions of the same base model ML.

**Bruno Le Floch:**

Bernhard's observation above about 25/24 having different strong and weak components seems very important actually.  I'm envisioning something like a core partial model and some "add-ons" that can attach in certain ways to the core.  Then there is some hope that we can start filling up a counterexample to 255 whose missing entries (to become a partial model) match the ones of some "add-ons", so that the 255 counterexample add-on, plus a core, would make a partial model which could then be completed into a full magma by standard gluing.

**Rudi Schneider:**

[attached: Here]'s a deduplicated list of partial models from the db.
The first 193 models from the db only contain 58 different partial models (induced by a single (x, y) pair).
So it might actually help to deduplicate. As expected, most redundancies were found for non-prime sized models and Steiner gluings.

25/24 seems to only contain 5/0 without idempotents (repeated in many ways), and the entire magma without idempotents as primitive partial models.

One question about strong components: I'm assuming that (x, y) gets an edge to (a, b) if and only if f(x, f(y, f(f(x, y), x))) evaluates f(a, b) at any point. Under this assumption, any partial model would have to be closed under outgoing edges. Do I assume correctly that strong components do not generally form partial models, as they might not satisfy that condition?

Edit: confused strong/weak.

**Rudi Schneider:**

Also, I think we can strengthen this to "we only care about self-contained partial models consisting of all pairs reachable from (x, x)" in the aforementioned graph.

**Bernhard Reinke:**

I think you mean that strongly connected components (two vertices are in the same scc if both can be reached from the other by a directed path) are not necessarily partial models, and then for 25/24 there is a strongly connected component with outgoing edges, so on its own it is not a partial model

**Rudi Schneider:**

I was looking into a slightly different notion of equivalence classes, that might yield something useful:

Consider a coloring of pairs (x, y), s.t. if (x, y) and (a, b) agree in color, then their 677 traces (i.e. the sequence of pairs evaluated in their 677 computation) fully agree in color.

The motivating example is translation invariance, where the color is the value of y-x; if you know y-x, then you'll know the deltas of all further 677 computation steps in f(y, f(x, f(f(y, x), y)))

Now, if you look at 5/0, 11/0 or 11/1 minus idempotents, all of them have a 2-coloring:
For 5/0, if y-x is 2 or 3, it's red; and if it's 1 or 4 it's blue.

The traces of these colors yield:
red trace: [red, red, blue, red]
blue trace: [blue, blue, red, blue]

Which means that you can build an extension of 5/0, one for the blue and one for the red case.

`f((x, s), (y, t)) = (M5(x, y), red(x, y)? f1(s, t): f2(s, t))`

Using this we can rephrase 677 as:
x = f1(y, f2(x, f1(f1(y, x), y)))
x = f2(y, f1(x, f2(f2(y, x), y)))

For 11/0 and 11/1 we get similar equations:
11/0:
x = f2(y, f2(x, f1(f1(y, x), y)))
x = f1(y, f1(x, f2(f2(y, x), y)))

[which under f1(x, y) = f2(y, x) becomes
x = f1(y, f1(x, f1(y, f1(x, y))))
x = f1(f1(f1(f1(y, x), y), x), y)
]

11/1:
x = f2(y, f1(x, f1(f1(y, x), y)))
x = f1(y, f2(x, f2(f2(y, x), y)))

So far, I've looked into some solutions with `f1, f2` being affine functions (sympy brings a couple solutions), that would be new in the db
but they could be covered by cohomological extensions + some re-shuffling

**Bernhard Reinke:**

I think it could be very helpful to construct these colorings systematically. I guess one can interpret them as possible quotients of an edge-labeled graph. In our study of the "quadratic residue models", we basically had the coloring given by whether `y-x` is a quadratic residue or not.

So in your language, we could add for example

25/24:
x = f1(y, f1(x, f1(f1(y, x), y)))
x = f2(y, f1(x, f2(f2(y, x), y)))

I would be curious to see whether we can also get a manageable coloring including pairs `(x,x)` such that the trace of `(x,x)` is not just one color. Using the "projective coloring" for 7/0 (or 7/1) we can go down to 8 colors, but can we do even fewer colors?

**Rudi Schneider:**

Interestingly, 29/0 without idempotents can be 2-colored in 3 different ways:
[attached: image.png]
[attached: image.png]
[attached: image.png]

I had no success with non-idempotent magmas though.

**Rudi Schneider:**

Based on the projective colorings of 7/0 and 7/1, I found a couple of non-right-cancellative & non-idempotent extensions.

77/65 is based on 7/0, and
49/18 is based on 7/1.

The search script is here: https://github.com/memoryleak47/eq677/blob/main/color-extensions.py

The model class is `f((x, s), (y, t)) = (M7(x, y), f_[x:y](s, t))`
where `f_[x:y](s, t) = (a_[x:y]*s + b_[x:y]*t + c_[x:y])%K`

**Matthew Bolan:**

I find that 77/65 is also generated by the single element $$0$$, making it perhaps the first singly-generated counterexample to right-cancellativity.

**Bernhard Reinke:**

I am looking for models that have a "non-commutative" transitive invariant model. So far I have found the following two models of size 21:
[attached: Two size 21 models]
Maybe they are also a gluing construction?

**Matthew Bolan:**

 These are idempotent and I find that every pair of distinct elements in these generates a submagma of size $$5$$, so my guess is that they do come from a gluing construction.

**Bernhard Reinke:**

Here is a non-commutative semitranslation invariant model for size 21 that might be interesting:
[*Spoiler: Semitranslation invariant model with 4-cycle — omitted*]text
G = SmallPermutationGroup(20, 3)
New Model "21/4" found by c_dpll:
00 20 03 02 17 14 19 16 13 18 15 12 11 08 05 10 07 04 09 06 01 
03 01 20 00 06 07 08 09 10 11 04 05 14 15 16 17 18 19 12 13 02 
01 00 02 20 19 12 13 14 15 16 17 18 09 10 11 04 05 06 07 08 03 
20 02 01 03 15 16 17 18 19 12 13 14 05 06 07 08 09 10 11 04 00 
13 09 05 14 04 20 12 19 17 03 07 10 15 00 01 16 06 08 02 11 18 
18 10 19 06 11 05 20 17 16 14 02 08 13 07 09 03 04 12 00 01 15 
10 11 07 16 09 04 06 20 14 13 00 03 02 05 17 19 01 18 08 15 12 
12 04 13 08 02 10 05 07 20 19 18 16 00 01 15 09 11 03 06 14 17 
04 05 09 18 00 03 11 06 08 20 16 15 10 17 02 07 19 13 01 12 14 
05 06 15 10 12 00 02 04 07 09 20 13 08 16 18 01 17 11 14 03 19 
19 07 11 12 18 17 15 03 05 08 10 20 01 14 04 06 02 09 13 00 16 
07 08 17 04 20 15 14 00 02 06 09 11 16 03 10 18 12 01 19 05 13 
16 17 08 13 03 19 09 11 01 10 14 07 12 20 06 05 00 02 15 18 04 
17 18 14 05 08 01 07 15 04 02 12 06 19 13 20 11 10 00 03 16 09 
09 19 10 15 16 18 03 13 11 00 01 04 17 12 14 20 08 07 05 02 06 
06 12 16 07 14 08 00 01 09 17 19 02 03 18 13 15 20 05 04 10 11 
11 13 04 17 01 06 18 12 03 15 05 00 07 02 19 14 16 20 10 09 08 
08 14 18 09 13 02 16 10 00 01 11 19 06 04 03 12 15 17 20 07 05 
14 15 06 19 07 09 01 08 12 05 03 17 04 11 00 02 13 16 18 20 10 
15 16 12 11 05 13 10 02 18 04 06 01 20 09 08 00 03 14 17 19 07 
02 03 00 01 10 11 04 05 06 07 08 09 18 19 12 13 14 15 16 17 20
New Model "21/5" found by c_dpll:
00 20 03 02 17 14 19 16 13 18 15 12 11 08 05 10 07 04 09 06 01 
03 01 20 00 06 07 08 09 10 11 04 05 14 15 16 17 18 19 12 13 02 
01 00 02 20 19 12 13 14 15 16 17 18 09 10 11 04 05 06 07 08 03 
20 02 01 03 15 16 17 18 19 12 13 14 05 06 07 08 09 10 11 04 00 
13 09 05 14 04 20 12 19 17 03 07 10 15 00 01 16 06 08 02 11 18 
18 10 19 06 11 05 20 17 16 14 02 08 13 07 09 03 04 12 00 01 15 
15 11 07 16 09 04 06 20 14 13 19 03 02 05 17 00 01 18 08 10 12 
12 04 13 08 02 10 05 07 20 19 18 16 00 01 15 09 11 03 06 14 17 
04 05 09 18 00 03 11 06 08 20 16 15 10 17 02 07 19 13 01 12 14 
05 06 15 10 12 00 02 04 07 09 20 13 08 16 18 01 17 11 14 03 19 
06 07 11 12 18 17 00 03 05 08 10 20 01 14 04 19 02 09 13 15 16 
07 08 17 04 20 15 14 00 02 06 09 11 16 03 10 18 12 01 19 05 13 
16 17 08 13 03 19 09 11 01 10 14 07 12 20 06 05 00 02 15 18 04 
17 18 14 05 08 01 07 15 04 02 12 06 19 13 20 11 10 00 03 16 09 
09 19 10 15 16 18 03 13 11 00 01 04 17 12 14 20 08 07 05 02 06 
19 12 16 07 14 08 10 01 09 17 06 02 03 18 13 15 20 05 04 00 11 
11 13 04 17 01 06 18 12 03 15 05 00 07 02 19 14 16 20 10 09 08 
08 14 18 09 13 02 16 10 00 01 11 19 06 04 03 12 15 17 20 07 05 
14 15 06 19 07 09 01 08 12 05 03 17 04 11 00 02 13 16 18 20 10 
10 16 12 11 05 13 15 02 18 04 00 01 20 09 08 06 03 14 17 19 07 
02 03 00 01 10 11 04 05 06 07 08 09 18 19 12 13 14 15 16 17 20
```
```

**Bernhard Reinke:**

By now it found also a small variant with the same group for the semitranslation approach.

**Bernhard Reinke:**

Both of them contain a partial model on 20 elements that is defined away from the disjoint union of 5 copies of `K_4`. So probably one can complete this partial model in numerous ways by adding an element an put a copy of `5/0` on each of the 5 copies of `K_5` that meet in the additional element.

**Bernhard Reinke:**

I think the partial model on 20 elements is a $$\mathbb F_4$$ -linear extension of `5/0` minus idempotents with the 2-coloring as in [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/564958584).

**Bernhard Reinke:**

Actually, I am not sure, whether the partial model is indeed such a linear extension, but something in this direction should exists.

**Bernhard Reinke:**

I am somewhat optimistic that we can use this kind of trick to produce a model of cardinality `76 = 5*15 + 1` or other cardinalities `n%30 = 16`.

**Bernhard Reinke:**

I managed to get a model of size 166: 
[attached: Model of size 166]
It contains a partial model of size 165 that is a linear extension over 11/0 very similar to  [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/558842589) , and then we add an extra point and glue in a bunch of copies of 16/0. Note that `166 = 83*2`, I think this is the first concrete model of size $$\equiv 2 \mod 4$$.

**Bernhard Reinke:**

I think this construction generalizes in the following way: If there is a model of size $$n$$ with at least one idempotent, then there is a model of size $$11 * (n -1) + 1 = 11n - 10$$. For example, here is a model of size 89 (I think we didn't have this size before): 
[attached: Model of size 89]
We can replace 11 by any number where we have an idempotent model admitting the same two-coloring as 11/0.

**Bernhard Reinke:**

Or even more: If there is a model of size $$n$$ that contains a model of size $$k$$, then there is a model of size $$11 * (n - k) + k = 11 n - 10 k$$.

**Bernhard Reinke:**

I thought a bit about constructing models of size 96 = 2⁵ * 3. My line of attack was using 2-(96,{5,16},1) block designs as a gluing pattern for 5/0 and 16/0. I looked quite a bit for block designs that have a 96 cyclic symmetry, I think I can exclude them by an exhaustive computer search, but maybe I made too many simplifying assumptions along the way. If we want to look at homogeneous block designs, there are basically two possibilities: either every point is contained in 20 5-blocks and 1 16-block, or every point is contained 5 5-blocks and 5 16-blocks. In the first case the 6 16-blocks partition the 96 points.

**Bernhard Reinke:**

I found a 2-(96,{5,16},1) block design whose points form a `SmallPermutationGroup(96,1)` torsor, here is a resulting [attached: Model of size 96]. By shuffling we should be getting a lot more. I haven't checked whether the model I constructed still has the same symmetries, but this should be probably doable if one is more careful at the gluing step.

Here is a sketch of the construction/search:
The group `G = SmallPermutationGroup(96,1)` has as Frattini quotient `Sym(3)`, the blocks `B_0, B_1, B_2, B_3, B_4, B_5` of size 16 are the cosets of the Frattini subgroup (with `B_0 = Phi(G)`). The blocks of size 5 are right-translates of 4 blocks of the form $$\{1, g_1, g_2, g_3, g_4\}$$ where $$g_i \in B_i$$. We can enumerate all four-tuples $$g_1,..,g_4$$ such that the set $$\{a*b^{-1} : a \neq b \in \{1, g_1, g_2, g_3, g_4\} \}$$ has cardinality 20. There are 29136 such four-tuples. We have to find a combination of 4 of such four-tuples such that the corresponding sets cover $$ G \setminus B_0 $$, this can be solved by an exact cover solver.

**Bernhard Reinke:**

Actually, I don't think we should still have the same set of symmetries, already because the Frattini subgroup is cyclic, but the model `16/0` is more naturally supported on an elementary abelian group.

**Bruno Le Floch:**

Great!  I think the known spectrum ≤100 is now: 1, 5, 7, 9, 11, 13, 16, 19, 21, 25, 29, 31, 35, 37, 41, 43, 45, 49, 55, 61, 63, 65, 67, 71, 73, 76, 77, 79, 80, 81, 85, 89, 91, 95, 96, 97, 99.

**Bernhard Reinke:**

I managed to find a [attached: Model of size 76] via a (non-homogeneous) 2-(76,{5,16],1) block design. It is also glued together using 5/0 and 16/0. The idea is to take as 5-blocks a transversal T(5,1,15) design (exists as there are 3 mutually orthogonal Latin squares of size 15), add an extra point an fill in the rest with blocks of size 16 that all meet in the extra point.

If we knew that 3 mutually orthogonal Latin squares of size 10 exist (still open), then we would be able to construct a model of size 51 using this method.

**Bruno Le Floch:**

I've edited my message above to reflect the new 76.   For 51 I had [pointed this out upthread](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/560767814) already; we are unlikely to make any progress beyond what's known.

Do we have any technique to show non-existence for certain sizes?

**Bernhard Reinke:**

I guess so far we only have the technique to have an exhaustive search return nothing, so probably we could use some `unsat` certificates of general model searches if we want to formalize this.

**Bernhard Reinke:**

I had a look a bit at highly symmetric partial models. For example, the biggest "connected" partial model contained in [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/565798849)  has the automorphism group acting sharply on the set of pairs of points whose multiplication lies in the partial model. A similar thing happens for 25/8.

Is it possible to search for partial models with given set of definition and given symmetries with your software @Rudi Schneider ? I would be particularly interested in the setting where we have a group `G` acting transitively (but not primitively) on some finite set, and there is a block structure for this action, and `G` acts sharply transitively on pairs of points `(x,y)` where `x` and `y` belong to different blocks. In this case one should be quite fast in filling in the partial model.

**Rudi Schneider:**

You could tweak the functions `c_complete` and `c_complete_extended` a bit.
They call `build_ctxt(n, Vec::new())` where this empty vec is the empty set of automorphisms.
I would assume that replacing this empty Vec with your intended automorphisms should do the trick.

Also, `c_complete` would probably perform better when we set `ctxt.nonfresh` to the number of non-fresh elements from the partial model. Setting it to n directly (as I had done) entirely disables symmetry breaking.

**Bernhard Reinke:**

At a first glance it seems to me that `c_complete` is about completing a partial model. But I want to compute a partial model with prescribed set of definition, so I guess there is more tweaking involved. I have an idea on how to fill in the complement, but I cannot guarantee the symmetries for my fillings.

**Rudi Schneider:**

Apologies, I misread.
The `Ctxt` represents a partial model, if and only if no `ClassXY::cs` contains a C11 or C12 constraint anymore (i.e. a started yet unfinished f(y, f(x, f(f(y, x), y))) computation).
One could technically check that eg. in `select_p`, but I don't think it would be guaranteed to find all partial models. Would probably require more structural changes

**Bernhard Reinke:**

So far my search for highly symmetric partial models didn't help me in constructing models with new cardinalities. Here is a curious partial model on 15 points:
[*Spoiler: Partial model on 15 points — omitted*]text
-  04 -  -  01 -  13 -  14 -  11 10 -  06 08 
06 -  07 -  13 -  00 02 -  11 -  09 -  04 -  
-  09 -  14 -  13 -  11 -  01 -  07 -  05 03 
-  -  13 -  07 14 -  04 -  -  12 -  10 02 05 
13 06 -  10 -  -  01 12 -  -  03 -  07 00 -  
-  -  03 02 -  -  08 -  06 12 -  -  09 14 13 
04 13 -  -  00 09 -  -  12 05 -  -  08 01 -  
-  11 09 12 10 -  -  -  -  02 04 01 03 -  -  
11 -  -  -  -  12 09 -  -  06 14 00 05 -  10 
-  07 11 -  -  08 12 01 05 -  -  02 06 -  -  
08 -  -  07 12 -  -  03 00 -  -  14 04 -  11 
14 02 01 -  -  -  -  09 10 07 08 -  -  -  00 
-  -  -  04 03 06 05 10 09 08 07 -  -  -  -  
01 00 14 05 06 03 04 -  -  -  -  -  -  -  02 
10 -  05 13 -  02 -  -  11 -  00 08 -  03 - 
```
```
It has as symmetry group S_5, acting on 15 points as on (non-trivial) involutions in A_5. I think the magma operation is defined iff the group multiplication of the involutions has order 5. Not sure whether this partial model embeds into a larger actual model.

**Bruno Le Floch:**

This partial model is a gluing of 5/0-minus-idempotents on the blocks (0,1,4,6,13), (0,8,10,11,14), (1,2,7,9,11), (2,3,5,13,14), (3,4,7,10,12), (5,6,8,9,12).

**Bernhard Reinke:**

The construction of [#Equational > FINITE: 677 -&gt; 255 @ 💬](#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/566987091) can be done more generally using group divisible designs. I looked a bit in the literature for 5-GDDs and found in https://ajc.maths.uq.edu.au/pdf/87/ajc_v87_p001.pdf a 5-GDD of type $$12^5 8^1$$. We can use this to construct a model of size $$5 \cdot 12 + 8 + 1 = 69$$: The blocks of size 5 become copies of 5/0, the groups of size 12 (respectively 8) glue with the extra point to 13/0 (resp. 9/0).

[attached: Model of size 69]

**Bernhard Reinke:**

Also, I think we should get from the main theorem of the paper applied to 5-GDDs of type $$6^u$$ that models of size `n%60 = 31` should exists up to a possible small explicit exceptional set.

**Bruno Le Floch:**

Good find! If I read correctly, their Theorem 1.2 would provide models of size n%60 = 11 and 31 except {11, 31, 211, 571}.  I think among these sizes, the first orders that are new are 371, 391, 611, but I did not track carefully such high orders.  With your other construction, order 69 is certainly new.  I think their $$24^7 8^1$$ gives a new order: 177.  Maybe their Lemma 2.1 could be useful to rescale some of their other group divisible designs of Theorem 3.1: for instance.

**Bruno Le Floch:**

Ah, one subtlety I didn't notice in your description is that the models are not idempotent: the models 13/0 and 9/0 have one idempotent element, which is selected as the extra point you add to the various blocks, then you glue the (diagonal-free) models 5/0 in each 5-block.

By the way, their Theorem 3.3 gives other new sizes, at least 57 from their $$1^{48}9^1$$ (without adding an extra point, just gluing 9/0 and 1/0 to many diagonal-free 5/0), [attached: block-model-57.txt], and 93 from their $$1^{80}13^1$$.  For higher sizes I don't know for sure whether they are new or not, such as size 107 from $$6^{16}10^1$$ plus one element.

**David Renshaw:**

Last week at a workshop in Aarhus, @George Tsoukalas|644040 and I (with some AI help) constructed some non-right-cancellative magmas satisfying eq677, having sizes 55, 77, 121, 143, 155, and 176. 
[attached: magma_55.py]
[attached: magma_77.py]
[attached: magma_121.py]
[attached: magma_143.py]
[attached: magma_155.py]
[attached: magma_176.py]

**David Renshaw:**

I opened some pull requests to start adding these to @Rudi Schneider's database: https://github.com/memoryleak47/eq677/pull/1,  https://github.com/memoryleak47/eq677/pull/2.
I didn't open PRs for the larger magmas, because the `present_model` function only adds magmas smaller than 100 to the database.

**David Renshaw:**

The construction for all of these is inspired by the "magma cohomology" approach for the size-496 magma discussed previously.

**David Renshaw:**

I also vibe-coded a visualization of the models in the database: https://dwrensha.github.io/eq677/index.html

**Bruno Le Floch:**

How do these compare with the non-right-cancellative models of [size 55 and 77 mentioned upthread](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/558778716)?

**Bruno Le Floch:**

For the visualization, I'm surprised that so much of the structure is visible.  Are you just assigning hue based on the value in order from 0 to n-1, or are you choosing the color assignment in some automated way that somehow picks up the structure?

**David Renshaw:**

Yes, the hue just uses the (canonicalized) value
```rust
fn value_to_rgb(val: usize, n: usize) -> (u8, u8, u8) {
    if val == usize::MAX || n == 0 {
        return (128, 128, 128); // gray for undefined
    }

    // Smooth cyclic rainbow using HSL with S=1, L=0.5 (full saturation, medium lightness)
    // Hue cycles from 0 to 1 as val goes from 0 to n-1
    let hue = (val as f64) / (n as f64);
    hsl_to_rgb(hue, 1.0, 0.5)
}
```

**David Renshaw:**

I get the sense the canonicalization can obscure the structure in the visualization. Here's what our new 55-element and 77-element magmas look like before canonicalization. 
[attached: magma_55.png]
[attached: magma_77.png]

**David Renshaw:**

(compare to the canonicalized versions at https://dwrensha.github.io/eq677/index.html, which I have updated with these two new magmas)

**David Renshaw:**

Did you add these models to @Rudi Schneider's database?

**Bruno Le Floch:**

Looking a bit at the commit history it seems I did not add them, sorry.  Here is the [attached: size 77 magma] for what it's worth, I had it lying around.  I don't know which script to use to add that to the db.

**David Renshaw:**

Opened a pull request for that one: https://github.com/memoryleak47/eq677/pull/3

**David Renshaw:**

The way I've been adding these to the database is to modify `src/main.rs` to call `load_file("path/to/magma_file.txt");`

**Bruno Le Floch:**

Thanks!  I confirm that the 55-element magma I found coincide with yours, and that the 77-element one differs.

**Jose Brox:**

@Rudi Schneider I asked Claude (Sonnet 4.5 extended) to analyze your program and write a user manual. Could you kindly confirm if it got everything right? I attach it here:
[attached: SCHNEIDER_User_Manual_CLAUDE.pdf]

**Rudi Schneider:**

The information looks roughly right, but I'm not sure it would be practically that helpful. If you have a question on how to do something with the tool, just let me know, happy to help :)
