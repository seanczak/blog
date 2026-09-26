---
layout: post
title: "What Took So Long in the Swing States?"
date: 2020-11-09 17:24:26 -0800
description: "Be nice to statisticians, they’re doing their best"
tags: [statistics]
---

![A small child pressing their hands to a window, reflected in the glass]({{ '/content/statistics/2020_election_series/03_swing_states/img/child-at-window.jpg' | relative_url }})
*Image Credit: [Johnny Cohen](https://unsplash.com/photos/sxzuj6npVGU)*

You might’ve noticed a peculiar trend last week as the election results came in. In fact, if you were like me, you not only noticed it… you were obsessively hitting refresh on your browser and not trusting the “Updated at {time}” message above the results page.

What I’m speaking of is that on Tuesday night, it seemed like an all-but-certainty that Donald Trump was going to be our President for 4 more years. He was winning in essentially all the battleground states and was otherwise tied in the states that had already been called. But for some reason, the news stations were not proclaiming victory for either side. Well, why not?

We see that [many states only required a few votes]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}) to be able to make a solid guess. Ok fine… some states break the mold a bit and follow a different trend. However, even in a state like [Virginia]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %}), which flipped sometime late Tuesday night, the statisticians were able to correctly guess the winner even when Biden was trailing by 20%.

So why couldn’t we apply the same magic in the case of Michigan or Pennsylvania? Why did we have to wait for 4 days before we knew who won?!

## Bring out the Marbles

If you’ve read any of the other posts I’ve written about this election, you’ll be quite familiar with my obsession with marbles to explain stats. If not, let’s quickly revisit them.

We started by positing that, instead of going to various polling offices, mail boxes, etc, the people cast their votes by bringing a colored marble to their state’s capital on election day. This made for a [nice first approximation]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}) of how many votes would be required to “call” a state.

But then we realized that the media was reporting votes as they came in and some counties counted faster than others. This gave a very biased sample of votes which, in Virginia, gave the early impression that Trump was going to have a landslide victory (when in fact Biden won that state).

Well, we learned we could save our beloved bag-o-marbles model by dividing the big bag of marbles (the state’s total votes) into smaller bags representing each county. This worked as a nice “[second order approximation]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %})” to help explain why states could be called so early. But what we’re seeing in this election is that not only does the county matter but also how you chose to vote (among other factors).

## Oh, Confound it!

In a world where one candidate might tell his supporters to avoid voting by mail, you might expect to see a huge difference between compositions of the “voted by mail” group and the “voted on election day” group.

In addition, we might assume that different ethnic groups may play a key role in some counties to swing a state based on how many vote that year.

In fact, you could keep going with this: gender, age groups, first-time voters, etc. Selecting a larger proportion of any of these voters could unnaturally bias your sample and give you an unrealistic view of your population (and thus the entire election).

These are what we call “confounding variables” which I find to be a hilariously appropriate name for the things that confuse and keep statisticians up at night. The role they play is to upset our assumption that the marble bag was “well-mixed” before we started sampling. Without accounting for them, one really doesn’t have a clue what is going on.

## The Russian Dolls of the Marble World

So what does this mean? Well, first off, it means that there definitely is not a bunch of people waiting for a certain number of votes to come in before they can call the state (at the time of this writing Georgia still hadn’t been called despite being at 99%).

Instead, it means that there is a team of people who try to figure out what important trends to look out for in each state, each county, each demographic.

For example, one exhaustive way to account for confounding variables is to go back to the bags within bags approach we used for the counties. Think about it like a set of Russian dolls. Within a state, you choose to separate counties because you imagine people vote differently based on where they live. Then, within the counties you assume that the way someone votes makes a difference in who they vote for. And then you can keep going with ethnicities within each of those sub-groups and on and on. Once you have a sense for how each of these tinier subgroups react, you can then make a prediction on the whole state’s final tally.

![Nested bags of red and blue votes: a Virginia bag split into county bags, one county split into early, mail-in and day-of voting bags, and one of those split into bags by ethnicity. Caption: think Russian dolls; split the state into counties, each county into bags by voting method, then by ethnicity if that matters, and on and on]({{ '/content/statistics/2020_election_series/03_swing_states/img/nested-bags.png' | relative_url }})
*Image by Author*

## All models are wrong, some are useful

Allow me to reiterate that I’m not privy to their process. I’m just a guy that works with statistics a bunch. The work we did for [Illinois]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}) and [Virginia]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %}) assumed that we had representative samples and that we knew the total number of voters (in each county and the state). In that way, we were able to approximate the worst and best case scenarios for each candidate and make a guess based on those cases. Unfortunately, none of those assumptions are ever valid. However, they worked in these other cases because the margin of error was wide enough that such uncertainty is absorbed (i.e. one candidate wins by over 5% in that state).

> Swing states are a different story…

A swing state designates a nearly split population which results in such tight races that can sometimes be decided by less than a percent.

## The Two Bag Problem (size matters)

We sometimes encounter situations for which there is no precedent and which are, thus, extremely hard to predict. In the case of this election, the massive numbers of mail-in ballots is something we’ve never experienced and saw that it’s really hard to predict exactly how many will come in (even a week later!).

This was made clear when Pennsylvania counted 100,000 more votes and decreased their reporting percentage from 89% to 88% (it went backwards!). What’s more is that some states allow for ballots to count even if they come in weeks late as long as they have been post-marked by a certain date. With this situation, it’s hard to know how big the bag of “mail in ballots” is even if you can already infer that ~70% of them are going to be in favor of a single candidate.

Think about it like this, if a state divided its ballots into those that voted in person and those who mailed in, we’d end up with two bags of votes (I guess we’re done with “marbles”). What appeared to happen this year was that they counted the votes from the “in person” bag first and, in general, had a pretty good sense of how big the bag was. However, for the second bag, even though we counted enough votes to get a sense for the contents (say it was 65% Biden), we may not have known how big the bag was.

## Hypothetical Example

If the “in person” bag was 65% Trump and contained a million votes, then Trump would have received 300,000 more votes in the first wave of counting and we probably wouldn’t need to finish counting [to know this]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}).

Now, the “mail in” bag gives us trouble not because we can’t determine the proportion of votes that are for Biden (that could be known early to be, say, 65%), but because we have no idea how big this bag is. Every time I turned on the news they were “finding” more ballots at the post office or polling sites. It really showed that we were not ready for something like this and thus the wheels weren’t as well oiled as they were for processing “in person” votes.

So we had no idea if there were enough ballots in this subset to make up those 300k votes that Biden was behind. So we just had to keep counting until we were more confident in the results.

## Consequences and Risk Assessment

I want to stress that I wasn’t there so I actually don’t know what truly caused the issues for each state. But I was seeing the same news coverage as all of you and this is how I think about the problem and felt like it might shed some light.

What it really comes down to is risk tolerance for uncertainty with the models I’ve presented throughout this series. It makes it difficult to confidently declare a state. The inherent flaws of a model that worked so well in Virginia are shown for what they really are in Georgia.

> The statistician… has no clothes.

Compound that with the external pressure to make the “right call” (as exemplified by the inquisition put to this [Fox News analyst](https://www.youtube.com/watch?v=OJDKS3d2RHk)) and you get the situation that we experienced last week.

To me, this is enough to convince me that each vote truly does count, but I imagine there may still be some doubts especially in the light of seeing how quickly a state can be called. It’s outside the scope of this article but I argue that [statistically speaking, your vote definitely counted]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/02_texas/2020-11-09-how-swing-able-is-texas-anyways %}).

Check out my other case studies on the election:

- [Illinois]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/00_calling_elections_early/2020-11-09-calling-elections-early-fake-news-or-statistics %}) (how many votes needed to call an election)
- [Virginia]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/01_virginia/2020-11-06-what-in-the-world-happened-in-virginia-tuesday-night %}) (how did statisticians know Biden wins even while he was losing by 20%)
- [Texas]({{ site.baseurl }}{% post_url content/statistics/2020_election_series/02_texas/2020-11-09-how-swing-able-is-texas-anyways %}) (how swing-able is it really?)
