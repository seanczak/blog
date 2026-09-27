---
layout: post
title: "Calling Elections Early: Fake News or Statistics?"
date: 2020-11-09 17:34:41 -0800
description: "A high-level, accessible walk through of the inference engine behind calling elections"
tags: [statistics]
---

At 8:40pm EST, most major news stations had called Illinois for Biden even though state officials had only reported about 500,000 votes. This was only an estimated 6% of the votes! How can a candidate win so early? Is this some sort of fake news/voter suppression?

![A tabby cat with wide green eyes looking up]({{ '/content/statistics/2020_election_series/00_calling_elections_early/img/cat-photo.jpg' | relative_url }})
*Image Credit: [Paul Hanaoka](https://unsplash.com/@plhnk)*

Well… it turns out that they were right so let’s see if we can unpack the magic behind the statistics that they used to infer these results days before the final votes were counted (they are still counting at writing of this article).

What I imagine happened here is a simple risk analysis coupled with the all-American drive to be FIRST.

On the one hand, it seems reasonable that at a certain point, we pretty much “know” who won, right? On the other, you don’t want to be wrong about something like that. These news sources are constantly competing for our eyeballs (and trust). Being first and not being wrong becomes a balancing act. Imagine how many hits the first 10 sentence article got when Michigan was called (translation: \$\$\$\$).

Better call in those weirdos who enjoy doing math. See if they can sort this out…

> **Accessibility note:**
>
> This is the foundation for the rest of the [series]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %}). There are numbers and figures included below…it would hardly be a statistics explanation if there weren’t. However, I recognize that I’m writing for a general audience so I do my best to remain accessible and hopefully demonstrate how simple and powerful the fundamentals of statistics actually are.

## Step 1: Marbles

I am not privy to the information that they are using to make these calls but I can show you something that I find kind of cool which could serve as a first order approximation of what I believe is going on behind the scenes.

I start, like any self-respecting statistician, by assuming that the votes are not actually votes but marbles. But not just ANY marbles. These are special voting marbles whose colors represent a person’s vote (let’s get a little crazy and say blue for Biden and red for Trump). And instead of going to various polling offices, mail boxes, etc, the people cast their votes by bringing their special marbles to one big-ol marble bag located in the state’s capital on election day. Now, once that’s been done, the state has a huge bag of marbles which effectively represents who the people of that state want to have as their next steward of the human-race-self-destruct button.

![A bag labeled Illinois full of mixed red and blue marbles, captioned: pretending your vote is actually a marble of a certain color that everyone in the state drops off in a bag at the doorstep of the state capital]({{ '/content/statistics/2020_election_series/00_calling_elections_early/img/marble-bag.png' | relative_url }})
*Image by Author*

Ok, now the fun begins. We first shake the bag to make sure it’s fully mixed. Then we start drawing marbles and recording the results. We get a better sense of what the composition of red/blue is of the bag as we draw each new marble. We know that if the composition of the bag is more than 50% red, then Trump wins. Otherwise, Biden will win.

So let’s phrase the problem this way: how many of these marbles need to be drawn in order to be confident in assigning a victor (e.g. saying that the bag has more or less than 50% of a single color).

## Step 2: Playing God

Ok let’s quantify that somehow. Let’s say 55% of people in Illinois voted for Biden. This means the composition of that magic bag is 55% blue and 45% red. Simple enough. But no one knows it yet!

For a moment, let’s pretend like we do know it… maybe we’re God. So we watch the humans start by drawing 100 marbles and they see that only 49 of them are blue. The humans, being rational beings, conclude that as far as they know, the bag’s composition is 49% blue and thus Trump wins (hooray for the red people).

As God, we might be confused here… how did they get it wrong? What were the odds of the humans drawing less than 50% blues if the bag itself is 55% blue? To answer we decide to run the same experiment (draw 100 from the bag and then put them back) a million times and plot the number of each observed outcome (shown below). Ahh, now we see, in 30% of the cases, the humans could have drawn less than 50 blue marbles (see the red line) and incorrectly concluded that the bag had more red marbles. Ok it all checks out.

![Histogram of 1 million simulated drawings of 100 ballots: number of votes for Biden (x axis, 30 to 80) against simulated occurrences (y axis, 0 to 100,000), peaking near 55, with a red line at 50]({{ '/content/statistics/2020_election_series/00_calling_elections_early/img/draws-n100.png' | relative_url }})
*Image by Author*

Luckily, the humans are smart. They also realize that they have a high probability of getting the answer wrong if they only grab 100 marbles. So they quickly increase their number to 1000 marbles. Before telling you what they saw, let’s first try to make a guess. A visual way to approach this would be to make the same graph as above (draw *n* = 1000 marbles from the bag a million times and plot the results) and see what that tells us.

![Histogram of 1 million simulated drawings of 1000 ballots: number of votes for Biden (x axis, 480 to 620) against simulated occurrences (y axis, 0 to 100,000), peaking near 550, with a red line at 501 that almost no draws fall below]({{ '/content/statistics/2020_election_series/00_calling_elections_early/img/draws-n1000.png' | relative_url }})
*Image by Author*

Now you can see in the overwhelming majority of the cases are above the necessary 501 blue marbles (see red) for the humans to get the right answer (Biden winning). In fact, these silly humans have less than 0.1% chance of getting the answer wrong now (or a 99.9% chance of getting it right). Ok we feel better now. Let the humans keep counting. We sit back with the rest of the world and turn on CNN/FOX news and let the drama unfold.

But wait, we’re not God (at least I’m not… I do hold my readers in high esteem though). So while God may feel comfortable with the above exercise, we can’t draw 1000 marbles a million times just to see how accurate our 1000 marble sample is. That would mean we’d have drawn a billion marbles just to say something about how confident we can be with our 1000 marbles! At that rate, we should just give up and count them all… right?

## Step 3: Bayesian Inference to the Rescue

As noted above, the question we’d like to answer is: what is the composition of the marbles in the bag? In other words, what percentage/proportion of the marbles are blue and what percentage/proportion are red?

Since Biden wins Illinois, let’s call the proportion of blue marbles “*p*” which allows us to say that if *p*>50% (also written as *p* > 0.5), then Biden wins. We’ve already established that we’re going to use a sample of *n* marbles to estimate this *p*. Our guess will be whatever the proportion of blue marbles we observe in our drawing (naturally). Since this guess is not necessarily the true value *p* inside the bag, let’s call it something else that’s similar but not the same. In stats we give *p* a cute little hat like this, *p^* to say: “this is not actually *p* but it’s our best guess based on some data.” Ok so to recap:

![Recap panel. Variables: p is the actual proportion of blue marbles in the bag (unknown); p-hat is the observed proportion of blue in a sample; n is the number of marbles drawn. Goal: determine the values p could be (if p is over 50% Biden wins). Constraints: use as few marbles as possible, and don't be wrong. Example: drawing n = 20 marbles gives 11 blue, so p-hat = 11/20 = 0.55]({{ '/content/statistics/2020_election_series/00_calling_elections_early/img/p-hat-recap.png' | relative_url }})
*Image by Author*

If only there was a way to say, I’m 99.99% confident that *p* is between two numbers. Then we could assess the uncertainty in our guess and cover our butts if we’re wrong.

I’m glad you asked because that is exactly what we invented confidence intervals for. They give us a way to take some observed data and use it to infer something about the world that produced that data. They tell us how “confident” we are the number is within a range (“interval”).

In our case, we want to know a range that we believe the marble bag’s proportion of blue marbles *p* will fall into (remember if we know *p* we know who won). So how do we do this? Well, that’s where statistical inference comes in. In order to be accessible, I plan to be brief about this and then we’ll jump back.

> {deep inhaling}

It turns out that the marble drawing situation is called a hypergeometric process. For those of you who don’t care what that is, just know that the important part is that it has a name which means that someone smart figured out what to do with it. In fact, that was how I simulated all the plots so far (python will just do it for you if you tell it the name of the distribution). Going deeper it turns out that when the number of marbles in the bag increases it approaches a different (easier to work with) situation called a binomial process. The only reason I bring any of this up is that the Binomial process has one important parameter and it’s called, you guessed it *p* which we can easily approximate a confidence interval for. I don’t plan on going into the approach that approximates the confidence interval on *p* but I’ll say that if you’re interested look up some of these terms: binomial distribution, confidence interval, Bayesian inference, conjugate prior. (This feels like a cop-out so I might write another blog just about this, stay tuned.)

> {big exhale}

## Step 4: Be Less Wrong and More Right

For the rest of us, let’s just look at pictures shall we? Let’s say that we were those humans from before that had drawn 49/100 blue balls from a bag that contains only God knows how many blue balls (again, *p* = proportion blue balls). So our *p*^ estimated from this is… you guessed it 0.49 (that’s how statisticians write 49%). Given that n=100, what can we say about *p*? Well, using the aforementioned, not to be mentioned again, Bayesian inference approach, we can generate a guess as to what values *p* (of the bag) could be after selecting 49/100 blue marbles (*n*=100). And of course, this is visualized as a probability distribution.

![Probability density of p for n = 100 (x axis p from 0.3 to 0.7, y axis density 0 to 8): a wide bell centered at 0.49 with a red line at 0.5. Caption: given 49/100 blue balls, p follows this distribution; if p is right of the red line Biden wins; right now both outcomes seem probable]({{ '/content/statistics/2020_election_series/00_calling_elections_early/img/posterior-n100.png' | relative_url }})
*Image by Author*

The red line is at the decision threshold where if *p* is to the left — Trump wins and if it’s to the right — Biden wins. We see that there is a decent probability that *p* could be anywhere from 0.35 to 0.65. Thus, due to the large “spread” in possible values for *p*, we still don’t know who will win. Of course, the majority of the probability is centered around *p* being 0.49 (which we know to be wrong due to an unlucky draw).

So let’s keep drawing and increase n = 1000. Now the results probably reflect something more realistic like, say, 541 blue balls (i.e. *p^* ~ 0.541) which is closer to bag’s true proportion of blue balls (*p* = 0.55). The purple lines I’ve drawn on the following plots show the boundaries which hold 99.99% of the probability between them. Since we have a 99.99% confidence that *p* is between these two lines, any value outside those bounds represents an unimaginably, unlikely event. When we do this, the spread of the distribution greatly decreases (i.e. the distribution has gotten thinner). This means that even though we haven’t counted all the samples, we have a very narrow window with which to guess *p* and none of them spell victory for Trump.

![Probability density of p for n = 1000 (x axis p from 0.30 to 0.70, y axis density 0 to 25): a narrower peak at about 0.55, a red line at 0.5 and purple lines at about 0.49 and 0.61 bounding 99.99% of the area, with an arrow marking a small window for Trump to win]({{ '/content/statistics/2020_election_series/00_calling_elections_early/img/posterior-n1000.png' | relative_url }})
*Image by Author*

If we increased *n* again, now to 10,000 marbles counted, we can see that the spread continues to shrink to almost nothing. In fact, it shrinks so much that we see that the probability that *p* is less than 0.5 (Trump winning) is essentially non-existent. So by the time we get to this point in the counting process, we are already 99.99% confident that *p* is between 0.53 and 0.57. In other words, even before counting 10,000 marbles, we knew that Biden would win.

![Probability density of p for n = 10,000 (x axis p from 0.30 to 0.70, y axis density 0 to 80): a sharp spike at 0.55 between purple lines at about 0.53 and 0.57, well right of the red line at 0.5, with an arrow noting essentially zero chance for Trump to win the state]({{ '/content/statistics/2020_election_series/00_calling_elections_early/img/posterior-n10000.png' | relative_url }})
*Image by Author*

But… that doesn’t seem like that many votes? And… [what about Virginia]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %})?

There were two assumptions that I made (and kind of hid) from you in the creation of this fake marble-selecting world which definitely do not hold in real life. These being:

> 1. The marbles were well mixed (so as to allow equal opportunity for any to be selected)
> 2. There is only one bag

But the main takeaway remains: in the case of a well mixed bag of marbles, you don’t need to select that many marbles in order to determine what the composition of the rest of the bag is. I find that fascinating and hard to believe sometimes.

## Further Reading

If this leaves you feeling disappointed in how long it takes swing states to be called or whether or not your vote matters… I wrote a few more articles using the following states as case studies:

- [Virginia]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %}) being called for Biden even though he was losing
- Could [Texas]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/03_texas/2020-11-09-how-swing-able-is-texas-anyways %}) really swing?
- [Pennsylvania]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/02_swing_states/2020-11-09-what-took-so-long-in-the-swing-states %}) mail-in ballots
