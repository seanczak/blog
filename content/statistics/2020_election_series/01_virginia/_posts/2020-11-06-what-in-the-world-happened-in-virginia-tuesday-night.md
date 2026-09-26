---
layout: post
title: "What in the World Happened in Virginia Tuesday Night?!"
date: 2020-11-06 16:53:41 -0800
description: "Statistics breaks when your sample is biased"
tags: [statistics]
---

![US map of 2020 election results as shown by Google on election night: states shaded light or dark red and blue, with Virginia dark blue]({{ '/content/statistics/2020_election_series/01_virginia/img/google-results-map.png' | relative_url }})
*Source: Google Macro on 11/3/2020 screenshot by author. [1]*

Like most American families, Tuesday night my mom and I closed up work around 5pm, heated up some leftovers, and huddled around a TV to commence what would turn into a long night of bingeing/“playing along at home” with the election results. Most of our analytics fix was generously provided for by CNN (oop, just called ourselves out with that one). But we’re not your ordinary group of sheep-le over here. No no, we’re some of the more savvy consumers of click-bait information. We use the Google too!! And what we (and many others probably) noticed early on, was that there was a discrepancy between Google’s little macro (powered by AP) and CNN’s classic US map dashboard (although it definitely is getting fancier). The numbers being reported were the same but a difference in information delivery paradigm caused an interesting bit of confusion in our household. Allow me to explain…

If a state had more Republican votes at the time, CNN would shade it red (or blue for the opposing case) which gave the impression that the candidate had won or at least was “winning” the state. Fine, makes sense. However, Google took it one step further. They provided two “grades” of shading! A light color meant the candidate was leading the popular vote of that state whereas a darker one meant that the [candidate had “won” the state]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}). Tip of the hat for the addition of this clever, intuitive visualization feature.

So what’s the problem? Shouldn’t the candidate that is winning the state’s popular vote be the one whom the analytics-gods inevitably deem as the “winner” of that state? Not necessarily. Take Virginia for example. Sometime around 8:30pm EST Biden was losing by ~20%. As the CNN anchors were stewing about how Biden needed to make some sort of heroic effort to save this “blue” state from flipping (as if that’s how election night worked), Google’s map filled in dark blue signifying that not only was Biden winning Virginia… he’d won!! Well now as you can imagine this caused a bit of confusion around here and I decided to investigate.

## Setting the scene

At around 8:30pm EST, state officials had counted 33% of votes and Biden was losing by 20%. However, the Google macro had shaded this state dark blue to signify an unquestionable Biden victory. Ok, what the heck? My mom felt that way and it wasn’t helped by the television pundits who kept the game-show illusion going with the rhetoric that “hopefully Biden pulls back in Virginia.” The statisticians knew something that we as viewers were not being told.

## Marbles again?

Mathematical modeling is all about simplifying the real world. [In another post]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}), we showed how quickly you can call an election if you simplify the model into hypergeometric equivalent (a bag of marbles). We pretended that instead of going to various polling offices, mail boxes, etc, the people cast their votes by bringing a marble of a specific color (red or blue) to one big-ol marble bag located in the state’s capital on election day. We showed that if the bag was well mixed, we would only need to draw a few thousand to make a really good guess as to what the composition of the bag was.

However, you can see how this is unrealistic because, in real life, there is more than one bag of marbles. In fact, there are 133 counties and over 2500 precincts in Virginia. If we were to use the one bag model, we’d make the egregious error of assuming that we could draw from any of these bags and make a general statement about the entire state.

Well why not? That’s how the information is displayed to us through the media? 33% of votes have been counted people! That’s well over our 10,000 marble threshold that we mathematically posited would be sufficient. Trump won Virginia folks…close the books!

So therein lies the real work of a professional statistician: choosing representative samples is hard.

## Marble Bags within Marble Bags…great

But let’s say that we needed to say SOMETHING even though we knew that our sample was biased. Well, what if instead of assuming a single bag of votes, we assumed that each county was a smaller bag within that bag. Yes, the state’s marble bag is actually a bag of county marble bags (the rabbit hole continues!).

![A Virginia bag of mixed red and blue marbles, regrouped by county into nine smaller bags inside one large bag. Caption: we can break up the bag and sort the votes by the county each came from; now instead of one bag to estimate p for, we have several]({{ '/content/statistics/2020_election_series/01_virginia/img/county-bags.png' | relative_url }})
*Image by Author*

But does this explain what happened Tuesday? Well, let’s look at the data. I took some numbers directly off the Virginia state’s official election reporting website sometime on 11/5 (votes should be in at that time). The final count at that time said that Biden had been awarded 53% of the counted votes. Recalling Tuesday night, CNN would’ve had us believing that this was some sort of heroic push but I think the statisticians would argue that it was inevitable. Let’s see.

## Asking the data

Ok, let’s start by doing a quick thought experiment to see if we can recreate the situation we saw at 8:30pm on Tues when Biden was losing by 20% but was declared the winner. Let’s pretend that 10,000 votes are counted from each county (i.e. ~1.5 million of Virginia’s ~4.5 million total votes). The following is a plot of 30 randomly selected counties in Virginia and how they might’ve looked after counting their first 10,000 votes. (I’ve put a box around Fairfax County because it becomes important later — stay tuned.)

![Bar chart of votes (y axis, 0 to 8,000) for Biden and Trump in 30 randomly selected Virginia counties and cities after each counts its first 10,000 votes; Trump leads in most, while Arlington County, Richmond City and the boxed Fairfax County lean heavily to Biden]({{ '/content/statistics/2020_election_series/01_virginia/img/county-first-10000.png' | relative_url }})
*Image by Author*

## Tale of two Virginias

If I add up the votes from all the counties, we can see that Trump would have a commanding lead over Biden at this early stage (shown on the left below). However, the statisticians look at the early estimate of the individual counties above and realize that Trump has already lost. How?

What they might’ve done is they take the votes that they’ve already counted and guess the proportion of Biden votes contained within the uncounted, future votes. In fact, if we think we know how many people will vote we can use Bayesian inference to infer a range of potential votes for each county ([by inferring a range on *p* like we did with Illinois]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %})). Then just repeat the process for each county and add up the totals for the low and high estimate cases (right figure). And with that, you can see that even the unimaginably worst case scenario for Biden (labeled “low” below), he still is well above the red “line to win” drawn at 50% of the votes.

![Two bar charts. What the public sees: early reported votes in Virginia (thousands of votes), Biden 43% and Trump 56%. What analysts see: estimated final votes in Virginia (millions of votes), Biden 53% in the low case and 57% in the high case, both above a red line at 50%. Estimates use 99.99% confidence intervals for each county]({{ '/content/statistics/2020_election_series/01_virginia/img/statewide-totals.png' | relative_url }})
*Image by Author*

Ok, for those of you who followed all the way up until now you might still be asking: how could this be? Well, let’s just look at the raw results from the 30 most populous counties and I feel like the answer should be obvious. Check out how many votes Biden picked up in Fairfax County. In fact, he won the top 12 most populous counties in Virginia (in some cases by a landslide).

![Bar chart of final votes (y axis, 0 to 400,000) for Biden and Trump in Virginia's 30 most populous counties; Fairfax County gives Biden about 400,000 votes to Trump's about 160,000]({{ '/content/statistics/2020_election_series/01_virginia/img/top-30-counties.png' | relative_url }})
*Image by Author*

Of course, votes aren’t actually counted at the same speed and my little model I presented here isn’t actually the numbers from Tuesday night (8:30pm). But… it shows that while the public is being fed one story about Trump leading by 20%, the statisticians have already realized he doesn’t have a prayer of winning Virginia.

Well, this is all very interesting, but [what about swing states]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/03_swing_states/2020-11-09-what-took-so-long-in-the-swing-states %})? And, this is not doing a whole lot to convince me whether or not [my vote counts]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/02_texas/2020-11-09-how-swing-able-is-texas-anyways %}). I’d argue that it does but this post is getting a bit long. I try to answer those questions in greater detail in other posts.

Check out my other case studies on the election:

- [Illinois]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}) (how many votes needed to call an election)
- [Pennsylvania]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/03_swing_states/2020-11-09-what-took-so-long-in-the-swing-states %}) (swing state drama statistical interpretation)
- [Texas]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/02_texas/2020-11-09-how-swing-able-is-texas-anyways %}) (how swing-able is it really?)

Images:

[1] Google, US election results (2020), <https://www.google.com/search?q=election+results>
