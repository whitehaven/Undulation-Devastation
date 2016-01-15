# Undulation-Devastation
An abstract life simulator written with pyglet. Cocos2d adds stuff that just doesn't matter to me. This idea is based on a menu background made by Jason Reinsvold from lostvectors.com, home of some of the most advanced flash games I've ever seen. Weirdly, I thought the background one of his coolest acheivements, even though it was hardly a main attraction.

After reading pyglet's docs and OpenGL's programming guide, I'm pretty convinced I can do it in a very light and adaptable way with pyglet. I've decided that because collisions are very important to the simulation, and it honestly seems like I'd just reimplement my own dumb version of what's already contained in the pymunk package, except that theirs would be in C, I'll just learn to bind pyglet and pymunk together. I'm okay letting the good pymunk folks help me out on this one.

The simulation proceeds as follows:
- Producers: passive organisms. They spontaneously grow in a simplistic way for now: a simple health counter. As time passes, their health goes up. When their health reaches a certain level, probably "100" or some maximum, they split in two, each organism steadily "growing." They will probably be depicted blue and will slowly wander the screen.
- Parasites: active organisms. They are constantly losing health in vacuum. If they come in contact with a Producer, however, they begin to consume it, gaining health and splitting. This damages the Producer and can result in its demise. They are canonically sickly green and fly across the screen, possibly under the influence of gravity. When they split, they launch their larvae into the air.
- Symbionts: active organisms. They are constantly losing health in a vacuum. If they come in contact with a Producer, they contribute to its health but lose their own. If they come in contact with a Parasite, the Symbiont consumes the Parasite's health and increases its own. It also launches larvae into the air at random angles (upward). They are canonically a light blue, like cartoon water.

The Producers in the lostvectors.com simulation change color from white to deep blue to signify health (death to maximum health), while the Parasites and Symbionts increase in radius or area. It is visually interesting, but I may make changes.

You're probably thinking that this doesn't look like anything you've seen in real life. Obviously. I think this probably models jellyfish or some kind of sea thing more than land animals.

It has probably not escaped notice that because of the randomness in the air-firing, eventually the Parasites and Symbionts will go extinct. On lostvectors.com, the simulation spontaneously adds new organisms when some ratio is not met. I will probably start by giving manual control for spawning, but I could see moving into an automatic option.

My vision is that this become a sort of fish tank, something you can leave running for hours.

Possible future directions:
- Genetic inheritance and mutation of different characteristics, like max health, health regeneration, health before reproduction, color, size, speed, movement tendency in any organism
- Mating, complete with chromosomes, crossing-over, etc.
- An kickoff energy source, like light that can be blocked by organisms closer to the light source. Radiation sources could also cause a higher chance of mutation.
- New organisms, of course: a Commensalist, a slow-growing parasite that does no damage but is vulnerable to other organisms, a Disease that spreads between organisms that touch, a Predator that attacks and damages other organisms, but reproduces and loses health slowly and thus usually only injures other organisms
- Cool graphics, like specially shaded vertices for contact points between organisms. Looks pretty easy to do, wierdly.
- If we're keeping with the aquatic model, we could add what the Producers eat, some kind of brine shrimp or something. It probably would just be a grid with a "food count" originating from a generator and spreading out, drawn as a sort of heatmap between ocean-colored and ocean-colored with a little cloudiness from the shrimp. As you would expect, the Producer would gain energy faster when over high concentrations. With a touch of AI using genetics as parameters, we could show evolution of the different organisms over time. I find that pretty cool.
- As complexity increases, a save and load capability would become more and more desirable. As I understand it, this would be pretty easy with the pickle module. Few problems are solved as elegantly as this one with Python's OOP parts. Organism -> Producer, anyone?
- Also, classic simulation functions like time stepping including pausing, direct editing of position, health, spawning, "DNA", and other variables
- If evolution turns out interesting, a capability to run the simulation in no-draw mode at a speed too quick to be drawn intelligibly to see where evolution takes the organisms under any given parameters. It could be run for a million years "real-time" with standard computing power.
