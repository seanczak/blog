---
layout: post
title: "How Swing-able is Texas Anyways?"
date: 2020-11-09 17:20:16 -0800
description: "Statistically speaking, your vote matters"
tags: [statistics]
---

After much [statistical reflection]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %}) of this past election, I’ve grappled with the concept of “does my vote actually matter” and I imagine I’m not alone.

![A weathered Texas flag flying from a pole against a blue sky]({{ '/content/statistics/2020_election_series/03_texas/img/texas-flag.jpg' | relative_url }})
*Image Credit: Adam Thomas [1]*

I know I’m not the only one who was surprised to see Texas included as a “swing state” in Google’s macro. How could that be? Some sort of mistake? I went to school in Texas and let me tell you, that place is a red state. It at least felt red…

However, we watched Georgia swing blue this year and it really does beg the question: which others could swing?

Let’s take Texas for example and I hope to demonstrate why, in fact, your vote really does matter and you should take it seriously (regardless of your political leaning).

## What is an Election Anyways?

When I wrote about [Virginia]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %}) and [Pennsylvania]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/02_swing_states/2020-11-09-what-took-so-long-in-the-swing-states %}), I made the point that the reports from the news were resulting from biased samples. Now, when I say “biased,” I don’t mean they were wrong or intentionally misleading. I mean that because of the manner that the results were collected (e.g. “in person” ballots were naturally counted faster), it gave an incomplete picture of the story that the underlying population (all the ballots combined) was telling.

Furthermore, since I started writing this little mini-series, I’ve been thinking of the [votes cast in each state]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}) as the “target” of my statistical analysis. Statistically speaking, I was treating “all the ballots” as “the population” which we could “sample” from to make inferences about the final results.

This is all well and mathematically sound… except when you bring up that the votes themselves are actually a biased sample of what the people of that state represent.

## Ballot Counting can be a Biased Sampling Technique

The way a democracy works is that we don’t assume we know what the will of the people is. We ask them. And the majority opinion is what we go with (kind of). So we have this whole process set up where you can go vote and tell the government what laws should be passed and which officials should be in office. But here’s the thing:

> NOT EVERYONE VOTES!!!

Voting is a biased sampling process because not everyone participates. We can’t assume that, since 75% of Democrats choose not to vote, then exactly 75% of Republicans do the same. Sometimes more of one group shows up to the polls. So what effect can this have on an election (and democracy)?

## The Texas Swing?

During the writing of this article, Texas had counted 98% of its votes and Donald Trump had won the state by 600,000 votes (52% to Biden’s 46%). But I was curious, could people’s perception of what they imagined to be an inevitable result have actually manifested this result? What I mean is: did assuming that the state would go red play a role in its eventual “red-ness” after counting votes in 2020?

> Was there a universe that existed where Texas actually swung… Democrat? Let’s take a look…

## Split by County

Let’s do a similar analysis we did with [Virginia]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %}) where we split the state by county to get a sense of how Texas is spatially distributed (i.e. [how did each county vote?](https://www.politico.com/2020-election/results/texas/)). First off, we see that, again, about 50% of the votes come from the largest 5 counties.

![Bar chart of votes (y axis, 0 to about 900,000) for Biden and Trump in Texas's 30 largest counties; Harris County leads with about 910,000 for Biden to 700,000 for Trump, followed by Dallas, Tarrant, Bexar and Travis]({{ '/content/statistics/2020_election_series/03_texas/img/county-votes.png' | relative_url }})
*Image by Author*

In Virginia’s case, this type of distribution ensured Biden’s victory (even though he was behind by 20% at one point). However, we can see that the largest county, Harris, is not nearly as imbalanced (in favor of Biden) as Fairfax County was for Virginia. I wonder…

> Did Biden supporters not show up in these big cities in the same numbers as they did in Virginia because they figured it was a lost cause? Could Texas be a “blue state” actually?

## Could Texas be a Blue State?

As we saw with the [Illinois]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}) example, we really don’t need more than ~10k votes to get a sense for how the underlying population behaves. Let’s just assume that the way people voted in these counties reflects the underlying population’s sentiment towards each candidate for that county (i.e. Harris County leans 55% blue). Then, let’s take the actual population and assume that 75% of people are of voting age ([a pretty good guess in 2016](https://www.pewresearch.org/fact-tank/2020/11/03/in-past-elections-u-s-trailed-most-developed-countries-in-voter-turnout/)).

We can use these two pieces of information to extrapolate what the results would be if EVERYONE of voting age had shown up to the polls. Could the larger, “blue” city populations do what they did in Virginia?

Unfortunately, the results are not as dramatic as I was hoping for. Biden goes from 46% to 47% and Trump drops from 52% to 51%. **Texas really is a red state**. (That is — if the proportions demonstrated by this election are representative — which would be hard to know from this data).

But I’m not satisfied. I wanted to know **how swing-able Texas was**… not just whether it was red or blue. First, let’s talk about an assumption I made earlier.

## Record Turnouts?

We’re all [celebrating a 66-ish% voter turnout](https://www.texastribune.org/2020/11/04/texas-voter-turnout-democrats/) this election because it’s smashing records that were decades old. But, that still means that 33% of people didn’t vote. And actually, that’s 33% of people who were registered to vote and then chose not to vote.

How many people are eligible to vote and just not registered? Since I had [population data](https://www.texas-demographics.com/counties_by_population), I chose to look at the numbers through that lens rather than the “registered voters” lens. It turns out that, if you assume [75% of people are voting age](https://www.pewresearch.org/fact-tank/2020/11/03/in-past-elections-u-s-trailed-most-developed-countries-in-voter-turnout/), the number drops to 51% voter turnout. Now, of course, some of that discrepancy is accounted for by immigrants or other non-eligible-to-vote adults… but I just wanted to point out that the number 66% is already inflated and, in general, unimpressive to be “record breaking.”

## Could Texas Democrats Surprise Us All?

Ok back to Texas… We already pseudo-established (I realize we’re doing a lot of hand-waving here) that Texas is a red state. But remember, voting is a biased sampling mechanism.

> Does a world exist where more Democrats show up at the polls?

We recall that the deficit that the blues needed to make up was 600,000. What percentage of the Texas population would that be? Turns out only about 3%.

Ok, but we already established that most Texans are Republican. So what percentage MORE of the Democrats would have to show up. Well, from the numbers from the toy model above, if 6.3% more democrats showed up to vote this year, Texas would’ve swung blue. It would’ve meant that 57% turnout among Texas Democrats could have surprised the 53% turnout among Texas Republicans (assuming their turnout doesn’t change) at the polls and Texas would have artificially given all 38 of its electoral college votes to Biden. We wouldn’t even be talking about [Pennsylvania]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/02_swing_states/2020-11-09-what-took-so-long-in-the-swing-states %}) right now…

## Your Vote Matters

Ok so this has been a toy example but I feel like it makes the point: there is a ton of room for growth in voter turnout and if one group figures it out before the other, they could really swing policy making even if they aren’t the majority.

Sure if one person doesn’t show up to vote, it might only slightly change the proportion of votes that the final tally reveals. But again, it still biases our sample if it happens in a way that is unbalanced.

Consider the concept of group-thinking. **Having a cavalier or fatalistic attitude could lead to those around you having the same attitude and, in turn, propagating it further to their friends.** If people can be assumed to vote similarly to their friends or at least those close by, then a huge group of your network not voting could lead to a biased sample on election day. Imagine if something like that had happened with Democrats in Fairfax County, Virginia? It could’ve unnaturally changed a predictable, landslide victory for Biden into a close-count as a result of biased sampling. The same (well, the opposite really) could be said about Texas.

The best way to avoid this is to just make a habit of voting. And make sure you let your friends and family know how important it is.

> It’s your right. And it’s a big deal.

Check out my other case studies on the election:

- [Illinois]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}) (how many votes needed to call an election)
- [Virginia]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %}) (how did statisticians know Biden wins even while he was losing by 20%)
- [Pennsylvania]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/02_swing_states/2020-11-09-what-took-so-long-in-the-swing-states %}) (swing state drama statistical interpretation)

Images

[1] A. Thomas. <https://unsplash.com/photos/lobgrHEL1GU>
