# all

- Feel free to just drop this into your session you're building the skills with by
- picture at top like medium
- All the AI ones should start with A staleness note something like I wrote this in Fall of 2026. So if you're reading this after the singularity has happened, forgive us, we didn't know yet
- I could have my coding style guides. Just read my blog and then write an update, say these were what they were before. We can even restructure completely and start over if it makes sense

# coding

## principles

- “Bloviating and…” gif for principles
- hand hold the components of the system design - THEN turn the agent loose
- Maybe title it? Software principles are still stable and then that first section can just be like a why I think so section, and I could remove the parts except for in the prose, and then put the list of them at the top and bottom of the other docs
-  - it's all about scaling complexity, maintainability and both of those are faster with cleaner code (I also personally just find a sense of enjoyment with it - just feels good to be able to say yes to really complex stuff and watch it be really easy)

- First starts with things are moving fast (slower changing principles are focus), then differentiation is still using principles, then why (maintainability, scalable complexity, velocity at those two things)

## dry

- Dry has the dynamic config (as the solution to string handlings and variable hard encoding - two things I've seen )

## organization (srp and soc)

- Separate srp and soc (generalization flow) - Modularity (lego blocks - think pandas builds on numpy and integrates with scipy) is at function level and repo organization level - srp goes first and solves walls of pandas but it could still be a mess

- Srp and generalization - what is principle make them as general and reusable as possible within reason (with inputs and output) - modular
- Srp - maybe start with an example (it puts everything in one file - none of the components can be reused so they have to be coded again or oddly called in where not needed)
- Soc - example is breaking up class that calls a loop on a bunch of instances of a subclass and that subclass simply holds all the logic that gets operated on a subclass. Whereas the governing one kind of operates on the like edge bucket defines how it's consumed and called and what it consumes and calls
- Srp - pandas is the least readable language, but it's what we got, rapping chunks of four or five lines into English statements is very helpful for code
- Soc - sql files go in their own files (schemas, sql to query might also be separated, feature store vs output as well - define the lines)



## yagni + naming


- Yagni - don't add functionality you don't need AND delete
- Maybe yagni and naming are in traversible and readable post? (“More on ….”) - answers how the code could STILL be unreadable (should read like a logical novel the whole way through )
- for naming conventions too (kind of a system one) -- example of the dev tagging on the job naming in dbx which was different by env - actually a convention that it wasn't clear what it was serving us but it was definitely making matching behavior challenging to predict and design around -- like being told to hop on one foot while cooking (are my hands still fine yes but now I have to deal with - how not to slip, how to minimize my movements, when do I switch feet, how do I go about the process of switching feet to stay in compliance, etc)

## documentation as code artifacts
- index
- when you have your design components nicely set up and now you're ready to turn th agent loose on them - making sure that it follows the standards you just set up and took time to do as it assembles the pieces together

## implementation stage (ai implement)
- see system ai below

- hand hold the components of the system design - THEN turn the agent loose
- What can I trust the ai to do - small well defined pieces - even some high level planning
- Hard to automate the whole thing because we are the ones that need to drive the intention (in ai research they're having this issue too, with defining appropriate objectives at each stage to push it to continue to do better and better, it's the same for our company and our code base and our conventions that we're setting, someone has to decide what goes into the Constitution or style guides or workflow organization, even if we aren't even the ones writing those documents) - 
- Ai code implement - principles and process (thats why we just spent so much time on the rest of it)
- Waterfall
- Agentic coding - giving feedback loop so it can check its own work - its good at trying a million things but not good at predicting which will be best


# exploration
## pricing model
- Pricing - add /context, agent view in section for how to monitor, also that timer tells you

## injecting context (skills, agents)
- Injecting system context - Claude.md com is that it only works in one repo and you can't choose when to inject it (also it doesn't get followed as closely if you inject closer to the task at hand)

- Parameterize it - so if the start up tax is this much and the task itself takes this long (say it's the same for each) so we save that many cached tokens on main thread but spend the tax in input, then based on the cache price of the model and input price of sub model, how long (turns of that extra cache charge) does it take to recoup as a function of task length (actually worse than this on both ends bc inline one has to pay it's cache tax for each turn and the other has to pay in the communication / skill reading as well)  - I'm not sure you'll ever recoup for sub agent stuff even if I was like ok run this whole experiment and give me results - it would be so close if not more expensive than just reading the raw file once (rather than with each agent) - only small ones make sense and it's simply to keep the context rot down - no free lunch, this doesn't like hyper speed us - agents are still only good at short shit and it would be expensive to string them together like this but at least I dont have to think as much
- Add what 10 figures turns into - 60ish k 
- Give dist of number of turns


## tracking file

- Tracking - the rise of the markdown file (it's your turn) - both human and agent readable and now we have a layer that can utilize all the functionality that nobody ever knew existed but is actually really clean and amazing (linking within document, tocs, anything else?) - also bash and git - secret sauce of cc harness
- Exploration - why git - local doesn't pay the remote tax that gdrive or confluence does
- Tracking doc - new session for each distinct thing this way, you can chunk them smaller and smaller (you can actually get to a point where you can do it mid task if you realize it's gone cold you it's getting big or squirrelly) - another benefit is multiple windows One for riding and analyzing the last plot and the other one for pulling data and making the plot for the next and they just hand off and write to each other while I switch between (it's not even context switching for the human. It's simply keeping the thread going instead of waiting, which was another problem before I started doing this) - maybe even one more window for asking one off questions in a chain (like for code, this is the second window and it helps write the plan)

## levels of refinement
- Maybe levels of refinement one is “context engineering” - all of this is what it was

## newbies
- Do one for newbies on exploratory that includes get basics and how to just let Claude do it after you know what is happening, also a note for coding to every once in a while have Claude check it's set up to make sure it's following best practices (take my docs) - kind of writing for you guys anyways - also show how to install vs code and stuff (even give Claude this post and say my picture doesn't look like his)

# system design

- System intro - just inherited a project that I completely redesigned and had to defend a lot of those decisions - that is where most of these posts came from - human decisions leading into unchecked ai additions onto suboptimal foundation was what I was detangling
- Versioning for ci/cd - keeps it from being a puzzle every ticket and big project design of how to integrate it (tied together our qc and everything)

- see above for yagni
- hand hold the components of the system design - THEN turn the agent loose
- System design - using less dependencies (soemthing about going down to the core and building from there - thats why cc is winning the ai coding agent game - beastly at bash/git), code should already be written so it can port between design decisions easily (generalization flow, only last layer should get hit), something about gha, versioning data with code (not related to gh releases but can be)
- System - refactor in stages (make the bare bones of the spine you're building on and then slowly start transitioning components to the new spine)

## crt (choosing right tool - maybe analog to srp), 
- Crt - if you don't know if you'll need the bells and whistles that come with a tool don't bend your service code to accommodate this over engineered solution - just choose the simplest tool for the job unless you know you'll need the rest
- System - crt - level on abstraction stack is a decision at every stage (processing vs training on sagemaker - either write more code or deal with rigidly defined api – eg do we need more security or flexibility over our outputs or schemas?) - tradeoffs to choosing something off the shelf vs stepping down a level and building up a bit (which could actually end up being less code in some cases)
    - System - obviously the other side of the argument is having to write your own code and test it and manage it has its own cost, so it's a balance
- System case study - using lists of lists instead of pandas (even though an agent could work with both happily to conform) - pandas might be messy but it's a nice balance of component and abstraction (can do enough with it but it doesn't go so deep that it's painful) - probably why df manipulation is messy looking (at least it's not element level - c code level) - allows for us to build on top of it like scipy and SK learn 
- System - using third party for their first class purposes (dbx, mlflow, Kafka as pubsub) - always a trade off between complexity (ie the drawback of using that thing) and the value it adds (mlflow for xgboost replaces an optuna/ for loop and jupyter notebooks for hosted complexity and rigid ui… feels like this only pays for itself with deep learning where managing all of it yourself becomes a big enough lift) - I’m probably a little farther on the “go to the root” end of the spectrum where I’d prefer the s3 type of solution that can be used easily, quickly spun up and hooked up to athena if I need over a delta table where I’m a little more limited
- System - level of abstraction choice - surely there will be agentic plugins for mlflow and dbx soon that actually work but i still feel like it will be a decision to make - you can really get tied in a knot if you just use technology to use it an a lot of times these ones aren’t much better than just designing it yourself the way you and your group work best with whatever constraints you have (and code is super cheap now, organization is key and expensive)
-System - level of abstraction choice - unless I know absolutely up on how I'm going to use the service and all of its primary features, it actually can be easier to just leave it out because sometimes something like ml flow is really easy to just add in later in the places that I need it


## DC (designing components - analog to soc)
- DC - components are how we learn. Generalizability as a species 2 through research
- DC - edges also include like how it's consumed within another application. Say the governing one
- DC - do one thing well - linux
- System - designing components (edges) well and letting services use them as they will (Microsoft sucks at this Google is amazing - Google docs vs word)


## define your edges / contracts

- System - define your edges (standardized system if possible) - this also goes into crt if one service doesn't integrate well with another - boundaries should be well defined (think all sql servers use the same ish sql) - also example of why aws is slightly better than gcp (maybe that's changed but it simply integrates better with its components and that could be worth the cost) - linux defines the boundary really well (same with git) - the glue code is super important - look at Nvidia - think garden hose and nozzle and spigot 

## agentic system design
- probably the same as ai implement above in the code section

- Nicks different models  - codex writes code, opus (to talk to writing the spec and the orchestrator), sonnet is the tester (reads pr and tests it)
- System - script and automate as much as possible - the smallest element of judgement is run as ethrough the LLM 
    - System - code that distills into a schema of outputs (and if those can keep being distilled, do it again), then have a layer of judgement that looks at outputs and make a decision or surface patterns (but it's a balance of is the scripting becoming too complex (eg with many if else conditions and unknown expansion in that dimension - maybe just let the LLM call) with scripts and being nondeterministic with LLM)
- System - LLM is also good at connecting different pueces of the output - like if the etl is off in this way and the train eval is like this (look through supporting output when eval is off) - also knows code so it's like oh ok this is why

- Matt on qc system
    - Runs registry table, script that can diff two runs - things to highlight (for metrics), LLM knows what to do based on the different types of diff events - writes a report
    - Diff-ing to model runs is primitive - if you run many models you can get a diff between each metric for each pair (df for each) - he has a skill that looks at that data and tries to find patterns
    - Llm- script and automate as much as possible - the smallest element of judgement is run through the LLM
    - Llm - Triage warnings and watch for them
    - LLM - Results of the test go to the ticket



# blog itself

- Nicks wow docs (from skill/sub agent, and mcp stuff)


about me
- About me - trying to write about slower changing principles - things like git are stable, llms are a new component to our stack and so we move up (maybe start The other series with that too. Things are changing fast but some things are stable, and while agi is still not here. I imagine the series will still be helpful
- About me - honestly just trying to wrap my mind around some of this, definition of essay, also writing to new folks (intention)


# other topics 
AI
- https://petergpt.github.io/bullshit-benchmark/viewer/index.v2.html
    - Nick's BS metric


- Wide distribution of realistic prompts (for distillation)
    - My help with the convention is actually to shrink the distribution into the agent's next turn, in a way to it's an attempt to have some element of deterministic behavior from it
    - 25min - Also distillation naively can go wrong if your training environment is focused solely on difficulty axis rather than (matching the teacher on the narrow benchmaxing distribution) vs the realism axis (be good in a realistic coding setting where there's a lot of back and forth with human and multiple objectives)

ML
- isolation foreat(do you even train it before doing inference every time, why unsupervised can be actually better 










